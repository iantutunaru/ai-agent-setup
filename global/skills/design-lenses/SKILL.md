---
name: design-lenses
description: Review a game mechanic, rule or design question against the project's pillars and the design books (Schell, Sellers, Fullerton, Rogers). Use in a game project when judging a proposed mechanic, unit or enemy; when preparing a design or grilling round's questions; on readability, HUD, alert or icon questions; on pace, difficulty or interest over a match or level; or when asked to look at something "with our design lenses".
---

# Design lenses

A **lens** is a question from a design book that a mechanic or decision has to survive (Schell's word; his book is
built from over a hundred of them). This skill picks the few lenses that bite on one question, answers each against
the project's facts, and makes every recommendation name the pillar and the lens it rests on. The user decides;
lenses only sharpen the question.

In a design round this skill works inside the grilling skill the rules name: grilling sets the round's shape
(numbered questions, a recommendation each, one round at a time); this skill chooses what each question asks and
why.

`<setup>` below is the agent-setup repo's link: `$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in
ChatGPT; use the one that exists.

## Steps

0. **Read the project's entry.** The **Game design** list under "Where things are" in the project's `AGENTS.md`
   (`CLAUDE.md` in a project not yet moved); its fields are defined in `<setup>/research/game-design/README.md`.
   This skill reads Vision, Rules, Data, Backlog and Playtests, Batch for facts, and Also for the project's
   extras. With no such list, tell the user in one line that the project needs `/setup-sync` to add it, and stop.
   A field read here that says `none yet` (every field does in a project `/setup-init` just made): name it, say
   what cannot be judged without it, and offer to set it now. With `Vision: none yet` there are no pillars to
   judge against: offer a round that sets them and writes the vision file, and stop until the entry names it.
   Done when the vision file is read.

1. **State the question and its pillar.** One sentence: what is proposed or open, and what the player would see
   change. Name the pillar it serves from the vision file. A feature serving no pillar meets the vision file's rule
   for that case (often: it is cut); say so. Done when the question and at least one pillar are written down.

2. **Pick the branch and read its reference:**

   | The question is about | Branch | Read |
   |---|---|---|
   | a new or changed mechanic, rule, unit, enemy, hazard or the bot's behaviour | judging a mechanic | [references/mechanic.md](references/mechanic.md) |
   | what to ask in a design round, and which lenses fit each question | preparing a round | [references/round-questions.md](references/round-questions.md), then the branch file each question needs |
   | seeing what happens: alerts, icons, highlights, the HUD, the minimap, the camera, being overwhelmed | readability | [references/readability.md](references/readability.md) |
   | how a match or level feels over time: tempo, difficulty, the opponent's pressure, rest beats, the ending | pace and interest | [references/pace.md](references/pace.md) |

   A question that spans two branches (losing track of a battle is both reading and pace) reads both. Done when
   the reference is read.

3. **Pick two to four lenses that bite.** A lens bites when its question has a different answer for the options on
   the table. Answer each against facts: the design docs, the data files, a replay, a playtest note, a measured
   batch (`balance-check` for win rates). An answer that needs a fact nobody has becomes a fact to gather first,
   or a playtest check. Done when every picked lens has an answer and its source.

4. **Show where lenses disagree.** Books pull in different directions (a small cue at the stuck moment, Fullerton
   ch. 11, against cutting parts when the screen is overloaded, Sellers ch. 8). Put both sides in the question; the
   user picks. Each reference file ends with its cautions: the places a book's advice may not fit this game (a
   competitive match, a strategy game, a mod of someone else's game). Check every lens you lean on against them.
   Done when every lens used has been checked against its cautions.

5. **Write the recommendation with its reasoning.** In grilling format, the ➡️ line ends with the pillar and the
   lens: `➡️ Alerts first, the easier bot second. (Pillar 4; Schell #62 Transparency, ch. 15; Sellers ch. 4,
   "the fast drives out the slow")`. Lens tags: `Schell #N Name, ch. N`; `Sellers ch. N, "section"`;
   `Fullerton ch. N, "section"`; `Rogers lvl N, "section"`. Done when every recommendation names one pillar and
   at least one lens with its book and chapter.

6. **Hand off what the lenses found.** A book that argues against a design rule becomes a candidate line in the
   backlog file (source, rule, why), never a design doc edit. A lens answer that only play can settle goes into the
   ticket's manual test or the playtest watch-list as a thing to watch. Done when each such finding has a line.

## Rules

- Lenses are hypotheses, and so is playtest feedback: a lens never overrules a measured result or the user.
- Cite the book's idea in our own words; quote no more than 12 words. The books are not in the repo: the
  digests in `references/` cite book and chapter.
- The sources: `<setup>/research/game-design/README.md`. When a lens needs a detail the reference doesn't carry
  and the project has the book at hand, look the passage up there.
