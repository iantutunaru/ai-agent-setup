# Claude Code part

What the shared rules (`global/rules.md`) leave to the tool, for Claude Code. Loaded after them through
`global/CLAUDE.md`.

- **Where the setup is.** The agent-setup repo is linked at `~/.claude/setup`, its skills at `~/.claude/skills`.
- **Grilling rounds.** The grilling skill is `mattpocock-skills:grilling` (Skill tool).
- **Budget.** The shared default, which a person's Preferences may change: plan each chat at about **320k**
  tokens of context; the quiet zone starts past ~250k; the hand-over is written before ~320k. Never resume a
  long chat after a pause (the whole context is cached again at full price): a fresh chat continues from the
  hand-over.
- **Model and effort.** The shared defaults, which a person's Preferences may change; a ticket's header still
  wins, as part of the project.
  - **Opus at high, the default:** planning, design rounds with a fixed aim, debugging, reading and checking,
    data, docs, UI, tooling. On a step that turns out hard, ask the user to raise the effort for that turn.
  - **Fable at high, only where critical thinking can change the plan:** a question round that re-evaluates the
    approach, reverse engineering, measure-first work with no known method, or a problem Opus has not solved in
    three chats. Fable uses several times more of the usage limits (the user's measure: 5 to 10 times a chat),
    so a ticket that names Fable says why.
  - **Sonnet at medium:** mechanical work that lint and tests catch.
  - **Agents:** Opus at medium for reading and checking that a coordinating chat verifies part by part; Sonnet
    only where a script checks every output; Fable only when the user asks. Tell the user a batch's size before
    starting it.

  A ticket chat first checks its model (the system prompt) and effort (`echo $CLAUDE_EFFORT`) against the
  header; on a mismatch it says what to switch in its first message and stops. Switching model mid-chat drops
  the cache and the earlier reasoning.
- **Shell.** Bash for git and Python; PowerShell for Windows-only work. `PYTHONUTF8` is set in the global
  settings. Multi-line Python goes in a scratchpad `.py` file run by path, not a heredoc: the Bash heredoc
  collapses backslash escapes.
