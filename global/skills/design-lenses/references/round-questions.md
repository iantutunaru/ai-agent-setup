# Preparing a design round

How to turn a design round's topics into questions the user can answer, with the lenses that fit each kind.
The round itself follows `mattpocock-skills:grilling` (numbered questions, a recommendation each, one frontier per
round); this file decides what each question weighs.

## Before the round

- **Facts first.** Gather what the question rests on before asking it: the design docs, the data files, replays,
  measured batches. A lens that needs a missing fact turns into a fact to gather, not a question.
- **Diagnose before remedies.** When the round answers a playtest complaint, find where the player's loop broke
  (readability.md, "Diagnose") before putting remedies on the table. The complaint is a hypothesis
  (the code profile).
- **Fresh testers are never wrong** (Fullerton ch. 11, "Is Your Game Accessible?"): if a player can't play it,
  there is no game. Designers can't see their own game's confusion; the playtester's report stands as data.

## Which lenses for which question

| Kind of question | Lenses to reach for | Reference |
|---|---|---|
| Should we add or change this mechanic? | formal elements, intentional choice, Schell #30 Emergence and #31 Action, local and generic rules | mechanic.md |
| Is this unit, enemy or weapon distinct? | Rogers' attack matrix, form follows function, Schell #28 State Machine | mechanic.md |
| Is this hazard or world event fair? | Rogers' hazard rules, Fullerton's arbitrary events, Schell #36 Chance | mechanic.md |
| What should the bot know or do? | Schell #29 Secrets, #95½ Cheatability, Rogers' Bruce Lee rule | mechanic.md, pace.md |
| Does it snowball or stall? | reinforcing and balancing loops, engines and economies, then `balance-check` to measure | mechanic.md |
| Why did the player lose track? | the interaction loop, information structure (fog against clutter), Schell #62 Transparency | readability.md |
| Which alert, icon or highlight? | Schell #66 Channels and Dimensions (rank the information first), feedback rules, cut before adding | readability.md |
| Where does it go on screen? | Rogers' placement and icon rules, Schell #61 Virtual Interface, never lose a unit | readability.md |
| Is the match too fast, too hard or too flat? | Schell #21 Flow, Yerkes-Dodson, tense and release, Schell #69 Interest Curve | pace.md |
| How should the match end? | endings, Schell #27 Time, comeback loops | pace.md |

## Writing each question

- **Options the user can see.** Each option says what changes on screen or in play, technical detail after
  (global rules, plain language).
- **Lenses that bite.** Name the two to four lenses whose answers differ between the options; leave out lenses
  that agree with every option.
- **Both sides of a disagreement.** When lenses pull apart, show the tension in the question rather than settling
  it in the recommendation's reasoning alone.
- **Recommendation with its reasoning:** the ➡️ line names one pillar and at least one lens with book and chapter
  (SKILL.md, step 5).
- **What only play can settle** goes into the build ticket's manual test as a thing to look for.

## Cautions

- A lens is a question, not evidence. Ten lenses agreeing don't outweigh one measured batch or the user's call.
- Picking lenses to fit a conclusion already reached is the failure this skill exists to prevent: pick by the
  question's kind, before writing the recommendation.
