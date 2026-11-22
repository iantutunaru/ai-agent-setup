# Verdicts and statistics

How to read a batch, how big it must be, and what a bot batch can and cannot prove.

## The verdict rule

- The batch reports the winning share of decided matches with its **95% Wilson range** (`verdict.py` in this skill's folder).
- **fair**: the whole range sits inside the entry's Fairness band (45-55% for "no faction above
  about 55%").
- **unbalanced**: the whole range sits outside it.
- **unclear**: the range straddles a band edge; the tool says roughly how many more matches would settle it.
  **borderline**: the rate sits on an edge, so no batch size settles it; report it as within a few points of 55%.
- Matches that hit the time limit count for neither side and are reported apart (a stall finding, see
  [match-health.md](match-health.md)). Never fold them into wins.

## Batch sizes

- A win rate's standard error is about 0.5 / sqrt(N). 100 matches give about ±10 points, so they cannot tell 50%
  from 55%. Calling a true 50/50 fair takes about 385 decided matches. A lopsided result settles fast: 20 of 20
  already has a range of 84-100%.
- Screen with 100, then follow the tool's "run about N more" with fresh seeds. Every look at the data and decision
  to stop raises the chance of a false call a little, so a verdict that only just settled at the edge of the band
  is reported as borderline.
- Compare two variants of a rule on the **same seeds** (paired seeds), so map and bot-style draws cancel.
- Change **one** value between batches and retest the whole match (Fullerton ch. 10, "Techniques for Balancing
  Your Game"). Try doubling or halving it first: a 10% nudge is easily mistaken for noise (Schell ch. 13,
  "Balancing Methodologies").

## What separates a side, a seat and a faction

- When seat 0 always starts on the same side of the map, a lead for that side in a mirror batch is the map's side
  **or** seat 0's place in the tick order. Run the same seeds again with the sides swapped and pool them: one
  side's share is the map, seat 0's share the seat (Sirlin, "Symmetric vs. Asymmetric"; Fullerton ch. 10,
  "Balancing Positions"). Each line in the output file should say which seat had which side.
- Symmetric games still have a first-mover edge; fixes are a weaker opening move, a longer match, chance, or
  compensating the second side (Fullerton ch. 10, "Balancing Positions"). For a map, the fix is in the map.
- Factions are locked in before the match, so they need fairness overall **and** in each pairing on each map
  (Sirlin, "Counter Matches"; Pardo in Fullerton ch. 10). Unit types bought during play don't: they need only a
  situation where each is worth buying (Sirlin, "Definitions").

## Local fights are not fairness

Only the whole match's win chance is a fairness verdict (Sirlin, "Local vs. Global Balance"). A unit fight that
one type wins 40 of 40 is a diagnostic about counters and cost, and may be fine. See
[options-and-counters.md](options-and-counters.md).

## The bot is not an expert

- Sirlin's method assumes expert players searching for the best line. A scripted bot may never find a strong plan,
  so a bot verdict means "balanced for this bot". It can pass an option humans will break, or bury one it misuses
  (Sirlin, "Playtesting").
- Pardo's lesson from StarCraft: Zerg Overlords were changed for their scouting value, which no stat sheet showed
  (Fullerton ch. 10, "A Conversation with Rob Pardo"). A bot that never scouts can't reveal a scouting imbalance.
- Weak bots kept the relative ranking of levels in single-player progression games (Borovikov, GameAIPro Online
  2021 ch. 10, "Case study 1"). Don't count on that in an adversarial RTS, where positioning, focus fire and
  retreats change who wins.
- Sanity checks before trusting a batch: the stronger bot level must beat the weaker clearly; the verdict should
  hold on both levels; the losing side's spending and idle time (the entry's Probe) should look
  like play, not a stuck bot. Bot skill is a balance variable in its own right (Fullerton ch. 10, "Balancing
  Computer-Controlled Characters").
- Bot results go to the user as hypotheses; feel and readability stay the user's manual check.

## Harness first

Balance data is only as good as the harness producing it: StarCraft's crash-prone builds starved its playtests to
the end (Wyatt, "Tough Times on the Road to StarCraft"). A batch whose replays don't reproduce their hashes
is a determinism bug to fix before any balance reading.
