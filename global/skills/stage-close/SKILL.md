---
name: stage-close
description: Close a stage of tickets in its own fresh chat - retro, revised ticket list for the user's approval, held tickets, cleanup, docs, commit. Use when a coordinator hands over at the end of a stage, when a stage's last ticket is done, or when the user asks for a stage close or a retro.
---

# Stage close

Runs in a **fresh chat** started from the coordinator's hand-over: a review full of questions for the user stays
cheap only while the chat is small. Merged from three projects' versions (SU-Q10, SU-Q23).

## 0. The project's entry

Read the **Stage close** list under "Where things are" in the project's `AGENTS.md` (`CLAUDE.md` in a project not yet moved).
Every step below takes its paths and choices from it. When the project has no such list, stop: tell the user in one
line that this project still needs `/setup-sync` (its own old stage-close is overridden by this global one,
SU-Q32), and end the chat.

The list, as `/setup-init` and `/setup-sync` write it (angle brackets are the project's values):

```markdown
- **Stage close:**
  - Tickets: <index file>; a stage is <how the index marks one: a table, a Stage column>; parked status: <held | parked>
  - Decisions: <where this chat's decisions go and their ids, e.g. the stage-close ticket's `<P>-Txx-Qn`>
  - Retro: <the stage-close ticket file | a file with one section per stage>
  - Roadmap: <where later stages are outlined and their status lines live, e.g. docs/design.md>
  - Cleanup: generic `--tickets <ticket folder>` | <the project's own command>
  - Tests: <commands, with the folder each runs from>
  - Branch: <own branch, merged into the main branch on the user's OK | the main checkout>
  - Push: <no, the user pushes | yes>
  - Also: <project extras: a token-baseline row, a side stage to offer, docs to refresh at close>
```

"Generic" cleanup is this skill's script: `python "${CLAUDE_SKILL_DIR}/cleanup.py" --tickets <folder>`, run from
the project folder (`--help` lists the sections and flags). The path in front of the script's name is this skill's
folder. A tool that shows it as a `${...}` name has not filled it in: put the folder this file is in there.

## 1. Facts

Read the hand-over, the ticket index, every ticket of the stage, and their decision-log sections. Run the cleanup
dry run and keep its output for steps 4 and 5.

Done when every ticket of the stage has a row in the retro table, filled from those files.

## 2. Retro

In the retro place, one row per ticket of the stage:

| Ticket | Estimated chats | Actual chats (peak context each) | Rounds with the user (grilling / test) | Why the estimate missed |

then **patterns** (each with the rows it rests on) and **lessons**: each lesson a rule change or a ticket, never
only prose. "Why it missed" names a cause written in the ticket's own log (a reopened decision, a test round that
brought fixes, a re-pick, a crash, a result that broke the plan), or says unknown. A read-only helper may gather
the rows; its tokens go into this chat's run log.

Done when every row has all five cells and every lesson points at the rule or ticket it became.

## 3. Roadmap

For every ticket not `done` or `dropped`, in order: still needed? still the right size, measured against the
retro's actual chats? dependencies still true after this stage's results? A ticket the stage's facts made
obsolete, merged or split is proposed as such; a re-size goes beside the first estimate, never over it. Each
held or parked ticket goes back to the user: start in the next stage, keep it parked, or drop it. Tickets of the
next stage that exist only as an outline in the roadmap are written as files with sizes. A roadmap item still "in
progress" gets a current one-line status.

Put the revised list to the user in **one** grilling round (plain language first: what each change does to what
the user will see and test next; a recommendation per item). The next stage starts only after the user approves.

Done when the user has answered every item, and the index and the roadmap show the approved list.

## 4. Cleanup

Show the user the dry run's totals and every `keep` line with its reason. Then, on the user's OK:

1. Copy every scratchpad file a doc cites into the repo (small text: next to the citing ticket's research or
   evidence; large: the project's git-ignored state folder), or, for a large dump a script remakes, replace the
   citation with the command that remakes it. Point the citing doc at the new place.
2. Run the cleanup with `--yes` and the flags the user approved (`--discard <worktree>`; `--keep-hours 0` once
   `list_sessions` shows no session of this project running).
3. Archive the app sessions whose worktrees were removed (`archive_session`; never delete a session).

Done when a second dry run lists only the `keep` lines the user saw, plus this chat's own branch.

## 5. Docs

Fix every `docs` line of the dry run. Then write each fact **once**:

- the ticket file holds the full result and the run log;
- the index row: status plus at most one short line, with the ids;
- the roadmap row: a few lines and a pointer to the index;
- the decision log holds the decisions; a hand-over lists only what is open, with links.

Copies left over from earlier stages are trimmed to that shape.

Done when a dry run's `docs` section is empty, or every remaining line has been shown to the user with its reason.

## 6. Close

The stage-close ticket (if the project keeps one) `done`; the setup and fact docs the entry's "Also" names, if
anything changed; every test command passes; commit; on the user's OK merge into the main branch when the chat
worked on its own branch; push only when the entry says yes. Recommend the next stage's first ticket in one line;
the user starts it.
