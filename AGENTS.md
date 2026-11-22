# agent-setup

Profile: code

The shared setup for AI assistants: the rules, profiles, skills, project template and install scripts that Claude
Code and ChatGPT load in every project. It is the live setup of every PC that installed it: each runs straight
from its clone, so what is checked out there is what the next chat on that PC loads.

## Safety

- A change to an install script or a hook is built and tried on a scratch folder, with the scripts' overrides
  (`-ClaudeDir`, `-AgentsDir`, `-CodexDir`; `HOME` for `session-start.sh`), before it runs on a real profile.
- The assistant never pushes `main`; see "How a change is made".
- Every tracked file is public: no personal data, no names of other projects or clients, no machine paths with a
  user or PC name. `tools/tests/test_public_guard.py` checks it; a person's own list of private terms goes in
  `local/private-terms.txt`, which git ignores.

## Where things are

- `docs/handoffs/`: one hand-over per open line of work, removed when that work is merged. A chat starts from
  the one it was given.
- `decisions.md`: every decision, ids `SU-Qnn`, one sequence. A new decision takes the next free id. A unit test
  fails on a duplicate; the pull request that merges second renumbers its new ids (SU-Q92).
- `local/handoff.md`: a person's own open items, in the folder git ignores; it may be missing.
- `README.md`: the front page, for people; `CONTRIBUTING.md`, `docs/install.md` and `docs/tried.md` are its
  side pages. `docs/tried.md` says only what was run.

## How a change is made

On a branch, with the commands the `setup-promote` skill uses: `python tools/setup_tools.py start-branch`,
`push-branch`, `switch-back`. The assistant pushes the branch, never `main`; the person opens the pull request
(SU-Q93). A change to a path in `.github/CODEOWNERS` waits for everyone's yes (SU-Q89).

Before every commit, from the repo's folder, the four suites:

- `python -m unittest discover -s tools/tests`
- `python -m unittest discover -s global/skills/stage-close/tests`
- `python -m unittest discover -s global/skills/web-rulebook/tests`
- `python -m unittest discover -s global/skills/balance-check/tests`

## Gotchas

- Remove a junction with `cmd /c rmdir <link>`. Never run a recursive delete (`Remove-Item -Recurse`) on a folder
  that still holds junctions: remove the links first.
- A helper agent started inside a chat sees that chat's already loaded rules, not the files on disk; only a new
  chat shows what a changed rules file loads.
- The Bash heredoc collapses backslashes, also inside `python - <<'EOF'`: scripts with `\n` or Windows paths go
  in a scratch `.py` file.
- `${CLAUDE_SKILL_DIR}` is filled in by Claude only in a skill's `SKILL.md`; ChatGPT puts the skill's folder in
  its place.
- `stage-close/cleanup.py` knows Claude's scratchpad and worktree names only; under ChatGPT its scratch and
  worktree parts find nothing.
- Dormant projects (SU-Q05) migrate with `/setup-sync` when next opened; that sync also moves their text into
  `AGENTS.md` (SU-Q59).
