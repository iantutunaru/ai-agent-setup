---
name: balance-check
description: Measure and judge game balance. Use in a game project when a change touches unit stats, costs, ranks, income, a map or the bot; when asked whether a side, faction, unit type or rule is fair, dominant or useless; or when tuning numbers toward a fairness target such as "no faction above 55%".
---

# Balance check

Balance has two halves (Sirlin, "Definitions"): **fairness**, every side or faction locked in before the match wins
about as often when played equally well; and **viable options**, play doesn't collapse onto one unit type or plan.
A check measures one or both with headless matches where the game has them, gives a **verdict**, and hands any rule
change to the user.

`<setup>` below is the agent-setup repo's link: `$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in
ChatGPT; use the one that exists.

## Steps

0. **Read the project's entry.** The **Game design** list under "Where things are" in the project's `AGENTS.md`
   (`CLAUDE.md` in a project not yet moved); its fields are defined in `<setup>/research/game-design/README.md`.
   This skill reads Rules, Data, Backlog, Batch, Probe, Tests, Fairness and Match length, and Also for the
   project's extras. With no such list, tell the user in one line that the project needs `/setup-sync` to add it,
   and stop. A field read here that says `none yet` (every field does in a project `/setup-init` just made):
   name it, say what the check cannot measure without it, and offer to set it now. With `Batch: none yet`, the
   fairness and match-health branches can only plan the batch and say what it needs; the option check can still
   reason from the data and fight tests. With `Fairness: none yet` there is no band for a verdict: ask the user
   for it before any batch runs. Done when the entry is read.

1. **Write the question as a problem statement** (Schell ch. 13, "Balancing Methodologies"): what is suspected, of
   which side, unit type or rule, and what result would settle it. Done when it names one measurable outcome.

2. **Pick the branch** and run it:

   | Question | Branch | Tool |
   |---|---|---|
   | Does one side, seat or faction win too often? | fairness batch | the entry's Batch command, about 100 matches to screen |
   | Is a unit type, rank or weapon dominant or useless? | option check | fight tests in the entry's Tests folder over a seed set, plus the batch's build mix |
   | Do matches snowball, stall, or end at the wrong length? | match health | the batch's length and early-leader lines; the entry's Probe for spending and losses |

   For the statistics, batch sizes and the bot's limits read
   [references/verdicts-and-statistics.md](references/verdicts-and-statistics.md) before the first batch. For
   options, counters and cost against power read [references/options-and-counters.md](references/options-and-counters.md).
   For snowballing, stalls and the economy read [references/match-health.md](references/match-health.md).

3. **Get a verdict**, not a percentage. Run `python "${CLAUDE_SKILL_DIR}/verdict.py" <wins> <decided> --band
   <low> <high>` with the entry's Fairness band (`--help` lists the options; the path in front of the script's name
   is this skill's folder, and a tool that shows it as a `${...}` name has not filled it in: put the folder this
   file is in there). It prints `fair`, `unbalanced`, `unclear, run about N more` or `borderline`. Rerun unclear
   batches with the next seeds and read them together, until the verdict is settled or borderline. A project batch
   tool that prints the same verdict may be used instead. Done when every question from step 1 has a verdict and
   the seed range behind it.

4. **Separate the game from the bot.** Before calling a rule unbalanced, rule out bot bias: repeat with another bot
   level, and read whether the losing side played worse (unspent resources, idle units in the Probe). A verdict
   that flips with the bot level is a bot finding, not a balance finding. Done when the verdict holds on both
   levels or is labelled a bot finding.

5. **If something is off, propose; don't tune.** Write the smallest mechanical change that targets the cause, as a
   candidate in the entry's Backlog file, with a test value that doubles or halves the number (Schell ch. 13) and
   the batch that would confirm it. Prefer raising the weak option over cutting the strong (Sirlin, "Adjusting the
   Tiers"). The user decides; a ticket that already owns the number may change it within its own brief.

6. **Record it** where the entry's Rules field says measured results go (beside the rule's file is the default):
   the ticket, command, seed range, bot levels, verdict and range. Done when another chat could rerun the exact
   batch.

## Running batches

- Every seed a test or batch hands the game goes through the project's seed rule (the entry's Tests field); fight
  tests assert a tendency over a seed set, never one seed. The same seeds must give the same result every run.
- A variant (another side, a changed data file, one seat with a changed bot) gets its own output file, so it never
  overwrites the baseline's; read which side the win rate is for before comparing.
- A batch that loads every core makes timed tests fail while it runs. Let it finish before running the project's
  checks or ending the turn.
- A batch whose replays don't reproduce is a determinism bug to fix before any balance reading
  ([references/verdicts-and-statistics.md](references/verdicts-and-statistics.md), "Harness first").
- The script's tests: `python -m unittest discover -s global/skills/balance-check/tests`, from the agent-setup
  repo's folder.
