# Full depth: the sheets of a whole stage

Read from `SKILL.md` step 1 when several sheets are prepared together. Steps 1 and 3 to 6 of `SKILL.md` stay;
this file replaces step 2. Quick depth picks entries by their titles; here every `look` entry of every topic is
read against all the sheets at once, which no single context can hold (about 150,000 tokens of entries).

## A. Write the frame to a file

`sheets.md`, in a folder the coordinating chat names: one numbered line per sheet with the question it answers
and its widths, then the settled picks, then what the site is for in two sentences.

## B. Tell the user the batch, then start it

`RB topics` lists the topics; every topic with `look` entries gets one agent (16 on the full rulebook), plus one
for the project's own ideas list when it has one (`docs/web-ideas.md`). Tell the user the number of agents
before starting, and follow the project's rules on the usage meter. Agents: Opus at medium effort, all started in one message. The brief, with the topic filled in:

```text
You are matching one topic of a web design rulebook to a list of design questions. Work only from the files
named here.

Topic: <topic>
The questions: <folder>/sheets.md

1. Run: python -I "<path to web-rulebook>/rb.py" topic look <topic>
   It prints one or more file paths. Read every file in full. These are all the entries of your topic.
2. Read sheets.md.
3. Write <folder>/look-<topic>.md: under a heading per sheet number, one line for every entry that bears on
   that sheet's question:
   <id> | <kind> | fixed or open | <why it bears on this sheet, in one sentence that quotes the entry's words>
   "open" means the entry has a Conflict line, or pulls against another entry you list for the same sheet;
   name the other side. Every other entry is "fixed". An entry may stand under several sheets.
   An entry that bears on no sheet is left out.
4. Never widen an entry to make it fit: if only a general principle connects it to the sheet, leave it out.
5. End your reply with: entries read, entries listed, and per sheet the number of lines.
```

Where the project has an ideas file, the ideas agent runs `rb.py ideas site` and `rb.py show` for the ideas it
lists, and writes `look-ideas.md` in the same shape, each line marked "idea, not proven, page not read".

## C. Read what the sheets will rest on

An agent's line is a lead. For each sheet, `RB show` every entry the agents listed for it and read the
statement: an entry enters step 3 of `SKILL.md` only if its statement, not its title or the agent's sentence,
bears on the question. Then `RB find <word> --use check` for what each sheet's built page will be measured on
(step 2.4 of `SKILL.md`), and go on with step 3.
