"""The front page and its side pages against the skill folders (SU-Q80, SU-Q116, SU-Q122, SU-Q125).
Run:  python -m unittest discover -s tools/tests

A skill added to or removed from global/skills must show in README.md (the count, a row in its group's table
under "The skills") and in docs/tried.md (a row), and its tests in CONTRIBUTING.md's tests list.
The pages tell a reader how to install it and how a change lands (SU-Q85): "Install" in README.md, "Working
together" in CONTRIBUTING.md, and no own-copy steps. Every cell of docs/tried.md starts with a status word, and the small
table on the front page agrees with them. Every link from the four pages to a file in the repo points to a file
that exists.
"""
import glob
import io
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS = os.path.join(REPO, "global", "skills")
PAGES = ["README.md", "CONTRIBUTING.md", os.path.join("docs", "install.md"), os.path.join("docs", "tried.md")]
WORDS = ("partly tried", "not tried", "tried")  # longest first, so "not tried" is not read as "tried"
RULES_ROW_README = "The rules and the session-start hook"
RULES_ROW_TRIED = "the rules file and the session-start hook"


def skill_names():
    """Folders of global/skills that hold a SKILL.md; synced/ is another program's (SU-Q37)."""
    return sorted(name for name in os.listdir(SKILLS)
                  if name != "synced" and os.path.isfile(os.path.join(SKILLS, name, "SKILL.md")))


def page(path):
    with io.open(os.path.join(REPO, path), encoding="utf-8") as fh:
        return fh.read()


def section(text, heading):
    """The text under a heading line, up to the next heading of the same or a higher level."""
    level = len(heading) - len(heading.lstrip("#"))
    parts = re.split(r"^%s$" % re.escape(heading), text, maxsplit=1, flags=re.M)
    if len(parts) < 2:
        return ""
    end = re.search(r"^#{1,%d} " % level, parts[1], re.M)
    return parts[1][:end.start()] if end else parts[1]


def tables(text):
    """Each Markdown table in the text as (header cells, list of row cells)."""
    found, current = [], None
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if current is None:
                current = (cells, [])
                found.append(current)
            elif not all(set(cell) <= set("-:") for cell in cells):
                current[1].append(cells)
        else:
            current = None
    return found


def row_names(cell):
    """The skill names in a first cell: plain ("web-look, web-text") or linked ("[/setup-init](...)")."""
    cell = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)
    return [part.strip().lstrip("/") for part in cell.split(",")]


def skill_groups(readme):
    """{skill name: its group heading} from the tables under "## The skills" in README.md."""
    groups = {}
    skills = section(readme, "## The skills")
    for group in re.findall(r"^### (.+)$", skills, re.M):
        for header, rows in tables(section(skills, "### " + group)):
            if header and header[0] == "Skill":
                for row in rows:
                    for name in row_names(row[0]):
                        groups[name] = group
    return groups


def tried_rows(tried):
    """{row name: {column: cell}} from the per-assistant table of docs/tried.md, one key per name in a row."""
    rows = {}
    for header, body in tables(section(tried, "## By assistant")):
        for row in body:
            for name in row_names(row[0]):
                rows[name] = dict(zip(header[1:], row[1:]))
    return rows


def status_word(cell):
    """The status word a cell starts with, or None."""
    for word in WORDS:
        if cell.startswith(word + ":"):
            return word
    return None


def cells_without_word(tried):
    """Every cell of docs/tried.md's tables, other than the first column, that does not start with a status
    word followed by a colon, as "row / column"."""
    missing = []
    for header, rows in tables(tried):
        for row in rows:
            for column, cell in zip(header[1:], row[1:]):
                if status_word(cell) is None:
                    missing.append("%s / %s" % (row[0], column))
    return missing


def group_word(words):
    """A group's word from its skills' words (SU-Q122): all tried, all not tried, else partly tried."""
    words = set(words)
    if words == {"tried"}:
        return "tried"
    if words == {"not tried"}:
        return "not tried"
    return "partly tried"


def status_table_problems(readme, tried):
    """Where the small table under "## Which assistants" disagrees with docs/tried.md. [] when it agrees."""
    groups = skill_groups(readme)
    rows = tried_rows(tried)
    table = [t for t in tables(section(readme, "## Which assistants")) if t[0] and t[0][0] == "Part"]
    if not table:
        return ['no table with a "Part" column under "## Which assistants"']
    header, body = table[0]
    problems = []
    expected_rows = sorted(set(groups.values())) + [RULES_ROW_README]
    seen = [row[0] for row in body]
    if sorted(seen) != sorted(expected_rows):
        problems.append("rows are %s, expected %s" % (", ".join(seen), ", ".join(expected_rows)))
    for row in body:
        if row[0] == RULES_ROW_README:
            members = [RULES_ROW_TRIED]
        else:
            members = [name for name, group in groups.items() if group == row[0]]
        for column, cell in zip(header[1:], row[1:]):
            words = [status_word(rows.get(name, {}).get(column, "")) for name in members]
            if not members or None in words:
                problems.append("%s / %s: no matching cells in docs/tried.md" % (row[0], column))
                continue
            if cell != group_word(words):
                problems.append("%s / %s says %s, docs/tried.md gives %s"
                                % (row[0], column, cell, group_word(words)))
    return problems


def broken_links(path, text):
    """Links from a page to a file in the repo whose file does not exist. Web links, anchors within the page
    and fenced code blocks are skipped; an anchor after a file name is dropped."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)
    targets = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'(?:src|srcset)="([^"]+)"', text)
    base = os.path.dirname(os.path.join(REPO, path))
    broken = []
    for target in targets:
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if not os.path.exists(os.path.join(base, target.split("#", 1)[0])):
            broken.append("%s -> %s" % (path.replace(os.sep, "/"), target))
    return broken


def group_section_problems(readme, contributing):
    """What the pages lack (SU-Q85): "Install" in README.md instead of the old own-copy steps, and "Working
    together" in CONTRIBUTING.md. [] when both are there and no own-copy heading."""
    problems = []
    if not re.search(r"^###? Install$", readme, re.M):
        problems.append('no "Install" heading in README.md')
    if not re.search(r"^## Working together$", contributing, re.M):
        problems.append('no "## Working together" heading in CONTRIBUTING.md')
    if re.search(r"^#+ .*as your own copy", readme + "\n" + contributing, re.M):
        problems.append('the old "as your own copy" heading is still there')
    return problems


class PagesMatchSkills(unittest.TestCase):
    def setUp(self):
        self.names = skill_names()
        self.readme = page("README.md")
        self.tried = page(os.path.join("docs", "tried.md"))

    def test_count(self):
        counts = re.findall(r"\b(\d+) skills\b", self.readme)
        self.assertTrue(counts, "README.md names no skill count")
        for count in counts:
            self.assertEqual(int(count), len(self.names),
                             "README.md says %s skills, global/skills holds %d" % (count, len(self.names)))

    def test_each_skill_has_a_row_in_its_group(self):
        listed = skill_groups(self.readme)
        missing = [name for name in self.names if name not in listed]
        self.assertEqual(missing, [], 'no row under "The skills" in README.md for: %s' % ", ".join(missing))

    def test_the_skills_tables_name_no_removed_skill(self):
        gone = [name for name in skill_groups(self.readme) if name not in self.names]
        self.assertEqual(gone, [], 'README.md lists skills that are not in global/skills: %s' % ", ".join(gone))

    def test_each_skill_is_in_the_tried_table(self):
        tried = tried_rows(self.tried)
        missing = [name for name in self.names if name not in tried]
        self.assertEqual(missing, [], "no row in docs/tried.md for: %s" % ", ".join(missing))

    def test_the_tried_table_names_no_removed_skill(self):
        gone = [name for name in tried_rows(self.tried)
                if re.fullmatch(r"[a-z0-9-]+", name) and name not in self.names]
        self.assertEqual(gone, [], "docs/tried.md names skills that are not in global/skills: %s"
                         % ", ".join(gone))

    def test_each_test_folder_is_in_the_tests_list(self):
        contributing = page("CONTRIBUTING.md")
        for name in self.names:
            if glob.glob(os.path.join(SKILLS, name, "tests", "test_*.py")):
                command = "python -m unittest discover -s global/skills/%s/tests" % name
                self.assertTrue(command in contributing, "CONTRIBUTING.md's tests list lacks: " + command)
        self.assertTrue("python -m unittest discover -s tools/tests" in contributing,
                        "CONTRIBUTING.md's tests list lacks the tools/tests suite")


class StatusWords(unittest.TestCase):
    """Each cell of docs/tried.md starts with a status word; the front page's small table follows (SU-Q122)."""

    def setUp(self):
        self.readme = page("README.md")
        self.tried = page(os.path.join("docs", "tried.md"))

    def test_every_tried_cell_starts_with_a_word(self):
        self.assertTrue(tables(self.tried), "docs/tried.md holds no table")
        self.assertEqual(cells_without_word(self.tried), [])

    def test_a_cell_without_a_word_is_found(self):
        changed = self.tried.replace("| tried: tested: ran both scripts |", "| tested: ran both scripts |")
        self.assertNotEqual(changed, self.tried)
        self.assertEqual(cells_without_word(changed), ["writing-check / ChatGPT desktop app"])

    def test_the_small_table_agrees(self):
        self.assertEqual(status_table_problems(self.readme, self.tried), [])

    def test_a_disagreeing_small_table_is_found(self):
        changed = self.readme.replace("| Web design | tried |", "| Web design | partly tried |")
        self.assertNotEqual(changed, self.readme)
        self.assertEqual(status_table_problems(changed, self.tried),
                         ["Web design / Claude Code says partly tried, docs/tried.md gives tried"])

    def test_a_changed_tried_cell_is_found(self):
        changed = self.tried.replace("| tried: tested: ran both scripts |",
                                     "| not tried: tested: ran both scripts |")
        self.assertNotEqual(changed, self.tried)
        self.assertEqual(status_table_problems(self.readme, changed), [])  # Writing stays partly tried
        changed = self.tried.replace("| not tried: not tested; they use", "| tried: not tested; they use")
        self.assertNotEqual(changed, self.tried)
        self.assertEqual(status_table_problems(self.readme, changed),
                         ["Web design / ChatGPT desktop app says partly tried, docs/tried.md gives tried"])

    def test_a_missing_group_row_is_found(self):
        changed = self.readme.replace("| Game design | partly tried | not tried |\n", "")
        self.assertNotEqual(changed, self.readme)
        problems = status_table_problems(changed, self.tried)
        self.assertEqual(len(problems), 1)
        self.assertTrue(problems[0].startswith("rows are "), problems)

    def test_the_word_rule(self):
        self.assertEqual(group_word(["tried", "tried"]), "tried")
        self.assertEqual(group_word(["not tried"]), "not tried")
        self.assertEqual(group_word(["tried", "not tried"]), "partly tried")
        self.assertEqual(group_word(["partly tried"]), "partly tried")


class Links(unittest.TestCase):
    """Every link from the four pages to a file in the repo points to a file that exists (SU-Q125)."""

    def test_no_broken_links(self):
        broken = []
        for path in PAGES:
            broken += broken_links(path, page(path))
        self.assertEqual(broken, [])

    def test_a_broken_link_is_found(self):
        text = page("README.md").replace("](docs/tried.md)", "](docs/tryed.md)", 1)
        self.assertEqual(broken_links("README.md", text), ["README.md -> docs/tryed.md"])

    def test_a_broken_picture_is_found(self):
        text = page("README.md").replace('srcset="docs/img/banner-dark.svg"', 'srcset="docs/img/gone.svg"')
        self.assertEqual(broken_links("README.md", text), ["README.md -> docs/img/gone.svg"])

    def test_a_side_page_link_is_read_from_its_folder(self):
        text = page(os.path.join("docs", "tried.md")) + "\n[x](../README.md#install) [y](README.md)\n"
        self.assertEqual(broken_links(os.path.join("docs", "tried.md"), text), ["docs/tried.md -> README.md"])


class PagesForAGroup(unittest.TestCase):
    """The pages tell a reader how to install the setup and how a change lands."""

    def setUp(self):
        self.readme = page("README.md")
        self.contributing = page("CONTRIBUTING.md")

    def test_install_and_working_together_are_there(self):
        self.assertEqual(group_section_problems(self.readme, self.contributing), [])

    def test_a_missing_install_is_found(self):
        changed = re.sub(r"^(###? )Install$", r"\1Install it", self.readme, flags=re.M)
        self.assertNotEqual(changed, self.readme)
        self.assertEqual(group_section_problems(changed, self.contributing), ['no "Install" heading in README.md'])

    def test_a_missing_working_together_is_found(self):
        changed = self.contributing.replace("\n## Working together\n", "\n## Sharing\n")
        self.assertNotEqual(changed, self.contributing)
        self.assertEqual(group_section_problems(self.readme, changed),
                         ['no "## Working together" heading in CONTRIBUTING.md'])

    def test_the_old_own_copy_heading_is_found(self):
        changed = self.readme.replace("\n## Day to day\n",
                                      "\n### The whole setup in Claude Code, as your own copy\n\n## Day to day\n")
        self.assertNotEqual(changed, self.readme)
        self.assertEqual(group_section_problems(changed, self.contributing),
                         ['the old "as your own copy" heading is still there'])


if __name__ == "__main__":
    unittest.main()
