# Judging a mechanic

Lenses for a new or changed mechanic, rule, unit, enemy, hazard or bot behaviour. Start with what it changes,
then whether it is a real choice, then what it does to the match as a system.

## What it touches

- **Formal elements** (Fullerton ch. 3, the chapter's intro): players, objectives, procedures, rules, resources,
  conflict, boundaries, outcome. Name which ones the mechanic changes; the knock-on effects sit in the others.
- **Resources** (Fullerton ch. 3, "Resources"): a resource needs both use and scarcity. Capture points, a map's
  center and safe ground are special-terrain resources; time is one too, and a dramatic one.
- **Conflict** (Fullerton ch. 3, "Conflict"): obstacles, opponents, dilemmas. Does a hazard or environment
  add one without crowding out the opponent as the main conflict?
- **Parts and attributes** (Sellers ch. 8, "Determining Attributes"): as few attributes as possible, reused across
  parts; merge two the player can't tell apart; ranges wide enough to feel. Detail per unit suits a few units and
  becomes a chore for many (his ships example): a handful of units earns per-unit detail.
- **Property count** (Fullerton ch. 5, "Deconstructing Set"): every property multiplies what the player tracks.
- **Schell #28 State Machine** (ch. 12): list the objects, their states and what triggers each change. Things that
  act differently must look different, and things that look alike must act alike (ch. 12, "Objects").

## Is it a real choice

- **Intentional choice** (Sellers ch. 4, "Making Intentional Choices"): the action is valid now, the player has
  the information, can predict the outcome, and has time to decide. Missing any one turns it into a reflex or a
  guess.
- **Decision types** (Fullerton ch. 11, "Types of Decisions"): hollow, obvious, uninformed, informed, dramatic,
  weighted, immediate, long-term. Good ones combine several; a big risk-for-reward push should be informed,
  weighted and dramatic, never uninformed. Dilemmas with no single right answer beat solved choices.
- **Schell #31 Action** and **#30 Emergence** (ch. 12): few basic actions, many strategic ones. Emergence grows
  from verbs that act on many objects, goals with several routes, many subjects to control, and side effects that
  change constraints (suppression, retreat and cover in a tactics game work this way).
- **Schell #34 Skill** (ch. 12): which skill does it really test? Name the skill the pillars ask for (reading position, say);
  speed of clicking or memorising is a drift. Power from stats (veterancy) must not replace positional skill.
- **Rules you can learn by play** (Fullerton ch. 3, "Rules"): players learn unit strength by feel, not numbers. If
  the rule fires against them, will they know why? Schell #33 Rules (ch. 12) adds the fork: when players are
  confused, change the rule or explain it better.
- **Local and generic** (Sellers ch. 8, "Principles of Behavior Creation"): a part may push another's state, not
  set it; generic rules over scripted cases; every part should affect others and be affected back.

## Chance, secrets and fairness

- **Rules against dice** (Fullerton ch. 5, "System Dynamics", the ogre example): fully random combat makes numbers
  the only strategy; fully determined combat has no play. Too random breaks any pillar that rewards skill.
- **Schell #35 Expected Value** and **#36 Chance** (ch. 12): real usable value (overkill is worth nothing) and the
  perceived odds, which players act on. Is the randomness exciting or hopeless?
- **Schell #29 Secrets** (ch. 12, "hierarchy of knowers"): a computer opponent is a knower like a player; one that
  seems to know everything is suspected of cheating. Does the bot read anything a player under fog could not?
  **#95½ Cheatability** (ch. 24): do players trust the game?

## The match as a system

- **Reinforcing and balancing loops** (Sellers ch. 7, "Using Loops in Game Design"; Fullerton ch. 5, "Feedback"):
  does it widen the leader's gap or pull the trailer back? Reinforcing loops collapse choices for both sides.
  A pillar may be a deliberate reinforcing loop (risk for reward): ask what stops it snowballing. Measure with `balance-check`.
- **Engines, economies, ecologies** (Sellers ch. 7, "Three Kinds of Gameplay Loops"): which one is this, and which
  failure is closest (runaway, deadlock, a dominant strategy; inflation or stagnation; a static or brittle
  ecology)? Patching a strong unit with a counter-unit starts a chain of fixes.
- **Loop parts** (Sellers ch. 7, "Parts as Loop Components"): source, stock, converter, decider, sink. Does each
  node add a decision or only load?

## Units, enemies, hazards

- **Attack matrix** (Rogers lvl 10, "Four hundred quatloos on the newbie" [«Четыреста кватлу на новичка!»]): table
  every attack by range, speed, damage and traits; each should fill its own cell, overlaps paid for by a drawback.
- **Form follows function** (Rogers lvl 11, [«ФОРМА СЛЕДУЕТ ЗА ФУНКЦИЕЙ»]): behaviour, speed, size and strength
  first, then the look. Strong and fast together reads as a cheat; chasers slightly slower than the player keep
  retreat alive (Rogers lvl 11). Archetypes (chaser, shooter, blocker...) should combine into "which first?".
- **Restriction gives options back** (Rogers lvl 10, status effects): losing control feels terrible; a restricted
  unit needs a way out (a pinned unit can still retreat).
- **Hazards** (Rogers lvl 12, [«НЕЛЬЗЯ БРОСАТЬ ИГРОКУ НА ГОЛОВУ БУЛЫЖНИКИ»], [«Время умирать»]): a hazard looks
  dangerous before anyone steps in, has a readable pattern and predictable timing, and shows safe and unsafe
  ground in the world. Test: after a unit dies to a hazard, can the player say what they should have done?
- **Arbitrary events** (Fullerton ch. 11, "Fun Killers"): warn at least three times before anything
  catastrophic, and leave a way to soften it; the bigger the impact, the bigger the warning. The world may be cruel,
  never arbitrary: a world event with a siren, a changed sky and a timer meets this.
- **Reasons to engage** (Rogers lvl 11, [«С ВРАГАМИ НУЖНО ДРАТЬСЯ, А НЕ ИЗБЕГАТЬ ИХ»]): the player should want to
  take on a threat: loot, a blocked path, power. A reward for risk is that reason.

## Cautions

- Fullerton's player types (Bartle, Yee) come from MUDs and broad audiences: a check, not segments to serve.
- Fullerton's "tip the balance toward the winner" stagnation fix is for three or more players; in a two-player match it
  feeds the snowball.
- Sellers' neurochemistry (dopamine, serotonin) is vocabulary for feelings, never a reason for a decision.
- Variable reward schedules and free-to-play economies (Sellers ch. 7, Fullerton ch. 5 and 11) don't apply.
- Rogers' "random patterns are bad" is about learned set pieces: apply it to hazard timing, not the bot's
  strategy, which needs some unpredictability.
- In a lockstep multiplayer game anything hidden must stay identical on both PCs: only what is shown may differ
  (fog). A random event comes from the simulation's seeded random generator.
