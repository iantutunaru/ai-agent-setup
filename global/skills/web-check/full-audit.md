# Full depth: one agent per topic

Read from `SKILL.md` step 1 when the depth is full. Steps 1, 2 and 5 of `SKILL.md` stay as they are; this file
replaces steps 3 and 4. Quick depth picks entries by their titles; full depth has every `check` entry of every
topic read against the page, which no single context can hold (about 150,000 tokens of entries).

## A. Put the page into files

Agents work from files, in one folder the coordinating chat names (the project's scratch or research folder):

- `measure-<width>.json`: the result of `measure.js` at each width, written out as it came.
- For every further state the frame names (a menu open, a form refused, a panel open): the measure of that
  part alone (`window.WEB_CHECK_ROOT`) as `measure-<width>-<state>.json`, and the part's HTML as
  `state-<state>.html`. A part's measure is 5 to 8 KB against 12 KB for a page, and every agent reads every
  file.
- `SKILL.md` step 2's receiver writes all of these straight from the page. Check `page.script` in each, and
  that `images.notLoaded` is empty.
- `page-<width>.html` or the page's address if agents can fetch it (a local demo: `curl` it), and the paths of
  the source files that build the page (components, styles, text files).
- `frame.md`: step 1's frame, the settled picks, what the page is for in two sentences, a table of the
  folder's files, and where the page's words come from (the site's own text, or text it only shows).

## B. Tell the user the batch, then start it

`RB topics` lists the topics; every topic with `check` entries gets one agent (16 on the full rulebook). Tell the
user the number of agents and entries before starting, and follow the project's rules on the usage meter.
Where a usage limit is near, start them in two waves and read the meter between.
For scale (one page at one width, measured 2026-11-21): 16 agents used 1.82 million tokens. An agent costs
83,000 to 91,000 tokens before its first entry (the frame, the measures, the HTML, the source), so a topic
that hardly applies to the page costs almost as much as one that does; the largest topic (171 entries) took
163,000 tokens and 6 minutes.
Agents: Opus at medium effort, each wave started in one message. Each gets this brief, with its topic filled
in:

```text
You are checking one web page against one topic of a design rulebook. Work only from the files named here.
Do not open a browser, and change no file except the verdicts file you write.

Topic: <topic>
The page: <folder>, files frame.md, measure-<width>.json, page-<width>.html; source: <paths>.

1. Run: python -I "<path to web-rulebook>/rb.py" topic check <topic>
   It prints the entries themselves or, for a long topic, one or more file paths: then read every file in
   full. These are all the entries of your topic.
2. Read frame.md and the measure files, then the page's HTML and source as far as your entries need.
3. Write <folder>/verdicts-<topic>.md with exactly one line per entry, in the entries' order:
   <id> | met | <evidence>
   <id> | not met | <evidence> | <what the entry asks that the page does not do> | <smallest fix>
   <id> | cannot tell | <what you would need to see: name the place on the page and the width>
   <id> | does not apply | <why, in a few words>
   Evidence starts with "measured:" (the field of the measure file and its value), "from the code:" (file and
   line) or "judged:" (what you read in the HTML). A verdict about how something looks that neither the
   measurements nor the code settle is "cannot tell": the coordinating chat will look at the page.
4. Never cite an entry from memory, and never soften or widen a statement: quote the part of it you judge by.
   Judge by the statement's own words: an entry that only a general principle connects to the page does not
   apply; a statement that only describes or permits asks nothing (met where the page does it, does not
   apply otherwise, never not met).
   A practice is a default, a rule binds; write the kind after the id in every "not met" line, as the entry
   gives it. An entry about an organisation's own network (an intranet) does not apply to a public page. An
   entry that speaks against one of the settled picks in frame.md is still "not met"; name the pick.
5. End your reply with three numbers: entries in the topic, lines written, lines "not met". The first two must
   be equal.
```

## C. Check every finding before it counts

An agent's line is a lead. `python -I "${CLAUDE_SKILL_DIR}/leads.py" <folder> <topic>` prints a topic's count,
every not met and cannot tell line, and a fixed sample of 8 of the others. Plan the chats by the leads, not by
the entries: checking is the larger part of the coordinating chat's work. One page left 218 leads, and the 7
of one topic took 25,000 tokens to check. Many leads are one fault under several entries: settle the fault
once and cite every entry. Write what was checked into a `checked.md` in the folder, topic by topic, so a
later chat knows which files still hold only leads.

For each topic file:

1. Count: lines written equals the topic's `check` entries (`RB topics`). A short file goes back to its agent.
2. Every **not met** line: read the entry with `RB show <id>` and confirm the evidence yourself, on the
   measurement or on the page. A line that does not hold becomes met, does not apply, or cannot tell.
3. Every **cannot tell** that names a place: look at that place at that width (a screenshot, a hover, the Tab
   key, the text enlarged) and give the verdict yourself, evidence `judged`.
4. Of the **met** and **does not apply** lines, read a sample of 8 a topic against the page. One wrong line in
   the sample means every line of that topic is read.
5. The same fault found under two entries is one finding that cites both.

Then go on with `SKILL.md` from "Then, for the entries not met" in step 4, and report as in step 5. The report's
"Loaded" line names the topics, the agents and the sample's result.
