"""Tests for tools/setup_tools.py. Run:  python -m unittest discover -s tools/tests"""
import contextlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import setup_tools  # noqa: E402


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


def get(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


class Base(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="setup-tools-")
        self.dest = os.path.join(self.root, "New Project")
        os.makedirs(self.dest)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)


class CopyTemplate(Base):
    def test_code_profile_copies_base_and_profile(self):
        code, out = run("copy-template", "code", "--dest", self.dest)
        self.assertEqual(code, 0)
        for rel in (".gitignore", ".gitattributes", "AGENTS.md", "CLAUDE.md",
                    os.path.join("docs", "tickets", "README.md"), os.path.join("docs", "decisions", "README.md")):
            self.assertTrue(os.path.isfile(os.path.join(self.dest, rel)), rel)
        self.assertEqual(get(os.path.join(self.dest, "CLAUDE.md")),
                         "@~/.claude/setup/profiles/code.md\n@AGENTS.md\n")
        self.assertIn("Profile: code", get(os.path.join(self.dest, "AGENTS.md")))

    def test_docs_profile(self):
        run("copy-template", "docs", "--dest", self.dest)
        self.assertTrue(os.path.isfile(os.path.join(self.dest, "decisions.md")))
        self.assertIn("Profile: docs", get(os.path.join(self.dest, "AGENTS.md")))
        self.assertFalse(os.path.exists(os.path.join(self.dest, "docs", "tickets")))

    def test_never_overwrites(self):
        put(os.path.join(self.dest, ".gitignore"), "mine\n")
        put(os.path.join(self.dest, "notes.txt"), "the user's file\n")
        code, out = run("copy-template", "docs", "--dest", self.dest)
        self.assertEqual(get(os.path.join(self.dest, ".gitignore")), "mine\n")
        self.assertEqual(get(os.path.join(self.dest, "notes.txt")), "the user's file\n")
        self.assertIn("kept    .gitignore", out)
        # a second run copies nothing
        code, out = run("copy-template", "docs", "--dest", self.dest)
        self.assertIn("done: 0 copied", out)

    def test_bytes_are_copied_unchanged(self):
        run("copy-template", "code", "--dest", self.dest)
        src = os.path.join(setup_tools.TEMPLATE, "base", ".gitattributes")
        with open(src, "rb") as a, open(os.path.join(self.dest, ".gitattributes"), "rb") as b:
            self.assertEqual(a.read(), b.read())


class FillAndCheck(Base):
    def test_fill_prefix_then_check_lists_open_placeholders(self):
        run("copy-template", "code", "--dest", self.dest)
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 1)
        self.assertIn("still holds <P>", out)
        code, out = run("fill-prefix", "ZZ", "--dest", self.dest)
        self.assertEqual(code, 0)
        self.assertIn("ZZ-Qnn", get(os.path.join(self.dest, "AGENTS.md")))
        code, out = run("check", "--dest", self.dest)
        self.assertNotIn("still holds <P>", out)
        self.assertIn("placeholder  AGENTS.md", out)          # <Project name> and the others are still open
        self.assertEqual(code, 1)

    def test_check_passes_when_all_is_filled(self):
        put(os.path.join(self.dest, "AGENTS.md"), "# Demo\n\nProfile: docs\n\nA paragraph.\n")
        put(os.path.join(self.dest, "decisions.md"), "# Decisions\n\n- **ZZ-Q01 Profile.** docs.\n")
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 0, out)

    def test_ticket_skeleton_placeholders_do_not_count(self):
        run("copy-template", "code", "--dest", self.dest)
        run("fill-prefix", "ZZ", "--dest", self.dest)
        put(os.path.join(self.dest, "AGENTS.md"), "# Demo\n\nProfile: code\n")
        put(os.path.join(self.dest, "docs", "decisions", "README.md"), "# Decisions\n")
        code, out = run("check", "--dest", self.dest)      # docs/tickets/README.md keeps its <title> skeleton
        self.assertEqual(code, 0, out)

    def test_bad_prefix(self):
        run("copy-template", "docs", "--dest", self.dest)
        code, out = run("fill-prefix", "toolong", "--dest", self.dest)
        self.assertEqual(code, 2)


class CheckBackticks(Base):
    """A name pattern in backticks is not an open placeholder (SU-Q147)."""

    def check_agents(self, body):
        put(os.path.join(self.dest, "AGENTS.md"), "# Demo\n\nProfile: code\n\n" + body)
        return run("check", "--dest", self.dest)

    def test_a_pattern_in_backticks_passes(self):
        code, out = self.check_agents("  - Playtests: checklists in `docs/sessions/<ticket>-r<N>.md`; `<a>` too\n")
        self.assertEqual(code, 0, out)

    def test_a_placeholder_beside_backticks_still_counts(self):
        code, out = self.check_agents("- `docs/tickets/`: <what goes here> and `<ticket>`\n")
        self.assertEqual(code, 1)
        self.assertIn("placeholder  AGENTS.md:5", out)

    def test_the_prefix_in_backticks_is_still_found(self):
        code, out = self.check_agents("- ids `<P>-Qnn`\n")
        self.assertEqual(code, 1)
        self.assertNotIn("placeholder", out)
        self.assertIn("prefix       AGENTS.md still holds <P>", out)


class AddEntry(Base):
    """add-entry writes the entries the global skills read, from the forms in template/entries (SU-Q142)."""

    def setUp(self):
        super(AddEntry, self).setUp()
        run("copy-template", "code", "--dest", self.dest)
        run("fill-prefix", "ZZ", "--dest", self.dest)
        self.agents = os.path.join(self.dest, "AGENTS.md")
        self.notes = os.path.join(self.dest, "docs", "sessions.md")

    def fields(self, text, title="Game design"):
        """The field names of an entry's list, in order."""
        lines = text.splitlines()
        at = next(i for i, line in enumerate(lines) if line.startswith("- **%s:**" % title))
        out = []
        for line in lines[at + 1:]:
            if not line.startswith("  - "):
                break
            out.append(line[4:].split(":")[0])
        return out

    def test_game_design_goes_in_before_stage_close_with_every_field_none_yet(self):
        before = get(self.agents)
        code, out = run("add-entry", "game-design", "--dest", self.dest)
        self.assertEqual(code, 0, out)
        after = get(self.agents)
        lines = after.splitlines()
        at = lines.index("- **Game design:**")
        self.assertEqual(lines[at + 14], "- **Stage close:**")
        self.assertEqual(lines[at + 1:at + 14], ["  - %s: none yet" % name for name in self.fields(after)])
        self.assertEqual(len(self.fields(after)), 13)
        self.assertEqual(lines[:at] + lines[at + 14:], before.splitlines())      # nothing else changed
        self.assertTrue(after.endswith("\n") and not after.endswith("\n\n"))

    def test_the_form_has_the_fields_the_three_skills_read(self):
        readme = get(os.path.join(setup_tools.REPO, "research", "game-design", "README.md"))
        form = get(os.path.join(setup_tools.ENTRIES, "game-design.md"))
        self.assertEqual(self.fields(form), self.fields(readme))
        self.assertEqual(len(self.fields(form)), 13)

    def test_guided_sessions_adds_the_line_and_writes_the_notes(self):
        code, out = run("add-entry", "guided-sessions", "--where", "Demo  Game 1.0", "--dest", self.dest)
        self.assertEqual(code, 0, out)
        lines = get(self.agents).splitlines()
        at = next(i for i, line in enumerate(lines) if line.startswith("- **Guided sessions:** `docs/sessions.md`"))
        self.assertIn("where the user tests: Demo Game 1.0)", lines[at])
        self.assertEqual(lines[at + 1], "- **Stage close:**")
        notes = get(self.notes)
        self.assertIn("Where the user tests: Demo Game 1.0.", notes)
        self.assertNotIn("<", notes)
        parts = notes.split("\n## ")[1:]
        self.assertEqual([part.split("\n")[0] for part in parts],
                         ["Tools between rounds", "Before a round", "Checklists and results", "Writes and undo",
                          "Safety", "Overrides"])
        for part in parts:
            self.assertEqual(part.split("\n", 1)[1].strip(), "none yet")

    def test_both_entries_then_only_the_template_placeholders_are_open(self):
        run("add-entry", "guided-sessions", "--where", "the test device", "--dest", self.dest)
        run("add-entry", "game-design", "--dest", self.dest)
        titles = [line for line in get(self.agents).splitlines() if line.startswith("- **")]
        self.assertEqual([t.split("**")[1] for t in titles], ["Guided sessions:", "Game design:", "Stage close:"])
        code, out = run("check", "--dest", self.dest)
        opened = [line for line in out.splitlines() if line.startswith("placeholder")]
        self.assertEqual(len(opened), 4, out)       # the name, the paragraph, Safety and the test command

    def test_an_entry_that_is_there_is_kept(self):
        run("add-entry", "game-design", "--dest", self.dest)
        text = get(self.agents).replace("  - Vision: none yet", "  - Vision: `docs/design/vision.md`")
        put(self.agents, text)
        code, out = run("add-entry", "game-design", "--dest", self.dest)
        self.assertEqual(code, 0)
        self.assertIn("kept    the Game design entry", out)
        self.assertEqual(get(self.agents), text)

    def test_notes_that_are_there_are_kept(self):
        put(self.notes, "# Mine\n")
        code, out = run("add-entry", "guided-sessions", "--where", "Demo Game 1.0", "--dest", self.dest)
        self.assertEqual(code, 0)
        self.assertIn("kept    %s" % os.path.join("docs", "sessions.md"), out)
        self.assertEqual(get(self.notes), "# Mine\n")
        self.assertIn("- **Guided sessions:**", get(self.agents))

    def test_guided_sessions_needs_a_place_without_an_angle_bracket(self):
        before = get(self.agents)
        for extra in ([], ["--where", "  "], ["--where", "the <device>"]):
            code, out = run("add-entry", "guided-sessions", "--dest", self.dest, *extra)
            self.assertEqual(code, 2, extra)
        self.assertEqual(get(self.agents), before)
        self.assertFalse(os.path.exists(self.notes))

    def test_without_a_stage_close_list_the_entry_ends_the_section(self):
        put(self.agents, "# Demo\n\nProfile: docs\n\n## Where things are\n\n- `sources/`: originals.\n\n"
                         "## Rules\n\nA rule.\n")
        run("add-entry", "guided-sessions", "--where", "the scanner", "--dest", self.dest)
        lines = get(self.agents).splitlines()
        self.assertEqual(lines[6], "- `sources/`: originals.")
        self.assertTrue(lines[7].startswith("- **Guided sessions:**"))
        self.assertEqual(lines[8:], ["", "## Rules", "", "A rule."])

    def test_an_empty_section_gets_a_blank_line_first(self):
        put(self.agents, "# Demo\n\n## Where things are\n")
        run("add-entry", "game-design", "--dest", self.dest)
        self.assertEqual(get(self.agents).splitlines()[2:5], ["## Where things are", "", "- **Game design:**"])

    def test_no_section_or_no_file_changes_nothing(self):
        put(self.agents, "# Demo\n\nProfile: code\n")
        code, out = run("add-entry", "game-design", "--dest", self.dest)
        self.assertEqual(code, 2)
        self.assertIn("Where things are", out)
        self.assertEqual(get(self.agents), "# Demo\n\nProfile: code\n")
        os.remove(self.agents)
        code, out = run("add-entry", "game-design", "--dest", self.dest)
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(self.agents))

    def test_the_forms_are_not_copied_into_a_project(self):
        self.assertFalse(os.path.exists(os.path.join(self.dest, "entries")))
        self.assertFalse(os.path.exists(os.path.join(self.dest, "game-design.md")))


class CheckScan(Base):
    """check reads what git would track: no ignored file, no binary file (SU-Q140, SU-Q141)."""

    def setUp(self):
        super(CheckScan, self).setUp()
        put(os.path.join(self.dest, "AGENTS.md"), "# Demo\n\nProfile: code\n")
        put(os.path.join(self.dest, ".gitignore"), "data/\n*.log\n")
        put(os.path.join(self.dest, "data", "a.cfg"), "text with <P>\n")
        put(os.path.join(self.dest, "run.log"), "<P>\n")

    def git_init(self, commit=True):
        git = ["git", "-C", self.dest, "-c", "user.name=t", "-c", "user.email=t@example.com",
               "-c", "core.autocrlf=false"]
        subprocess.run(["git", "init", "-q", "-b", "main", self.dest], check=True)
        if commit:
            subprocess.run(git + ["add", "-A"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "skeleton"], check=True)

    def put_bytes(self, rel, data):
        path = os.path.join(self.dest, rel)
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, "wb") as fh:
            fh.write(data)

    def test_ignored_files_are_not_read_in_a_repo(self):
        self.git_init()
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 0, out)

    def test_ignored_files_are_not_read_before_git_init(self):
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 0, out)
        self.assertNotIn("note:", out)                                  # git listed the files, no fallback
        self.assertFalse(os.path.exists(os.path.join(self.dest, ".git")))   # and left nothing in the project

    def test_an_ignored_file_is_never_opened(self):
        opened = []
        real = setup_tools.holds_prefix
        self.addCleanup(setattr, setup_tools, "holds_prefix", real)
        setup_tools.holds_prefix = lambda path: opened.append(os.path.relpath(path, self.dest)) or real(path)
        run("check", "--dest", self.dest)
        self.assertEqual(sorted(opened), [".gitignore", "AGENTS.md"])

    def test_tracked_and_untracked_text_files_are_read(self):
        self.git_init()
        put(os.path.join(self.dest, "docs", "new note.md"), "ticket <P>-T01\n")          # untracked, not ignored
        put(os.path.join(self.dest, "docs", "заметка.md"), "<P>-Q01\n")
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 1)
        self.assertIn("prefix       %s still holds <P>" % os.path.join("docs", "new note.md"), out)
        self.assertIn("заметка.md still holds <P>", out)
        self.assertIn("2 to fill", out)

    def test_a_tracked_file_an_ignore_line_matches_is_still_read(self):
        self.git_init(commit=False)
        subprocess.run(["git", "-C", self.dest, "-c", "core.autocrlf=false", "add", "-f", "run.log"], check=True)
        code, out = run("check", "--dest", self.dest)
        self.assertIn("prefix       run.log still holds <P>", out)

    def test_binary_files_are_skipped(self):
        self.put_bytes(os.path.join("art", "wall.png"), b"\x89PNG\x00\x00\x7c<P>\x00" * 50)
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 0, out)
        self.git_init()
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 0, out)

    def test_prefix_across_a_block_edge_is_found(self):
        real = setup_tools.BLOCK
        self.addCleanup(setattr, setup_tools, "BLOCK", real)
        setup_tools.BLOCK = 8
        for pad in range(8):
            put(os.path.join(self.dest, "pad%d.md" % pad), "x" * pad + "<P>-T01 and more text\n")
        code, out = run("check", "--dest", self.dest)
        self.assertIn("8 to fill", out)

    def test_a_tracked_file_gone_from_disk_is_passed_over(self):
        self.git_init()
        os.remove(os.path.join(self.dest, ".gitignore"))
        code, out = run("check", "--dest", self.dest)
        self.assertNotIn("Traceback", out)
        self.assertIn("a.cfg", out)                 # with its ignore file gone, the folder's file counts again

    def test_without_git_every_folder_is_walked_and_binary_files_still_skipped(self):
        real = setup_tools.git_listed
        self.addCleanup(setattr, setup_tools, "git_listed", real)
        setup_tools.git_listed = lambda dest: None
        self.put_bytes(os.path.join("art", "wall.png"), b"\x00<P>\x00")
        code, out = run("check", "--dest", self.dest)
        self.assertEqual(code, 1)
        self.assertIn("note: git could not list the files", out)
        self.assertIn("run.log still holds <P>", out)
        self.assertNotIn("wall.png", out)


class Prefixes(Base):
    def test_lists_prefixes_of_sibling_projects(self):
        put(os.path.join(self.root, "Alpha", "CLAUDE.md"), "ids AL-T01 and AL-Q02\n")
        put(os.path.join(self.root, "Beta", "AGENTS.md"), "BE-Q01\n")
        put(os.path.join(self.root, "Beta", "docs", "decisions", "process.md"), "BE-Q02, BE-T03-Q1, not-an-ID x-Q1\n")
        put(os.path.join(self.root, "Gamma", "decisions.md"), "GAM-Q10\n")
        code, out = run("prefixes", "--dest", self.dest)
        self.assertEqual(code, 0)
        lines = {l.split()[0]: l for l in out.splitlines()}
        self.assertEqual(set(lines), {"AL", "BE", "GAM"})
        self.assertIn("Beta", lines["BE"])
        self.assertEqual(lines["BE"].split()[1], "3")


class BaseLines(Base):
    def test_reports_missing_lines_and_bare_text_auto(self):
        put(os.path.join(self.dest, ".gitattributes"), "* text=auto\n*.png binary\n")
        code, out = run("base-lines", "--dest", self.dest)
        self.assertIn(".gitignore: the project has none", out)
        self.assertIn(".gitattributes lacks: * text=auto eol=lf", out)
        self.assertNotIn(".gitattributes lacks: *.png binary", out)
        self.assertIn("bare `* text=auto`", out)

    def test_nothing_missing_after_copy(self):
        run("copy-template", "docs", "--dest", self.dest)
        code, out = run("base-lines", "--dest", self.dest)
        self.assertIn("ok: no base line is missing", out)


class MoveInstructions(Base):
    OLD = ("@~/.claude/setup/profiles/code.md\n\n# Demo\n\nWhat it is.\n\n## Safety\n\nNone.\n\n"
           "## Where things are\n\n- `docs/tickets/`: the work.\n")

    def test_move_puts_text_in_agents_and_leaves_two_imports(self):
        put(os.path.join(self.dest, "CLAUDE.md"), self.OLD)
        code, out = run("instructions", "--dest", self.dest)
        self.assertIn("not moved", out)
        code, out = run("move-instructions", "--dest", self.dest)
        self.assertEqual(code, 0, out)
        self.assertEqual(get(os.path.join(self.dest, "CLAUDE.md")), "@~/.claude/setup/profiles/code.md\n@AGENTS.md\n")
        self.assertEqual(get(os.path.join(self.dest, "AGENTS.md")),
                         "# Demo\n\nProfile: code\n\nWhat it is.\n\n## Safety\n\nNone.\n\n"
                         "## Where things are\n\n- `docs/tickets/`: the work.\n")
        code, out = run("instructions", "--dest", self.dest)
        self.assertIn("state:     moved", out)

    def test_move_refuses_when_agents_exists(self):
        put(os.path.join(self.dest, "CLAUDE.md"), self.OLD)
        put(os.path.join(self.dest, "AGENTS.md"), "something\n")
        code, out = run("move-instructions", "--dest", self.dest)
        self.assertEqual(code, 2)
        self.assertEqual(get(os.path.join(self.dest, "AGENTS.md")), "something\n")
        self.assertEqual(get(os.path.join(self.dest, "CLAUDE.md")), self.OLD)

    def test_move_needs_a_profile(self):
        put(os.path.join(self.dest, "CLAUDE.md"), "# Demo\n\nNo import line.\n")
        code, out = run("move-instructions", "--dest", self.dest)
        self.assertEqual(code, 2)
        code, out = run("move-instructions", "--profile", "docs", "--dest", self.dest)
        self.assertEqual(code, 0)
        self.assertTrue(get(os.path.join(self.dest, "AGENTS.md")).startswith("# Demo\n\nProfile: docs\n\nNo import line.\n"))

    def test_other_import_lines_are_kept_and_named(self):
        put(os.path.join(self.dest, "CLAUDE.md"), "@~/.claude/setup/profiles/docs.md\n@docs/extra.md\n\n# Demo\n")
        code, out = run("move-instructions", "--dest", self.dest)
        self.assertIn("@docs/extra.md", get(os.path.join(self.dest, "AGENTS.md")))
        self.assertIn("note: AGENTS.md keeps the import line @docs/extra.md", out)

    def test_template_project_counts_as_moved(self):
        run("copy-template", "docs", "--dest", self.dest)
        code, out = run("instructions", "--dest", self.dest)
        self.assertIn("state:     moved", out)


class Where(unittest.TestCase):
    def test_where_is_the_repo(self):
        code, out = run("where")
        self.assertTrue(os.path.isdir(os.path.join(out.strip(), "template", "base")))


if __name__ == "__main__":
    unittest.main()
