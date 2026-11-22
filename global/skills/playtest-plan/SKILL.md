---
name: playtest-plan
description: Plan a game playtest and read its notes afterwards. Use in a game project when the user is about to play (against the bot, on two PCs, a milestone gate, "what should I look for?"); when writing a playtest file; when turning playtest notes or feedback into hypotheses, watch-list entries or backlog candidates; or when deciding whether a question needs a human playtest or a headless batch.
---

# Playtest plan

A playtest answers **questions**; a session without them is just playing (Fullerton ch. 9, "A Primer for
Playtesting"; Schell ch. 28, "Why?"). This skill writes each question with a **prediction** before play, gives the
user a short **script** and a **notes sheet**, and afterwards turns what was seen into **hypotheses** with a check
each. When the user is the only tester, their notes are evidence about their experience, never a decision (the
code profile).

`<setup>` below is the agent-setup repo's link: `$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in
ChatGPT; use the one that exists.

## Steps

0. **Read the project's entry.** The **Game design** list under "Where things are" in the project's `AGENTS.md`
   (`CLAUDE.md` in a project not yet moved); its fields are defined in `<setup>/research/game-design/README.md`.
   This skill reads Rules, Data, Backlog, Playtests, Builds, Levers, Batch, Probe and Tests, and Also for the
   project's extras. With no such list, tell the user in one line that the project needs `/setup-sync` to add it,
   and stop. A field read here that says `none yet` (every field does in a project `/setup-init` just made):
   name it, say what the plan lacks without it, and offer to set it now; the plan goes on with what the other
   fields give. With `Builds: none yet` the script cannot say how to start the build: ask the user. With
   `Playtests: none yet` the playtest file goes where the `guided-session` skill puts checklists. Done when the
   entry is read.

1. **Collect the candidate questions.** From the ticket's manual test, the latest playtest file (its candidate
   tickets and verdict), the open entries of the watch-list, and what the build changed since the last playtest
   (`git log` since its build or date). Done when every source is read and each candidate is one line.

2. **Route each question** with [references/human-or-batch.md](references/human-or-batch.md): win rates, counts,
   timings and "does X ever happen" go to a headless batch (`balance-check` skill); reading, feel, confusion, pace
   and "do I want another match" stay for the human. Done when every candidate is marked *play* or *batch*, and
   each *batch* one names its command (or says the project has no batch yet).

3. **Pick at most three play questions** and write each as a prediction that could fail: what the user will see,
   by when, as a number where one exists ("I spot an attacked unit within 5 s of the first shot"; Fullerton ch. 9,
   "Metrics in Game Design"). Write the expected result before play, so a surprise can be noticed (Schell ch. 28,
   "The Second What"). The rest wait for a later session. Done when each picked question has a prediction and a
   way to answer it (a note, a replay number, a debug readout).

4. **Pick the branch and set up the session:**

   | The session | Branch | Read |
   |---|---|---|
   | the user alone against the bot, on one PC | solo | [references/solo.md](references/solo.md) |
   | two PCs: a gate, a netcode check, or a second person playing | two-PC | [references/two-pc.md](references/two-pc.md) |

   A setup choice that is the user's (who plays the other seat, which network, how long a match) goes to them as a
   question with a recommendation, in one round (the grilling skill the rules name). Done when the plan names the
   build, map, bot level, match settings, number and length of matches, and each step that needs the second PC is
   marked **(second PC)**.

5. **Write the notes sheet** with [references/watching.md](references/watching.md): the picked questions with
   their predictions, the categories to tally during play, and the after-match questions. Done when the user could
   fill it in without asking what a line means.

6. **Show the plan** to the user in one message: questions with predictions, setup, steps, notes sheet, and the
   *batch* questions with who runs them. Keep it to one screen; the playtest file (from the entry's template)
   takes the long form. Done when the user has the plan before they start.

7. **After play, read the notes** with [references/reading-notes.md](references/reading-notes.md): ask the
   after-match questions, turn each note into a problem and a hypothesis, check what a replay or batch can check,
   and file each one. Done when every note has landed in exactly one place: the playtest file's verdict, a
   watch-list entry, a backlog candidate, or a ticket that already owns it.

## Rules

- A ticket's manual test and a two-PC netcode pass/fail check follow the global `guided-session` skill; this skill
  plans playtests of feel and reading.
- One session, one to three questions. A new question found in play becomes a hypothesis for the next session.
- Change one thing between sessions you mean to compare (build, bot level, map, match settings), and record it.
- A note names a problem; the user's proposed fix goes beside it as one option (Fullerton ch. 9, the tester as
  patient and the designer as doctor). Design decisions stay with the user, in a grilling round.
- A source that argues against how the project runs playtests or against a design rule becomes a candidate line
  in the entry's Backlog file (source, rule, why).
- Cite the books in our own words, no quote over 12 words. Sources: `<setup>/research/game-design/README.md`.
