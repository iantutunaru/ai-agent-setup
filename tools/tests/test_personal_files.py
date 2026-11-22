"""Each person's own files stay out of the repo (SU-Q90, SU-Q102). Run:  python -m unittest discover -s tools/tests

The installs make local/personal.md and local/settings.personal.json from tracked examples in global/; git
ignores local/. The examples carry nothing of one person's, and nothing tracked still points at the old places.
"""
import io
import json
import os
import re
import subprocess
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXAMPLES = ["global/personal.example.md", "global/settings.personal.example.json"]
OLD_PLACES = ["global/personal.md", "global/settings.personal.json"]
# files that read or describe the personal files; the history (decisions.md, docs/) may name the old places
CURRENT = ["install.ps1", "install-chatgpt.ps1", "global/hooks/build-agents-md.ps1", "global/hooks/session-start.sh",
           "global/rules.md", "global/rules-claude.md", "global/rules-chatgpt.md", "README.md"]


def read(relative):
    with io.open(os.path.join(REPO, relative), encoding="utf-8") as fh:
        return fh.read()


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True, check=True).stdout


class PersonalFiles(unittest.TestCase):
    def test_local_is_ignored(self):
        lines = [line.strip() for line in read(".gitignore").splitlines()]
        self.assertIn("local/", lines, ".gitignore does not ignore local/")

    def test_the_examples_are_tracked(self):
        tracked = git("ls-files", "--", *EXAMPLES).split()
        self.assertEqual(sorted(tracked), sorted(EXAMPLES))

    def test_no_personal_file_is_tracked(self):
        tracked = git("ls-files", "--", "local", *OLD_PLACES).split()
        self.assertEqual(tracked, [], "tracked personal files: %s" % ", ".join(tracked))

    def test_the_personal_example_has_preferences(self):
        text = read("global/personal.example.md")
        self.assertIn("\n## Preferences\n", text)
        for point in ("Language", "Background", "Model", "Chat size"):
            self.assertIn("**%s:** not set." % point, text)

    def test_the_settings_example_is_json_with_the_projects_slot(self):
        text = read("global/settings.personal.example.json")
        data = json.loads(text)
        self.assertIsInstance(data["autoMode"]["environment"], list)
        self.assertIn("{{PROJECTS}}", text)

    def test_the_examples_name_no_one(self):
        for path in EXAMPLES:
            text = read(path)
            for word in ("iantutunaru", "Tutunaru", "Unity", "3ds Max"):
                self.assertNotIn(word, text, "%s names %s" % (path, word))

    def test_nothing_current_points_at_the_old_places(self):
        for path in CURRENT:
            for old in OLD_PLACES:
                hits = [line for line in read(path).splitlines()
                        if re.search(re.escape(old) + "|" + re.escape(old.replace("/", "\\")), line)
                        and "before SU-Q90" not in line]
                self.assertEqual(hits, [], "%s still names %s: %s" % (path, old, hits))


if __name__ == "__main__":
    unittest.main()
