"""cleanup.py on temporary repos: what the dry run removes, what it keeps, and the doc check.

    python -m unittest discover -s global/skills/stage-close/tests
"""
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import cleanup  # noqa: E402

SID = "0b6c1a52-2f7e-4c1e-9a55-1d2e3f4a5b6c"
SID2 = "1c7d2b63-3a8f-4d2f-8b66-2e3f4a5b6c7d"
OLD = time.time() - 48 * 3600


def run(cwd, *args):
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=cwd, check=True,
                   capture_output=True)


def touch(p: Path, text: str = "x") -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def age(p: Path, when: float = OLD) -> None:
    for f in [p, *p.rglob("*")]:
        os.utime(f, (when, when))


class Repo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        self.main = self.root / "proj"
        self.main.mkdir()
        run(self.main, "init", "-q", "-b", "main")
        touch(self.main / "README.md", "# p\n")
        run(self.main, "add", ".")
        run(self.main, "commit", "-q", "-m", "init")

    def tearDown(self):
        subprocess.run(["git", "worktree", "prune"], cwd=self.main, capture_output=True)
        self.tmp.cleanup()

    def worktree(self, name: str, branch: str, commit: bool = False) -> Path:
        p = self.main / ".claude" / "worktrees" / name
        run(self.main, "worktree", "add", "-q", "-b", branch, str(p))
        if commit:
            touch(p / f"{name}.txt")
            run(p, "add", ".")
            run(p, "commit", "-q", "-m", name)
        return p


class WorktreePlanTest(Repo):
    def test_merged_clean_goes_unmerged_and_dirty_stay(self):
        merged = self.worktree("done", "claude/done")
        unmerged = self.worktree("open", "claude/open", commit=True)
        dirty = self.worktree("dirty", "claude/dirty")
        touch(dirty / "notes.txt")
        for p in (merged, unmerged, dirty):
            age(p)
        plan = {i.path.name: i for i in cleanup.worktree_plan(self.main, "main", set()) if i.path}
        self.assertEqual(plan["done"].action, "remove")
        self.assertEqual(plan["open"].action, "keep")
        self.assertIn("not merged", plan["open"].why)
        self.assertEqual(plan["dirty"].action, "keep")
        self.assertIn("--discard dirty", plan["dirty"].why)
        forced = {i.path.name: i for i in cleanup.worktree_plan(self.main, "main", {"dirty"}) if i.path}
        self.assertEqual(forced["dirty"].action, "remove")

    def test_recent_worktree_stays_even_when_merged(self):
        self.worktree("fresh", "claude/fresh")
        plan = [i for i in cleanup.worktree_plan(self.main, "main", set()) if i.path]
        self.assertEqual([(i.path.name, i.action) for i in plan], [("fresh", "keep")])

    def test_branches_without_worktree(self):
        run(self.main, "branch", "claude/old")
        run(self.main, "branch", "feature")
        plan = {i.ref: i for i in cleanup.worktree_plan(self.main, "main", set()) if i.path is None}
        self.assertEqual(plan["claude/old"].action, "remove")
        self.assertEqual(plan["feature"].action, "keep")          # merged, but not Claude's: never deleted
        self.assertNotIn("main", plan)

    def test_yes_removes_worktree_and_branch(self):
        p = self.worktree("done", "claude/done")
        age(p)
        item = next(i for i in cleanup.worktree_plan(self.main, "main", set()) if i.path and i.path.name == "done")
        msg = cleanup.remove(self.main, item, set())
        self.assertIn("deleted branch claude/done", msg)
        self.assertFalse(cleanup.registered(self.main, p))
        branches = subprocess.run(["git", "branch", "--list", "claude/done"], cwd=self.main, capture_output=True,
                                  text=True).stdout
        self.assertEqual(branches.strip(), "")

    def test_main_checkout_and_branch_from_a_worktree(self):
        p = self.worktree("w", "claude/w")
        self.assertEqual(cleanup.main_checkout(p), self.main)
        self.assertEqual(cleanup.main_branch(self.main), "main")


class ScratchTest(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(cleanup.project_slug(Path(r"E:\Projects\Demo App")), "E--Projects-Demo-App")

    def test_session_ids_of_project_and_its_worktrees_only(self):
        with tempfile.TemporaryDirectory() as d:
            root, slug = Path(d), "E--Projects-P"
            touch(root / slug / f"{SID}.jsonl")
            touch(root / f"{slug}--claude-worktrees-t1-abc" / f"{SID2}.jsonl")
            touch(root / f"{slug}-old" / "2d8e3c74-4b9a-4e3a-9c77-3f4a5b6c7d8e.jsonl")   # another project
            touch(root / slug / "notes.jsonl")
            self.assertEqual(cleanup.session_ids(root, slug), {SID, SID2})

    def test_cited_recent_and_old(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cited = touch(root / "3b8d183c862ccddc" / SID / "scratchpad" / "a.txt").parent.parent
            old = touch(root / "E--Projects-P" / SID2 / "b.txt").parent
            fresh = touch(root / "aaaa" / "2d8e3c74-4b9a-4e3a-9c77-3f4a5b6c7d8e" / "c.txt").parent
            other = touch(root / "aaaa" / "3e9f4d85-5cab-4f4b-8d88-4a5b6c7d8e9f" / "d.txt").parent
            for p in (cited, old, other):
                age(p)
            ids = {SID, SID2, fresh.name}
            plan = {i.path.name: i.action for i in cleanup.scratch_plan(root, ids, f"see {SID}/scratchpad")}
            self.assertEqual(plan, {SID: "keep", SID2: "remove", fresh.name: "keep"})
            self.assertNotIn(other.name, plan)                    # not this project's session

    def test_remove_refuses_outside_the_scratch_root(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / "claude"
            outside = touch(Path(d) / "keep" / "x.txt").parent
            item = cleanup.Item("scratch", "remove", outside, 0, "")
            self.assertTrue(cleanup.remove(Path(d), item, set(), root).startswith("REFUSED"))
            self.assertTrue(outside.exists())
            inside = touch(root / "h" / SID / "x.txt").parent
            cleanup.remove(Path(d), cleanup.Item("scratch", "remove", inside, 0, ""), set(), root)
            self.assertFalse(inside.exists())


class DocsTest(Repo):
    def test_broken_links_and_tickets_missing_from_the_index(self):
        t = self.main / "docs" / "tickets"
        touch(t / "README.md", "| [P-T01](P-T01-a.md) | x |\n")
        touch(t / "P-T01-a.md", "See [notes](P-T01-notes.md) and [b](../design.md#top) and [web](https://x.org).\n")
        touch(t / "P-T01-notes.md", "companion\n")
        touch(t / "P-T02-b.md", "orphan\n")
        touch(self.main / "docs" / "design.md", "[gone](missing.md) [root](/README.md) `[code](nowhere.md)`\n"
                                                 "```\n[fenced](nowhere2.md)\n```\n[space](my%20file.md)\n")
        touch(self.main / "docs" / "my file.md")
        touch(self.main / ".gitignore", "ignored/\n")
        touch(self.main / "ignored" / "x.md", "[bad](zzz.md)\n")
        lines = sorted(i.why for i in cleanup.doc_issues(self.main))
        self.assertEqual(lines, ["docs/design.md: broken link missing.md",
                                 "docs/tickets/P-T02-b.md is not in the index"])


if __name__ == "__main__":
    unittest.main()
