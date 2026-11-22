# Human playtest or headless batch

Every question goes to the cheapest test that can answer it. A human session is the scarce one: one designer, a
few matches a week. The headless runner plays a hundred bot matches in minutes and gives the same result for the
same seeds.

## The split

| The question asks | Test | How |
|---|---|---|
| how often, how much, how long: win rates, match length, income, units bought, losses | batch | the entry's Batch command (the `balance-check` skill) |
| does a rule ever fire, does a loophole or dead end exist, what happens at an extreme | batch or scenario test | a headless test in the entry's Tests folder, a batch with a forced setting (Fullerton ch. 9, "Test Control Situations") |
| what the bot does with its money and units | batch | the entry's Probe |
| can the player see it, read it, follow it | human | a solo session (references/solo.md) |
| how it feels: pace, pressure, fairness, frustration, wanting another match | human | a solo session |
| does it work on two real PCs: stalls, desync, identical replays | two-PC | references/two-pc.md |

The books draw the same line: numbers, cross-tabs and repeated controlled situations answer "how much"; feel,
emotion, confusion and learning need a person (Fullerton ch. 9, "Metrics in Game Design", "Data Gathering"; Schell
ch. 28, "Why?"). A simulation tests an algorithm, not the game (Sellers ch. 12, "Effective Game Prototyping").

## Pairing them

The strongest reading uses both, one checking the other:

- A playtest note that sounds like a number ("the bot always out-builds me") becomes a batch question. One
  project's case is the model: the user's "impossible to understand what's going on" read, in the replays, as
  being outnumbered in one fight (3 squads against 8), not as losing track of several. The headless
  numbers changed which fix was on the table.
- A batch result that says nothing about feel ("North wins 67 of 100") gets a play question beside it ("does
  North's opening feel stronger from the South seat?").
- Crackdown's team crossed a rating with a behaviour: players who collected more of one power-up rated the game
  more fun (Wixon, in Fullerton ch. 9). Here: a note about a match set beside that match's replay numbers.

## Cautions

- The bot is a test condition, not a tester. It gives no feedback, and what the user feels depends on how good
  it is. A finding that flips with the bot level is a bot finding first (`balance-check`, step 4).
- Bot data misleads the way novice and habit-bound players do (Fullerton ch. 9, "Data Gathering"): the bot plays
  one style. A batch answers balance and edge cases, never fun.
- Numbers don't overrule the user's feel; distrust of one's own instincts is the risk Schell names in
  "quantitative design" (ch. 28, "How?").
- Write the batch's purpose and expected result before running it, as for any measurement (Fullerton ch. 9, "Data
  Gathering").
