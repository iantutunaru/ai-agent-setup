# Trying the web skills with agents

The cases are the folders under each skill's `evals/` (`web-check`, `web-look`, `web-text`, `web-rulebook`), in
skill-creator's layout: `prompt.md` is what the user types, `case.yaml` says what a good result looks like,
`graders/` holds one statement a file. The first four graders of every case are the citing rules.

## Running a case

One agent a case, Opus at medium effort, all cases of a batch started in one message. Read the usage meter
before and after, and tell the user the batch's size first. Outputs go to a work folder outside the repos
(`<skill>-workspace/iteration-<n>/<case>/with_skill/outputs/`); a case's input files are copied there first.
No run without the skill is planned: without `rb.py` an agent cannot reach the rulebook, so the comparison
shows nothing.

The brief, with the four marked places filled in:

```text
You are trying out a skill that is not installed yet. Work as if a user had typed the task below and the skill
had fired.

- Skill path: <the skill's folder>
  Read its SKILL.md first and follow it. Wherever it writes ${CLAUDE_SKILL_DIR}, that is this folder. Its
  sibling folder web-rulebook (same parent) holds the lookup tool it names.
- Work folder (your input files are here; save every output here): <work folder>
- Input files: <names, or "none">. There is no project around this task: no CLAUDE.md, no brand file, no
  settled picks.
- Task, as the user typed it:

  "<the text of prompt.md under its settings block>"

Limits of this trial:
- Do not use any browser tool (the browser pane belongs to another chat). Do not read anything inside a
  skill's `tests` or `evals` folders. Do not open the rulebook's files directly; use only the lookup tool the
  skill names. Change nothing outside the work folder.
- In a Bash tool call `python` is Python 3.14; `python3` is a placeholder that does nothing.
- If the Write tool refuses a .md file, write it with a short Python script instead.

Save in the work folder:
1. `report.md`: the skill's result, exactly as you would give it to the user (and any file the task asks for).
2. `commands.md`: first line your model name and the output of `echo $CLAUDE_EFFORT`; then every lookup
   command you ran, in the order you ran it, one per line, complete (with all ids), and a marker line
   `-- result written` at the point where you began writing the result.
3. `notes.md`: where the skill's text was unclear, missing something, or made you guess; where the tool's
   output surprised you; anything you did that the skill did not tell you to do. Quote the line of SKILL.md.

Your final reply: three lines only (what the result holds, the number of entries read in full, the most
important unclear point).
```

## Grading a run

An agent's transcript is `~/.claude/projects/<project>/<session id>/subagents/agent-<agent id>.jsonl` (the
`.output` file the Agent tool names stayed empty on 2026-11-21).

    python trial_grade.py <outputs folder> <transcript.jsonl> <path to rb.py>
    python trial_usage.py <transcript.jsonl> ...

`trial_grade.py` prints the steps the run really took, in order, and for every id the result cites: whether
the rulebook holds it, whether the kind written after it is the entry's, and whether the run printed the entry
in full. An id flagged "never printed" that stands only inside a quoted Conflict line is no fault. It does not
read statements: take a sample of the findings, `rb.py show` their entries, and read each finding against the
statement. Then go through the case's other graders by hand, and read `notes.md`: it is where the skill's gaps
show.
