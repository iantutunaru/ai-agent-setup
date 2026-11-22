"""Flag AI-writing tells in texts others will read (SU-Q27).

usage: python -I check_text.py [--rules <project rules>] <file> [<file> ...]
Exits 1 if any em/en dash, " -- " or banned word is found. Banned words are the "Never use" sections of the shared
writing-rules.md next to this script and of the project's rules file (default: style/writing-rules.md in the
current folder; the check runs on the shared list alone, and says so, when the project has none).
HTML tags are ignored, so .html email templates can be checked as they are.
"""
import argparse
import os
import re
import sys

SHARED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "writing-rules.md")


def never_use(path):
    """The comma-separated words of a rules file's "## Never use" section ([] when it has none)."""
    text = open(path, encoding="utf-8").read()
    if "## Never use" not in text:
        return []
    block = text.split("## Never use", 1)[1].split("\n", 1)[1].split("\n## ", 1)[0]
    block = "\n".join(l for l in block.splitlines() if not l.startswith("#"))
    return [w.strip(" .\n") for w in block.split(",") if w.strip(" .\n") and "..." not in w]


def issues(path, words):
    out = []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        plain = re.sub(r"<[^>]+>", " ", line)
        for m in re.finditer(r"[—–]|(?<=\w) -- (?=\w)", plain):
            out.append(f"{path}:{n}: dash {m.group()!r}: {plain.strip()[:90]}")
        low = plain.lower()
        for w in words:
            if re.search(r"\b" + re.escape(w.lower()) + r"\b", low):
                out.append(f"{path}:{n}: banned '{w}': {plain.strip()[:90]}")
    return out


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rules", default=os.path.join("style", "writing-rules.md"), help="the project's rules file")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args(argv)
    words = never_use(SHARED)
    if os.path.isfile(args.rules):
        words += [w for w in never_use(args.rules) if w not in words]
    else:
        print(f"note: no project rules at {args.rules}; shared list only")
    found = [i for p in args.files for i in issues(p, words)]
    print("\n".join(found + [f"{len(found)} issue(s)"]))
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
