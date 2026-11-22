"""Every SU-Q id in decisions.md is defined once (SU-Q92). Run:  python -m unittest discover -s tools/tests

Several people add decisions on their own branches, so two pull requests can take the same next id. A decision is
defined where its id opens a list item in bold (`- **SU-Q92 ...`); every other mention is a reference. The pull
request that merges second renumbers its new ids; this test is what tells it to.
"""
import collections
import io
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFINITION_RE = re.compile(r"^\s*- \*\*SU-Q(\d+)\b", re.M)


def defined_ids(text):
    """The ids of the decisions defined in the text, in order, as numbers."""
    return [int(number) for number in DEFINITION_RE.findall(text)]


def duplicates(text):
    """The ids defined more than once, each once, in order."""
    return sorted(number for number, count in collections.Counter(defined_ids(text)).items() if count > 1)


def decisions():
    with io.open(os.path.join(REPO, "decisions.md"), encoding="utf-8") as fh:
        return fh.read()


SAMPLE = """# Decisions

## Round 1

- **SU-Q01 First.** Text that refers to SU-Q02.
- **SU-Q02 Second.** More text.
  - **SU-Q03 Nested, still a definition.** Text.

Not a definition: **SU-Q01** in a paragraph, and a line that says - SU-Q02 without bold.
"""


class DecisionIds(unittest.TestCase):
    def test_no_id_is_defined_twice(self):
        found = duplicates(decisions())
        self.assertEqual(found, [], "decisions.md defines these ids more than once: %s. The pull request that "
                         "merged second renumbers its new ids (SU-Q92)."
                         % ", ".join("SU-Q%02d" % number for number in found))

    def test_the_real_file_has_definitions(self):
        self.assertGreater(len(defined_ids(decisions())), 100)

    def test_definitions_and_references_are_told_apart(self):
        self.assertEqual(defined_ids(SAMPLE), [1, 2, 3])
        self.assertEqual(duplicates(SAMPLE), [])

    def test_a_duplicated_id_is_found(self):
        doubled = SAMPLE + "\n## Round 2\n\n- **SU-Q02 Taken again on another branch.** Text.\n"
        self.assertEqual(duplicates(doubled), [2])

    def test_a_duplicate_in_the_real_text_is_found(self):
        text = decisions()
        last = defined_ids(text)[-1]
        doubled = text.rstrip("\n") + "\n- **SU-Q%02d A second decision with the last id.** Text.\n" % last
        self.assertEqual(duplicates(doubled), [last])


if __name__ == "__main__":
    unittest.main()
