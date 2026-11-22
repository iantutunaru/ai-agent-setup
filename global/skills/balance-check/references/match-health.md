# Match health

Whether matches end the right way: not decided too early, not stalled, not won by whoever leads first, with an
economy that neither floods nor starves.

## Snowballing

- Fullerton's test: does the early leader usually win (ch. 10, "Reinforcing Relationships")? Have the batch report how
  often the side ahead on the win measure (points, territory) for longer in the first 10 minutes won. Near 100%
  means the opening decides the match; compare with what the design docs want before calling it a problem.
- Never read a whole-match lead on the win measure as a snowball when that lead is what wins: in a game where
  holding points drains the other side's tickets, the longer holder wins nearly every match by construction (one
  project's first batch: 100 of 100).
- Brakes, from the sources: make the leader pay for strong positions, temporary help for the side behind, chance,
  upkeep that drains a large army's income (Pardo, in Fullerton ch. 10), and a ticket bleed tied to objectives, as
  in Battlefield 1942 (Fullerton ch. 10).
- Once past the climax, the match should tip and end quickly (Fullerton ch. 10).
- Sellers names the core resource of strategy games as the area held; armies and forts support it (ch. 10,
  "Defining Costs and Benefits"). Balance income around points held.

## Lame ducks and stalls

- A **lame duck**: the match is decided but plays on, which moves the real climax to the middle (Sirlin, "Lame-duck
  Situations"). Fixes: another way to win, or help that grows with how far behind a side is.
- A near-certain win before the end is fine if reaching it was hard. Avoid the victim feeling helpless: a strong
  weapon needs visible warnings and a window to answer it (Sirlin, "Checkmate Situations").
- A **dead end**: both sides broke with nothing to fight with, so the match can't resolve (Fullerton ch. 10, "Dead
  Ends"). Time-limit matches in a batch are the sign. Forced convergence after a time limit beats a points
  tiebreak (Schell ch. 13, "Short vs. Long").
- Target length: the entry's Match length field. Have the batch print the median, the spread and how many fall outside.

## Economy

From Sellers ch. 10, "Economic System Balance":
- Sources against sinks. Too much income inflates (everything affordable, choices vanish); too little stagnates.
- **Arbitrage**: any loop that makes resources from nothing. Habitat's money supply grew fivefold overnight and was
  caught only because total money was tracked daily. Here: recapturing a point for repeated payouts, or a refund
  that beats a cost.
- Track total income per side over time, and the time to afford each unit as a range from fastest to slowest.
  The entry's Probe shows what each side earned and how it was spent.
- Bracket the economy between bounds: unlimited resources gives the fastest possible progress, passive income alone
  the slowest; a good bot sits near the fast end (Borovikov, GameAIPro Online 2021 ch. 10, "Agents for 4X genre").
  A large unspent pile means a weak bot before it means a rich economy.
