"""Print what the coordinating chat must check in one topic's verdicts file (web-check, full-audit.md, part C).

    python -I leads.py <folder> <topic> [--sample 8] [--seed 20]

Prints the counts, every "not met" and "cannot tell" line, and a fixed random sample of the "met" and
"does not apply" lines. Reads only; the seed makes the sample the same on every run.
"""
import random
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # -I ignores PYTHONUTF8; a Windows console codepage has no "²"

folder, topic = Path(sys.argv[1]), sys.argv[2]
args = sys.argv[3:]
sample = int(args[args.index("--sample") + 1]) if "--sample" in args else 8
seed = int(args[args.index("--seed") + 1]) if "--seed" in args else 20

lines = [ln for ln in (folder / f"verdicts-{topic}.md").read_text(encoding="utf-8").splitlines() if ln.strip()]
kinds = {"not met": [], "cannot tell": [], "met": [], "does not apply": []}
odd = []
for ln in lines:
    parts = [p.strip() for p in ln.split("|")]
    if len(parts) >= 2 and parts[1] in kinds:
        kinds[parts[1]].append(ln)
    else:
        odd.append(ln)

print(f"{topic}: {len(lines)} lines; " + ", ".join(f"{k} {len(v)}" for k, v in kinds.items()) + f"; unreadable {len(odd)}")
for k in ("not met", "cannot tell"):
    print(f"\n## {k}")
    for ln in kinds[k]:
        print(ln)
rest = kinds["met"] + kinds["does not apply"]
random.Random(seed).shuffle(rest)
print(f"\n## sample of {min(sample, len(rest))} met / does not apply")
for ln in rest[:sample]:
    print(ln)
if odd:
    print("\n## unreadable")
    for ln in odd:
        print(ln)
