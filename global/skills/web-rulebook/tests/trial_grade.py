"""Grade a trial run's citing: usage  trial_grade.py <outputs folder> <transcript.jsonl> <rb.py>

Prints, from the transcript itself (not the agent's own commands.md):
- the rb.py commands the run really ran, in order, with the position of the first file writes;
- every id the result files cite, whether the rulebook holds it, the kind the entry carries against the kind
  the result writes after it, and whether an rb.py `show` (or `topic`) of the run printed it.
"""
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
out_dir, transcript, rb = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
TOPICS = ("accessibility colour content forms images layout logo navigation persuasion phone "
          "search-and-filters spacing speed testing trust type idea").split()
ID = re.compile(r"\b(?:%s)-\d{3}\b" % "|".join(TOPICS))


def tool_uses(node):
    if isinstance(node, dict):
        if node.get("type") == "tool_use":
            yield node
        for value in node.values():
            yield from tool_uses(value)
    elif isinstance(node, list):
        for value in node:
            yield from tool_uses(value)


def tool_results(node):
    if isinstance(node, dict):
        if node.get("type") == "tool_result":
            yield json.dumps(node.get("content"), ensure_ascii=False)
        for value in node.values():
            yield from tool_results(value)
    elif isinstance(node, list):
        for value in node:
            yield from tool_results(value)


steps, printed, seen = [], set(), set()
for line in transcript.read_text(encoding="utf-8").splitlines():
    try:
        record = json.loads(line)
    except json.JSONDecodeError:
        continue
    for use in tool_uses(record):
        if use.get("id") in seen:
            continue
        seen.add(use.get("id"))
        name, data = use.get("name"), use.get("input", {})
        if name in ("Bash", "PowerShell") and "rb.py" in data.get("command", ""):
            for part in re.findall(r"rb\.py\"?\s+([^|;&\n>]+)", data["command"]):
                steps.append("RB " + part.strip())
        elif name in ("Write", "Edit"):
            steps.append("WRITE " + Path(data.get("file_path", "?")).name)
        elif name == "Read":
            steps.append("READ " + Path(data.get("file_path", "?")).name)
        elif name == "Skill":
            steps.append("SKILL " + str(data.get("skill")))
    for text in tool_results(record):
        # an id counts as printed when a tool result held its entry heading or a file of entries was read
        printed.update(re.findall(r"###\s+((?:%s)-\d{3})" % "|".join(TOPICS), text))

print("== steps, in order (%d)" % len(steps))
for step in steps:
    print("  " + step[:230])

print("\n== ids cited")
cited = {}
for path in sorted(out_dir.glob("*")):
    if path.suffix.lower() not in (".md", ".html") or path.name in ("commands.md", "notes.md"):
        continue
    text = path.read_text(encoding="utf-8")
    for match in ID.finditer(text):
        after = text[match.end():match.end() + 14].lower()
        kind = "rule" if after.startswith(" (rule") else "practice" if after.startswith(" (practice") else ""
        cited.setdefault(match.group(), set()).add(kind)
bad = 0
for ident in sorted(cited):
    shown = subprocess.run([sys.executable, "-I", rb, "show", ident], capture_output=True, text=True,
                           encoding="utf-8").stdout
    real = re.search(r"\*\*Kind:\*\* (\w+)", shown)
    exists = ("### " + ident) in shown or ident.startswith("idea-") and ident in shown
    kinds = cited[ident] - {""}
    flags = []
    if not exists:
        flags.append("NOT IN RULEBOOK")
    if real and kinds and kinds != {real.group(1)}:
        flags.append("KIND WRONG: written %s, entry says %s" % (sorted(kinds), real.group(1)))
    if ident not in printed:
        flags.append("NEVER PRINTED IN FULL BY THE RUN")
    bad += bool(flags)
    print("  %-26s %-9s %s" % (ident, real.group(1) if real else "-", "; ".join(flags) or "ok"))
print("\n%d ids cited, %d with a flag; %d entries printed in full by the run" % (len(cited), bad, len(printed)))
