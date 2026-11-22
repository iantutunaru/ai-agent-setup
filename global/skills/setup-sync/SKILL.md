---
name: setup-sync
description: Bring this project up to date with agent-setup, or migrate it the first time - pull the setup repo, the project's text in AGENTS.md with its profile, the entries the global skills read, missing base lines, old copies of global skills and rules. Shows the whole change before one commit.
disable-model-invocation: true
---

# Sync a project with agent-setup

Works in Claude Code and in ChatGPT (the desktop app, Codex). `<setup>` below is the agent-setup repo's link:
`$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in ChatGPT; use the one that exists. The commands run
as written in bash and in PowerShell.

    TOOLS:  python "<setup>/tools/setup_tools.py"

The same procedure migrates an old project the first time and keeps a migrated one current (SU-Q05, SU-Q11,
SU-Q28). It only adds and moves: a line the project wrote for itself stays unless the user approves its removal,
and where the project says otherwise than the shared rules, the project wins.

## 1. Pull

`TOOLS repo-state` says where the setup stands (it runs git there: in ChatGPT, with approval, as the pull). On
`main` (its first line `state: main`):
`git -C "<setup>" pull --ff-only`. If it fails, show its line; go on with the files on disk only on the user's
OK. On a branch or on no branch, there is no pull (a setup change waits for its pull request there, SU-Q95): tell
the user in one line that the sync uses the setup as it is on that branch, and go on; when the branch is merged,
add that `/setup-promote` switches the setup back to `main`. Run inside the setup repo itself, there is nothing
to sync: stop.

## 2. Survey

Read-only. Build a numbered list of proposed changes, each with what it changes for the user and the file lines
it rests on. Values for new entries come from the project's own files (an old skill copy, the tickets README, the
current `AGENTS.md` or `CLAUDE.md`); a value no file gives is a question for step 3, never a guess.

1. **The project's file, for both tools (SU-Q59).** `TOOLS instructions` shows the state. The aim: `AGENTS.md`
   holds the project's text, with a line `Profile: code` or `Profile: docs` under its title; `CLAUDE.md` is two
   lines, `@~/.claude/setup/profiles/<profile>.md` and `@AGENTS.md`. ChatGPT reads `AGENTS.md` and takes the
   profile from its rules file; Claude Code reads both through `CLAUDE.md`.
   - *Not moved* (the text is in `CLAUDE.md`): propose the move. If the file names no profile, propose the one
     that fits (code: the assistant builds software, mods or tools; docs: research, decisions, paperwork,
     outgoing text).
   - *Mixed* (both files hold text): propose one merged `AGENTS.md`, shown to the user in full.
   - In the project's live docs, a mention of `CLAUDE.md` that means the project's text becomes `AGENTS.md`.
     Done tickets and old decision rows stay as history.
2. **Duplicated rules.** A line in the project's file (or a doc it imports) that says what
   `<setup>/global/rules.md`, the tool parts beside it (`rules-claude.md`, `rules-chatgpt.md`) or the profile
   already say: propose removing it, quoting both. A line that is stricter or different is the project's own and
   stays; a real contradiction goes to the user.
3. **Entries the global skills read** under "Where things are" (each skill's SKILL.md defines its entry). In
   step 4, `TOOLS add-entry game-design` and `TOOLS add-entry guided-sessions --where "<the place>"` write the
   Game design list and the Guided sessions line with its notes file, every field `none yet`, as `/setup-init`
   does; then fill in what the project's files give:
   - **Stage close** (`<setup>/global/skills/stage-close/SKILL.md`, step 0) for a project with tickets in
     stages: fill it from the project's old `stage-close` copy and tickets README, or from the project's layout.
   - **Guided sessions** (`guided-session`, step 0) for a project whose user does rounds in a game, at a device or
     in a GUI: the project's notes file (`docs/sessions.md`), written from its old `re-session`, `car-session` or
     `playtest` skill and its own file: tools, before-a-round steps, file places and names, writes and undo,
     safety, overrides.
   - **Game design** (`<setup>/research/game-design/README.md`, "The project's entry"; read by `design-lenses`,
     `balance-check` and `playtest-plan`) for a game project: fill it from the project's old copies of those
     skills and its own docs (vision file, data folder, backlog, playtest folder, batch command, fairness band);
     a field with no answer says `none yet`.
   - **Writing rules** (`writing-check`) only when the project's rules file is not `style/writing-rules.md`.
4. **Old copies.** A skill in the project's `.claude/skills/` or `.agents/skills/` that a global skill replaces
   (`stage-close`, `re-session`, `car-session`, `playtest`) or that has the name of one in
   `<setup>/global/skills/`: its project-specific parts move into the entry or notes file of item 3, then the
   copy is deleted (SU-Q10). The project's own `cleanup.py` stays (SU-Q24).
5. **Writing tools.** A project `check_text.py` or `audit_text.py`: deleted, and every doc that runs it points at
   the `writing-check` skill instead. The project's `writing-rules.md` loses the lines the shared
   `<setup>/global/skills/writing-check/writing-rules.md` already holds and keeps its own; any project word that
   `check_text.py` should flag stays in its "Never use" section.
6. **Base lines.** `TOOLS base-lines` lists every line of the template's `.gitignore` and `.gitattributes` the
   project's file lacks. Each is added; none is removed (SU-Q34).
   - **Order.** In `.gitattributes` the last matching line wins, so the base block goes at the top: a `*` line
     appended below a project rule such as `*.CT -text` overrides it. An existing bare `* text=auto` is replaced
     in place by `* text=auto eol=lf`.
   - **Files read byte for byte.** Before proposing `eol=lf`, look for files a game, device or tool reads exactly
     as checked out (deployed mod files, game data, firmware, anything a restore must reproduce). `eol=lf` makes
     every new checkout write them with LF, while `core.autocrlf=true` (Git for Windows' default) writes CRLF
     today. For those paths propose a project `text eol=crlf` or `-text` line after the base block, or leave
     `eol=lf` out until a test shows LF is safe; each is a question for the user.
   - **Estimate here, read-only:** `git ls-files --eol` counts `i/crlf` and `i/mixed` (committed files whose line
     endings would change) and `w/crlf` (files that only change on disk at the next checkout).
7. **Settings (Claude Code).** A project `.claude/settings.json` `env` block that sets only what
   `<setup>/global/settings.json` now sets (`PYTHONUTF8`, `PYTHONIOENCODING`): propose removing it.

## 3. Ask

One grilling round (run the grilling skill first): every item of the list, plain language first (what the user
will see change), a recommendation each, and the questions step 2 raised. Log the answers in the project's
decisions log.

## 4. Apply and check

First `git status --short` must be empty: `git add --renormalize .` stages every modified tracked file, so on a
dirty tree the user's own edits would land in the sync commit (SU-Q34). If it is not empty, stop and ask the user
to commit or stash. Make the approved changes; delete tracked files with `git rm` (after a plain delete,
renormalize stops with "unable to stat").

The move of item 1 is `TOOLS move-instructions` (add `--profile code` or `--profile docs` when `CLAUDE.md` names
none): it writes `AGENTS.md` from the text of `CLAUDE.md`, puts the `Profile:` line under the title and leaves
the two import lines in `CLAUDE.md`. It refuses when `AGENTS.md` already exists. `git add AGENTS.md CLAUDE.md`
afterwards, so git records the move.

After the `.gitattributes` change run `git add --renormalize .` and check that `git status --short` shows only
the files this sync touched; new files stay untracked until the commit's `git add`. In `AGENTS.md`, "## Safety"
holds only what must not be done without the user's OK; the project's other kept rules go under "## Rules" right
after it. Then check what they touch: a cleanup dry run when a Stage close entry was written
(`python "<setup>/global/skills/stage-close/cleanup.py" --tickets <folder>`, or the project's own command);
`check_text.py` on one existing output file when writing tools moved; the project's tests when code or config
changed. Show the user `git diff --stat` and the full diff of `AGENTS.md` and `CLAUDE.md`.

## 5. Commit

One commit, `Sync with agent-setup: <the items>`, saying how it was checked. The user pushes, unless the
project's file says otherwise.

Done when a second survey proposes nothing but the items the user declined.
