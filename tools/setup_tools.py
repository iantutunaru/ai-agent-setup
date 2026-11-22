#!/usr/bin/env python3
"""The steps of the setup skills that would otherwise need one shell or the other (SU-Q66).

The skills setup-init, setup-sync and setup-promote run in Claude Code (bash) and in ChatGPT (PowerShell). The
steps below were bash-only lines (cp -rn, grep pipelines); here they are one script both tools call the same way:

    python "<setup>/tools/setup_tools.py" <command> [options]

    where                          the setup repo's folder
    prefixes [--projects DIR]      id prefixes the sibling projects already use (default: the parent of --dest)
    copy-template code|docs        copy template/base and template/<profile> into --dest, never overwriting
    fill-prefix <PREFIX>           replace <P> in the files the template gave
    add-entry game-design          add the Game design list to AGENTS.md, every field `none yet`
    add-entry guided-sessions --where PLACE
                                   add the Guided sessions line to AGENTS.md and write docs/sessions.md
    check                          open placeholders in the project's file and decisions log, text in backticks
                                   left out; files still holding <P> (text files git would track: no ignored
                                   file, no binary file)
    base-lines                     lines of the template's .gitignore and .gitattributes the project lacks (read-only)
    instructions                   which of AGENTS.md and CLAUDE.md the project has, and what a move would change
    move-instructions              move the project's text from CLAUDE.md into AGENTS.md (SU-Q59)

The setup repo's own branch workflow (SU-Q93, SU-Q95, SU-Q108, SU-Q112), used by setup-promote, setup-sync and
both session-start hooks:

    branch-name TOPIC...           the branch for a setup change, <name>/<topic>, the name from git's user.name
    repo-state                     where the setup stands: main, a branch (merged or not, pushed or not), detached
    start-branch BRANCH            on main: bring main up to date with the remote and make the branch from it
    push-branch                    push the current branch with its upstream and show the pull request link; never main
    switch-back                    after the merge: back to main, up to date, the merged branch deleted (never forced)

Every command takes --dest DIR (default: the current folder); the branch commands take --repo DIR instead
(default: the setup repo this script lives in). Only copy-template, fill-prefix, add-entry, move-instructions,
start-branch, push-branch and switch-back write. Standard library only.
"""
import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MAIN = "main"
TEMPLATE = os.path.join(REPO, "template")
ID_RE = re.compile(r"\b([A-Z]{2,3})-[TQ][0-9]+")
PROFILE_IMPORT_RE = re.compile(r"^@~/\.claude/setup/profiles/(code|docs)\.md\s*$")
PROFILE_LINE_RE = re.compile(r"^Profile:\s*(code|docs)\b", re.M)
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}


def read(path):
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def template_files(profile):
    """(source path, path relative to the project) for every file of base and of the profile."""
    out = []
    for part in ("base", profile):
        root = os.path.join(TEMPLATE, part)
        for folder, _dirs, files in os.walk(root):
            for name in sorted(files):
                src = os.path.join(folder, name)
                out.append((src, os.path.relpath(src, root)))
    return out


def detect_profile(dest):
    """The profile a project has: from AGENTS.md's Profile line, else from CLAUDE.md's import line."""
    agents = os.path.join(dest, "AGENTS.md")
    if os.path.isfile(agents):
        m = PROFILE_LINE_RE.search(read(agents))
        if m:
            return m.group(1)
    claude = os.path.join(dest, "CLAUDE.md")
    if os.path.isfile(claude):
        for line in read(claude).splitlines():
            m = PROFILE_IMPORT_RE.match(line.strip())
            if m:
                return m.group(1)
    return None


# --- commands ---------------------------------------------------------------------------------------------------

def cmd_where(args):
    print(REPO)
    return 0


def cmd_prefixes(args):
    projects = args.projects or os.path.dirname(os.path.abspath(args.dest))
    found = {}
    for name in sorted(os.listdir(projects)):
        folder = os.path.join(projects, name)
        if not os.path.isdir(folder):
            continue
        files = [os.path.join(folder, n) for n in ("AGENTS.md", "CLAUDE.md", "decisions.md")]
        decisions = os.path.join(folder, "docs", "decisions")
        if os.path.isdir(decisions):
            for sub, _dirs, names in os.walk(decisions):
                files += [os.path.join(sub, n) for n in names if n.endswith(".md")]
        for path in files:
            if not os.path.isfile(path):
                continue
            for prefix in ID_RE.findall(read(path)):
                entry = found.setdefault(prefix, {"count": 0, "projects": set()})
                entry["count"] += 1
                entry["projects"].add(name)
    if not found:
        print("no id prefixes found under %s" % projects)
        return 0
    for prefix in sorted(found):
        entry = found[prefix]
        print("%-4s %5d  %s" % (prefix, entry["count"], ", ".join(sorted(entry["projects"]))))
    return 0


def cmd_copy_template(args):
    copied = kept = 0
    for src, rel in template_files(args.profile):
        target = os.path.join(args.dest, rel)
        if os.path.exists(target):
            print("kept    %s (already there, not touched)" % rel)
            kept += 1
            continue
        folder = os.path.dirname(target)
        if folder and not os.path.isdir(folder):
            os.makedirs(folder)
        with open(src, "rb") as fh:
            data = fh.read()
        with open(target, "wb") as fh:
            fh.write(data)
        print("copied  %s" % rel)
        copied += 1
    print("done: %d copied, %d kept" % (copied, kept))
    return 0


def cmd_fill_prefix(args):
    if not re.match(r"^[A-Z]{2,3}$", args.prefix):
        print("the prefix is 2 or 3 capital letters, got %r" % args.prefix)
        return 2
    profile = detect_profile(args.dest)
    if profile is None:
        print("no profile found in AGENTS.md or CLAUDE.md: run copy-template first")
        return 2
    changed = 0
    for _src, rel in template_files(profile):
        target = os.path.join(args.dest, rel)
        if not os.path.isfile(target):
            continue
        text = read(target)
        if "<P>" in text:
            write(target, text.replace("<P>", args.prefix))
            print("filled  %s (%d)" % (rel, text.count("<P>")))
            changed += 1
    print("done: %d files" % changed)
    return 0


ENTRIES = os.path.join(TEMPLATE, "entries")
ENTRY_FORMS = {"game-design": ("game-design.md", "Game design"),
               "guided-sessions": ("guided-sessions.md", "Guided sessions")}
SESSIONS_NOTES = os.path.join("docs", "sessions.md")
WHERE_THINGS_ARE = "## where things are"
STAGE_CLOSE_RE = re.compile(r"^-\s+\*\*Stage close:?\*\*")


def cmd_add_entry(args):
    """Write one entry the global skills read into AGENTS.md, under "Where things are", from its form in
    template/entries/ (SU-Q142): every field `none yet`. guided-sessions also writes the notes file the entry
    names. An entry or a notes file that is there stays as it is."""
    form, title = ENTRY_FORMS[args.entry]
    where = " ".join((args.where or "").split())
    if args.entry == "guided-sessions" and not where:
        print('guided-sessions needs --where "<the game, program or device the user tests in>"')
        return 2
    if "<" in where:
        print("--where holds a `<`, which check reads as an open placeholder: name the place without it")
        return 2
    agents = os.path.join(args.dest, "AGENTS.md")
    if not os.path.isfile(agents):
        print("no AGENTS.md in %s: run copy-template first" % args.dest)
        return 2
    lines = read(agents).splitlines()
    if any(re.match(r"^\s*-\s+\*\*%s:?\*\*" % re.escape(title), line) for line in lines):
        print("kept    the %s entry in AGENTS.md (already there, not touched)" % title)
        return 0
    start = next((i for i, line in enumerate(lines) if line.strip().lower() == WHERE_THINGS_ARE), None)
    if start is None:
        print('AGENTS.md has no "## Where things are" section: add the heading, then run this again')
        return 2
    end = next((i for i in range(start + 1, len(lines)) if re.match(r"^#{1,2}\s", lines[i])), len(lines))
    at = next((i for i in range(start + 1, end) if STAGE_CLOSE_RE.match(lines[i])), None)
    if at is None:                                    # no Stage close list: after the section's last line
        at = end
        while at > start + 1 and not lines[at - 1].strip():
            at -= 1
    block = read(os.path.join(ENTRIES, form)).replace("<where>", where).splitlines()
    if at == start + 1:
        block = [""] + block
    lines[at:at] = block
    write(agents, "\n".join(lines) + "\n")
    print("added   the %s entry to AGENTS.md, before line %d" % (title, at + 1))
    if args.entry == "guided-sessions":
        notes = os.path.join(args.dest, SESSIONS_NOTES)
        if os.path.exists(notes):
            print("kept    %s (already there, not touched)" % SESSIONS_NOTES)
        else:
            if not os.path.isdir(os.path.dirname(notes)):
                os.makedirs(os.path.dirname(notes))
            write(notes, read(os.path.join(ENTRIES, "sessions.md")).replace("<where>", where))
            print("wrote   %s" % SESSIONS_NOTES)
    return 0


def decisions_logs(dest):
    out = []
    root_log = os.path.join(dest, "decisions.md")
    if os.path.isfile(root_log):
        out.append(root_log)
    folder = os.path.join(dest, "docs", "decisions")
    if os.path.isdir(folder):
        for sub, _dirs, names in os.walk(folder):
            out += [os.path.join(sub, n) for n in sorted(names) if n.endswith(".md")]
    return out


def cmd_check(args):
    problems = 0
    # 1. a placeholder's opening in the project's file and the decisions log (it may span two lines)
    targets = [p for p in (os.path.join(args.dest, "AGENTS.md"),) if os.path.isfile(p)] + decisions_logs(args.dest)
    if not targets:
        print("no AGENTS.md and no decisions log in %s" % args.dest)
        problems += 1
    for path in targets:
        for number, line in enumerate(read(path).splitlines(), 1):
            # text in backticks is a name pattern (`docs/sessions/<ticket>-r<N>.md`), not a placeholder (SU-Q147)
            if re.search(r"<[A-Za-z]", re.sub(r"`[^`]*`", "", line)):
                print("placeholder  %s:%d  %s" % (os.path.relpath(path, args.dest), number, line.strip()[:100]))
                problems += 1
    # 2. <P> in any text file git would track
    paths = git_listed(args.dest)
    if paths is None:
        print("note: git could not list the files, so every folder is read, ignored ones too")
        paths = walked(args.dest)
    for path in paths:
        try:
            if holds_prefix(path):
                print("prefix       %s still holds <P>" % os.path.relpath(path, args.dest))
                problems += 1
        except OSError:
            pass
    print("ok: nothing left to fill" if problems == 0 else "%d to fill" % problems)
    return 1 if problems else 0


def git_listed(dest):
    """The files check reads for <P>: tracked ones, and untracked ones no ignore rule matches, so a folder git
    ignores is never opened (SU-Q140). In a folder that is not a repo yet (setup-init runs check before and after
    its `git init`), git answers through an empty scratch git folder with dest as its work tree; nothing is
    written in dest. None when git gives no list (not installed, or it refuses the folder)."""
    dest = os.path.abspath(dest)
    names = git_names(dest, ["ls-files", "--cached", "--others", "--exclude-standard", "-z"])
    if names is None:
        scratch = tempfile.mkdtemp(prefix="setup-check-")
        try:
            if git_names(dest, ["init", "--quiet", "--bare", scratch]) is not None:
                names = git_names(dest, ["--git-dir", scratch, "--work-tree", dest,
                                         "ls-files", "--others", "--exclude-standard", "-z"])
        finally:
            shutil.rmtree(scratch, ignore_errors=True)
    if names is None:
        return None
    paths = [os.path.join(dest, name.replace("/", os.sep)) for name in names]
    return [p for p in paths if os.path.isfile(p)]          # a tracked file may be gone from disk


def git_names(folder, args):
    """The NUL-separated names a git command prints, run in folder; None when git fails or is not there."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", LC_ALL="C")
    try:
        done = subprocess.run(["git", "-C", folder] + args, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL, env=env)
    except OSError:
        return None
    if done.returncode != 0:
        return None
    return [name.decode("utf-8", "surrogateescape") for name in done.stdout.split(b"\0") if name]


def walked(dest):
    """Every file under dest but the folders of SKIP_DIRS: what check reads when git gives no list."""
    out = []
    for folder, dirs, names in os.walk(dest):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        out += [os.path.join(folder, name) for name in sorted(names)]
    return out


BLOCK = 1 << 20
BINARY_HEAD = 8000


def holds_prefix(path):
    """True when a text file holds <P>. A file with a NUL byte in its first 8000 bytes is binary, the test git
    itself uses, and is not read further: by chance a texture holds the three bytes too (SU-Q141). Read in blocks,
    so a large text file is never in memory whole."""
    with open(path, "rb") as fh:
        block = fh.read(max(BLOCK, BINARY_HEAD))
        if b"\0" in block[:BINARY_HEAD]:
            return False
        tail = b""
        while block:
            if b"<P>" in tail + block:
                return True
            tail = block[-2:]
            block = fh.read(BLOCK)
    return False


def cmd_base_lines(args):
    missing_total = 0
    for name in (".gitignore", ".gitattributes"):
        base = [l.rstrip() for l in read(os.path.join(TEMPLATE, "base", name)).splitlines()]
        base = [l for l in base if l.strip() and not l.lstrip().startswith("#")]
        target = os.path.join(args.dest, name)
        have = set()
        if os.path.isfile(target):
            have = {l.strip() for l in read(target).splitlines()}
        else:
            print("%s: the project has none" % name)
        missing = [l for l in base if l.strip() not in have]
        for line in missing:
            print("%s lacks: %s" % (name, line))
        missing_total += len(missing)
        if name == ".gitattributes" and "* text=auto" in have:
            print(".gitattributes has a bare `* text=auto`: it is replaced in place by `* text=auto eol=lf`")
    print("ok: no base line is missing" if missing_total == 0 else "%d base lines missing" % missing_total)
    return 0


def instruction_state(dest):
    agents = os.path.join(dest, "AGENTS.md")
    claude = os.path.join(dest, "CLAUDE.md")
    state = {"agents": os.path.isfile(agents), "claude": os.path.isfile(claude), "profile": detect_profile(dest),
             "claude_lines": [], "imports": []}
    if state["claude"]:
        lines = [l.strip() for l in read(claude).splitlines() if l.strip()]
        state["claude_lines"] = lines
        state["imports"] = [l for l in lines if l.startswith("@")]
    state["agents_has_profile"] = bool(state["agents"] and PROFILE_LINE_RE.search(read(agents)))
    profile = state["profile"]
    wanted = ["@~/.claude/setup/profiles/%s.md" % profile, "@AGENTS.md"] if profile else None
    state["moved"] = bool(state["agents"] and state["agents_has_profile"] and wanted and state["claude_lines"] == wanted)
    return state


def cmd_instructions(args):
    s = instruction_state(args.dest)
    print("AGENTS.md: %s%s" % ("yes" if s["agents"] else "no",
                               (", Profile line: %s" % ("yes" if s["agents_has_profile"] else "no")) if s["agents"] else ""))
    print("CLAUDE.md: %s%s" % ("yes" if s["claude"] else "no",
                               (", %d lines, imports: %s" % (len(s["claude_lines"]), ", ".join(s["imports"]) or "none"))
                               if s["claude"] else ""))
    print("profile:   %s" % (s["profile"] or "none named"))
    if s["moved"]:
        print("state:     moved: AGENTS.md holds the text, CLAUDE.md is the two import lines")
    elif s["claude"] and not s["agents"]:
        print("state:     not moved: the text is in CLAUDE.md; `move-instructions` moves it into AGENTS.md")
    elif not s["claude"] and not s["agents"]:
        print("state:     the project has neither file")
    else:
        print("state:     mixed: both files hold text or a line is missing; merge by hand, showing the user the result")
    return 0


def cmd_move_instructions(args):
    dest = args.dest
    agents = os.path.join(dest, "AGENTS.md")
    claude = os.path.join(dest, "CLAUDE.md")
    if os.path.exists(agents):
        print("AGENTS.md is already there: nothing moved. Run `instructions` to see the state.")
        return 2
    if not os.path.isfile(claude):
        print("no CLAUDE.md in %s" % dest)
        return 2
    lines = read(claude).splitlines()
    profile = args.profile
    body = []
    for line in lines:
        m = PROFILE_IMPORT_RE.match(line.strip())
        if m:
            profile = profile or m.group(1)
            continue                      # the profile import stays in CLAUDE.md, not in the shared text
        body.append(line)
    if profile is None:
        print("CLAUDE.md names no profile: pass --profile code or --profile docs")
        return 2
    while body and not body[0].strip():
        body.pop(0)
    # the Profile line goes under the first heading, or on top when the text has none
    out, placed = [], False
    for line in body:
        out.append(line)
        if not placed and line.startswith("# "):
            out += ["", "Profile: %s" % profile]
            placed = True
    if not placed:
        out = ["Profile: %s" % profile, ""] + body
    text = "\n".join(out).rstrip("\n") + "\n"
    text = re.sub(r"(Profile: (?:code|docs)\n)\n\n+", r"\1\n", text)
    write(agents, text)
    write(claude, "@~/.claude/setup/profiles/%s.md\n@AGENTS.md\n" % profile)
    print("AGENTS.md written (%d lines, Profile: %s); CLAUDE.md is now the two import lines" % (len(out), profile))
    others = [l.strip() for l in body if l.strip().startswith("@")]
    for line in others:
        print("note: AGENTS.md keeps the import line %s; Claude Code follows it, ChatGPT reads it as plain text" % line)
    return 0


# --- the setup repo's branch workflow (SU-Q93, SU-Q95, SU-Q108, SU-Q112) ----------------------------------------

class GitResult(object):
    def __init__(self, code, out, err):
        self.code, self.out, self.err = code, out, err

    @property
    def said(self):
        """The first line git wrote, error output first."""
        return first_line(self.err) or first_line(self.out)


def first_line(text):
    for line in (text or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def git(repo, *args, **kwargs):
    """git in repo. Output goes to temporary files, not pipes, so a time limit holds even when git leaves a helper
    behind (git fetch starts git-remote-https). Code -1: no answer in time; -2: git could not be started."""
    timeout = kwargs.get("timeout")
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", LC_ALL="C")
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        try:
            code = subprocess.run(["git", "-C", repo] + list(args), stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                  env=env, timeout=timeout).returncode
        except subprocess.TimeoutExpired:
            return GitResult(-1, "", "no answer in %d seconds" % timeout)
        except OSError as exc:
            return GitResult(-2, "", "git could not be started (%s)" % exc)
        out.seek(0)
        err.seek(0)
        return GitResult(code, out.read().decode("utf-8", "replace").strip(),
                         err.read().decode("utf-8", "replace").strip())


def safe_part(text):
    """Lower case letters and digits joined by single hyphens; accents dropped, anything else is a separator."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def branch_name(user_name, topic, limit=40):
    """<name>/<topic> (SU-Q112), or raises ValueError saying what is missing."""
    words = (user_name or "").split()
    name = safe_part(words[0]) if words else ""
    if not name:
        raise ValueError("git's user.name (%r) holds no letter a branch name can use: pass --name" % (user_name or ""))
    topic = safe_part(topic)
    if not topic:
        raise ValueError("the topic holds no letter a branch name can use: give a few words")
    if len(topic) > limit:
        cut = topic[:limit + 1].rfind("-")
        topic = topic[:cut if cut > 0 else limit].strip("-")
    return "%s/%s" % (name, topic)


def main_remote(repo):
    """The remote main comes from: main's own, else origin."""
    r = git(repo, "config", "branch.%s.remote" % MAIN)
    return r.out if r.code == 0 and r.out else "origin"


def ref_exists(repo, ref):
    return git(repo, "rev-parse", "--verify", "-q", ref + "^{commit}").code == 0


def repo_state(repo, fetch=True, timeout=10):
    """Where the setup stands. state is one of:
      main        on main
      merged      on a branch whose last commit reached <remote>/main through a merge (SU-Q108)
      no-commits  on a branch whose last commit is on main's own line: it holds nothing that is not on main
      not-merged  on a pushed branch (an upstream is set) that is not in <remote>/main
      no-upstream on a branch never pushed, with commits of its own
      unknown     on a branch, and there is no <remote>/main to compare with
      detached    on no branch
    fetch is 'ok', 'skipped' or the reason it failed; the state is then judged on what was fetched before.
    Returns None when repo is not a git repo with a commit."""
    head = git(repo, "rev-parse", "--verify", "-q", "HEAD")
    if head.code != 0:
        return None
    remote = main_remote(repo)
    s = {"state": None, "branch": None, "sha": head.out, "remote": remote, "remote_main": "%s/%s" % (remote, MAIN),
         "fetch": "skipped", "dirty": [], "upstream": None, "upstream_gone": False, "unpushed": 0, "own": [],
         "behind": 0, "contained": False}
    status = git(repo, "status", "--porcelain")
    s["dirty"] = [line for line in status.out.splitlines() if line.strip()]
    if fetch:
        f = git(repo, "fetch", "--quiet", "--prune", remote, timeout=timeout)
        s["fetch"] = "ok" if f.code == 0 else (f.said or "git fetch stopped with code %d" % f.code)
    remote_main = "refs/remotes/%s/%s" % (remote, MAIN)
    have_remote_main = ref_exists(repo, remote_main)
    sym = git(repo, "symbolic-ref", "--short", "-q", "HEAD")
    if sym.code != 0:
        s["state"] = "detached"
        refs = git(repo, "for-each-ref", "--contains", "HEAD", "--format=%(refname)", "refs/heads", "refs/remotes")
        s["contained"] = bool(refs.out.strip())
        return s
    branch = s["branch"] = sym.out
    if branch == MAIN:
        s["state"] = "main"
        if have_remote_main:
            behind = git(repo, "rev-list", "--count", "HEAD.." + remote_main)
            s["behind"] = int(behind.out) if behind.code == 0 and behind.out.isdigit() else 0
        return s
    merge = git(repo, "config", "branch.%s.merge" % branch)
    if merge.code == 0 and merge.out:
        up_remote = git(repo, "config", "branch.%s.remote" % branch).out or remote
        up_branch = re.sub(r"^refs/heads/", "", merge.out)
        s["upstream"] = "%s/%s" % (up_remote, up_branch)
        up_ref = "refs/remotes/%s/%s" % (up_remote, up_branch)
        if ref_exists(repo, up_ref):
            ahead = git(repo, "rev-list", "--count", up_ref + "..HEAD")
            s["unpushed"] = int(ahead.out) if ahead.code == 0 and ahead.out.isdigit() else 0
        else:
            s["upstream_gone"] = True
    if not have_remote_main:
        s["state"] = "unknown"
        return s
    if git(repo, "merge-base", "--is-ancestor", "HEAD", remote_main).code == 0:
        line = set(git(repo, "rev-list", "--first-parent", remote_main).out.split())
        s["state"] = "no-commits" if s["sha"] in line else "merged"
        return s
    own = git(repo, "log", "--format=%h %s", remote_main + "..HEAD")
    s["own"] = [l for l in own.out.splitlines() if l.strip()]
    s["state"] = "not-merged" if s["upstream"] else "no-upstream"
    return s


def hook_line(s, tool):
    """The one line a session-start hook prints when the setup is not on main (SU-Q95); '' on main."""
    skill = "/setup-promote" if tool == "claude" else "the setup-promote skill"
    if s is None:
        return "agent-setup: git could not read the setup repo, so it was not pulled; tell the user."
    if s["state"] == "main":
        return ""
    if s["state"] == "detached":
        return ("agent-setup: the setup is on no branch (detached HEAD at %s), so it was not pulled and gets no "
                "updates from main. Tell the user to run %s to get back to main." % (s["sha"][:7], skill))
    base = ("agent-setup: the setup is on the branch %s, not on main, so this machine runs that change and gets no "
            "updates from main meanwhile" % s["branch"])
    if s["fetch"] not in ("ok", "skipped"):
        return base + "; whether the branch is merged could not be checked (%s)." % s["fetch"]
    if s["state"] == "unknown":
        return base + "; whether the branch is merged could not be checked (no %s)." % s["remote_main"]
    if s["state"] == "merged":
        return ("agent-setup: the setup's branch %s is merged into main. Tell the user to run %s to switch back to "
                "main, pull and delete the branch; until then this machine gets no updates from main."
                % (s["branch"], skill))
    if s["state"] == "no-upstream":
        return base + "; the branch is not pushed yet."
    if s["state"] == "no-commits":
        return base + "; the branch has no commits of its own yet."
    return base + "."


def pull_request_link(text):
    """The link a host prints after a push of a new branch. GitHub, seen on this repo:
    remote: Create a pull request for '<branch>' on GitHub by visiting:
    remote:      https://github.com/<owner>/<repo>/pull/new/<branch>"""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "pull request" in line.lower():
            for later in lines[i:i + 3]:
                m = re.search(r"https?://\S+", later)
                if m:
                    return m.group(0)
    return None


def say_git(result):
    for text in (result.out, result.err):
        for line in text.splitlines():
            print("  git: %s" % line.rstrip())


def print_dirty(s, limit=20):
    for line in s["dirty"][:limit]:
        print("  %s" % line)
    if len(s["dirty"]) > limit:
        print("  ... and %d more" % (len(s["dirty"]) - limit))


def no_repo(repo):
    print("%s is not a git repo with a commit" % repo)
    return 2


def cmd_branch_name(args):
    user = args.name
    if user is None:
        r = git(args.repo, "config", "user.name")
        user = r.out if r.code == 0 else ""
    try:
        name = branch_name(user, " ".join(args.topic))
    except ValueError as exc:
        print(exc)
        return 2
    if git(args.repo, "check-ref-format", "--branch", name).code != 0:
        print("git does not accept %r as a branch name: give other words" % name)
        return 2
    print(name)
    return 0


def cmd_repo_state(args):
    s = repo_state(args.repo, fetch=not args.no_fetch, timeout=args.timeout)
    if args.hook:
        line = hook_line(s, args.hook)
        if line:
            print(line)
        return 0
    if s is None:
        return no_repo(args.repo)
    state = s["state"]
    print("state: %s" % state)
    print("branch: %s" % (s["branch"] or "none (detached HEAD at %s)" % s["sha"][:7]))
    fetched = {"ok": "fetched just now", "skipped": "not fetched"}.get(
        s["fetch"], "the fetch failed (%s); judged on what was fetched before" % s["fetch"])
    print("compared with: %s, %s" % (s["remote_main"], fetched))
    if state == "main":
        print("on main: a new change starts here with start-branch")
        if s["behind"]:
            print("main is %d commits behind %s: start-branch brings it up to date" % (s["behind"], s["remote_main"]))
    elif state == "merged":
        print("the branch is merged into %s: switch-back returns to main, brings it up to date and deletes the branch"
              % s["remote_main"])
    elif state == "no-commits":
        print("the branch holds nothing that is not on %s: switch-back returns to main and deletes it"
              % s["remote_main"])
    elif state in ("not-merged", "no-upstream"):
        if state == "no-upstream":
            print("the branch is not pushed yet and not merged")
        else:
            print("the branch is pushed to %s and not merged into %s" % (s["upstream"], s["remote_main"]))
            if s["upstream_gone"]:
                print("the branch is no longer on the remote (deleted there)")
            elif s["unpushed"]:
                print("%d commits not pushed yet" % s["unpushed"])
        print("commits of its own (%d):" % len(s["own"]))
        for line in s["own"][:10]:
            print("  %s" % line)
        if len(s["own"]) > 10:
            print("  ... and %d more" % (len(s["own"]) - 10))
    elif state == "unknown":
        print("there is no %s to compare with: whether the branch is merged is not known" % s["remote_main"])
    elif state == "detached":
        print("on no branch; this commit is %s" % ("also on a branch or on the remote: switch-back returns to main"
                                                 if s["contained"] else
                                                 "on no branch and not on the remote: keep it with git branch first"))
    if s["dirty"]:
        print("uncommitted changes (%d):" % len(s["dirty"]))
        print_dirty(s)
    else:
        print("uncommitted changes: none")
    return 0


def cmd_start_branch(args):
    repo, branch = args.repo, args.branch
    s = repo_state(repo, fetch=True, timeout=args.timeout)
    if s is None:
        return no_repo(repo)
    if s["state"] != "main":
        print("the setup is on %s, not on main: a new branch starts from main only. Run repo-state, then "
              "switch-back or go on with that branch." % (s["branch"] or "no branch"))
        return 2
    if branch == MAIN or git(repo, "check-ref-format", "--branch", branch).code != 0:
        print("%r cannot be the branch: use branch-name" % branch)
        return 2
    for ref in ("refs/heads/" + branch, "refs/remotes/%s/%s" % (s["remote"], branch)):
        if ref_exists(repo, ref):
            print("the branch %s is already there (%s): choose another topic" % (branch, ref))
            return 2
    if s["dirty"] and not args.carry:
        print("uncommitted changes in the setup; nothing done. If they belong to this change, run again with "
              "--carry to take them onto the branch:")
        print_dirty(s)
        return 2
    if s["fetch"] != "ok":
        print("could not fetch from %s (%s): main cannot be brought up to date; nothing done" % (s["remote"], s["fetch"]))
        return 1
    if not ref_exists(repo, "refs/remotes/" + s["remote_main"]):
        print("there is no %s to start from; nothing done" % s["remote_main"])
        return 1
    ff = git(repo, "merge", "--ff-only", "-q", s["remote_main"])
    if ff.code != 0:
        print("main could not be brought up to date with %s; nothing else done:" % s["remote_main"])
        say_git(ff)
        return 1
    switch = git(repo, "switch", "-c", branch)
    if switch.code != 0:
        print("the branch could not be made:")
        say_git(switch)
        return 1
    sha = git(repo, "rev-parse", "--short", "HEAD").out
    print("on the new branch %s, made from %s at %s" % (branch, s["remote_main"], sha))
    if s["dirty"]:
        print("the uncommitted changes came along (%d files)" % len(s["dirty"]))
    return 0


def cmd_push_branch(args):
    repo = args.repo
    s = repo_state(repo, fetch=False)
    if s is None:
        return no_repo(repo)
    if s["state"] == "main":
        print("the setup is on main: main is never pushed (SU-Q93). Make a branch first with start-branch.")
        return 2
    if s["state"] == "detached":
        print("the setup is on no branch (detached HEAD at %s): nothing pushed" % s["sha"][:7])
        return 2
    if s["state"] == "merged":
        print("the branch %s is merged already: nothing pushed. switch-back returns to main; a further change "
              "starts a new branch." % s["branch"])
        return 2
    if s["state"] == "no-commits":
        print("the branch %s has no commits of its own: nothing to push" % s["branch"])
        return 2
    branch = s["branch"]
    remote = s["upstream"].split("/", 1)[0] if s["upstream"] else s["remote"]
    push = git(repo, "push", "-u", remote, "%s:%s" % (branch, branch), timeout=args.timeout)
    say_git(push)
    if push.code != 0:
        print("the push failed: the commits stay on the branch for the next push")
        return 1
    print("pushed the branch %s to %s" % (branch, remote))
    link = pull_request_link(push.out + "\n" + push.err)
    if link:
        print("pull request link: %s" % link)
    else:
        print("git printed no pull request link: the pull request is opened on the repo's page on the host")
    if s["dirty"]:
        print("uncommitted changes were not pushed (%d files)" % len(s["dirty"]))
    return 0


def cmd_switch_back(args):
    repo = args.repo
    s = repo_state(repo, fetch=True, timeout=args.timeout)
    if s is None:
        return no_repo(repo)
    if s["state"] == "main":
        print("the setup is on main already: nothing to switch")
        return 0
    if s["fetch"] != "ok":
        print("could not fetch from %s (%s): whether the branch is merged cannot be checked; nothing changed"
              % (s["remote"], s["fetch"]))
        return 1
    if s["dirty"]:
        print("uncommitted changes in the setup; nothing changed. Commit them on the branch, or the user decides "
              "what happens to them:")
        print_dirty(s)
        return 2
    if s["state"] == "unknown":
        print("there is no %s to go back to; nothing changed" % s["remote_main"])
        return 1
    delete = None
    if s["state"] == "detached":
        if not s["contained"] and not args.abandon:
            print("the commit %s is on no branch and not on the remote; nothing changed. Keep it first with "
                  "git branch <name>, or run again with --abandon." % s["sha"][:7])
            return 1
    elif s["state"] in ("merged", "no-commits"):
        delete = None if args.keep else "-d"
    elif args.keep:
        delete = None
    elif args.abandon:
        delete = "-D"
    else:
        print("the branch %s is not merged into %s: nothing changed. Go on with it, or with the user's yes run "
              "again with --keep (back to main, the branch kept) or --abandon (back to main, the branch deleted)."
              % (s["branch"], s["remote_main"]))
        return 1
    switch = git(repo, "switch", MAIN)
    if switch.code != 0:
        print("could not switch to main:")
        say_git(switch)
        return 1
    ff = git(repo, "merge", "--ff-only", "-q", s["remote_main"])
    if ff.code != 0:
        print("on main, but it could not be brought up to date with %s%s:"
              % (s["remote_main"], "; the branch %s is kept" % s["branch"] if s["branch"] else ""))
        say_git(ff)
        return 1
    sha = git(repo, "rev-parse", "--short", "HEAD").out
    print("on main at %s, up to date with %s" % (sha, s["remote_main"]))
    if s["branch"] is None:
        return 0
    if delete is None:
        print("the branch %s is kept" % s["branch"])
        return 0
    gone = git(repo, "branch", delete, s["branch"])
    if gone.code != 0:
        print("the branch %s could not be deleted:" % s["branch"])
        say_git(gone)
        return 1
    if delete == "-D":
        print("deleted the branch %s, not merged; its last commit was %s: git branch %s %s brings it back"
              % (s["branch"], s["sha"][:7], s["branch"], s["sha"]))
    else:
        print("deleted the merged branch %s" % s["branch"])
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Steps of the setup skills that run the same in bash and PowerShell.")
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    def add(name, func, **kwargs):
        p = sub.add_parser(name, **kwargs)
        p.add_argument("--dest", default=".", help="the project folder (default: the current folder)")
        p.set_defaults(func=func)
        return p

    add("where", cmd_where)
    add("prefixes", cmd_prefixes).add_argument("--projects", help="the folder that holds the projects")
    add("copy-template", cmd_copy_template).add_argument("profile", choices=("code", "docs"))
    add("fill-prefix", cmd_fill_prefix).add_argument("prefix")
    p = add("add-entry", cmd_add_entry)
    p.add_argument("entry", choices=sorted(ENTRY_FORMS))
    p.add_argument("--where", help="guided-sessions: the game, program or device the user tests in")
    add("check", cmd_check)
    add("base-lines", cmd_base_lines)
    add("instructions", cmd_instructions)
    add("move-instructions", cmd_move_instructions).add_argument("--profile", choices=("code", "docs"))

    def add_git(name, func, timeout, **kwargs):
        p = sub.add_parser(name, **kwargs)
        p.add_argument("--repo", default=REPO, help="the setup repo (default: the one this script lives in)")
        if timeout:
            p.add_argument("--timeout", type=int, default=timeout, help="seconds git may take on the network")
        p.set_defaults(func=func)
        return p

    p = add_git("branch-name", cmd_branch_name, 0)
    p.add_argument("topic", nargs="+", help="a few words for what the change is")
    p.add_argument("--name", help="the name part, instead of the first word of git's user.name")
    p = add_git("repo-state", cmd_repo_state, 10)
    p.add_argument("--no-fetch", action="store_true", help="judge on what was fetched before")
    p.add_argument("--hook", choices=("claude", "chatgpt"), help="print only the session-start hook's line")
    p = add_git("start-branch", cmd_start_branch, 30)
    p.add_argument("branch")
    p.add_argument("--carry", action="store_true", help="take the uncommitted changes onto the new branch")
    add_git("push-branch", cmd_push_branch, 120)
    p = add_git("switch-back", cmd_switch_back, 30)
    choice = p.add_mutually_exclusive_group()
    choice.add_argument("--keep", action="store_true", help="keep the branch (only with the user's yes)")
    choice.add_argument("--abandon", action="store_true",
                        help="delete a branch that is not merged (only with the user's yes)")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(errors="replace")     # a git message in another script on a cp1252 console
        except (AttributeError, ValueError):
            pass
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
