"""Stage-close cleanup (SU-Q24): lists what can go, deletes only with --yes. Stdlib only, Python 3.10+.

    python cleanup.py                              dry run from the project folder; nothing is touched
    python cleanup.py --repo <path>                the same for another checkout
    python cleanup.py --only worktrees,docs        some sections (worktrees, scratch, docs)
    python cleanup.py --yes                        delete what the dry run lists as "remove"
    python cleanup.py --yes --discard <worktree>   also that dirty merged worktree (its uncommitted files are lost)
    --tickets docs/tickets   the ticket folder, its index is README.md there (default docs/tickets)
    --main <branch>          the branch work merges into (default: origin's HEAD, else main, else master)
    --keep-hours 12          worktrees and scratchpads used this recently always stay

Sections:
- worktrees: a worktree whose HEAD is merged into the main branch and that has no uncommitted or untracked files is
  removed with its branch (`git worktree remove`, `git branch -d`). When git unregisters it but the folder cannot be
  deleted, the branch still goes and the empty folder is left for the app. A merged `claude/*` branch with no
  worktree goes too. Unmerged worktrees are only listed; a dirty merged one goes only when named with --discard.
  Other merged branches are listed, never deleted: they were not made by Claude.
- scratch: this project's session scratchpads, `%TEMP%/claude/*/<session id>/`. The session ids are the project's
  transcripts, `~/.claude/projects/<slug>/<id>.jsonl` and its worktrees' (`<slug>--claude-worktrees-*`), where the
  slug is the main checkout's path with every character other than a letter or digit turned into '-'. A scratchpad
  whose session id a `.md` file in the repo cites is kept and listed "cited" until its evidence is copied in.
- docs (report only): broken relative links in the repo's `.md` files, and ticket files the index does not link.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

KEEP_HOURS = 12
SECTIONS = ("worktrees", "scratch", "docs")
SCRATCH_ROOT = Path(tempfile.gettempdir()) / "claude"
PROJECTS_ROOT = Path.home() / ".claude" / "projects"
SESSION_ID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


@dataclass
class Item:
    section: str
    action: str          # "remove", "keep" or "report"
    path: Path | None
    size: int
    why: str
    ref: str = ""        # the worktree's or branch's name


def du(p: Path) -> int:
    if p.is_file():
        return p.stat().st_size
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())


def newest_mtime(p: Path) -> float:
    return max([p.stat().st_mtime] + [f.stat().st_mtime for f in p.rglob("*")])


def gb(n: int) -> str:
    return f"{n / 1e9:.2f} GB"


# --- git -------------------------------------------------------------------------------------------------------------

def git(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8")


def main_checkout(repo: Path) -> Path:
    """The main checkout's root, also when `repo` is a worktree."""
    common = git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip()
    if not common:
        raise SystemExit(f"{repo} is not a git checkout")
    return Path(common).parent


def main_branch(repo: Path) -> str:
    head = git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD").stdout.strip()
    if head:
        return head.split("/", 1)[1]
    for b in ("main", "master"):
        if git(repo, "rev-parse", "--verify", "--quiet", f"refs/heads/{b}").returncode == 0:
            return b
    return git(repo, "branch", "--show-current").stdout.strip()


def parse_worktrees(porcelain: str) -> list[dict]:
    """`git worktree list --porcelain` -> [{"path", "head", "branch"}], the main checkout's block first."""
    out = []
    for block in porcelain.strip().split("\n\n"):
        w = {"branch": None}
        for line in block.splitlines():
            key, _, val = line.partition(" ")
            if key == "worktree":
                w["path"] = Path(val)
            elif key == "HEAD":
                w["head"] = val
            elif key == "branch":
                w["branch"] = val.removeprefix("refs/heads/")
        out.append(w)
    return out


def registered(repo: Path, path: Path) -> bool:
    trees = parse_worktrees(git(repo, "worktree", "list", "--porcelain").stdout)
    return any(w["path"].resolve() == path.resolve() for w in trees)


def merged(repo: Path, rev: str, main: str) -> bool:
    return git(repo, "merge-base", "--is-ancestor", rev, main).returncode == 0


def worktree_plan(repo: Path, main: str, discard: set[str], keep_hours: float = KEEP_HOURS) -> list[Item]:
    """A worktree used in the last keep_hours stays: a session that has just started has no commits of its own yet,
    so its HEAD counts as merged."""
    items, now = [], time.time()
    first, *trees = parse_worktrees(git(repo, "worktree", "list", "--porcelain").stdout)
    for w in trees:
        p, branch = w["path"], w["branch"]
        exists = p.exists()
        dirty = git(p, "status", "--porcelain").stdout.splitlines() if exists else []
        size = du(p) if exists else 0
        if exists and now - newest_mtime(p) < keep_hours * 3600:
            items.append(Item("worktrees", "keep", p, size, f"used in the last {keep_hours:g} h", branch or ""))
        elif not merged(repo, w["head"], main):
            items.append(Item("worktrees", "keep", p, size, f"{branch or 'detached HEAD'} not merged into {main}",
                              branch or ""))
        elif dirty and p.name not in discard:
            items.append(Item("worktrees", "keep", p, size,
                              f"merged, {len(dirty)} uncommitted/untracked file(s): --discard {p.name} to remove",
                              branch or ""))
        else:
            items.append(Item("worktrees", "remove", p, size,
                              f"{branch or 'detached HEAD'} merged" + (", changes discarded" if dirty else ""),
                              branch or ""))
    with_tree = {w["branch"] for w in [first, *trees]} | {main}   # the checked-out branches are never touched
    for b in git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads/").stdout.split():
        if b in with_tree:
            continue
        is_merged = merged(repo, b, main)
        if b.startswith("claude/"):
            items.append(Item("worktrees", "remove" if is_merged else "keep", None, 0,
                              f"branch {b} (no worktree) " + ("merged" if is_merged else "not merged"), b))
        elif is_merged:
            items.append(Item("worktrees", "keep", None, 0,
                              f"branch {b} merged but not made by Claude: delete it by hand if it is done", b))
    return items


# --- scratchpads -----------------------------------------------------------------------------------------------------

def project_slug(checkout: Path) -> str:
    """The app's folder name for a project: every character other than a letter or digit becomes '-'."""
    return re.sub(r"[^A-Za-z0-9]", "-", str(checkout))


def session_ids(projects_root: Path, slug: str) -> set[str]:
    """The session ids of the main checkout's transcripts and its worktrees'."""
    ids: set[str] = set()
    if not projects_root.is_dir():
        return ids
    for d in projects_root.iterdir():
        if d.is_dir() and (d.name == slug or d.name.startswith(slug + "--claude-worktrees-")):
            ids.update(f.stem for f in d.glob("*.jsonl") if SESSION_ID.fullmatch(f.stem))
    return ids


def scratch_plan(scratch_root: Path, ids: set[str], cited_text: str, keep_hours: float = KEEP_HOURS,
                 now: float | None = None) -> list[Item]:
    now = time.time() if now is None else now
    items = []
    if not scratch_root.is_dir():
        return items
    for top in sorted(p for p in scratch_root.iterdir() if p.is_dir()):
        for s in sorted(p for p in top.iterdir() if p.is_dir() and p.name in ids):
            size = du(s)
            if s.name in cited_text:
                items.append(Item("scratch", "keep", s, size, "cited by a doc: copy the evidence in first"))
            elif now - newest_mtime(s) < keep_hours * 3600:
                items.append(Item("scratch", "keep", s, size, f"used in the last {keep_hours:g} h"))
            else:
                items.append(Item("scratch", "remove", s, size, "old session scratchpad"))
    return items


# --- docs ------------------------------------------------------------------------------------------------------------

def md_files(checkout: Path) -> list[Path]:
    """The checkout's .md files, tracked or new but not ignored."""
    out = git(checkout, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.md").stdout
    return sorted({checkout / f for f in out.split("\0") if f and (checkout / f).is_file()})


def strip_code(text: str) -> str:
    """Drop fenced code blocks and inline code: a link written as an example there is not a link."""
    text = re.sub(r"^(```|~~~).*?^\1", "", text, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", text)


LINK = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


def doc_issues(checkout: Path, tickets: str = "docs/tickets") -> list[Item]:
    items = []
    files = md_files(checkout)
    for f in files:
        rel = f.relative_to(checkout).as_posix()
        for target in LINK.findall(strip_code(f.read_text(encoding="utf-8"))):
            if target.startswith("#") or re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue                                  # an anchor, a URL, mailto:, a drive path
            path = unquote(target.split("#", 1)[0])
            base = checkout if path.startswith("/") else f.parent
            if not (base / path.lstrip("/")).exists():
                items.append(Item("docs", "report", None, 0, f"{rel}: broken link {target}"))
    folder = checkout / tickets
    index = folder / "README.md"
    if index.is_file():
        linked = {Path(unquote(t.split("#", 1)[0])).name for t in LINK.findall(index.read_text(encoding="utf-8"))}
        ticket_files = sorted(p for p in folder.glob("*.md") if p.name != "README.md")
        texts = {p: p.read_text(encoding="utf-8") for p in ticket_files}
        for t in ticket_files:                    # a companion note another ticket file names is not a ticket
            named = any(t.name in txt for o, txt in texts.items() if o != t)
            if t.name not in linked and not named:
                items.append(Item("docs", "report", None, 0, f"{tickets}/{t.name} is not in the index"))
    return items


# --- apply -----------------------------------------------------------------------------------------------------------

def allowed(p: Path, root: Path) -> bool:
    p, root = p.resolve(), root.resolve()
    return p != root and p.is_relative_to(root)


def _writable_and_retry(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(p: Path) -> None:
    if sys.version_info >= (3, 12):
        shutil.rmtree(p, onexc=_writable_and_retry)
    else:
        shutil.rmtree(p, onerror=_writable_and_retry)


def remove(repo: Path, item: Item, discard: set[str], scratch_root: Path = SCRATCH_ROOT) -> str:
    if item.section == "worktrees":
        if item.path is None:
            r = git(repo, "branch", "-d", item.ref)
            return f"FAILED branch {item.ref}: {r.stderr.strip()}" if r.returncode else f"deleted branch {item.ref}"
        force = ["--force"] if item.path.name in discard else []
        r = git(repo, "worktree", "remove", *force, str(item.path))
        done = f"removed worktree {item.path.name}"
        if r.returncode:
            # git unregisters the worktree even when the folder delete fails (the app's sandbox may refuse it): the
            # branch can still go, and the empty folder is left for the app (archiving the session removes it).
            if registered(repo, item.path):
                return f"FAILED {item.path}: {r.stderr.strip()}"
            done += f" (unregistered; folder left for the app: {r.stderr.strip()})"
        if not item.ref:
            return f"{done} (detached, no branch)"
        r = git(repo, "branch", "-D" if force else "-d", item.ref)
        return done + (f" (branch kept: {r.stderr.strip()})" if r.returncode else f", deleted branch {item.ref}")
    if not allowed(item.path, scratch_root):
        return f"REFUSED {item.path}: outside {scratch_root}"
    rmtree(item.path)
    return f"removed {item.path}"


def report(items: list[Item], sections=SECTIONS) -> None:
    for sec in (s for s in SECTIONS if s in sections):
        group = [i for i in items if i.section == sec]
        if not group:
            print(f"\n== {sec}: nothing found")
            continue
        gone = [i for i in group if i.action == "remove"]
        print(f"\n== {sec}: {len(gone)} to remove, {gb(sum(i.size for i in gone))}")
        for i in group:
            # a scratchpad's session id can sit under two parents (the app's old and new layout): show both parts
            where = "" if not i.path else f"{i.path.parent.name}/{i.path.name}" if sec == "scratch" else i.path.name
            size = gb(i.size) if i.size else ""
            print(f"  {i.action:6} {where:56} {size:>9}  {i.why}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=".", help="a checkout of the project (default: the current folder)")
    ap.add_argument("--only", default=",".join(SECTIONS), help="comma-separated sections")
    ap.add_argument("--tickets", default="docs/tickets", help="the ticket folder, relative to the repo")
    ap.add_argument("--main", help="the branch work merges into")
    ap.add_argument("--yes", action="store_true", help="delete what the dry run lists as remove")
    ap.add_argument("--discard", action="append", default=[], metavar="WORKTREE",
                    help="also remove this dirty (merged) worktree; its uncommitted files are lost")
    ap.add_argument("--keep-hours", type=float, default=KEEP_HOURS,
                    help="worktrees and scratchpads used this recently stay")
    args = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    checkout = Path(git(Path(args.repo), "rev-parse", "--show-toplevel").stdout.strip() or args.repo).resolve()
    repo = main_checkout(checkout)
    branch = args.main or main_branch(repo)
    only, discard = set(args.only.split(",")), set(args.discard)
    unknown = only - set(SECTIONS)
    if unknown:
        ap.error(f"unknown section(s): {', '.join(sorted(unknown))}")
    print(f"project {repo}, merges into {branch}")
    items: list[Item] = []
    if "worktrees" in only:
        items += worktree_plan(repo, branch, discard, args.keep_hours)
    if "scratch" in only:
        cited = "\n".join(f.read_text(encoding="utf-8") for f in md_files(repo))
        items += scratch_plan(SCRATCH_ROOT, session_ids(PROJECTS_ROOT, project_slug(repo)), cited, args.keep_hours)
    if "docs" in only:
        items += doc_issues(checkout, args.tickets)
    report(items, only)
    gone = [i for i in items if i.action == "remove"]
    if not args.yes:
        print(f"\ndry run: {len(gone)} item(s), {gb(sum(i.size for i in gone))}; nothing touched (--yes deletes)")
        return 0
    for i in gone:
        print(remove(repo, i, discard))
    return 0


if __name__ == "__main__":
    sys.exit(main())
