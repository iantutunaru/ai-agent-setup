# Options and counters

Judging whether each unit type, rank, weapon or plan is worth choosing, and what to do when one isn't.

## Words

- **Dominant**: better than the alternatives with no counter, so knowing it's coming doesn't help. The worst flaw
  (Sirlin, "Yomi Layer 3"). A dominant strategy removes the choice and with it the fun (Schell ch. 13, "Meaningful
  Choices"). A **favourite** is merely popular and still has counters (Fullerton ch. 10, "Dominant Strategies").
- **Counter cycle**: A beats B beats C beats A. **Cost-ordered**: some options are simply better and cost
  proportionally more. Sellers calls these "transitive" and "intransitive", the reverse of common usage; use the
  plain words (Sellers ch. 9, "Requirements for Transitive Balance", "Intransitive Balance").
- **Chaff**: options nobody uses. They cost learning and add nothing (Sirlin, "Wheat from the Chaff").
- **Tiers** (Sirlin, "The Tier List"): god (must-pick), top, middle, bottom (playable but hard), garbage. Rank in
  tiers, not 1..N, so the gaps show.

## Checks

- **Every strong option has a counter, and the counter has a counter.** Past about three layers the replies loop
  back. A situation with no loop hides a dominant option (Sirlin, "Yomi Layer 3"; Schell ch. 13, "Rock, Paper,
  Scissors").
- **Tie ratios.** For each pair of unit types, find the size ratio (and the cost ratio) at which homogeneous groups
  tie. Draw an arrow from stronger to weaker; a type in no cycle is dominant or useless (Borovikov, GameAIPro Online
  2021 ch. 10, "RPS balance evaluation").
- **Across conditions.** Rerun pairings in the open, in heavy cover, flanked, suppressed. A matchup that one
  terrain makes unbeatable is fragile balance; one that never resolves is too rigid (Sellers ch. 9, "Achieving
  Transitive Balance"). For ranks, say: open ground against heavy cover, over 40 seeds.
- **Usage.** Compare each type's share in the winners' purchases with the losers' and with an even share; a large
  gap is a lead (Manabe and Miyake, GameAIPro Online 2021 ch. 17, "Data statistics"). An unbought type is a lead
  too (Sellers ch. 9, "Sample Size and Information Distortion"). Have the batch record each side's planned mix per
  match; per-type purchases and losses come from the entry's Probe.
- **Risk against reward.** A riskier option must pay in proportion: half the success chance needs about double the
  payoff in expected value (Schell ch. 13, "Triangularity").
- **Differ in kind, not size.** Options that only vary damage, speed and cost drift into strictly-better pairs;
  different effects make value depend on the situation (Sirlin, "Explore the Design Space").

## Cost against power

Sellers's recipe (ch. 10, "Balancing Parts"):
1. List each unit type's attributes along the chain that drains the enemy: how often it fires, whether it hits,
   how much it hurts; add suppression and survivability.
2. Weight them (his example ended at speed 1.75, attack 1.3, damage 1.0) and sum into a power score.
3. Pick a middle type as the reference and plot power against cost. Look for outliers and clumps.
4. Set cost separately from the score. Cheap types may run slightly underpriced and top ones carry a small premium.

The weights are a hypothesis: score, compare with measured fights, re-weight, retest, and write the model down
(Schell ch. 13, "Biplane Battle"; Sellers ch. 9, "Overview of Methods and Tools"). Equal point budgets spent
differently are the first estimate for asymmetric sides (Sellers ch. 9; Schell ch. 13, "Fairness"). Compare growth
rates: a rank ladder whose power grows faster than its cost snowballs (Sellers ch. 10, "Defining Cost-Benefit
Curves").

## Lanchester's laws as a cross-check

From Stanescu, Barriga and Buro (GameAIPro 3 ch. 25, "Lanchester's Attrition Models"):
- Sides of size A and B with per-unit kill rates a and b: A wins when a·A^n > b·B^n. n = 1 is one-on-one
  (melee-like), n = 2 the **square law** (everyone can shoot anyone). Mixed StarCraft fights fit n ≈ 1.56.
- Under the square law one unit with 4x the power only ties two normal ones, not four (Borovikov ch. 10, "Combat
  mechanics"), and one army of 1000 beats 500 + 500 arriving one after the other, losing about 30%.
- Use it to flag fight-test results that contradict the model, and buffs whose effect is far from what the model
  predicts. Cover, suppression, retreat and reinforcement all break its assumptions, so it is a sanity check, never a
  verdict. Fitting lives in tools or tests, where floats are fine, never in a lockstep simulation.

## Writing fight tests

- Narrow setups that pin one cause: an armed unit against a target that does nothing, then perception, then
  movement. "Ten against five, the bigger side wins" fails in countless ways and explains none of them (Skarupke,
  GameAIPro Online 2021 ch. 1, "Simple Tests").
- Assert that a result happens within a tick ceiling, not on an exact tick (ch. 1, "Testing in a Game Engine").
- A tendency is asserted over a seed set through the project's seed rule; an exact rule is set up so no roll
  changes it.

## When an option is off

In order (Sirlin, "The Tier List", "Adjusting the Tiers"):
1. Empty the god tier, then the garbage tier, then shrink the gap between best and worst.
2. Raise the weak option toward the top tier rather than cutting the strong one.
3. A new option of unknown strength starts too strong and is tuned down: one that starts too weak gets ignored, so
   its later buffs go unnoticed (Pardo, in Sirlin).
4. Fix a bad pairing with a mechanical change that touches only that pairing, never a hidden per-pair damage table:
   that breaks the player's intuition (Sirlin, "Counter Matches").
5. Prefer one simple rule that balances itself over a pile of exceptions; "unless" and "except" in a rule are a
   warning (Schell ch. 13, "Natural vs. Artificial Balancing").
6. Cut chaff that stays unused after the buff (Sirlin, "Wheat from the Chaff").
