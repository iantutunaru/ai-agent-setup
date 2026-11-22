# Reading the notes afterwards

A note is a hypothesis to test, not a decision (the code profile). Players identify problems well and solutions badly
(Sellers ch. 12, "Analyzing Feedback"): treat a suggestion as a symptom, the tester as patient and the user as
doctor. "Tear the wall down" means "it feels small" (Fullerton ch. 9, "A Primer for Playtesting"). The user is
both patient and doctor here, so the reading separates the two on purpose.

## Steps for each note

1. **Write it down as said**, lightly cleaned, in the session's playtest file (its notes), the same day: impressions fade
   fast (Sellers ch. 12, "Analyzing Feedback"). Mark which notes came first and unprompted; they weigh most
   (Sellers ch. 12, "Finishing Up the Playtest").
2. **Name the problem** behind it, as what the player experienced: "lost track of which squad was under fire", not
   "add minimap pings". Keep the user's fix beside it as one option.
3. **Write the hypothesis and its check:** a cause that could be wrong, and the cheapest test that would show it.
   Check what can be checked now: the match's replay read headless, a batch, a scenario test.
4. **Weigh it.** Sellers trusts what several players share and calls a lone reaction an outlier; with one tester,
   weight comes from recurrence across sessions and builds, and from the replay agreeing. One designer playing five
   sessions is not five testers: the same blind spots recur every time (RITE's 4 to 5 participants assume five
   different people; Fullerton ch. 9). Rank the problems by how badly they hurt the match (Fullerton ch. 9, "Basic
   Usability Techniques").
5. **File it** in exactly one place:

   | The note | Goes to |
   |---|---|
   | answers a picked question | the playtest file's verdict, with the prediction and what happened |
   | a problem with a likely cause and a fix to try | a candidate in the entry's Backlog file (source: the playtest file; the problem; the fix options) |
   | a hunch nobody can check yet | an entry in the watch-list: what to watch and the levers to try |
   | already owned by an open ticket | a line in that ticket, quoting the note |
   | a source or the note argues against a design rule | a backlog candidate (source, rule, why); never a design doc edit |

## The worked example: "impossible to understand what's going on"

From the first project: a note said the battle was impossible to follow against either bot. As a fix it suggested
alerts and red attackers. A later ticket checked it headless against the two replays: the player never had more than
3 squads and fought in one place at a time, while the bot had 8 by minute 5 and nearly twice the income by minute 2. The
problem behind the note was being outnumbered in one fight, not losing track of several. The alerts may still
help, but the check moved the question towards production and land grab. That is the pattern: the note is real,
its cause is a hypothesis, and the replay tested the cause.

The same session showed a bookkeeping gap: which replay was Basic and which Standard is unknown, because replays
don't record the bot level. Note the setup per match (references/solo.md).

## After a fix lands

Retest the problem the fix was for, in the next session's questions: fixes create new problems (Fullerton ch. 9,
"Rapid Iterative Testing and Evaluation"). Keep the original prediction so before and after compare.

## Cautions

- Statistical significance needs dozens of players; look for the direction across sessions and builds instead
  (Sellers ch. 12, "Analyzing Feedback").
- Testers invent reasons after the fact and forget details by the end (Schell ch. 28, "How?"). A reason given
  afterwards is a lead; the replay is the evidence.
- A playtest note never overrules a measured result, and a batch never overrules how the match felt; when they
  disagree, the disagreement is the next question.
