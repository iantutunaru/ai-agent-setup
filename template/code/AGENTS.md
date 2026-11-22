# <Project name>

Profile: code

<One paragraph: what is being built, for whom, and what "done" looks like for the user.>

## Safety

<What must never be changed, run, sent or committed without the user's OK, and why: e.g. the user's only copy of
a device's settings, a live account, personal data folders. "None beyond the global rules" if there is nothing.>

## Where things are

- `docs/tickets/`: the work, one ticket per chat (index and rules in its `README.md`).
- `docs/decisions/`: decision logs, ids `<P>-Qnn` (project-wide) and `<P>-Txx-Qn` (a ticket's).
- **Stage close:**
  - Tickets: `docs/tickets/README.md`; a stage is one table; parked status: held
  - Decisions: the stage-close ticket's `<P>-Txx-Qn`, in its file
  - Retro: the stage-close ticket file
  - Roadmap: `docs/tickets/README.md`
  - Cleanup: generic `--tickets docs/tickets`
  - Tests: <command, and the folder it runs from>
  - Branch: own branch, merged into main on the user's OK
  - Push: no, the user pushes
  - Also: none
