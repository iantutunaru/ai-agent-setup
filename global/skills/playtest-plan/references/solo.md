# Solo playtest: the user against the bot

The common session: one PC, a match against the bot. The user is tester and observer at once, the most biased
tester there is (Sellers ch. 12, "Who Playtests Your Game?"). Fullerton still counts self-testing as the right
tester while the core is being found (ch. 9, "Self-Testing"). The plan's job is to make that bias show: questions
and predictions written down before play, a notes sheet, and the after-match questions asked by the assistant.

## Setup

- **Build:** the entry's Builds field. A dev build for a quick check (with its debug readouts on); a release build
  when the session judges what players get. Name the commit either way.
- **Match:** map, bot level, the match settings that set its length (tickets, score limit, timer), and which seat.
  Note them per match: a replay that doesn't record the bot level or settings can't be read back without the
  notes sheet (the first project learned this when it couldn't tell which replay was which bot level).
- **Length:** 15 to 20 minutes of play, then notes while memory holds (Fullerton ch. 9, "Conducting a Playtesting
  Session"); several short sessions beat one long one (Sellers ch. 12, "When to Test"). Read the batches' match
  length spread (`balance-check`) and pick the settings that fit the question.
- **Replays:** write the file name of each match into the notes. The replay is how the assistant checks a note
  headless.

## Test control situations

Force the situation the question is about instead of waiting for it (Fullerton ch. 9, "Test Control Situations"):
the book's examples are fog off to watch the AI, huge resources to test unit caps, and a start near the end that
tests an ending four times in an hour. The entry's Levers field lists what this game offers.

| To test | Lever |
|---|---|
| the ending, a comeback, the win condition's drain | the shortest match setting |
| the bot's plan and its army's movement | fog off or the bot's view (a debug lever); the bot playing your seat |
| one rule in isolation | a scenario test in the entry's Tests folder first; play only what the test can't show |
| a variant of a number | change it in the entry's Data files, one number per session, and say so in the notes |

If a question needs a lever the game lacks (a match started from a set state: a mid-match army, set resources),
say so in the plan.

## Script (the user reads it, the assistant keeps to it)

1. Before: the assistant shows the questions, the predictions and the notes sheet. No talk of what a change
   "should" feel like beyond the prediction: priming spoils the test (Schell ch. 28, "The Intro").
2. Play with a **beginner's mind**: as if for the first time, noticing what you'd miss if you knew less (Fullerton
   ch. 9, "Self-Testing"). Jot a mark and the match time at each moment of confusion, surprise or frustration;
   the words can wait.
3. After each match: fill the sheet before the next one (memory fades by the end of a session; Schell ch. 28,
   "How?").
4. After the session: the assistant asks the after-match questions (references/watching.md), then reads the notes
   with references/reading-notes.md.

## Plan template (one screen)

```
Playtest <date>, solo. Build: <dev @ hash | release label>. Map: <map>. Bot: <level>. Settings: <length settings>. Matches: <n> x ~<min>.
Questions (prediction):
1. <question>? I expect <observable result, number>.
Steps: <setup>, <what to try in the match>, <fill the sheet after each match>.
Notes sheet: <categories to tally>, <after-match questions>.
Batch questions (the assistant runs): <question> -> <command>.
```
