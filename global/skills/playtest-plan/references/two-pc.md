# Two-PC playtest

Two PCs test two different things, and the plan keeps them apart (Schell ch. 28, intro: QA and playtesting are
different tests):

- **The netcode check:** does a real match on two machines stay in sync, without stalls, with identical replays?
  Pass or fail, measured, filled into the session template's tables. Milestone gates are mostly this.
- **The experience check:** how the match feels against a person (or the bot on the other seat). The same
  questions-and-predictions as a solo session (references/solo.md), plus a second player if there is one.

A session can run both, but the plan lists their steps separately and the netcode results never wait on feel.

## Before the session

- Fill the session file from the entry's playtest template before play: build, PCs, network. A table filled
  beforehand doesn't depend on memory afterwards (the first project's first gate left the Windows versions, the
  second PC's connection and the build's checksum unrecorded).
- The build and how it reaches the second PC: the entry's Builds field. Both PCs must show the same build label.
- The network: LAN, a VPN, or both, each with its own steps. One network per session row.

## Steps to mark (second PC)

Every step done at the second PC gets **(second PC)** in the plan, so the user can walk the steps in order:

- copying the build and checking its checksum (`Get-FileHash` on Windows) **(second PC)**;
- unpacking, starting, joining (host on one, join on the other) **(second PC)**;
- reading the debug readout's ping, stall, input delay and state hash now and then **(both PCs)**;
- after the match, the replay file's name and its replay check **(both PCs)**;
- on a desync: the dump each PC writes, read with the project's desync tool **(both PCs)**.

Visible failures to list in the plan: a desync message or dump, the two PCs showing different end screens, stalls
more than about once a minute.

## When the other seat is a person

The user's notes can be checked against a second player only once: nobody can un-know the game, so a fresh
player's first session is the only first impression there will be (Schell ch. 28, "Who?"; Sellers ch. 12, "Who
Playtests Your Game?"). Spend it on questions only a newcomer can answer: can they read the battle, do they know
what to do next.

- Write the intro down and read it word for word; say that the test is of the game, not of them (Sellers ch. 12,
  "Preparing Your Playtest"). Explain nothing beyond it: the designer won't be in the box (Fullerton ch. 9,
  "Conducting a Playtesting Session"). Help only when they are truly stuck, and note where.
- Ask them to think aloud; expect silence in the hardest moments (Schell ch. 28, "How?").
- Afterwards, each player answers the after-match questions alone before any talk together, so one voice doesn't
  steer the other (Fullerton ch. 9, "Methods of Playtesting"; Schell ch. 28, "Interviews"). Record the first thing
  they say: it matters most, and praise first often cushions the real criticism (Sellers ch. 12, "Finishing Up the
  Playtest").
- Their suggested fixes are symptoms, as with the user's own (references/reading-notes.md).

## When the other seat is the bot

The user alone on two PCs with the bot on one seat is a netcode check with a bot opponent, not an experience test
of human play. Feel questions from it read like a solo session against that bot level.
