# Game design skills: sources and the project entry

The skills `design-lenses`, `balance-check` and `playtest-plan` are built from the owner's game design reading.
They were first written for one game project and made general on 2026-11-21 (SU-Q75 to SU-Q78). Their
`references/` files hold the books' ideas in our own words, and every claim there names its source and chapter.

This page says where those sources live, how to add to a skill from them, and what the project entry the three
skills read looks like.

## Where the sources live

The books, essays and chapters below are third-party texts and are not in this repo. Never commit them or
quote them at length. A skill quotes at most 12 words from a book.

- **Books**, in a folder on the owner's PC, not in the repo.
  - Jesse Schell, *The Art of Game Design* (2019). Cited as `Schell #N Name, ch. N`.
  - Michael Sellers, *Advanced Game Design: A Systems Approach* (2017). Cited as `Sellers ch. N, "section"`.
  - Tracy Fullerton, *Game Design Workshop*, 5th edition. Cited as `Fullerton ch. N, "section"`.
  - Scott Rogers, *Level Up!*, 2nd edition in Russian (2023). Cited as `Rogers lvl N, "section"`.
    The section headings are quoted in Russian, in `[«...»]`, so you can find them with grep.
  - Also in that folder, for the game programming skills that are still being made general (SU-Q78): Robert
    Nystrom, *Game Programming Patterns*, and two books by Jeremy Gibson Bond: *Introduction to Game
    Design, Prototyping, and Development* (in English) and Bond's Unity and C# book (in Russian).
- **Essays and chapters** that `balance-check` cites: David Sirlin's balance essays ("Balancing Multiplayer
  Games", cited as `Sirlin, "section"`), and chapters of *Game AI Pro 3* and *Game AI Pro Online 2021* (cited
  with the chapter number and section). The first project kept these in a folder that git ignored.

To look a passage up, read it in your own copy of the book. A book's text never goes into a repo.

## Adding to a skill from the books

1. Read the chapters from your own copy of the book, outside any repo. Hand them to subagents in groups of about 100k words. Give each a
   brief with the skill's purpose, the files with line ranges, and the return format:
   - notes in their own words, with no quote over 12 words;
   - each idea tagged with the author and the "section heading";
   - a section "Applies", mapped to the skill's branches;
   - a section "Doesn't apply / caution", with reasons;
   - under 1800 words, and no files written.
2. Treat the digests as leads. Check every number, name and example the skill will rely on against the
   book itself.
3. Write it into the branch's `references/` file, in that file's own style, with examples that come from no one
   project.

## The project's entry

The three skills read a **Game design** list under "Where things are" in the project's `AGENTS.md` (`CLAUDE.md`
in a project not yet moved). `/setup-init` and `/setup-sync` write it for a game project, from the form
`template/entries/game-design.md` (`setup_tools.py add-entry game-design`; a test keeps the form's fields equal
to the list below). Angle brackets stand for the project's values. A field the project has no answer for says
`none yet`.

```markdown
- **Game design:**
  - Vision: <the file with the pillars or design goals every feature must serve, and the rule for a feature that serves none>
  - Rules: <where the design docs live, how a rule change is logged, where a measured result is recorded>
  - Data: <where the tuned numbers live>
  - Backlog: <the file candidate changes go to, for the user to accept>
  - Playtests: <the folder, the session file template, the standing watch-list>
  - Builds: <how to start a dev build and a release build; the steps for a second PC>
  - Levers: <debug keys or settings that force a situation: fog off, the bot plays a seat, a short match>
  - Batch: <the headless batch command and its options (count, seed, bot level, side swap, variants) | none yet>
  - Probe: <the tool that shows how a side spent and idled in a match | none yet>
  - Tests: <the scenario test folder and its seed rule>
  - Fairness: <the band, e.g. 45-55%; what is locked in before a match: sides, seats, factions>
  - Match length: <the target, e.g. 20-30 minutes>
  - Also: <project extras: a worked example, a milestone gate>
```

Which skill reads which field:

| Field | design-lenses | balance-check | playtest-plan |
|---|---|---|---|
| Vision | yes | | |
| Rules | yes | yes | yes |
| Data | yes | yes | yes |
| Backlog | yes | yes | yes |
| Playtests | yes | | yes |
| Builds, Levers | | | yes |
| Batch | yes (facts) | yes | yes (routing) |
| Probe, Tests | | yes | yes (routing) |
| Fairness, Match length | | yes | |
| Also | yes | yes | yes |
