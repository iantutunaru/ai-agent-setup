"""Tests for rb.py: python -m unittest discover -s global/skills/web-rulebook/tests"""
import contextlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import rb  # noqa: E402

FORMS = """# Web design rulebook: forms

3 entries: 1 rule, 2 practice.

### forms-001 · Ask only for what the task needs
- **Statement:** Ask only for the information the task needs.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-153 (page s116)
- **Read:** 2026-11-20, page; candidate forms E01

### forms-003 · Give the information first
- **Statement:** Let visitors reach useful content before a form. Twice as likely to complete it.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NEURO-025 (page 52)
- **Study (as the book reports it):** NEURO-025: Gamberini et al., 2007.
- **Current source:** confirmed by https://example.org/a (read 2026-11-20)
- **Current source:** confirmed by https://example.org/b (read 2026-11-20)
- **Conflict:** the abstract adds a caveat
- **Read:** 2026-11-20, page; candidate forms E03

### forms-004 · Word the button for what it does
- **Statement:** A button's label names the action.
- **Kind:** practice
- **Use:** text
- **Sources:** KRUG-001 (page s1)
- **Read:** 2026-11-20, page; candidate forms E04
"""
PHONE = """# Web design rulebook: phone

1 entries: 0 rule, 1 practice.

### phone-021 · Make links large enough to hit with a finger
- **Statement:** At least 24 by 24 CSS pixels.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-328 (page 608)
- **Read:** 2026-11-20, passage; candidate phone E34, joined by forms E02
"""
IDEAS = """# Ideas for this project's site

## Ideas

### idea-001 · Put the opening hours where people look first
- **Statement:** A visitor who cannot see when you are open goes elsewhere.
- **Where:** site
- **Would change:** The opening hours in the page header.
- **Sources:** GODIN-016 (page 41-42)
- **From:** candidate ideas E01

### idea-002 · Open the pitch with one story
- **Statement:** A story is remembered.
- **Where:** pitch
- **Would change:** The first slide.
- **Sources:** HEATH-001 (page 1)
- **From:** candidate ideas E02

## Dropped

### not an idea
- GODIN-999: project advice
"""
TASTE = """# Web design rulebook: taste and unconfirmed

- KIRSANOV-308: a splash page before the site; overturned by https://example.org (read 2026-11-20)
- COLOUR-001: prefers warm greys to neutral ones
"""


def run(*argv):
    out = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(out):
        try:
            rb.main(list(argv))
        except SystemExit as stop:
            code = stop.code
    return out.getvalue(), code


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        folder = Path(self.tmp.name)
        for name, text in (("forms", FORMS), ("phone", PHONE), ("taste", TASTE),
                           ("README", "# readme"), ("dropped", "# dropped\n### not an entry\n")):
            (folder / f"{name}.md").write_text(text, encoding="utf-8")
        (folder / "_joined.json").write_text(json.dumps(
            {"forms-002": "phone-021", "forms-008": "forms-999"}), encoding="utf-8")
        self.ideas = folder / "project" / "web-ideas.md"
        self.ideas.parent.mkdir()
        self.ideas.write_text(IDEAS, encoding="utf-8")
        os.environ["WEB_RULEBOOK_DIR"] = str(folder)
        os.environ["WEB_IDEAS_FILE"] = str(self.ideas)
        rb.STDOUT_LIMIT, rb.PART_BYTES = 24000, 60000

    def tearDown(self):
        os.environ.pop("WEB_RULEBOOK_DIR", None)
        os.environ.pop("WEB_IDEAS_FILE", None)
        self.tmp.cleanup()

    def test_topics_lists_only_topic_files(self):
        out, _ = run("topics")
        self.assertIn("forms | 3 | 1 | 2 | 2 | 1", out)
        self.assertIn("phone | 1 | 0 | 1 | 1 | 0", out)
        self.assertNotIn("dropped", out)
        self.assertNotIn("taste |", out)
        self.assertIn("2 ideas", out)

    def test_titles_filter_by_use_and_topic(self):
        out, _ = run("titles", "check", "forms", "phone")
        self.assertIn("forms-001 | practice | Ask only for what the task needs", out)
        self.assertIn("forms-003 | rule |", out)
        self.assertIn("phone-021", out)
        self.assertNotIn("forms-004", out)
        out, _ = run("titles", "text", "all")
        self.assertIn("forms-004", out)
        self.assertNotIn("forms-001", out)

    def test_titles_header_names_the_topics(self):
        self.assertIn("topics forms, phone:", run("titles", "check", "forms", "phone")[0])

    def test_show_is_slim_unless_sources_asked(self):
        out, code = run("show", "forms-003")
        self.assertEqual(code, 0)
        self.assertIn("Gamberini", out)
        self.assertEqual(out.count("Current source"), 2)
        self.assertIn("Conflict", out)
        self.assertNotIn("NEURO-025 (page 52)", out)
        self.assertNotIn("**Read:**", out)
        out, _ = run("show", "forms-003", "--sources")
        self.assertIn("NEURO-025 (page 52)", out)
        self.assertIn("**Read:**", out)

    def test_show_follows_a_join_and_names_a_missing_id(self):
        out, code = run("show", "forms-002,", "forms-777")
        self.assertEqual(code, 1)
        self.assertIn("forms-002 was joined into phone-021", out)
        self.assertIn("### phone-021", out)
        self.assertIn("Not in the rulebook", out)
        self.assertIn("forms-777", out)
        out, code = run("show", "forms-008")   # joined into an id that is not in the rulebook
        self.assertEqual(code, 1)
        self.assertIn("Not in the rulebook", out)

    def test_no_ideas_file_means_no_ideas(self):
        os.environ.pop("WEB_IDEAS_FILE")
        here = os.getcwd()
        os.chdir(self.tmp.name)   # no docs/web-ideas.md here
        try:
            out, code = run("ideas")
            self.assertEqual(code, 0)
            self.assertIn("This project has no ideas list", out)
            self.assertIn("docs/web-ideas.md", out)
            self.assertIn("ideas list: none in this project", run("topics")[0])
            self.assertIn("Not in the rulebook", run("show", "idea-001")[0])
            docs = Path(self.tmp.name) / "docs"
            docs.mkdir()
            (docs / "web-ideas.md").write_text(IDEAS, encoding="utf-8")
            self.assertIn("idea-002", run("ideas")[0])
        finally:
            os.chdir(here)

    def test_idea_is_never_shown_as_a_rule(self):
        out, _ = run("show", "idea-001")
        self.assertIn("idea, not proven", out)
        self.assertIn("Would change", out)
        out, _ = run("ideas", "pitch")
        self.assertIn("idea-002", out)
        self.assertNotIn("idea-001", out)
        self.assertNotIn("not an idea", run("ideas")[0])

    def test_find_needs_every_word_and_ranks_title_hits_first(self):
        out, _ = run("find", "form")
        ids = re.findall(r"(?m)^(\S+-\d+) \|", out)
        self.assertEqual(ids, ["forms-003"])
        out, _ = run("find", "links", "pixels")
        self.assertIn("phone-021", out)
        self.assertIn("every one of: links, pixels", out)
        self.assertIn('Find "no such phrase" (use any)', run("find", "no such phrase")[0])
        self.assertLess(out.index("## A word is in the title"), out.index("phone-021"))
        out, _ = run("find", "nothing-like-this")
        self.assertIn("No entry is not a rule against", out)
        out, _ = run("find", "label", "--use", "text")
        self.assertIn("forms-004", out)

    def test_taste_lines(self):
        out, _ = run("taste", "splash")
        self.assertIn("KIRSANOV-308", out)
        self.assertNotIn("COLOUR-001", out)

    def test_long_output_goes_to_files_in_parts(self):
        rb.STDOUT_LIMIT, rb.PART_BYTES = 100, 200
        out, _ = run("topic", "check", "forms")
        paths = re.findall(r"(?m)^  (.+?\.md)  \(", out)
        self.assertGreaterEqual(len(paths), 2)
        joined = "".join(Path(p).read_text(encoding="utf-8") for p in paths)
        self.assertIn("### forms-001", joined)
        self.assertIn("### forms-003", joined)
        for later in paths[1:]:
            self.assertTrue(Path(later).read_text(encoding="utf-8").startswith("### "))

    def test_unknown_topic_and_use_stop_with_the_choices(self):
        self.assertIn("the topics are: forms, phone", str(run("titles", "check", "nope")[1]))
        self.assertIn("look, check, text or any", str(run("titles", "build", "forms")[1]))


class RealRulebook(unittest.TestCase):
    """The master copy in this repo: the tool's parse agrees with each file's own count line."""

    def test_counts_match_each_file_header(self):
        os.environ.pop("WEB_RULEBOOK_DIR", None)
        folder = Path(__file__).resolve().parents[4] / "research" / "web-design" / "rulebook"
        if not folder.is_dir():
            self.skipTest("no rulebook beside this checkout")
        book = rb.Rulebook(folder)
        self.assertEqual(len(book.topics), 16)
        for topic in book.topics:
            head = (folder / f"{topic}.md").read_text(encoding="utf-8").split("\n", 3)[2]
            n, rules, practices = (int(x) for x in re.match(r"(\d+) entries: (\d+) rule, (\d+) practice", head).groups())
            es = book.entries(topic)
            self.assertEqual((len(es), sum(e.kind == "rule" for e in es), sum(e.kind == "practice" for e in es)),
                             (n, rules, practices), topic)
            for e in es:
                self.assertRegex(e.id, rf"^{topic}-\d{{3}}$")
                self.assertTrue(e.uses and e.uses <= set(rb.USES), e.id)
                self.assertTrue(e.get("Statement"), e.id)

    def test_joined_file_points_only_at_entries(self):
        folder = Path(__file__).resolve().parents[4] / "research" / "web-design" / "rulebook"
        if not (folder / "_joined.json").is_file():
            self.skipTest("no rulebook beside this checkout")
        book = rb.Rulebook(folder)
        joined = json.loads((folder / "_joined.json").read_text(encoding="utf-8"))
        self.assertEqual(list(joined), sorted(joined))
        for old, new in joined.items():
            self.assertIsNotNone(book.by_id(new), old)


if __name__ == "__main__":
    unittest.main()
