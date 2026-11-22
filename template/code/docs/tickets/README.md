# Tickets

One file per ticket, `<P>-Txx-<slug>.md`. **One ticket = one chat**; a ticket bigger than a chat continues in
more chats under the same id, never cut down. Decisions behind the tickets are in `docs/decisions/`; a ticket
links the ids. The shared rules and the code profile apply as well; these are the ticket mechanics (SU-Q30).

Status: `open` (dependencies not met), `ready` (can start), `active`, `held` (paused by the user), `done`,
`dropped` (with the reason).

## Rules for every ticket chat

1. **Start.** Read the ticket and the decisions its dependencies logged. Every dependency is `done`, and no active
   ticket is still changing its output; if one is, the choice (start now and rework once, or wait) goes to the
   user. Set the ticket `active` here.
2. **Scope.** This ticket only. Anything else found goes into this index as a note or a new ticket.
3. **Roadmap changes.** A chat may update later tickets' facts, dependencies and size, and split a ticket, logged
   in a decision. A change to what the user will see or has decided goes to the user first. A result that breaks
   the plan stops the chat there and goes to the user before any downstream work.
4. **Side by side.** Tickets that touch separate files may run at the same time, each in its own worktree, merged
   when it closes.
5. **One source per fact.** The ticket file holds the full result and the run log; its row here holds the status
   plus at most one short line with the ids; a hand-over lists only what is open, with links.
6. **Close.** Decisions under the ticket's own ids (`<P>-Txx-Q1`, ...) in the ticket file or a decision log; the
   ticket `done` here; every ticket now `ready` marked; a one-line recommendation for the next. The Size column
   keeps the first estimate and the close writes the actual beside it ("1 chat; ran 2"). The run log gives each
   chat's peak context and each helper's tokens. Commit; the user pushes and picks the next ticket.
7. **Stage close.** When a stage's last ticket is merged, a fresh chat runs the `stage-close` skill. The next stage
   starts after the user approves its ticket list.

## A ticket file

```markdown
# <P>-Txx <title>

**Model:** <model and effort, from the tiers in the rules: e.g. Opus, high effort | Fable, high effort,
because ... | Sonnet, medium effort>. **Size:** <n chats>.
**Depends on:** <ids or none>. **Settles:** <what is known or built when it is done>.

## Goal
## Done when
## User steps
## Decisions
| Id | Decision |
|---|---|
## Run log
## Handoff
```

## Stage 1: <name>

| Ticket | What | Depends on | User steps | Model | Size | Status |
|---|---|---|---|---|---|---|
