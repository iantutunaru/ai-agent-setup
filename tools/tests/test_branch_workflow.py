"""The setup repo's branch workflow (SU-Q93, SU-Q95, SU-Q108, SU-Q112). Run:  python -m unittest discover -s tools/tests

The branch commands of tools/setup_tools.py on temporary git repos: a bare remote and two clones, as two PCs. A
pull request is played by a merge with --no-ff in the second clone, pushed, and the branch deleted on the remote,
as GitHub does (SU-Q108). These need only git and run on Linux too. Then both session-start hooks on such a repo:
those need Windows (PowerShell, junctions, Git for Windows' bash) and are skipped elsewhere.
"""
import contextlib
import io
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import setup_tools  # noqa: E402
from test_skill_links import WINDOWS, git_bash, junction, make_skill, unlink_all  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))


def run(*argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = setup_tools.main(list(argv))
    return code, out.getvalue()


def put(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def remove_tree(path):
    def writable(func, target, _):          # git keeps its objects read-only
        os.chmod(target, stat.S_IWRITE)
        func(target)
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=writable)
    else:
        shutil.rmtree(path, onerror=writable)


class Repos(unittest.TestCase):
    """origin.git (bare), one (this PC's setup) and two (the other PC, where the pull request is merged)."""

    def setUp(self):
        # the long form: a temp folder can come in its short 8.3 form on GitHub's Windows machines
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="branch-flow-"))
        self.origin = os.path.join(self.tmp, "origin.git")
        self.one = os.path.join(self.tmp, "one")
        self.two = os.path.join(self.tmp, "two")
        self.g(self.tmp, "init", "-q", "--bare", self.origin)
        self.g(self.origin, "symbolic-ref", "HEAD", "refs/heads/main")
        self.g(self.tmp, "init", "-q", self.one)
        self.g(self.one, "symbolic-ref", "HEAD", "refs/heads/main")     # never the default branch name
        self.configure(self.one)
        self.populate(self.one)
        self.g(self.one, "add", "-A")
        self.g(self.one, "commit", "-q", "-m", "first")
        self.g(self.one, "remote", "add", "origin", self.origin)
        self.g(self.one, "push", "-q", "-u", "origin", "main")
        self.g(self.tmp, "clone", "-q", self.origin, self.two)
        self.configure(self.two)

    def tearDown(self):
        if WINDOWS:
            unlink_all(self.tmp)                # the hooks' setup links, before any folder is deleted
        remove_tree(self.tmp)

    def populate(self, repo):
        put(os.path.join(repo, "README.md"), "setup\n")

    def configure(self, repo):
        for key, value in (("user.name", "Ianis Test"), ("user.email", "test@example.invalid"),
                           ("core.autocrlf", "false"), ("commit.gpgsign", "false")):
            self.g(repo, "config", key, value)

    def g(self, repo, *args):
        run_ = subprocess.run(["git", "-C", repo] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              universal_newlines=True)
        self.assertEqual(run_.returncode, 0, "git %s: %s%s" % (" ".join(args), run_.stdout, run_.stderr))
        return run_.stdout.strip()

    def commit(self, repo, name, text="x\n"):
        put(os.path.join(repo, name), text)
        self.g(repo, "add", name)
        self.g(repo, "commit", "-q", "-m", "add " + name)
        return self.g(repo, "rev-parse", "HEAD")

    def state(self, repo=None, fetch=True):
        return setup_tools.repo_state(repo or self.one, fetch=fetch)

    def branch_with_commit(self, branch="ianis/fix-a-rule", push=True):
        code, out = run("start-branch", branch, "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.commit(self.one, "rule.md")
        if push:
            code, out = run("push-branch", "--repo", self.one)
            self.assertEqual(code, 0, out)
        return branch

    def merge_on_github(self, branch):
        """What merging the pull request does on GitHub: a merge commit on main, the branch deleted (SU-Q108)."""
        self.g(self.two, "fetch", "-q", "origin")
        self.g(self.two, "switch", "-q", "main")
        self.g(self.two, "merge", "-q", "--no-ff", "-m", "Merge pull request #1", "origin/" + branch)
        self.g(self.two, "push", "-q", "origin", "main")
        self.g(self.two, "push", "-q", "origin", "--delete", branch)

    def current(self, repo=None):
        return self.g(repo or self.one, "symbolic-ref", "--short", "-q", "HEAD")

    def local_branches(self, repo=None):
        return self.g(repo or self.one, "for-each-ref", "--format=%(refname:short)", "refs/heads").split()

    def remote_branches(self):
        return self.g(self.origin, "for-each-ref", "--format=%(refname:short)", "refs/heads").split()


class BranchName(Repos):
    def test_name_from_the_first_word_of_user_name(self):
        self.assertEqual(setup_tools.branch_name("Ianis Tutunaru", "Fix the hook line"), "ianis/fix-the-hook-line")

    def test_accents_and_signs_are_made_safe(self):
        self.assertEqual(setup_tools.branch_name("Zoë Müller", "Größe: the 2nd rule!"),
                         "zoe/gro-e-the-2nd-rule")
        self.assertEqual(setup_tools.branch_name("Jean-Luc Picard", "x"), "jean-luc/x")

    def test_a_name_with_no_usable_letter_asks_for_one(self):
        with self.assertRaises(ValueError) as caught:
            setup_tools.branch_name("Ианис", "topic")
        self.assertIn("--name", str(caught.exception))
        with self.assertRaises(ValueError):
            setup_tools.branch_name("", "topic")
        with self.assertRaises(ValueError):
            setup_tools.branch_name("Ianis", "!!!")

    def test_a_long_topic_is_cut_at_a_hyphen(self):
        name = setup_tools.branch_name("Ianis", "one two three four five six seven eight nine ten eleven")
        self.assertEqual(name, "ianis/one-two-three-four-five-six-seven-eight")

    def test_the_command_reads_user_name_of_the_repo(self):
        code, out = run("branch-name", "Branch", "workflow", "--repo", self.one)
        self.assertEqual((code, out.strip()), (0, "ianis/branch-workflow"))
        code, out = run("branch-name", "x", "--name", "Test Person", "--repo", self.one)
        self.assertEqual(out.strip(), "test/x")


class StateAndBranch(Repos):
    def test_main_up_to_date(self):
        s = self.state()
        self.assertEqual((s["state"], s["branch"], s["fetch"], s["dirty"]), ("main", "main", "ok", []))
        self.assertEqual(setup_tools.hook_line(s, "claude"), "")

    def test_start_branch_brings_main_up_to_date_first(self):
        theirs = self.commit(self.two, "theirs.md")
        self.g(self.two, "push", "-q", "origin", "main")
        code, out = run("start-branch", "ianis/new-thing", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.current(), "ianis/new-thing")
        self.assertEqual(self.g(self.one, "rev-parse", "HEAD"), theirs)
        self.assertEqual(self.g(self.one, "rev-parse", "main"), theirs)
        self.assertEqual(self.state()["state"], "no-commits")

    def test_a_branch_moves_through_its_states(self):
        run("start-branch", "ianis/fix-a-rule", "--repo", self.one)
        self.commit(self.one, "rule.md")
        s = self.state()
        self.assertEqual((s["state"], s["upstream"]), ("no-upstream", None))
        self.assertEqual(len(s["own"]), 1)
        code, out = run("push-branch", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertIn("ianis/fix-a-rule", self.remote_branches())
        self.assertIn("no pull request link", out)        # a bare remote prints none
        s = self.state()
        self.assertEqual((s["state"], s["upstream"], s["unpushed"]), ("not-merged", "origin/ianis/fix-a-rule", 0))
        self.merge_on_github("ianis/fix-a-rule")
        self.assertEqual(self.state(fetch=False)["state"], "not-merged")    # not fetched yet
        s = self.state()
        self.assertEqual(s["state"], "merged")
        self.assertTrue(s["upstream_gone"])

    def test_more_commits_on_an_open_change(self):
        branch = self.branch_with_commit()
        self.commit(self.one, "more.md")
        self.assertEqual(self.state()["unpushed"], 1)
        code, out = run("push-branch", "--repo", self.one)
        self.assertEqual(code, 0, out)
        s = self.state()
        self.assertEqual((s["state"], s["unpushed"], len(s["own"])), ("not-merged", 0, 2))
        self.assertEqual(self.g(self.origin, "rev-parse", branch), self.g(self.one, "rev-parse", "HEAD"))

    def test_start_branch_refuses_off_main_a_taken_name_and_uncommitted_changes(self):
        put(os.path.join(self.one, "README.md"), "changed\n")
        code, out = run("start-branch", "ianis/x", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("--carry", out)
        self.assertIn("README.md", out)
        self.assertEqual(self.current(), "main")
        code, out = run("start-branch", "ianis/x", "--carry", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.current(), "ianis/x")
        self.assertTrue(self.state()["dirty"])
        code, out = run("start-branch", "ianis/y", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("not on main", out)
        self.g(self.one, "commit", "-q", "-am", "x")
        run("push-branch", "--repo", self.one)
        self.g(self.one, "switch", "-q", "main")
        self.g(self.one, "branch", "-q", "-D", "ianis/x")
        code, out = run("start-branch", "ianis/x", "--repo", self.one)        # still on the remote
        self.assertEqual(code, 2)
        self.assertIn("already there", out)
        code, out = run("start-branch", "main", "--repo", self.one)
        self.assertEqual(code, 2)

    def test_push_branch_never_pushes_main(self):
        before = self.g(self.origin, "rev-parse", "main")
        self.commit(self.one, "on-main.md")
        code, out = run("push-branch", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("never pushed", out)
        self.assertEqual(self.g(self.origin, "rev-parse", "main"), before)

    def test_push_branch_refuses_detached_merged_and_empty_branches(self):
        self.g(self.one, "switch", "-q", "--detach")
        self.assertEqual(run("push-branch", "--repo", self.one)[0], 2)
        self.g(self.one, "switch", "-q", "main")
        run("start-branch", "ianis/empty", "--repo", self.one)
        code, out = run("push-branch", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("no commits of its own", out)
        self.g(self.one, "switch", "-q", "main")
        branch = self.branch_with_commit()
        self.merge_on_github(branch)
        self.state()                                                     # the fetch
        code, out = run("push-branch", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("merged already", out)
        self.assertNotIn(branch, self.remote_branches())

    def test_detached(self):
        self.g(self.one, "switch", "-q", "--detach")
        s = self.state()
        self.assertEqual((s["state"], s["contained"]), ("detached", True))
        self.commit(self.one, "loose.md")
        self.assertFalse(self.state()["contained"])

    def test_a_second_pc_on_main_the_whole_time(self):
        branch = self.branch_with_commit()
        self.merge_on_github(branch)
        s = self.state(self.two)
        self.assertEqual(s["state"], "main")
        self.assertEqual(setup_tools.hook_line(s, "claude"), "")
        code, out = run("repo-state", "--repo", self.two)
        self.assertIn("state: main", out)

    def test_the_fetch_fails(self):
        self.branch_with_commit()
        self.g(self.one, "remote", "set-url", "origin", os.path.join(self.tmp, "no-such-remote.git"))
        s = self.state()
        self.assertNotIn(s["fetch"], ("ok", "skipped"))
        self.assertEqual(s["state"], "not-merged")                      # judged on what was fetched before
        code, out = run("repo-state", "--repo", self.one)
        self.assertIn("the fetch failed", out)


class HookLine(Repos):
    def test_each_state_gives_one_line(self):
        branch = self.branch_with_commit(push=False)
        line = setup_tools.hook_line(self.state(), "claude")
        self.assertTrue(line.startswith("agent-setup: the setup is on the branch ianis/fix-a-rule, not on main"))
        self.assertIn("no updates from main", line)
        self.assertIn("not pushed yet", line)
        run("push-branch", "--repo", self.one)
        line = setup_tools.hook_line(self.state(), "claude")
        self.assertTrue(line.endswith("gets no updates from main meanwhile."), line)
        self.merge_on_github(branch)
        s = self.state()
        claude, chatgpt = setup_tools.hook_line(s, "claude"), setup_tools.hook_line(s, "chatgpt")
        self.assertIn("is merged into main", claude)
        self.assertIn("run /setup-promote to switch back", claude)
        self.assertIn("run the setup-promote skill to switch back", chatgpt)
        self.assertNotIn("/setup-promote", chatgpt)
        code, out = run("repo-state", "--hook", "claude", "--repo", self.one)
        self.assertEqual(out.strip(), claude)
        for text in (claude, chatgpt):
            self.assertNotIn("\n", text)
            self.assertNotIn("\u2014", text)
            self.assertNotIn("\u2013", text)

    def test_fetch_impossible_and_detached(self):
        self.branch_with_commit()
        self.g(self.one, "remote", "set-url", "origin", os.path.join(self.tmp, "gone.git"))
        line = setup_tools.hook_line(self.state(), "claude")
        self.assertIn("could not be checked", line)
        self.g(self.one, "switch", "-q", "--detach")
        line = setup_tools.hook_line(self.state(), "chatgpt")
        self.assertIn("detached HEAD", line)
        self.assertIn("the setup-promote skill", line)

    def test_not_a_repo(self):
        os.makedirs(os.path.join(self.tmp, "empty"))
        self.assertIn("could not read", setup_tools.hook_line(self.state(os.path.join(self.tmp, "empty")), "claude"))

    def test_the_pull_request_link_github_prints(self):
        text = ("remote: \nremote: Create a pull request for 'ianis/x' on GitHub by visiting:\n"
                "remote:      https://github.com/owner/agent-setup/pull/new/ianis/x\nremote: \n"
                "To https://github.com/owner/agent-setup.git\n * [new branch]      ianis/x -> ianis/x\n")
        self.assertEqual(setup_tools.pull_request_link(text), "https://github.com/owner/agent-setup/pull/new/ianis/x")
        self.assertIsNone(setup_tools.pull_request_link("To /tmp/origin.git\n * [new branch] x -> x\n"))


class SwitchBack(Repos):
    def test_after_the_merge_back_on_main_and_the_branch_gone(self):
        branch = self.branch_with_commit()
        self.merge_on_github(branch)
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.current(), "main")
        self.assertEqual(self.local_branches(), ["main"])
        self.assertEqual(self.g(self.one, "rev-parse", "main"), self.g(self.origin, "rev-parse", "main"))
        self.assertIn("deleted the merged branch", out)
        self.assertEqual(setup_tools.hook_line(self.state(), "claude"), "")

    def test_a_branch_with_nothing_of_its_own_is_deleted(self):
        run("start-branch", "ianis/nothing", "--repo", self.one)
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.local_branches(), ["main"])

    def test_not_merged_changes_nothing_without_the_users_yes(self):
        branch = self.branch_with_commit()
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 1)
        self.assertIn("not merged", out)
        self.assertEqual(self.current(), branch)
        code, out = run("switch-back", "--keep", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.current(), "main")
        self.assertIn(branch, self.local_branches())
        self.g(self.one, "switch", "-q", branch)
        tip = self.g(self.one, "rev-parse", "HEAD")
        code, out = run("switch-back", "--abandon", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.local_branches(), ["main"])
        self.assertIn(tip, out)                                           # how to bring it back
        self.assertIn(branch, self.remote_branches())                     # the remote's copy is the user's to delete

    def test_uncommitted_changes_or_no_fetch_change_nothing(self):
        branch = self.branch_with_commit()
        self.merge_on_github(branch)
        put(os.path.join(self.one, "rule.md"), "edited\n")
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 2)
        self.assertIn("rule.md", out)
        self.assertEqual(self.current(), branch)
        self.g(self.one, "checkout", "--", "rule.md")
        self.g(self.one, "remote", "set-url", "origin", os.path.join(self.tmp, "gone.git"))
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 1)
        self.assertIn("could not fetch", out)
        self.assertEqual(self.current(), branch)

    def test_detached_returns_to_main_only_when_nothing_is_lost(self):
        self.g(self.one, "switch", "-q", "--detach")
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.current(), "main")
        self.g(self.one, "switch", "-q", "--detach")
        self.commit(self.one, "loose.md")
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 1)
        self.assertIn("git branch", out)

    def test_on_main_already(self):
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 0)
        self.assertIn("main already", out)


# --- both session-start hooks on a branch -----------------------------------------------------------------------

HOOK_FILES = ["session-start.sh", "session-start.ps1", "skill-links.ps1", "build-agents-md.ps1", "local-files.ps1"]


@unittest.skipUnless(WINDOWS and git_bash(), "needs Windows: PowerShell, junctions and Git for Windows' bash")
class Hooks(Repos):
    """Each hook on a profile whose setup link points at clone one: one line about the branch, at most."""

    def populate(self, repo):
        for name in HOOK_FILES:
            target = os.path.join(repo, "global", "hooks", name)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(os.path.join(REPO, "global", "hooks", name), target)
        os.makedirs(os.path.join(repo, "tools"))
        shutil.copyfile(os.path.join(REPO, "tools", "setup_tools.py"), os.path.join(repo, "tools", "setup_tools.py"))
        make_skill(os.path.join(repo, "global", "skills"), "alpha")
        for rel in ("global/rules.md", "global/rules-chatgpt.md", "profiles/code.md", "profiles/docs.md",
                    "global/personal.example.md", "local/personal.md"):
            put(os.path.join(repo, rel), "# %s\n" % rel)
        put(os.path.join(repo, ".gitignore"), "local/\n")

    def setUp(self):
        super().setUp()
        self.home = os.path.join(self.tmp, "home")
        self.claude = os.path.join(self.home, ".claude")
        self.codex = os.path.join(self.home, ".codex")
        self.agents = os.path.join(self.home, ".agents")
        for folder in (self.claude, self.codex, os.path.join(self.claude, "skills"), os.path.join(self.agents, "skills")):
            os.makedirs(folder, exist_ok=True)
        junction(os.path.join(self.claude, "setup"), self.one)
        junction(os.path.join(self.codex, "setup"), self.one)
        put(os.path.join(self.claude, "CLAUDE.md"),
            "@~/.claude/setup/global/CLAUDE.md\n@~/.claude/setup/local/personal.md\n")
        for hook in (self.claude_hook, self.chatgpt_hook):
            hook()                                       # the links and the rules file, made once

    def claude_hook(self):
        env = dict(os.environ, HOME=self.home)
        run_ = subprocess.run([git_bash(), os.path.join(self.claude, "setup", "global", "hooks", "session-start.sh")],
                              stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              universal_newlines=True, env=env, timeout=60)
        self.assertEqual(run_.returncode, 0, run_.stderr)
        return [line for line in run_.stdout.splitlines() if line.strip()]

    def chatgpt_hook(self):
        script = os.path.join(self.codex, "setup", "global", "hooks", "session-start.ps1")
        run_ = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File",
                               script, "-CodexDir", self.codex, "-AgentsDir", self.agents],
                              stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              universal_newlines=True, timeout=90)
        self.assertEqual(run_.returncode, 0, run_.stderr)
        return [line for line in run_.stdout.splitlines() if line.strip()]

    def both(self):
        """The lines each hook printed about the setup's branch or pull."""
        out = {}
        for tool, hook in (("claude", self.claude_hook), ("chatgpt", self.chatgpt_hook)):
            out[tool] = [l for l in hook() if l.startswith("agent-setup: the setup") or "pull" in l]
        return out

    def test_on_main_silent_and_pulled(self):
        self.assertEqual(self.both(), {"claude": [], "chatgpt": []})
        theirs = self.commit(self.two, "theirs.md")
        self.g(self.two, "push", "-q", "origin", "main")
        self.assertEqual(self.claude_hook(), [])
        self.assertEqual(self.g(self.one, "rev-parse", "HEAD"), theirs)

    def test_a_branch_not_merged_then_merged_then_back_on_main(self):
        branch = self.branch_with_commit()
        theirs = self.commit(self.two, "theirs.md")
        self.g(self.two, "push", "-q", "origin", "main")
        main_before = self.g(self.one, "rev-parse", "main")
        lines = self.both()
        for tool in ("claude", "chatgpt"):
            self.assertEqual(len(lines[tool]), 1, lines)
            self.assertIn("on the branch %s, not on main" % branch, lines[tool][0])
            self.assertIn("no updates from main", lines[tool][0])
        self.assertEqual(self.g(self.one, "rev-parse", "main"), main_before)   # no pull on a branch
        self.assertEqual(self.current(), branch)
        self.merge_on_github(branch)
        lines = self.both()
        self.assertEqual(len(lines["claude"]), 1, lines)
        self.assertIn("is merged into main", lines["claude"][0])
        self.assertIn("run /setup-promote", lines["claude"][0])
        self.assertEqual(len(lines["chatgpt"]), 1, lines)
        self.assertIn("run the setup-promote skill", lines["chatgpt"][0])
        code, out = run("switch-back", "--repo", self.one)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.both(), {"claude": [], "chatgpt": []})
        self.assertEqual(self.local_branches(), ["main"])
        self.g(self.one, "merge-base", "--is-ancestor", theirs, "HEAD")

    def test_fetch_impossible(self):
        self.branch_with_commit()
        self.g(self.one, "remote", "set-url", "origin", os.path.join(self.tmp, "gone.git"))
        lines = self.both()
        for tool in ("claude", "chatgpt"):
            self.assertEqual(len(lines[tool]), 1, lines)
            self.assertIn("could not be checked", lines[tool][0])

    def test_detached(self):
        self.g(self.one, "switch", "-q", "--detach")
        lines = self.both()
        for tool in ("claude", "chatgpt"):
            self.assertEqual(len(lines[tool]), 1, lines)
            self.assertIn("detached HEAD", lines[tool][0])

    def test_uncommitted_changes_point_at_the_branch_workflow(self):
        put(os.path.join(self.one, "README.md"), "changed\n")
        for hook in (self.claude_hook, self.chatgpt_hook):
            lines = [l for l in hook() if "uncommitted" in l]
            self.assertEqual(len(lines), 1)
            self.assertIn("setup-promote", lines[0])
            self.assertIn("on a branch", lines[0])
            self.assertIn("main is never pushed", lines[0])


if __name__ == "__main__":
    unittest.main()
