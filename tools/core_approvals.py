"""Everyone's yes on a change to the shared core, as a check GitHub runs (SU-Q105).

A pull request that changes a file named in .github/CODEOWNERS stays red until every owner named on the
matching lines, other than the author, has approved the pull request's current head commit. GitHub's own
code owners rule asks for one owner only ("an approval from any of the owners is sufficient"), so this
check adds the rest.

Run by .github/workflows/core-approvals.yml:

    python tools/core_approvals.py

It reads the event from GITHUB_EVENT_PATH, the repo from GITHUB_REPOSITORY and the token from GITHUB_TOKEN
(never printed), fetches the pull request, its files and its reviews, and sets the commit status
"core-approvals" on the head commit. Exit code 0 when it decided (the status says which way), 1 when it
could not decide; then it first tries to set a failure status.

Standard library only. Tests: python -m unittest discover -s tools/tests
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

CONTEXT = "core-approvals"
CODEOWNERS = ".github/CODEOWNERS"
# GitHub's REST docs give no length for a commit status description; 140 characters is the documented
# limit for a deployment status description and what other tools trim commit statuses to.
DESCRIPTION_LIMIT = 140
API_VERSION = "2026-03-10"
# Review states that end what a reviewer said before. COMMENTED and PENDING do not.
DECIDING_STATES = ("APPROVED", "CHANGES_REQUESTED", "DISMISSED")

LOGIN = re.compile(r"^@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?$")
# One name of a path: anything but the forms GitHub does not support (!, [ ], \) and those this check does
# not (?, #). A "*" inside the name is fine; "**" is refused where the pattern is read.
NAME = re.compile(r"^[^?\[\]!\\#]+$")


class CodeownersError(ValueError):
    """A line of the code owners file in a form this check does not understand."""

    def __init__(self, lineno, reason, label=CODEOWNERS):
        ValueError.__init__(self, "%s line %d: %s" % (label, lineno, reason))
        self.lineno = lineno


class Rule(object):
    def __init__(self, lineno, pattern, owners):
        self.lineno = lineno
        self.pattern = pattern
        self.owners = owners
        self.folder = pattern.endswith("/")
        self.parts = [_name_regex(part) for part in pattern.strip("/").split("/")]

    def matches(self, path):
        """gitignore's rule for an anchored pattern: the path itself, or a file below it."""
        names = path.split("/")
        if len(names) < len(self.parts) or (self.folder and len(names) == len(self.parts)):
            return False
        return all(part.match(name) for part, name in zip(self.parts, names))


def _name_regex(part):
    return re.compile("^" + "[^/]*".join(re.escape(piece) for piece in part.split("*")) + "$")


def parse_codeowners(text, label=CODEOWNERS):
    """The rules of a code owners file, in file order. Raises CodeownersError on a form not understood."""
    rules = []
    for lineno, line in enumerate(text.splitlines(), 1):
        words = line.split()
        for i, word in enumerate(words):
            if word.startswith("#"):
                words = words[:i]
                break
        if not words:
            continue
        pattern, owners = words[0], words[1:]
        reason = _pattern_problem(pattern)
        if reason:
            raise CodeownersError(lineno, reason, label)
        for owner in owners:
            if not LOGIN.match(owner):
                raise CodeownersError(lineno, "owner %r is not an @login" % owner, label)
        rules.append(Rule(lineno, pattern, owners))
    return rules


def _pattern_problem(pattern):
    if not pattern.startswith("/") or pattern == "/":
        return "pattern %r does not start with / and a name" % pattern
    names = pattern.strip("/").split("/")
    for name in names:
        if name in ("", ".", "..") or "**" in name or not NAME.match(name):
            return "pattern %r has a form this check does not understand" % pattern
    return None


def owners_of(path, rules):
    """The owners of the last matching rule (GitHub: the last matching pattern wins), or []."""
    owners = []
    for rule in rules:
        if rule.matches(path):
            owners = rule.owners
    return owners


def approvers(reviews, head_sha):
    """Logins (lower case) whose latest deciding review is an approval of head_sha.

    reviews: the pull request's reviews in GitHub's order (chronological), each with user.login, state and
    commit_id. A plain comment does not cancel an approval; changes requested or a dismissal does.
    """
    latest = {}
    for review in reviews:
        user = review.get("user") or {}
        login = user.get("login")
        if login and review.get("state") in DECIDING_STATES:
            latest[login.lower()] = review
    return set(login for login, review in latest.items()
               if review.get("state") == "APPROVED" and review.get("commit_id") == head_sha)


def decide(changed_files, codeowners, author, reviews, head_sha, base_codeowners=None):
    """(state, description) for the core-approvals status: state is "success" or "failure".

    changed_files: paths of the pull request (for a rename, both names). codeowners: the text of the pull
    request's .github/CODEOWNERS. base_codeowners: the base branch's text, or None when it has none; GitHub's
    own review requests use that version, so owners named in either version are needed.
    """
    try:
        rule_sets = [parse_codeowners(codeowners)]
        if base_codeowners is not None:
            rule_sets.append(parse_codeowners(base_codeowners, CODEOWNERS + " on the base branch"))
    except CodeownersError as error:
        return "failure", fit(str(error))
    needed = {}
    core = False
    for path in changed_files:
        for rules in rule_sets:
            owners = owners_of(path, rules)
            core = core or bool(owners)
            for owner in owners:
                needed.setdefault(owner[1:].lower(), owner)
    if not core:
        return "success", "No shared core file changed."
    needed.pop((author or "").lower(), None)
    if not needed:
        return "success", "Shared core changed; the author is its only owner."
    have = approvers(reviews, head_sha)
    missing = [needed[login] for login in sorted(needed) if login not in have]
    if not missing:
        return "success", "Shared core changed; every owner has approved the current commit."
    return "failure", waiting_for(missing)


def waiting_for(missing):
    """Names who is still missing, shortened to fit the status description limit."""
    lead = "Shared core: waiting for a yes on the current commit from "
    for shown in range(len(missing), 0, -1):
        rest = len(missing) - shown
        text = lead + ", ".join(missing[:shown]) + (" and %d more" % rest if rest else "") + "."
        if len(text) <= DESCRIPTION_LIMIT:
            return text
    return fit(lead + "%d owners." % len(missing))


def fit(text):
    return text if len(text) <= DESCRIPTION_LIMIT else text[:DESCRIPTION_LIMIT - 3] + "..."


# The command line part, for the workflow.

class ApiError(Exception):
    pass


class Api(object):
    def __init__(self, base, repo, token):
        self.base = base.rstrip("/")
        self.repo = repo
        self._token = token

    def _request(self, method, url, body=None):
        data = None if body is None else json.dumps(body).encode("utf-8")
        request = urllib.request.Request(url, data=data, method=method, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + self._token,
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "agent-setup-core-approvals",
        })
        if data is not None:
            request.add_header("Content-Type", "application/json")
        try:
            response = urllib.request.urlopen(request, timeout=30)
        except urllib.error.HTTPError as error:
            raise ApiError("%s %s answered %d" % (method, _path(url), error.code))
        except (urllib.error.URLError, OSError) as error:
            raise ApiError("%s %s failed: %s" % (method, _path(url), getattr(error, "reason", error)))
        with response:
            raw = response.read()
            link = response.headers.get("Link") or ""
        try:
            return (json.loads(raw.decode("utf-8")) if raw else None), link
        except ValueError:
            raise ApiError("%s %s did not answer JSON" % (method, _path(url)))

    def url(self, path):
        return "%s/repos/%s/%s" % (self.base, self.repo, path)

    def get(self, path):
        return self._request("GET", self.url(path))[0]

    def get_all(self, path):
        """Every item of a list endpoint, following the Link header's rel="next"."""
        items = []
        url = self.url(path) + ("&" if "?" in path else "?") + "per_page=100"
        while url:
            page, link = self._request("GET", url)
            if not isinstance(page, list):
                raise ApiError("GET %s did not answer a list" % _path(url))
            items.extend(page)
            url = next_link(link)
        return items

    def text_at(self, path, ref):
        """A file's text at a commit, or None when it is not there."""
        try:
            item = self.get("contents/%s?ref=%s" % (path, urllib.parse.quote(ref)))
        except ApiError as error:
            if " answered 404" in str(error):
                return None
            raise
        if not isinstance(item, dict) or item.get("encoding") != "base64":
            raise ApiError("GET contents/%s did not answer a base64 file" % path)
        return base64.b64decode(item["content"]).decode("utf-8")

    def set_status(self, sha, state, description, target_url=None):
        body = {"state": state, "context": CONTEXT, "description": fit(description)}
        if target_url:
            body["target_url"] = target_url
        self._request("POST", self.url("statuses/" + sha), body)


def next_link(header):
    for part in header.split(","):
        bits = part.split(";")
        if len(bits) > 1 and any(bit.strip() == 'rel="next"' for bit in bits[1:]):
            return bits[0].strip().strip("<>")
    return None


def _path(url):
    """The path of an API url, for messages (no host, no query)."""
    return urllib.parse.urlsplit(url).path


def main(argv=None, env=None):
    env = os.environ if env is None else env
    argv = sys.argv[1:] if argv is None else argv
    codeowners_path = argv[0] if argv else CODEOWNERS
    for name in ("GITHUB_EVENT_PATH", "GITHUB_REPOSITORY", "GITHUB_TOKEN"):
        if not env.get(name):
            print("core-approvals: %s is not set" % name, file=sys.stderr)
            return 1
    api = Api(env.get("GITHUB_API_URL") or "https://api.github.com", env["GITHUB_REPOSITORY"],
              env["GITHUB_TOKEN"])
    run_url = None
    if env.get("GITHUB_RUN_ID"):
        run_url = "%s/%s/actions/runs/%s" % (env.get("GITHUB_SERVER_URL") or "https://github.com",
                                             env["GITHUB_REPOSITORY"], env["GITHUB_RUN_ID"])
    head_sha = None
    try:
        with open(env["GITHUB_EVENT_PATH"], encoding="utf-8") as fh:
            event = json.load(fh)
        pull = event.get("pull_request") or {}
        head_sha = (pull.get("head") or {}).get("sha")
        number = pull.get("number")
        if not number:
            raise ApiError("the event has no pull request")
        # The event can be older than the pull request: read its current head, author and base.
        pull = api.get("pulls/%d" % number)
        head_sha = pull["head"]["sha"]
        files = []
        for item in api.get_all("pulls/%d/files" % number):
            files.append(item["filename"])
            if item.get("previous_filename"):
                files.append(item["previous_filename"])
        reviews = api.get_all("pulls/%d/reviews" % number)
        base_codeowners = api.text_at(CODEOWNERS, pull["base"]["sha"])
        with open(codeowners_path, encoding="utf-8") as fh:
            codeowners = fh.read()
        # A form the matcher does not understand fails closed: a red status naming the line, exit 1.
        parse_codeowners(codeowners)
        if base_codeowners is not None:
            parse_codeowners(base_codeowners, CODEOWNERS + " on the base branch")
        state, description = decide(files, codeowners, (pull.get("user") or {}).get("login"), reviews,
                                    head_sha, base_codeowners)
        api.set_status(head_sha, state, description, run_url)
    except (ApiError, CodeownersError, OSError, ValueError, KeyError, TypeError) as error:
        reason = ("%s" if isinstance(error, CodeownersError) else "Could not decide: %s") % error
        print("core-approvals: " + reason, file=sys.stderr)
        if head_sha:
            try:
                api.set_status(head_sha, "failure", reason, run_url)
            except ApiError as second:
                print("core-approvals: could not set the failure status either: %s" % second, file=sys.stderr)
        return 1
    print("core-approvals: %s on %s: %s" % (state, head_sha, description))
    return 0


if __name__ == "__main__":
    sys.exit(main())
