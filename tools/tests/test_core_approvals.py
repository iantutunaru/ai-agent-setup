"""Tests for tools/core_approvals.py (SU-Q105). Run:  python -m unittest discover -s tools/tests"""
import base64
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import core_approvals  # noqa: E402
from core_approvals import decide, parse_codeowners, owners_of, CodeownersError  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HEAD = "c" * 40
OLD = "a" * 40
OWNERS = "/tools/ @iantutunaru @owner-b @owner-c\n"


def review(login, state, commit=HEAD):
    return {"user": {"login": login}, "state": state, "commit_id": commit}


def real_codeowners():
    with io.open(os.path.join(REPO, ".github", "CODEOWNERS"), encoding="utf-8") as fh:
        return fh.read()


class Matcher(unittest.TestCase):
    def test_real_file_is_understood(self):
        rules = parse_codeowners(real_codeowners())
        self.assertEqual(len(rules), 8)
        for rule in rules:
            self.assertTrue(rule.owners, "line %d names no owner" % rule.lineno)

    def test_every_core_path_is_matched(self):
        rules = parse_codeowners(real_codeowners())
        core = [  # SU-Q89 and SU-Q106
            "global/rules.md", "global/rules-claude.md", "global/rules-chatgpt.md",
            "profiles/code.md", "profiles/docs.md", "global/settings.json",
            "global/hooks/session-start.sh", "global/hooks/session-start.ps1",
            "install.ps1", "install-chatgpt.ps1",
            "tools/setup_tools.py", "tools/tests/test_readme.py",
            ".github/CODEOWNERS", ".github/workflows/tests.yml", ".github/pull_request_template.md",
        ]
        for path in core:
            self.assertEqual(owners_of(path, rules), ["@iantutunaru"], path)

    def test_other_paths_are_not_matched(self):
        rules = parse_codeowners(real_codeowners())
        for path in ("README.md", "decisions.md", "global/skills/stage-close/SKILL.md", "global/CLAUDE.md",
                     "global/personal.example.md", "global/settings.personal.example.json",
                     "docs/handoffs/shared-repo.md", "template/base/AGENTS.md", "x/tools/a.py",
                     "global/rules/a.md", "tools"):
            self.assertEqual(owners_of(path, rules), [], path)

    def test_star_stays_inside_one_name(self):
        rules = parse_codeowners("/global/rules*.md @a\n")
        self.assertEqual(owners_of("global/rules-x.md", rules), ["@a"])
        self.assertEqual(owners_of("global/rules/x.md", rules), [])

    def test_last_matching_line_wins(self):
        rules = parse_codeowners("/tools/ @a @b\n/tools/tests/ @c\n")
        self.assertEqual(owners_of("tools/x.py", rules), ["@a", "@b"])
        self.assertEqual(owners_of("tools/tests/t.py", rules), ["@c"])

    def test_comments(self):
        rules = parse_codeowners("# a comment\n\n/tools/ @a #inline comment\n")
        self.assertEqual(owners_of("tools/x.py", rules), ["@a"])

    def test_unknown_forms_name_the_line(self):
        for line in ("*.js @a", "tools/ @a", "/a/**/b @a", "/a?.md @a", "!/tools/ @a", "/[ab]/ @a",
                     "/a\\#b @a", "/ @a", "/a//b @a", "/../x @a", "/tools/ @org/team", "/tools/ a@b.c"):
            with self.assertRaises(CodeownersError) as caught:
                parse_codeowners("# first\n/install.ps1 @a\n" + line + "\n")
            self.assertEqual(caught.exception.lineno, 3, line)
            self.assertIn("line 3", str(caught.exception))


class Decide(unittest.TestCase):
    def test_no_core_file(self):
        state, text = decide(["README.md"], OWNERS, "owner-b", [], HEAD)
        self.assertEqual(state, "success")
        self.assertIn("No shared core", text)

    def test_core_file_owned_only_by_the_author(self):
        state, _ = decide(["tools/x.py"], "/tools/ @iantutunaru\n", "iantutunaru", [], HEAD)
        self.assertEqual(state, "success")

    def test_one_of_two_other_owners_approved(self):
        state, text = decide(["tools/x.py"], OWNERS, "iantutunaru", [review("owner-b", "APPROVED")], HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-c", text)
        self.assertNotIn("@owner-b", text)
        self.assertNotIn("@iantutunaru", text)

    def test_both_approved(self):
        reviews = [review("owner-b", "APPROVED"), review("Owner-C", "APPROVED")]
        state, _ = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "success")

    def test_approval_of_an_older_commit_does_not_count(self):
        reviews = [review("owner-b", "APPROVED"), review("owner-c", "APPROVED", OLD)]
        state, text = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-c", text)

    def test_changes_requested_after_an_approval(self):
        reviews = [review("owner-b", "APPROVED"), review("owner-c", "APPROVED"), review("owner-c", "CHANGES_REQUESTED")]
        state, text = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-c", text)

    def test_a_later_comment_does_not_cancel_an_approval(self):
        reviews = [review("owner-b", "APPROVED"), review("owner-c", "APPROVED"), review("owner-c", "COMMENTED"),
                   review("owner-b", "PENDING")]
        state, _ = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "success")

    def test_a_dismissed_approval_does_not_count(self):
        reviews = [review("owner-b", "APPROVED"), review("owner-c", "DISMISSED")]
        state, text = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-c", text)

    def test_the_author_approving_their_own_change(self):
        reviews = [review("iantutunaru", "APPROVED"), review("owner-b", "APPROVED")]
        state, text = decide(["tools/x.py"], OWNERS, "iantutunaru", reviews, HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-c", text)

    def test_unknown_pattern_form_fails_closed(self):
        state, text = decide(["README.md"], "/tools/ @a\n*.md @a\n", "x", [], HEAD)
        self.assertEqual(state, "failure")
        self.assertIn("line 2", text)

    def test_owners_of_the_base_branch_version_count_too(self):
        state, text = decide(["tools/x.py"], "/tools/ @iantutunaru\n", "iantutunaru", [], HEAD,
                             base_codeowners=OWNERS)
        self.assertEqual(state, "failure")
        self.assertIn("@owner-b", text)

    def test_a_renamed_file_counts_by_its_old_name(self):
        state, _ = decide(["notes/x.py", "tools/x.py"], OWNERS, "iantutunaru", [], HEAD)
        self.assertEqual(state, "failure")

    def test_description_fits_the_limit(self):
        many = " ".join("@friend-number-%02d" % i for i in range(30))
        state, text = decide(["tools/x.py"], "/tools/ %s\n" % many, "x", [], HEAD)
        self.assertEqual(state, "failure")
        self.assertLessEqual(len(text), core_approvals.DESCRIPTION_LIMIT)
        self.assertIn("more", text)


class FakeResponse(object):
    def __init__(self, body, link=""):
        self._body = json.dumps(body).encode("utf-8") if body is not None else b""
        self.headers = {"Link": link} if link else {}

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeGitHub(object):
    """Serves GET answers by url and records each POST body."""

    def __init__(self, answers):
        self.answers = answers
        self.posts = []
        self.seen = []

    def __call__(self, request, timeout=None):
        url = request.full_url
        self.seen.append((request.get_method(), url, dict(request.header_items())))
        if request.get_method() == "POST":
            self.posts.append((url, json.loads(request.data.decode("utf-8"))))
            return FakeResponse({})
        answer = self.answers.get(url)
        if answer is None or isinstance(answer, int):
            raise urllib.error.HTTPError(url, answer or 404, "error", {}, None)
        return answer


API = "https://api.example.test/repos/owner/repo/"


class CommandLine(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="core-approvals-")
        self.event = os.path.join(self.root, "event.json")
        with io.open(self.event, "w", encoding="utf-8") as fh:
            json.dump({"pull_request": {"number": 7, "head": {"sha": OLD}}}, fh)
        self.codeowners = os.path.join(self.root, "CODEOWNERS")
        self.write_codeowners(OWNERS)
        self.env = {"GITHUB_EVENT_PATH": self.event, "GITHUB_REPOSITORY": "owner/repo",
                    "GITHUB_TOKEN": "secret-token-value", "GITHUB_API_URL": "https://api.example.test",
                    "GITHUB_SERVER_URL": "https://github.example.test", "GITHUB_RUN_ID": "99"}

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def write_codeowners(self, text):
        with io.open(self.codeowners, "w", encoding="utf-8") as fh:
            fh.write(text)

    def answers(self, **changes):
        base_file = {"encoding": "base64", "content": base64.b64encode(OWNERS.encode("utf-8")).decode("ascii")}
        answers = {
            API + "pulls/7": FakeResponse({"head": {"sha": HEAD}, "base": {"sha": "b" * 40},
                                           "user": {"login": "iantutunaru"}}),
            API + "pulls/7/files?per_page=100": FakeResponse(
                [{"filename": "README.md"}], link='<%spulls/7/files?per_page=100&page=2>; rel="next", '
                                                  '<%spulls/7/files?per_page=100&page=2>; rel="last"' % (API, API)),
            API + "pulls/7/files?per_page=100&page=2": FakeResponse(
                [{"filename": "tools/new.py", "previous_filename": "tools/old.py"}],
                link='<%spulls/7/files?per_page=100&page=1>; rel="first"' % API),
            API + "pulls/7/reviews?per_page=100": FakeResponse(
                [review("owner-b", "APPROVED")], link='<%spulls/7/reviews?per_page=100&page=2>; rel="next"' % API),
            API + "pulls/7/reviews?per_page=100&page=2": FakeResponse([review("owner-c", "APPROVED")]),
            API + "contents/.github/CODEOWNERS?ref=" + "b" * 40: FakeResponse(base_file),
        }
        answers.update(changes)
        return answers

    def run_main(self, fake):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("urllib.request.urlopen", fake), contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(err):
            code = core_approvals.main([self.codeowners], self.env)
        text = out.getvalue() + err.getvalue()
        self.assertNotIn("secret-token-value", text)
        return code, text

    def test_follows_pagination_and_sets_success(self):
        fake = FakeGitHub(self.answers())
        code, _ = self.run_main(fake)
        self.assertEqual(code, 0)
        self.assertEqual(len(fake.posts), 1)
        url, body = fake.posts[0]
        self.assertEqual(url, API + "statuses/" + HEAD)
        self.assertEqual(body["context"], "core-approvals")
        self.assertEqual(body["state"], "success")
        self.assertEqual(body["target_url"], "https://github.example.test/owner/repo/actions/runs/99")
        gets = [seen[1] for seen in fake.seen if seen[0] == "GET"]
        self.assertIn(API + "pulls/7/files?per_page=100&page=2", gets)
        self.assertIn(API + "pulls/7/reviews?per_page=100&page=2", gets)
        self.assertEqual(fake.seen[0][2].get("Authorization"), "Bearer secret-token-value")

    def test_missing_owner_sets_failure_and_exits_zero(self):
        fake = FakeGitHub(self.answers(**{API + "pulls/7/reviews?per_page=100&page=2": FakeResponse([])}))
        code, _ = self.run_main(fake)
        self.assertEqual(code, 0)
        self.assertEqual(fake.posts[0][1]["state"], "failure")
        self.assertIn("@owner-c", fake.posts[0][1]["description"])

    def test_no_codeowners_on_the_base_branch(self):
        fake = FakeGitHub(self.answers(**{API + "contents/.github/CODEOWNERS?ref=" + "b" * 40: 404}))
        code, _ = self.run_main(fake)
        self.assertEqual(code, 0)
        self.assertEqual(fake.posts[0][1]["state"], "success")

    def test_api_error_sets_failure_and_exits_non_zero(self):
        fake = FakeGitHub(self.answers(**{API + "pulls/7/reviews?per_page=100": 500}))
        code, text = self.run_main(fake)
        self.assertEqual(code, 1)
        self.assertEqual(len(fake.posts), 1)
        url, body = fake.posts[0]
        self.assertEqual(url, API + "statuses/" + HEAD)
        self.assertEqual(body["state"], "failure")
        self.assertIn("Could not decide", body["description"])
        self.assertIn("500", text)

    def test_pull_request_unreadable_uses_the_event_head(self):
        fake = FakeGitHub(self.answers(**{API + "pulls/7": 403}))
        code, _ = self.run_main(fake)
        self.assertEqual(code, 1)
        self.assertEqual(fake.posts[0][0], API + "statuses/" + OLD)
        self.assertEqual(fake.posts[0][1]["state"], "failure")

    def test_unknown_form_sets_failure_and_exits_non_zero(self):
        self.write_codeowners("/tools/ @a\n*.md @a\n")
        fake = FakeGitHub(self.answers())
        code, _ = self.run_main(fake)
        self.assertEqual(code, 1)
        self.assertEqual(fake.posts[0][1]["state"], "failure")
        self.assertIn("line 2", fake.posts[0][1]["description"])

    def test_missing_environment(self):
        del self.env["GITHUB_TOKEN"]
        fake = FakeGitHub(self.answers())
        code, _ = self.run_main(fake)
        self.assertEqual(code, 1)
        self.assertEqual(fake.seen, [])


if __name__ == "__main__":
    unittest.main()
