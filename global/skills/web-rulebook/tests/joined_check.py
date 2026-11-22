"""After the merge: which ids left, and does `rb.py show <old id>` lead to the entry each went into?

usage: joined_check.py <titles list before the merge> <rb.py>
"""
import io
import re
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
before_file, rb = Path(sys.argv[1]), sys.argv[2]
ID = re.compile(r"(?m)^([a-z-]+-\d{3}) \| (\w+) \| (.*)$")


def run(*args: str) -> str:
    return subprocess.run([sys.executable, "-I", rb, *args], capture_output=True, text=True,
                          encoding="utf-8").stdout


before = {m.group(1): m.group(3) for m in ID.finditer(before_file.read_text(encoding="utf-8"))}
listing = run("titles", "any", "all")
path = re.search(r"(\S:\\.*?\.md)", listing)
after_text = Path(path.group(1)).read_text(encoding="utf-8") if path else listing
after = {m.group(1): m.group(3) for m in ID.finditer(after_text)}
gone = sorted(set(before) - set(after))
new = sorted(set(after) - set(before))
moved_title = [i for i in set(before) & set(after) if before[i].split(" | ")[0] != after[i].split(" | ")[0]]
print(f"before {len(before)}, after {len(after)}, ids gone {len(gone)}, ids new {len(new)}, "
      f"same id with another title {len(moved_title)}")

kinds = {"led to its target": [], "cross-topic": [], "not found": [], "other": []}
for ident in gone:
    out = run("show", ident)
    m = re.search(r"was joined into (\S+?);", out)
    if m:
        kinds["led to its target"].append(ident)
        if m.group(1).rsplit("-", 1)[0] != ident.rsplit("-", 1)[0]:
            kinds["cross-topic"].append(f"{ident} -> {m.group(1)}")
    elif "### " in out:
        kinds["other"].append(ident)
    else:
        kinds["not found"].append(ident + ": " + out.strip().splitlines()[0][:110] if out.strip() else ident)
for name, items in kinds.items():
    print(f"\n{name}: {len(items)}")
    for item in items[:6]:
        print("  ", item)
for ident in moved_title[:5]:
    print("retitled:", ident, "|", before[ident][:60], "=>", after[ident][:60])
