"""Lookup in the web design rulebook: hands out only the entries asked for.

The rulebook is the master copy in research/web-design/rulebook/ of the agent-setup repo (one file per topic,
written by a build that is not published). Skills never open those files; they call this script.

    python -I rb.py topics                         the topics, with entry counts per use
    python -I rb.py titles <use> <topic>...        one line per entry: id, kind, title ("all" = every topic)
    python -I rb.py show <id>...                   the full text of entries (add --sources for the book pages)
    python -I rb.py topic <use> <topic>            every entry of one topic for one use, in full
    python -I rb.py find <word>...                 entries whose title or statement holds every word
    python -I rb.py ideas [site|pitch] [word...]   titles of the project's own ideas list, if it has one
    python -I rb.py taste <word>...                lines of the taste and unconfirmed list

The ideas list is not part of the rulebook: it is read from the file named by the environment variable
WEB_IDEAS_FILE, else from docs/web-ideas.md under the current folder.

<use> is look, check, text or any. Output longer than a tool result can carry is written to a file in the
temp folder and the path is printed; read that file. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

USES = ("look", "check", "text")
SLIM = ("Statement", "Kind", "Study (as the book reports it)", "Current source", "Needs source", "Conflict")
IDEA = ("Statement", "Where", "Would change")
PROVENANCE = ("Use", "Sources", "Also in (not read)", "Also in", "Asked of the source", "Read", "From")
SKIP_FILES = {"README.md", "dropped.md", "taste.md", "ideas.md"}
IDEAS_DEFAULT = Path("docs") / "web-ideas.md"   # under the current folder
STDOUT_LIMIT = 24000   # characters; a Bash tool result is cut at 30,000
PART_BYTES = 60000     # one Read call carries about this much
ABOUT = {   # what a topic mostly holds; a subject is spread over topics, so `find` its words as well
    "accessibility": "screen readers, keyboard use, the heading outline, native elements, text alternatives, zoom",
    "colour": "palettes and schemes, what colours signal, contrast, colour on screens",
    "content": "what a page says and in what order: text for scanning, headings, lists, the home page's message, "
               "video and audio, dates, languages, keeping content current",
    "forms": "what to ask, fields and labels, errors, buttons, steps, passwords",
    "images": "photos, icons, illustrations, formats and file weight, text alternatives",
    "layout": "grids, hierarchy and composition, page parts (cards, sliders, accordions, captions), layouts that "
              "fit any width, wireframes",
    "logo": "drawing a logo and placing it",
    "navigation": "site structure, menus, how links look and behave, breadcrumbs, page addresses, language choice",
    "persuasion": "how people choose: defaults, framing, prices and bundles, what others do, memory and stories",
    "phone": "touch, small screens, the viewport, forms and navigation on a phone",
    "search-and-filters": "the search box, results, sorting, filters",
    "spacing": "empty space, margins, units, the baseline grid",
    "speed": "response-time limits, page weight, requests, how fast a page feels",
    "testing": "testing with real people (most entries), and technical checks: browsers, text size, slow lines",
    "trust": "first impression, credibility, contact facts, prices shown, honesty",
    "type": "typefaces, sizes, line length, leading, emphasis, punctuation, web fonts, Greek and Cyrillic",
}
CITE = ("\n---\nCite an entry by its id and kind, written `<id> (rule)` or `<id> (practice)`. A rule binds: going against it is a finding, or "
        "the user's explicit decision with the evidence shown. A practice is a default: say what it gives and "
        "what bending it loses. Pass on a Conflict line with the entry. An id that is not in this output is not "
        "cited from memory.")


def rulebook_dir() -> Path:
    env = os.environ.get("WEB_RULEBOOK_DIR")
    places = [Path(env)] if env else []
    places.append(Path(__file__).resolve().parents[3] / "research" / "web-design" / "rulebook")
    places.append(Path.home() / ".claude" / "setup" / "research" / "web-design" / "rulebook")
    for place in places:
        if (place / "README.md").is_file():
            return place
    sys.exit("rb.py: the rulebook was not found; looked in: " + "; ".join(str(p) for p in places))


def ideas_file() -> Path | None:
    """The project's own ideas list: WEB_IDEAS_FILE, else docs/web-ideas.md under the current folder."""
    env = os.environ.get("WEB_IDEAS_FILE")
    place = Path(env) if env else Path.cwd() / IDEAS_DEFAULT
    return place if place.is_file() else None


class Entry:
    def __init__(self, topic: str, block: str):
        head, _, body = block.partition("\n")
        self.id, _, self.title = (part.strip() for part in head.partition(" · "))
        self.topic = topic
        self.fields: list[tuple[str, str]] = []
        for line in body.splitlines():
            m = re.match(r"- \*\*(.+?):\*\* (.*)", line)
            if m:
                self.fields.append((m.group(1), m.group(2).strip()))

    def get(self, name: str) -> str:
        return " ".join(v for k, v in self.fields if k == name)

    @property
    def kind(self) -> str:
        return self.get("Kind") or "idea"

    @property
    def uses(self) -> set[str]:
        return {u.strip() for u in self.get("Use").split(",") if u.strip()}

    def line(self) -> str:
        return f"{self.id} | {self.kind} | {self.title}" + (" | conflict" if self.get("Conflict") else "")

    def text(self, sources: bool = False) -> str:
        keep = IDEA if self.kind == "idea" else SLIM
        out = [f"### {self.id} · {self.title}"]
        for k, v in self.fields:
            if k in keep or (sources and k in PROVENANCE):
                out.append(f"- **{k}:** {v}")
        if self.kind == "idea":
            out.append("- **Kind:** idea, not proven, its book page not read")
        return "\n".join(out)


def read_entries(path: Path, topic: str) -> list[Entry]:
    text = path.read_text(encoding="utf-8")
    if topic == "ideas":   # the file's own "Dropped" section holds no ideas
        text = text.split("\n## Dropped", 1)[0]
    return [Entry(topic, block) for block in re.split(r"(?m)^### ", text)[1:]]


class Rulebook:
    def __init__(self, folder: Path):
        self.folder = folder
        self.topics = sorted(p.stem for p in folder.glob("*.md") if p.name not in SKIP_FILES)
        self._cache: dict[str, list[Entry]] = {}

    def entries(self, topic: str) -> list[Entry]:
        if topic not in self._cache:
            if topic != "ideas" and topic not in self.topics:
                sys.exit(f"rb.py: no topic '{topic}'; the topics are: {', '.join(self.topics)}")
            if topic == "ideas":
                path = ideas_file()
                self._cache[topic] = read_entries(path, topic) if path else []
            else:
                self._cache[topic] = read_entries(self.folder / f"{topic}.md", topic)
        return self._cache[topic]

    def pick(self, use: str, topics: list[str]) -> list[Entry]:
        if use not in USES + ("any",):
            sys.exit(f"rb.py: the use is look, check, text or any, not '{use}'")
        names = self.topics if topics in (["all"], []) else topics
        found = [e for t in names for e in self.entries(t)]
        return found if use == "any" else [e for e in found if use in e.uses]

    def by_id(self, entry_id: str) -> Entry | None:
        topic = "ideas" if entry_id.startswith("idea-") else entry_id.rsplit("-", 1)[0]
        if topic != "ideas" and topic not in self.topics:
            return None
        return next((e for e in self.entries(topic) if e.id == entry_id), None)

    def joined_into(self, entry_id: str) -> str | None:
        """The id that now holds an entry folded into another one, from `_joined.json` (old id -> current id)."""
        joined_file = self.folder / "_joined.json"
        if not joined_file.is_file():
            return None
        target = json.loads(joined_file.read_text(encoding="utf-8")).get(entry_id)
        return target if target and self.by_id(target) else None


def emit(text: str, name: str, parts: bool = False) -> None:
    """Print, or write to the temp folder when a tool result could not carry it."""
    if len(text) <= STDOUT_LIMIT:
        print(text)
        return
    folder = Path(tempfile.gettempdir()) / "web-rulebook"
    folder.mkdir(exist_ok=True)
    chunks = [text]
    if parts and len(text.encode("utf-8")) > PART_BYTES:
        chunks, current = [], ""
        for block in re.split(r"(?m)^(?=### )", text):
            if current and len((current + block).encode("utf-8")) > PART_BYTES:
                chunks.append(current)
                current = ""
            current += block
        chunks.append(current)
    print(f"Too long for a tool result ({len(text):,} characters). Read in full:")
    for n, chunk in enumerate(chunks, 1):
        suffix = f"-{n}of{len(chunks)}" if len(chunks) > 1 else ""
        path = folder / f"{name}{suffix}.md"
        path.write_text(chunk, encoding="utf-8")
        print(f"  {path}  ({chunk.count(chr(10)) + 1} lines)")


def header(rb: Rulebook, what: str, n: int) -> str:
    return (f"# {what}: {n} entries\n"
            "A rule rests on a study, a measurement or a current primary source. A practice is an author's "
            "working rule, a default a pick may override.\n")


def cmd_topics(rb: Rulebook, args) -> None:
    rows = ["topic | entries | rules | look | check | text | mostly holds"]
    for t in rb.topics:
        es = rb.entries(t)
        rows.append(f"{t} | {len(es)} | {sum(e.kind == 'rule' for e in es)} | "
                    + " | ".join(str(sum(u in e.uses for e in es)) for u in USES) + f" | {ABOUT.get(t, '')}")
    ideas = rb.entries("ideas")
    rows.append("\nA subject is spread over topics (buttons: navigation, forms, layout, images), so besides a "
                "topic's titles run `rb.py find <word>` for the nouns of what you are working on.")
    rows.append(f"ideas list: {len(ideas)} ideas (never a rule; `rb.py ideas`)" if ideas_file()
                else "ideas list: none in this project")
    print("\n".join(rows))


def cmd_titles(rb: Rulebook, args) -> None:
    es = rb.pick(args.use, args.topics)
    names = "all" if args.topics in (["all"], []) else "-".join(args.topics)
    listed = "all" if names == "all" else ", ".join(args.topics)
    lines = [header(rb, f"Titles, use {args.use}, topics {listed}", len(es)), "id | kind | title (| conflict: another entry or source says otherwise)"]
    topic = None
    for e in es:
        if e.topic != topic:
            topic = e.topic
            lines.append(f"\n## {topic}")
        lines.append(e.line())
    lines.append("\nFull text of the ones that apply: rb.py show <id> <id> ...")
    emit("\n".join(lines), f"titles-{args.use}-{names}")


def cmd_show(rb: Rulebook, args) -> None:
    out, missing = [], []
    for entry_id in args.ids:
        entry_id = entry_id.strip(",;")
        e = rb.by_id(entry_id)
        target = None if e else rb.joined_into(entry_id)
        if e:
            out.append(e.text(args.sources))
        elif target:
            out.append(f"{entry_id} was joined into {target}; cite {target} from now on.\n"
                       + rb.by_id(target).text(args.sources))
        else:
            missing.append(entry_id)
    if missing:
        out.append("Not in the rulebook (check the id; `rb.py find <words>` finds an entry by its words): "
                   + ", ".join(missing))
    emit("\n\n".join(out) + CITE, "show-" + "-".join(args.ids[:3]), parts=True)
    if missing:
        sys.exit(1)


def cmd_topic(rb: Rulebook, args) -> None:
    es = rb.pick(args.use, [args.topic])
    text = header(rb, f"{args.topic}, use {args.use}", len(es)) + "\n" + "\n\n".join(
        e.text(args.sources) for e in es) + CITE
    emit(text, f"topic-{args.use}-{args.topic}", parts=True)


def cmd_find(rb: Rulebook, args) -> None:
    words = [w.lower() for w in args.words]
    starts = [re.compile(r"\b" + re.escape(w)) for w in words]   # "form" finds "forms", not "information"
    scored = []
    for e in rb.pick(args.use, args.topic or ["all"]):
        title, body = e.title.lower(), e.get("Statement").lower()
        in_title = [bool(w.search(title)) for w in starts]
        hits = [t or bool(w.search(body)) for t, w in zip(in_title, starts)]
        if any(hits) if args.any else all(hits):
            scored.append((-sum(in_title), -sum(hits), e.id, e))
    scored.sort(key=lambda s: s[:3])
    how = "" if len(words) == 1 else "any of: " if args.any else "every one of: "
    shown = ", ".join(f'"{w}"' if " " in w else w for w in words)
    lines = [header(rb, f"Find {how}{shown} (use {args.use})", len(scored)),
             "A word matches a word's start; a phrase goes in quotes as one word.\n",
             "id | kind | title (| conflict: another entry or source says otherwise)"]
    in_titles = [s for s in scored if s[0]]
    if in_titles:
        lines += ["\n## A word is in the title"] + [s[3].line() for s in in_titles]
    if len(in_titles) < len(scored):
        lines += ["\n## Only in the statement"] + [s[3].line() for s in scored if not s[0]]
    if not scored:
        lines.append("Nothing found. The rulebook holds what the books say; try another word for the same "
                     "thing, or `rb.py titles any <topic>`. No entry is not a rule against.")
    emit("\n".join(lines), "find-" + "-".join(words[:3]))


def cmd_ideas(rb: Rulebook, args) -> None:
    if not ideas_file():
        print("This project has no ideas list. To add one, write docs/web-ideas.md (or name a file in "
              "WEB_IDEAS_FILE) with entries in the rulebook's format: `### idea-001 · <title>`, then "
              "`- **Statement:**`, `- **Where:** site|pitch` and `- **Would change:**` lines.")
        return
    where = args.words[0] if args.words and args.words[0] in ("site", "pitch") else None
    words = [w.lower() for w in (args.words[1:] if where else args.words)]
    es = [e for e in rb.entries("ideas")
          if (not where or where in e.get("Where"))
          and all(w in (e.title + " " + e.get("Statement") + " " + e.get("Would change")).lower() for w in words)]
    lines = [f"# Ideas: {len(es)}\nFrom this project's ideas file ({ideas_file()}). An idea is never a rule, nothing "
             "in it is proven, and its book page has not been read.\n", "id | where | title"]
    lines += [f"{e.id} | {e.get('Where')} | {e.title}" for e in es]
    emit("\n".join(lines), "ideas-" + "-".join([where or "all"] + words[:2]))


def cmd_taste(rb: Rulebook, args) -> None:
    words = [w.lower() for w in args.words]
    lines = [ln for ln in (rb.folder / "taste.md").read_text(encoding="utf-8").splitlines()
             if ln.startswith("- ") and all(w in ln.lower() for w in words)]
    head = (f"# Taste and unconfirmed: {len(lines)} lines\nAn author's preference, or a claim a current source "
            "overturned. Never a reason for or against a design; say \"designers differ here\".\n")
    emit(head + "\n".join(lines), "taste-" + "-".join(words[:3]))


def main(argv: list[str] | None = None) -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):   # python -I ignores PYTHONUTF8; the entries are not ASCII
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("topics").set_defaults(run=cmd_topics)
    p = sub.add_parser("titles")
    p.add_argument("use")
    p.add_argument("topics", nargs="*")
    p.set_defaults(run=cmd_titles)
    p = sub.add_parser("show")
    p.add_argument("ids", nargs="+")
    p.add_argument("--sources", action="store_true")
    p.set_defaults(run=cmd_show)
    p = sub.add_parser("topic")
    p.add_argument("use")
    p.add_argument("topic")
    p.add_argument("--sources", action="store_true")
    p.set_defaults(run=cmd_topic)
    p = sub.add_parser("find")
    p.add_argument("words", nargs="+")
    p.add_argument("--use", default="any")
    p.add_argument("--topic", action="append")
    p.add_argument("--any", action="store_true")
    p.set_defaults(run=cmd_find)
    p = sub.add_parser("ideas")
    p.add_argument("words", nargs="*")
    p.set_defaults(run=cmd_ideas)
    p = sub.add_parser("taste")
    p.add_argument("words", nargs="+")
    p.set_defaults(run=cmd_taste)
    args = ap.parse_args(argv)
    args.run(Rulebook(rulebook_dir()), args)


if __name__ == "__main__":
    main()
