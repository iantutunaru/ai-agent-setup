# Hand-over: the game programming skills, and the first use of the game design skills

Done: the three game design skills are global (`design-lenses`, `balance-check` with `verdict.py` and its unit
tests, `playtest-plan`; SU-Q75 to SU-Q78), and a check chat fixed the README, the entry's **Also** field and the
guard for a new skill (SU-Q79 to SU-Q83). Their project entry and the books' places: `research/game-design/README.md`.

Left: five game programming skills to make engine-neutral, and the first real use of each design skill as its
trial.

## The five game programming skills

One chat each (two for `frame-budget`), from the first game project's `.claude/skills/<skill>/`
(in the main PC's projects folder). **Model:** Opus, high effort. **Load:** light (reading and
writing; no game runs). Each chat:

1. Reads the skill in full, this repo's `research/game-design/README.md`, and SU-Q76 to SU-Q78.
2. Writes `global/skills/<skill>/`: the method engine-neutral, in the style of the three design skills (step 0
   reads the project's entry; new fields go into the entry's definition and `setup-sync` item 3); engine facts in
   `references/engines/threejs.md` (the project's measured findings, with their tickets turned into dates) and
   `references/engines/unity.md` (only what is measured: the first game project's
   `unity-port-tooling.md`, `unity-netcode-model.md` and its decisions; say
   "not measured" elsewhere). Scripts that read the old TypeScript game stay in the project.
3. Puts the project's facts into the first game project's entry, deletes the project copy, and commits there
   (staging only its own files); commits here, on a branch (this repo's `AGENTS.md`); the README, `docs/tried.md`
   and the other places follow the list "A new skill" in step 3 of `setup-promote`, and `python -m unittest
   discover -s tools/tests` checks them.

| Order | Skill | Words | Notes |
|---|---|---|---|
| 1 | `lockstep-desync` | 3,200 | has `scripts/clean-run.mjs`, which reads the TypeScript game: stays in the project |
| 2 | `sim-patterns` | 5,600 | already names the Unity C# shape of each pattern |
| 3 | `unit-movement` | 4,600 | fixed-point and path cost notes carry over; search cost numbers are the TypeScript game's |
| 4 | `bot-ai` | 6,200 | the decision and map-reading method is general; levels and fairness tie in to `balance-check` |
| 5, 6 | `frame-budget` | 9,500 | three.js and Electron throughout; most of it becomes `threejs.md`, the method is short |

The word counts and notes are as the earlier hand-over gave them on 2026-11-21; not counted again since.

## The first real use of each game design skill is its trial (SU-Q82)

The general versions of `design-lenses`, `balance-check` and `playtest-plan` have no run on record; checked so
far: `balance-check`'s script has unit tests, and the first project's entry holds every field the skills read.
They are not yet run in a second game project. The chat that first uses one in the first game project notes
whether step 0 read the entry and whether a step failed for want of a project fact, and updates the row in
`docs/tried.md`.

## Gotchas

- `research/game-design/README.md` holds the entry's field table; it must match what the skills read in step 0
  (the **Also** field was once read by no skill, SU-Q81).
- `tools/tests/test_readme.py` fails when the README's skill count or skill tables, `docs/tried.md` or the
  tests list in `CONTRIBUTING.md` do not match the skill folders: a new skill changes them in the same commit
  (SU-Q80).
