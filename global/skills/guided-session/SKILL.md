---
name: guided-session
description: Protocol for a round of steps only the user can do - playing a build, working at a device or car unit, reading values in a running program, taking photos or timings. Use when a ticket needs such a round, when writing its checklist, when reading the user's results, or when a fix round starts on a failed row.
---

# Guided session

The user does the steps; the assistant prepares the round, reads the results and records them. Every round costs the user
minutes and the chat tokens, so a round is short and every row asks one thing. Merged from three projects' earlier
versions (`re-session`, `car-session`, `playtest`) (SU-Q10, SU-Q25, SU-Q26).

## 0. The project's notes

Read the file the project's `AGENTS.md` (`CLAUDE.md` in a project not yet moved) names under "Where things are" as **Guided
sessions** (e.g. `docs/sessions.md`). It holds what is particular to this project: the tools the assistant runs between
rounds and which to try first, what must be done before a round (build synced, automatic checks, what to bring),
where checklists and results go and how files are named, what counts as a write and how it is undone, safety
conditions, and any rule that overrides a default below. With no entry, use the defaults below (checklists in
`docs/sessions/<ticket>-r<N>.md`) and tell the user in one line that `/setup-sync` adds the project's notes. A
part of the notes that says `none yet` (every part does in a project `/setup-init` just made) takes the default
below; the round that learns what belongs there writes it into the notes.

## 1. Open the round

- One line: what the round is for, which ticket, the targets, the rounds expected per target, and the fallback if
  a target is not found.
- **Cap:** 3 rounds per target unless the user agrees to more.
- The round is **read-only**, or it names each write (a setting changed, a file put on a device, a memory write, an
  install). Each write needs the user's OK for this round and an undo prepared before it (backup, export, photo of
  the old value, the restore file on hand).
- Everything the notes list as "before a round" is done, and what the user runs matches a commit.

## 2. The checklist

Written to the notes' checklist place, so the user can follow it with the chat closed:

- Title: the ticket, the round, the time it takes (`~5 min`).
- **Why**, in plain language: what was wrong or what is new, and what changed, without code names.
- **Where to start:** the exact starting state (program, save, screen, device state).
- Rows **R1..Rn**, at most ~8. Each row is one place to go and **one observation** to bring back, with what "pass"
  looks like or what to read. Place names as the screen shows them, plus the original-language name where the
  labels are not yet confirmed by a photo. For a change: the value before (photo first), what to set, what to check
  after. A timing names the same start every run and is run twice.
- The last row: "anything odd".
- **Automatic (done):** the commands the assistant ran and what they showed.

## 3. The reply

Ask for a text reply in one line: `R1 pass · R2 fail: spins before firing · R3 12,500`. Ask for a screenshot,
photo or clip only when the fact is visual and words would be ambiguous, cropped to the region, named so it can be
filed (`<ticket>-r<N>-R5-bt-list.jpg`). Read clips at per-frame resolution (~0.07 s sheets, tight crops): faults of
1-2 frames vanish at 0.5 s steps. The assistant runs every command and reads every log itself; the user never runs
commands.

## 4. After the round

- Record each row next to the checklist (or where the notes say): what came back, in the user's words; what it
  settles; what is still unknown. New facts go into the ticket and the project's fact docs, never only the chat. A
  row that could not be done is recorded as not done, with the reason.
- All rows pass: commit the results; the ticket continues or closes.
- Failed rows: a fix list to the user as a grilling round (plain language, a recommendation each). The fix goes on
  in this chat while it is under the quiet zone (~250k), otherwise in a fresh chat of the same ticket after a
  hand-over; a project's notes may require a fresh chat every time. The next round is `r<N+1>`.
- A failure that is a different problem from this ticket becomes a new ticket, not a fix row.
- A target at its cap stops the patching. Write what was tried and what each attempt showed, record the target's
  status (for a search: candidate or not found, and the fallback taken), and put the options to the user: another
  route, a different design, or park it.

Done when every row of the round has a recorded result and every failed row is in a fix list, a new ticket, or a
capped target's options put to the user.
