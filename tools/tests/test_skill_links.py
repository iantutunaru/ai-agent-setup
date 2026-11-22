"""One link per skill (SU-Q98, SU-Q110, SU-Q111). Run:  python -m unittest discover -s tools/tests

Runs global/hooks/skill-links.ps1, the link code both installs and both session-start hooks share, on temporary
folders: a fake repo's global/skills and a fake assistant skills folder. Then Claude's session-start.sh on a fake
profile: its cheap check, the call to PowerShell and the line for a PC still on the old single link. Needs
Windows (PowerShell and junctions); skipped elsewhere. Junctions are removed with cmd /c rmdir before any folder
is deleted, so a delete never reaches through a link into the repo.
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIB = os.path.join(REPO, "global", "hooks", "skill-links.ps1")
HOOK = os.path.join(REPO, "global", "hooks", "session-start.sh")
WINDOWS = sys.platform == "win32"


def is_link(path):
    """A junction or symbolic link, without following it."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return bool(getattr(st, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT) or os.path.islink(path)


def link_target(path):
    return os.path.normcase(os.path.normpath(os.readlink(path).replace("\\\\?\\", "")))


def same(a, b):
    return os.path.normcase(os.path.normpath(a)) == os.path.normcase(os.path.normpath(b))


def junction(link, target):
    subprocess.run(["cmd", "/c", "mklink", "/J", link, target], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                   check=True)


def unlink_all(folder):
    """Removes every junction under folder (the link only), without walking through any of them."""
    if is_link(folder):
        subprocess.run(["cmd", "/c", "rmdir", folder], check=True)
        return
    if not os.path.isdir(folder):
        return
    for entry in os.scandir(folder):
        if is_link(entry.path):
            subprocess.run(["cmd", "/c", "rmdir", entry.path], check=True)
        elif entry.is_dir(follow_symlinks=False):
            unlink_all(entry.path)


def make_skill(root, name):
    os.makedirs(os.path.join(root, name))
    with open(os.path.join(root, name, "SKILL.md"), "w", encoding="utf-8") as fh:
        fh.write("---\nname: %s\n---\n" % name)


def ps_quote(text):
    return "'" + text.replace("'", "''") + "'"


def git_bash():
    """Git for Windows' bash (the one Claude Code runs hooks in), not WSL's."""
    git = shutil.which("git")
    if not git:
        return None
    here = os.path.dirname(git)
    for _ in range(4):
        candidate = os.path.join(here, "bin", "bash.exe")
        if os.path.isfile(candidate):
            return candidate
        here = os.path.dirname(here)
    return None


@unittest.skipUnless(WINDOWS, "needs Windows: PowerShell and junctions")
class Base(unittest.TestCase):
    def setUp(self):
        # the long form of the path: a temp folder can come in its short 8.3 form (C:\Users\RUNNER~1 on
        # GitHub's Windows machines), while a junction's target reads back in the long one
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="skill-links-"))
        self.skills = os.path.join(self.tmp, "repo", "global", "skills")
        os.makedirs(self.skills)
        for name in ("alpha", "beta"):
            make_skill(self.skills, name)
        os.makedirs(os.path.join(self.skills, "notaskill"))           # a folder without SKILL.md
        with open(os.path.join(self.skills, "README-sources.md"), "w", encoding="utf-8") as fh:
            fh.write("a file, not a skill\n")
        self.target = os.path.join(self.tmp, "profile", "skills")

    def tearDown(self):
        unlink_all(self.tmp)

        def writable(func, path, _):          # git keeps its objects read-only
            os.chmod(path, stat.S_IWRITE)
            func(path)
        if sys.version_info >= (3, 12):
            shutil.rmtree(self.tmp, onexc=writable)
        else:
            shutil.rmtree(self.tmp, onerror=writable)

    def ps(self, code, check=True):
        # PowerShell writes in the console's OEM codepage (cp866 on a ru-RU PC), and its error frame is in the
        # PC's language ("строка:1 знак:57"), so it is told to write UTF-8. CREATE_NO_WINDOW gives it a console
        # of its own: otherwise setting OutputEncoding switches the code page of the console the tests run in.
        # The phrases the tests look for are the English text of skill-links.ps1's own throws.
        script = ("[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false); $ErrorActionPreference = 'Stop'; "
                  ". %s; %s") % (ps_quote(LIB), code)
        run = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                              "-Command", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             encoding="utf-8", errors="replace", creationflags=subprocess.CREATE_NO_WINDOW)
        if check:
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        run.said = " ".join((run.stdout + run.stderr).split())     # PowerShell wraps its error text
        return run

    def sync(self, skills=None, target=None):
        """Runs Sync-SkillLinks; returns {name: action} and the hook's line."""
        code = ("$r = Sync-SkillLinks %s %s; $r | ForEach-Object { 'R ' + $_.Name + '=' + $_.Action }; "
                "'H ' + (Get-SkillLinkHookLine $r 'X')") % (ps_quote(skills or self.skills),
                                                            ps_quote(target or self.target))
        out = self.ps(code).stdout.splitlines()
        actions = dict(line[2:].split("=", 1) for line in out if line.startswith("R "))
        hook = [line[2:] for line in out if line.startswith("H ")][0].strip()
        return actions, hook

    def assertLinked(self, name):
        path = os.path.join(self.target, name)
        self.assertTrue(is_link(path), "%s is not a link" % path)
        self.assertTrue(same(link_target(path), os.path.join(self.skills, name)))


class SyncSkillLinks(Base):
    def test_first_run_links_each_skill_and_nothing_else(self):
        actions, hook = self.sync()
        self.assertEqual(actions, {"alpha": "linked", "beta": "linked"})
        self.assertLinked("alpha")
        self.assertLinked("beta")
        self.assertEqual(sorted(os.listdir(self.target)), ["alpha", "beta"])
        self.assertIn("linked alpha, beta", hook)

    def test_second_run_changes_nothing_and_the_hook_stays_silent(self):
        self.sync()
        actions, hook = self.sync()
        self.assertEqual(actions, {"alpha": "ok", "beta": "ok"})
        self.assertEqual(hook, "")

    def test_a_persons_own_skill_folder_is_left_alone(self):
        make_skill(self.target, "mine")
        actions, _ = self.sync()
        self.assertNotIn("mine", actions)
        self.assertFalse(is_link(os.path.join(self.target, "mine")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "mine", "SKILL.md")))

    def test_a_folder_with_a_skills_name_is_kept(self):
        make_skill(self.target, "alpha")
        with open(os.path.join(self.target, "alpha", "own.txt"), "w", encoding="utf-8") as fh:
            fh.write("mine")
        actions, hook = self.sync()
        self.assertEqual(actions["alpha"], "kept")
        self.assertFalse(is_link(os.path.join(self.target, "alpha")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "alpha", "own.txt")))
        self.assertNotIn("alpha", hook)

    def test_stale_links_are_removed_and_other_links_kept(self):
        self.sync()
        make_skill(self.skills, "gamma")
        self.sync()
        shutil.rmtree(os.path.join(self.skills, "gamma"))             # the skill leaves the repo
        junction(os.path.join(self.target, "notaskill"), os.path.join(self.skills, "notaskill"))
        elsewhere = os.path.join(self.tmp, "elsewhere")
        make_skill(self.tmp, "elsewhere")
        junction(os.path.join(self.target, "theirs"), elsewhere)      # a link of the person's own
        actions, hook = self.sync()
        self.assertEqual(actions["gamma"], "removed")
        self.assertEqual(actions["notaskill"], "removed")
        self.assertNotIn("theirs", actions)
        self.assertFalse(os.path.lexists(os.path.join(self.target, "gamma")))
        self.assertTrue(is_link(os.path.join(self.target, "theirs")))
        self.assertTrue(os.path.isdir(os.path.join(self.skills, "notaskill")), "rmdir reached the target")
        self.assertIn("removed", hook)
        self.assertIn("gamma", hook)

    def test_a_new_skill_is_linked_and_named_in_the_hook_line(self):
        self.sync()
        make_skill(self.skills, "gamma")
        actions, hook = self.sync()
        self.assertEqual(actions["gamma"], "linked")
        self.assertLinked("gamma")
        self.assertEqual(hook, "agent-setup: skill links in X: linked gamma.")

    def test_a_link_to_an_old_place_is_repointed(self):
        old = os.path.join(self.tmp, "old-repo", "global", "skills")
        make_skill(old, "alpha")
        os.makedirs(self.target)
        junction(os.path.join(self.target, "alpha"), os.path.join(old, "alpha"))
        actions, _ = self.sync()
        self.assertEqual(actions["alpha"], "relinked")
        self.assertLinked("alpha")
        self.assertTrue(os.path.isfile(os.path.join(old, "alpha", "SKILL.md")))

    def test_the_repo_reached_through_a_link_counts_as_the_same(self):
        # the ChatGPT hook runs from %USERPROFILE%\.codex\setup, Claude's from ~/.claude/setup
        self.sync()
        setup = os.path.join(self.tmp, "setup")
        junction(setup, os.path.join(self.tmp, "repo"))
        actions, hook = self.sync(skills=os.path.join(setup, "global", "skills"))
        self.assertEqual(actions, {"alpha": "ok", "beta": "ok"})
        self.assertEqual(hook, "")

    def test_a_single_link_as_target_is_refused(self):
        os.makedirs(os.path.dirname(self.target))
        junction(self.target, self.skills)
        run = self.ps("Sync-SkillLinks %s %s" % (ps_quote(self.skills), ps_quote(self.target)), check=False)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("install.ps1", run.said)
        self.assertEqual(sorted(os.listdir(self.skills)), ["README-sources.md", "alpha", "beta", "notaskill"])


    def test_a_file_in_the_way_stops_with_a_reason(self):
        os.makedirs(os.path.dirname(self.target))
        with open(self.target, "w", encoding="utf-8") as fh:
            fh.write("not a folder")
        run = self.ps("Sync-SkillLinks %s %s" % (ps_quote(self.skills), ps_quote(self.target)), check=False)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("is not a folder", run.said)

    def test_failures_make_one_short_hook_line(self):
        code = ("$r = @((New-SkillLinkResult 'a' 'failed' 'denied'), (New-SkillLinkResult 'b' 'failed' 'denied'), "
                "(New-SkillLinkResult 'c' 'linked' '')); Get-SkillLinkHookLine $r 'X'")
        self.assertEqual(self.ps(code).stdout.strip(),
                         "agent-setup: skill links in X: linked c; could not link a, b (denied).")


class FromOneJunction(Base):
    """install.ps1 step 2 on a PC set up by the old install: ~/.claude/skills was one junction to global/skills."""

    def migrate(self):
        code = ("$a = Convert-SkillsJunction {t} {s}; New-Item -ItemType Directory -Force -Path {t} | Out-Null; "
                "$b = Move-SyncedSkills {s} {t}; 'C ' + $a; 'M ' + $b").format(t=ps_quote(self.target),
                                                                           s=ps_quote(self.skills))
        out = self.ps(code).stdout.splitlines()
        return ([line[2:] for line in out if line.startswith("C ")][0],
                [line[2:] for line in out if line.startswith("M ")][0])

    def make_synced(self):
        synced = os.path.join(self.skills, "synced", "account", "org", "some-skill")
        os.makedirs(synced)
        for name in ("SKILL.md", "notes.txt"):
            with open(os.path.join(synced, name), "w", encoding="utf-8") as fh:
                fh.write(name)
        with open(os.path.join(self.skills, "synced", ".manifest"), "w", encoding="utf-8") as fh:
            fh.write("hidden-ish")

    def test_the_junction_becomes_a_folder_and_synced_moves_out_of_the_repo(self):
        os.makedirs(os.path.dirname(self.target))
        junction(self.target, self.skills)
        self.make_synced()
        converted, moved = self.migrate()
        self.assertIn("one link", converted)
        self.assertIn("moved", moved)
        self.assertFalse(is_link(self.target))
        self.assertTrue(os.path.isdir(self.target))
        self.assertTrue(os.path.isfile(os.path.join(self.skills, "alpha", "SKILL.md")), "rmdir reached the repo")
        self.assertFalse(os.path.exists(os.path.join(self.skills, "synced")))
        moved_skill = os.path.join(self.target, "synced", "account", "org", "some-skill")
        self.assertEqual(sorted(os.listdir(moved_skill)), ["SKILL.md", "notes.txt"])
        self.assertTrue(os.path.isfile(os.path.join(self.target, "synced", ".manifest")))
        actions, _ = self.sync()
        self.assertEqual(actions, {"alpha": "linked", "beta": "linked"})
        self.assertFalse(is_link(os.path.join(self.target, "synced")))

    def test_a_dead_junction_after_a_rename_is_replaced(self):
        old = os.path.join(self.tmp, "old-name", "global", "skills")
        os.makedirs(old)
        os.makedirs(os.path.dirname(self.target))
        junction(self.target, old)
        shutil.rmtree(os.path.join(self.tmp, "old-name"))
        converted, moved = self.migrate()
        self.assertIn("one link", converted)
        self.assertEqual(moved, "")
        self.assertFalse(is_link(self.target))

    def test_a_junction_to_something_else_is_refused(self):
        other = os.path.join(self.tmp, "my-own-skills")
        make_skill(other, "mine")
        os.makedirs(os.path.dirname(self.target))
        junction(self.target, other)
        run = self.ps("Convert-SkillsJunction %s %s" % (ps_quote(self.target), ps_quote(self.skills)), check=False)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("move it away first", run.said)
        self.assertTrue(is_link(self.target))

    def test_a_plain_folder_is_not_converted(self):
        make_skill(self.target, "mine")
        converted, moved = self.migrate()
        self.assertEqual((converted, moved), ("", ""))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "mine", "SKILL.md")))

    def test_synced_is_left_when_the_profile_has_one_already(self):
        self.make_synced()
        os.makedirs(os.path.join(self.target, "synced"))
        _, moved = self.migrate()
        self.assertIn("left both", moved)
        self.assertTrue(os.path.isdir(os.path.join(self.skills, "synced")))


@unittest.skipUnless(WINDOWS and git_bash(), "needs Windows and Git for Windows' bash")
class ClaudeHook(Base):
    """session-start.sh on a fake profile whose ~/.claude/setup points at a fake repo (a git repo, no upstream)."""

    def setUp(self):
        super().setUp()
        repo = os.path.join(self.tmp, "repo")
        hooks = os.path.join(repo, "global", "hooks")
        os.makedirs(hooks)
        for name in ("session-start.sh", "skill-links.ps1"):
            shutil.copyfile(os.path.join(REPO, "global", "hooks", name), os.path.join(hooks, name))
        os.makedirs(os.path.join(repo, "local"))
        with open(os.path.join(repo, "local", "personal.md"), "w", encoding="utf-8") as fh:
            fh.write("# me\n")
        with open(os.path.join(repo, ".gitignore"), "w", encoding="utf-8") as fh:
            fh.write("local/\n")
        self.git = ["git", "-C", repo, "-c", "user.name=test", "-c", "user.email=test@example.invalid",
                    "-c", "core.autocrlf=false"]
        subprocess.run(["git", "init", "-q", repo], check=True)
        # on main, as the setup is (SU-Q95): on any other branch the hook prints a line about it
        subprocess.run(self.git + ["symbolic-ref", "HEAD", "refs/heads/main"], check=True)
        self.commit()
        self.home = os.path.join(self.tmp, "home")
        self.claude = os.path.join(self.home, ".claude")
        os.makedirs(self.claude)
        junction(os.path.join(self.claude, "setup"), repo)
        with open(os.path.join(self.claude, "CLAUDE.md"), "w", encoding="utf-8") as fh:
            fh.write("@~/.claude/setup/global/CLAUDE.md\n@~/.claude/setup/local/personal.md\n")
        self.target = os.path.join(self.claude, "skills")

    def commit(self):
        subprocess.run(self.git + ["add", "-A"], check=True)
        subprocess.run(self.git + ["commit", "-q", "--allow-empty", "-m", "x"], check=True)

    def hook(self):
        env = dict(os.environ, HOME=self.home)
        run = subprocess.run([git_bash(), os.path.join(self.claude, "setup", "global", "hooks", "session-start.sh")],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, env=env,
                             timeout=60)
        self.assertEqual(run.returncode, 0, run.stderr)
        return [line for line in run.stdout.splitlines() if line.strip()]

    def test_links_after_a_pull_then_silent(self):
        os.makedirs(self.target)
        lines = self.hook()
        self.assertEqual(len(lines), 1, lines)
        self.assertIn("linked alpha, beta", lines[0])
        self.assertLinked("alpha")
        self.assertEqual(self.hook(), [])

    def test_a_removed_skill_loses_its_link(self):
        os.makedirs(self.target)
        self.hook()
        shutil.rmtree(os.path.join(self.skills, "beta"))
        self.commit()
        lines = self.hook()
        self.assertEqual(len(lines), 1, lines)
        self.assertIn("removed beta", lines[0])
        self.assertFalse(os.path.lexists(os.path.join(self.target, "beta")))

    def test_a_same_name_folder_does_not_call_powershell_each_time(self):
        make_skill(self.target, "alpha")
        self.hook()
        self.assertEqual(self.hook(), [])
        self.assertFalse(is_link(os.path.join(self.target, "alpha")))

    def test_the_old_single_link_gets_one_line_and_no_change(self):
        junction(self.target, os.path.join(self.claude, "setup", "global", "skills"))
        lines = self.hook()
        self.assertEqual(len(lines), 1, lines)
        self.assertIn("still one link", lines[0])
        self.assertIn("install.ps1", lines[0])
        self.assertTrue(is_link(self.target))
        self.assertEqual(sorted(os.listdir(self.skills)), ["README-sources.md", "alpha", "beta", "notaskill"])


if __name__ == "__main__":
    unittest.main()
