"""Token use of subagent transcripts: trial_usage.py <transcript.jsonl>...  (one usage record per API reply)."""
import json
import sys
from pathlib import Path

for name in sys.argv[1:]:
    seen, total = set(), {"input_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0,
                          "output_tokens": 0}
    first = last = None
    model = set()
    for line in Path(name).read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        stamp = record.get("timestamp")
        if stamp:
            first = first or stamp
            last = stamp
        message = record.get("message") or {}
        usage = message.get("usage")
        if not usage or message.get("id") in seen:
            continue
        seen.add(message.get("id"))
        model.add(message.get("model"))
        for key in total:
            total[key] += usage.get(key) or 0
    fresh = total["input_tokens"] + total["cache_creation_input_tokens"] + total["output_tokens"]
    print(Path(name).name, sorted(m for m in model if m), "replies", len(seen))
    print("  new input %d, cache written %d, cache read %d, output %d; without cache reads %d, with %d; %s to %s"
          % (total["input_tokens"], total["cache_creation_input_tokens"], total["cache_read_input_tokens"],
             total["output_tokens"], fresh, fresh + total["cache_read_input_tokens"], first, last))
