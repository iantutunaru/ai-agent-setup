# Code profile

For projects where the assistant builds software, mods or tools. The project's `AGENTS.md` names it
(`Profile: code`); in Claude Code the project's `CLAUDE.md` imports it (`@~/.claude/setup/profiles/code.md`), in
ChatGPT it is part of the built rules file. The shared rules apply as well.

- **Roles.** The assistant writes all code; the user does the manual steps (in game, on the device, in a GUI) and the
  visual picks.
- **The best solution keeps the code modular** and easy to change later.
- **Rounds the user does** (playing a build, working at a device, reading a running program) follow the
  `guided-session` skill.
- **Every build chat ends with manual test steps:** what changed, what to do, what to look for, where errors show
  up. Done means the project's checks pass and the user has run the manual test.
- **Visual picks together.** Every visual asset gets a small option sheet (contact-sheet size, never full-size
  images) with 2-4 labelled options and a recommendation; the user picks. Never iterate looks alone and ship a
  favourite.
- **User and playtest feedback is a hypothesis to test**, not a decision.
- **Tickets.** Work goes in tickets, one ticket per chat; the ticket is the brief. New projects keep tickets in
  `docs/tickets/` (index and rules in its `README.md`) and decisions in `docs/decisions/`, with a project id
  prefix. Existing projects name their own paths under "Where things are".
- **Worktrees.** A worktree and its branch are removed right after the branch merges (unmerged or dirty ones only
  on the user's OK). The end of a stage runs the `stage-close` skill.
