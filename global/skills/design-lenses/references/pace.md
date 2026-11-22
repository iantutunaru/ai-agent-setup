# Pace and interest

Lenses for how a match feels over time: tempo, difficulty, the bot's pressure, rest beats and the ending. In a strategy
match the curve emerges from the players and the world; it is shaped through systems (a points bleed, event timers,
the bot's tempo), not scripted.

## Challenge against skill

- **Schell #21 Flow** (ch. 10, "Focus"): clear goals, no distractions, direct feedback, challenge matched to skill.
  A player out of the channel has two ways back: lower the challenge (a slower or easier bot) or raise their skill
  (feedback that teaches). Ask which one the player is short of.
- **Yerkes-Dodson** (Sellers ch. 4, "Arousal and Performance"): performance rises with pressure up to a point, then
  falls into panic, sooner for complex tasks. Practised players tolerate more (the expert effect), which argues for
  a difficulty setting a player outgrows, rather than slowing the game for everyone.
- **Matched fights** (Rogers lvl 10, combat): the best fights are close; actions meet resistance in proportion.
  **Enemies sometimes win** (Rogers lvl 11): easy victories give no pleasure. A guard against over-softening.
- **Hard against challenging** (Rogers lvl 12, [«НЕЛЬЗЯ БРОСАТЬ ИГРОКУ НА ГОЛОВУ БУЛЫЖНИКИ»]): hard is loss and pain;
  challenging is mastery. Don't cross his "fun curve".

## Pressure and rest

- **Tense and release** (Schell ch. 10, "Focus"): a sawtooth of rising tension and relief beats steady climbing.
  Constant tension wears players out.
- **Stacked loops** (Sellers ch. 4, "A Time-Scale View", Halo's 3 s / 30 s / 3 min): loops of different lengths make
  waves of tension and release; does each length have content, and where are the troughs? A rest phase lets the
  player consolidate.
- **Decision intensity** (Fullerton ch. 11, "Types of Decisions"): not every decision should be life and death;
  breathers between waves, importance rising toward the climax.
- **The Bruce Lee rule** (Rogers lvl 11, the passage on groups, grep [«Брюсом Ли»]): of a crowd around the hero only one or
  two attack at once, so a group threatens without overloading. For the bot: does it press on one front at a time
  or on all at once? Fast enemies shouldn't hit constantly without a chance to answer (Rogers lvl 11).
- **Introduce, combine, rest** (Rogers lvl 12, [«Музыка механик»]): bring in one element at a time, then combine
  them; rest a mechanic between uses. Fits a map that grows more dangerous toward its center, and the order of
  world events.

## Shape of a match

- **Schell #69 Interest Curve** (ch. 16): a hook, rising peaks with dips, a climax, a short resolution; below the
  interest threshold the player quits. Curves are fractal: match, engagement, firefight. A cheap playtest tool: ask
  the tester to draw their own curve of the match.
- **Schell #68 Moments** (ch. 16): name a match's key moments; make each as strong as it can be.
- **Schell #70 Inherent Interest** (ch. 16): risk, change and the anticipation of change. A warning before a world event is
  anticipation by design.
- **Schell #27 Time** (ch. 12): clocks are absolute, races relative; nested time (a shot clock in a game clock).
  A points bleed is a race, a timed event a clock. Does the match end too early or drag?
- **Endings** (Fullerton ch. 11, Librande's sidebar "Tuning and Balance: Us vs. It"): end soon after the emotional
  peak; a long mop-up is a known failure. Fullerton ch. 5, "Feedback": balancing loops stop a match ending too fast.
- **Stagnation** (Fullerton ch. 11, "Fun Killers"): repetition, a trapping loop, no clear goal.
- **Habituation** (Sellers ch. 7, "Habituation and Utility"): rewards lose meaning as they repeat; a risk-for-reward push
  needs rising stakes. An early success hooks a first-time player.
- **Comeback** (Sellers ch. 7, "Using Loops in Game Design"): one sharp corrective is often enough to keep both
  sides in play. Whether the opening decides too much is measured with `balance-check`.

## Cautions

- Schell's difficulty ramps and authored interest curves assume levels or a linear show. A competitive match has neither:
  use the curve to diagnose observed matches (replays), and shape it only through systems.
- Against a human opponent, flow comes from who is matched, not a designed curve; only the bot is a difficulty
  knob.
- Lowering the challenge fixes overwhelm but doesn't build the skill a player needs against a human (our reading
  of Schell's two ways back to flow, ch. 10, not his claim): weigh an easier bot against feedback that teaches.
- Librande's "Hollywood ending" tunes a scripted opponent for drama. Applied to the bot it means rubber-banding or
  sandbagging, which hides imbalance from `balance-check`. Dynamic difficulty, if any, stays vs-bot only and visible
  or opt-in, never in a LAN match or a balance batch.
- Rules of thumb with numbers (Halo's 3 s / 30 s / 3 min, EA's one-hour arcs in Fullerton) are practice, not
  measurement: label them heuristics.
