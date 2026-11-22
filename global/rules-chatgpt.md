# ChatGPT part

What the shared rules leave to the tool, for the ChatGPT desktop app and Codex (command line, editor extension).
The model names, context sizes and prices below were read on OpenAI's pages and in the app's own files on
2026-11-21 (SU-Q61, SU-Q62); none of it has been measured on the user's work yet, so treat the tiers and the
numbers as starting values.

- **"The assistant" is you.** A skill taken from GitHub may say "Claude" for the one doing the work: that is
  you as well.
- **Where the setup is.** The agent-setup repo is linked at `~/.codex/setup`, its skills one by one in
  `~/.agents/skills`. This rules file (`~/.codex/AGENTS.md`) is built from the repo's `global/rules.md`,
  `global/rules-chatgpt.md`, `profiles/` and the person's own `local/personal.md` (git ignores `local/`):
  change those, never the built file. The session-start hook rebuilds it; a change applies from the next chat.
- **Skills by name.** Where a rule or a skill writes `/setup-sync` or another `/name`, that is the skill
  `$name` here (`@` and its name in the desktop app).
- **Grilling rounds.** The grilling skill is `grilling`. The app's own question tool works in Plan mode only;
  in any other mode put the round in the chat as numbered questions in the skill's format and wait for the
  answers.
- **Budget.** The shared default, which a person's Preferences may change. On GPT-6.2 Sol plan each chat at
  about **320k** tokens of context, with the quiet zone past
  ~250k. On GPT-6.2 Astra, whose context is smaller, write the hand-over before ~230k, with the quiet zone past
  ~180k. The app compacts the chat by itself when the context fills: write the hand-over before that happens,
  not after.
- **Model and effort.** The shared defaults, which a person's Preferences may change; a ticket's header still
  wins, as part of the project.
  - **GPT-6.2 Sol at High, the default:** planning, design rounds with a fixed aim, debugging, reading and
    checking, data, docs, UI, tooling. On a step that turns out hard, ask the user to raise the effort for that
    turn.
  - **GPT-6.2 Astra at High, only where critical thinking can change the plan:** a question round that
    re-evaluates the approach, reverse engineering, measure-first work with no known method, or a problem Sol
    has not solved in three chats. Astra costs four times Sol's credits for the same tokens, so a ticket that
    names Astra says why.
  - **GPT-6 Luna at High:** mechanical work that lint and tests catch.
  - **Agents:** Sol at Medium for reading and checking that a coordinating chat verifies part by part; Luna only
    where a script checks every output; Astra only when the user asks. Tell the user a batch's size before
    starting it.
  - **A ticket header written for Claude** translates: Opus to Sol, Fable to Astra, Sonnet to Luna, at the
    effort the header names.

  A ticket chat first checks its model against the header: the session-start hook prints the model's name in a
  line that begins `agent-setup: model`. On a mismatch it says what to switch in its first message and stops.
  The effort cannot be read from inside the chat: name the effort the header asks for in the first message and
  go on.
- **Shell.** Commands run in PowerShell. `git` and `python` lines in the skills are written to run there as they
  stand; `$HOME` is the user's folder. `PYTHONUTF8` is not set: run a Python script that prints or reads other
  than Latin text with `python -X utf8`.
- **Git.** On Windows a command you run by yourself runs inside the sandbox as another Windows user, and git
  refuses a repo that someone else owns ("dubious ownership"). A command you ask approval for runs outside the
  sandbox as the user. So ask approval for every command that creates a repo or its folder (`git init`,
  `git clone`, `git worktree add`): a `.git` made inside the sandbox belongs to the sandbox's user, the user's
  own git then refuses the project, and the sandbox stops working in it. Ask approval as well for every git
  command on the agent-setup repo: it lies outside the project, and a pull needs the network. When git answers
  "dubious ownership", run the command again with approval; never add `safe.directory` to the user's git config.

## The two profiles

Both profiles follow. Only the one the project's `AGENTS.md` names in its `Profile:` line applies (`Profile:
code` or `Profile: docs`). In a project with no such line neither applies: say so once and suggest the
`setup-sync` skill.
