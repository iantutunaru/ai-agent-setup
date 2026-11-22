"""Every tracked file is public: no machine path with a user name, no PC name, no personal email address, and
none of a person's own private terms.
Run:  python -m unittest discover -s tools/tests -p "test_public_guard.py"

The scan reads the files `git ls-files` lists, as UTF-8 text, and skips binary files (a NUL byte in the first
8000 bytes). It fails with file:line for:

- a Windows user folder with a real-looking name (placeholders such as <you> or %USERPROFILE% pass);
- a Windows PC name of the forms DESKTOP- or LAPTOP- followed by 7 or 8 capitals and digits;
- an email address outside a short allow list of domains (example domains, GitHub's noreply addresses);
- any term of local/private-terms.txt: one term per line, "#" starts a comment, matched case-insensitively as a
  whole word or phrase. local/ is ignored by git, so without that file this part is skipped, as on GitHub.

The samples in the tests below are built from pieces, so this file does not trip its own scan.
"""
import io
import os
import re
import subprocess
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TERMS_FILE = os.path.join(REPO, "local", "private-terms.txt")

# A user folder: drive, "Users", then the name up to the next separator, quote, space or bracket.
USER_RE = re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+(<[^>\s]*>|[^\\/\s\"'`<>|*?:,;()\[\]{}]+)", re.I)
USER_OK = {"<you>", "<user>", "username", "runner~1", "public", "default", "me", "you", "name"}

PC_RE = re.compile(r"\b(?:DESKTOP|LAPTOP)-([A-Z0-9]{7,8})\b")

EMAIL_RE = re.compile(r"(?<![\w.%+-])[A-Za-z0-9][A-Za-z0-9._%+-]*@((?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,})(?![\w-])")
EMAIL_OK_DOMAINS = ("example.com", "example.org", "example.net", "example.invalid",
                    "users.noreply.github.com", "anthropic.com")
# Not addresses: a file name after the "@" (an import line such as n@AGENTS.md, a git ref).
NOT_A_TLD = {"md", "py", "json", "txt", "sh", "ps1", "yml", "yaml", "js", "ts", "html", "css", "toml", "cfg",
             "ini", "lock", "csv", "xml", "svg", "png", "jpg"}


def user_ok(name):
    return (name.lower() in USER_OK or name.startswith("%") or name.lower().startswith("$env:")
            or name.startswith("$"))


def path_hits(line):
    return [m.group(0) for m in USER_RE.finditer(line) if not user_ok(m.group(1))]


def pc_hits(line):
    return [m.group(0) for m in PC_RE.finditer(line) if set(m.group(1)) != {"X"}]


def email_ok(domain):
    domain = domain.lower()
    if domain.rsplit(".", 1)[-1] in NOT_A_TLD:
        return True
    return any(domain == ok or domain.endswith("." + ok) for ok in EMAIL_OK_DOMAINS)


def email_hits(line):
    return [m.group(0) for m in EMAIL_RE.finditer(line) if not email_ok(m.group(1))]


def read_terms(path):
    """The terms of a private-terms file: one per line, blank lines and "#" comments skipped."""
    terms = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if line:
                terms.append(line)
    return terms


def term_pattern(terms):
    """One pattern for all terms, each a whole word or phrase, any run of spaces between its words."""
    if not terms:
        return None
    parts = [r"\s+".join(re.escape(word) for word in term.split()) for term in terms]
    return re.compile(r"(?<!\w)(?:%s)(?!\w)" % "|".join(parts), re.I)


def term_hits(line, pattern):
    return [m.group(0) for m in pattern.finditer(line)] if pattern else []


def tracked_files():
    """The files git tracks, or None when git is missing or the folder is not a repo."""
    try:
        out = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, capture_output=True)
    except OSError:
        return None
    if out.returncode != 0:
        return None
    return [name for name in out.stdout.decode("utf-8").split("\0") if name]


def text_of(name):
    """A tracked file as text, or None for a binary or missing file."""
    path = os.path.join(REPO, name)
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as fh:
        data = fh.read()
    if b"\0" in data[:8000]:
        return None
    return data.decode("utf-8", errors="replace")


def scan(checks):
    """file:line: what, for every hit of the checks [(what, function of a line)] in the tracked files."""
    files = tracked_files()
    if files is None:
        raise unittest.SkipTest("git is missing or this folder is not a git repo")
    hits = []
    for name in files:
        text = text_of(name)
        if text is None:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            for what, check in checks:
                for found in check(line):
                    hits.append("%s:%d: %s: %s" % (name, number, what, found))
    return hits


class Matchers(unittest.TestCase):
    """Each matcher on small strings: a hit and a non-hit."""

    def test_user_folder(self):
        sep = "\\"
        self.assertEqual(path_hits("C:" + sep + "Users" + sep + "alice" + sep + "x"),
                         ["C:" + sep + "Users" + sep + "alice"])
        self.assertEqual(path_hits("D:/Users/" + "bob.smith/.claude"), ["D:/Users/" + "bob.smith"])
        for name in ("<you>", "<user>", "USERNAME", "RUNNER~1", "Public", "Default", "me", "%USERPROFILE%",
                     "$env:USERNAME"):
            self.assertEqual(path_hits("C:" + sep + "Users" + sep + name + sep + "x"), [], name)
        self.assertEqual(path_hits("%USERPROFILE%" + sep + ".claude"), [])

    def test_pc_name(self):
        self.assertEqual(pc_hits("on " + "DESKTOP-" + "AB12CD3" + " today"), ["DESKTOP-" + "AB12CD3"])
        self.assertEqual(pc_hits("LAPTOP-" + "Q1W2E3R4"), ["LAPTOP-" + "Q1W2E3R4"])
        self.assertEqual(pc_hits("DESKTOP-" + "XXXXXXX"), [])
        self.assertEqual(pc_hits("DESKTOP-" + "abc"), [])
        self.assertEqual(pc_hits("a desktop app"), [])

    def test_email(self):
        self.assertEqual(email_hits("write to " + "jane.doe" + "@" + "mail.co.uk" + "."),
                         ["jane.doe" + "@" + "mail.co.uk"])
        self.assertEqual(email_hits("x" + "@" + "example.com"), [])
        self.assertEqual(email_hits("1+x" + "@" + "users.noreply.github.com"), [])
        self.assertEqual(email_hits("noreply" + "@" + "anthropic.com"), [])
        for text in ("@AGENTS.md", "n" + "@" + "AGENTS.md", "t" + "@" + "t", "a" + "@" + "b.c",
                     "mattpocock-skills" + "@" + "mattpocock", "@" + "~/.claude/setup/global/CLAUDE.md"):
            self.assertEqual(email_hits(text), [], text)

    def test_private_terms(self):
        pattern = term_pattern(["Acme Corp", "zork"])
        self.assertEqual(term_hits("made for acme  corp in 2026", pattern), ["acme  corp"])
        self.assertEqual(term_hits("Zork's map", pattern), ["Zork"])
        self.assertEqual(term_hits("zorkish acmecorp", pattern), [])
        self.assertIsNone(term_pattern([]))
        self.assertEqual(term_hits("anything", None), [])


class TrackedFiles(unittest.TestCase):
    """No machine path with a user name, no PC name, no personal email address in a tracked file."""

    def test_no_user_folder_pc_name_or_email(self):
        hits = scan([("user folder", path_hits), ("PC name", pc_hits), ("email", email_hits)])
        self.assertEqual(hits, [], "\n" + "\n".join(hits))

    def test_no_private_term(self):
        if not os.path.isfile(TERMS_FILE):
            self.skipTest("no local/private-terms.txt")
        pattern = term_pattern(read_terms(TERMS_FILE))
        if pattern is None:
            self.skipTest("local/private-terms.txt holds no term")
        hits = scan([("private term", lambda line: term_hits(line, pattern))])
        self.assertEqual(hits, [], "\n" + "\n".join(hits))


if __name__ == "__main__":
    unittest.main()
