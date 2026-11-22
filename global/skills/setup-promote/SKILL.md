---
name: setup-promote
description: Move an improvement made in this project into agent-setup (a rule, a skill fix, a template or settings change) so every project gets it; makes a branch in the setup repo, commits, pushes the branch (never main) and shows the pull request link for the user to open. Run again after the merge, it switches the setup back to main.
disable-model-invocation: true
---

# Promote a change to agent-setup

Works in Claude Code and in ChatGPT (the desktop app, Codex). `<setup>` below is the agent-setup repo's link:
`$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in ChatGPT; use the one that exists. The repo is the
one source for every project (SU-Q02). The commands run as written in bash and in PowerShell.

    TOOLS:  python "<setup>/tools/setup_tools.py"

The `TOOLS` commands below run git on the setup repo; in ChatGPT ask approval for each, as for a git command
there (the Git line of its rules).

A change reaches the repo as a pull request (SU-Q85). It is made on a branch in the setup itself, so this machine
runs it at once and tries it in real chats; while the setup is on the branch, this machine gets no updates from
`main` (SU-Q95). The assistant commits and pushes the branch, never `main`; the user opens the pull request,
because a pull request is a message to other people (SU-Q93). It lands as a merge commit and GitHub deletes the
branch there (SU-Q108); the skill then brings the setup back to `main`.

## 0. Where the setup stands

`TOOLS repo-state` fetches and prints the state in its first line:

| state | what it means | go to |
|---|---|---|
| `main` | no change open | step 1 |
| `not-merged`, `no-upstream` | a change is open on this branch (pushed, or not yet) | step 6 |
| `merged`, `no-commits` | the branch is merged, or holds nothing that is not on `main` | step 7, then step 1 for a new change |
| `detached` | on no branch | step 7 |
| `unknown` | on a branch, and no `main` on the remote to compare with | show it to the user and wait |

When the fetch failed, it says so and judges on what was fetched before: tell the user. Uncommitted changes it
lists are the user's until they say otherwise.

## 1. Place it

Say in one line what the change is and where it goes:

| The change | Goes to |
|---|---|
| a rule for every project, in both tools | `global/rules.md` |
| a rule about one tool (its models, chat budget, shell, skill names) | `global/rules-claude.md` or `global/rules-chatgpt.md` |
| a rule for code or for docs projects | `profiles/code.md` or `profiles/docs.md` |
| a fix or step in a global skill | `global/skills/<skill>/` |
| a whole new skill | `global/skills/<skill>/`, and the places "A new skill" in step 3 lists |
| a file new projects should start with | `template/` |
| a step of the setup skills that needs a script | `tools/setup_tools.py` |
| an env var, hook, plugin or permission for Claude Code | `global/settings.json`, `global/hooks/` |

A change only this project wants stays in the project; say so and stop.

## 2. Make the branch

`TOOLS branch-name <a few words for the change>` prints the branch, `<name>/<topic>`: the name is the first word of
git's user name, the topic the words joined by hyphens (SU-Q112). Show it to the user before the branch is made;
they may change the words, or the name with `--name`. When git's user name holds no letter a branch name can use,
it asks for `--name`.

`TOOLS start-branch <branch>` then brings `main` up to date with the remote and makes the branch from it. It
changes nothing and says why when:

- the setup has uncommitted changes: show them to the user (`git -C "<setup>" status --short` and the diff). If
  they belong to this change, run it again with `--carry`, which takes them onto the branch; otherwise the user
  decides what happens to them first;
- `main` cannot be brought up to date, the fetch failed or the branch exists already (here or on the remote): show
  its line and wait.

## 3. Write it

In the target file's own style, written for any project and for both tools: no project names, project paths read
from the project's `AGENTS.md` entry instead, "the assistant" for the one doing the work. Search the repo for the
same meaning first (over `global/`, `profiles/`, `template/`): change the one place that holds it, never add a
second copy. A change that contradicts a decision in `decisions.md` reopens it: put it to the user as a grilling
round and log the answer as the next `SU-Qnn`. A changed skill or script with a `tests/` folder: run them
(`python -m unittest discover -s global/skills/<skill>/tests`, `python -m unittest discover -s tools/tests`),
from the repo's folder.

**A new skill** also changes what the repo says about its skills (SU-Q80). In the same commit:

- `README.md`: the skill count (two places); the skill's row in its group's table under "The skills" (name
  linked to its `SKILL.md`, what it does, what to say); the group's word in the small status table under "Which
  assistants" if the new row changes it.
- `docs/tried.md`: the skill's row, saying only what was run, each cell starting with tried, partly tried or
  not tried (SU-Q127).
- `docs/install.md`: the "One skill" note if the skill reads files outside its own folder.
- `CONTRIBUTING.md`: the tests list if it has a `tests/` folder; the Layout if it adds a folder.
- `global/skills/README-sources.md`: where the skill came from.
- `global/skills/setup-sync/SKILL.md`, item 3: the entry the skill reads in a project's `AGENTS.md`, if it has
  one, with every field of the entry read by at least one skill.
- The hand-over of that line of work in `docs/handoffs/`, if one is open: what was moved and what is left.

`python -m unittest discover -s tools/tests` checks these against the skill folders: the README's count and
one row per skill, one row per skill in `docs/tried.md` with a status word in every cell, the README's small
status table against it, the tests list in `CONTRIBUTING.md`, and every link from the four pages to a file in
the repo. Nothing needs to be installed again for a new skill: on each PC the session-start hooks
of both assistants link it after the pull.

## 4. Commit and push the branch

Show the user the diff. On their OK: `git -C "<setup>" add` the files of this change, commit
`Promote from <project>: <what>`, saying how it was checked, then `TOOLS push-branch`. It pushes the branch with its
upstream and refuses `main`, a detached head and a branch with nothing to push; never push the setup any other way.
It prints git's lines and, when git printed one, `pull request link: <url>`. Give the user that link: they open it,
write the pull request and create it. Without a link, tell them to open the repo's page on GitHub and start the
pull request from the branch. If the push fails, show its line; the commit stays on the branch for the next
`TOOLS push-branch`.

Tell the user who must approve before it can be merged: one person other than its author; a change to the files
every chat loads or every machine runs (`global/rules*.md`, `profiles/`, `global/settings.json`, `global/hooks/`,
both install scripts, `tools/`, `.github/`) waits for everyone's yes (SU-Q89, SU-Q106).

A changed rule or profile reaches Claude Code on this machine at once. ChatGPT reads a built copy
(`~/.codex/AGENTS.md`): its session-start hook rebuilds it, so the change applies there from the next chat. The
other machines get it once the pull request is merged.

## 5. Tidy the project

Remove the project's own copy of what was promoted, if it had one, and commit there (the user pushes). If other
projects need a new entry or file for it, tell the user: the `setup-sync` skill in each project adds it.

## 6. A change is open on this branch

Say which branch it is and the commits `TOOLS repo-state` lists as its own, and ask the user which case it is:

- **More for the same pull request.** Write it on this branch (step 3), commit as in step 4 and run
  `TOOLS push-branch` again: the open pull request takes the new commits.
- **A separate change.** It waits until this one is merged (then step 7 and a new branch), or, if the user wants it
  now, `TOOLS switch-back --keep` returns to `main` and keeps the branch (it is on the remote once pushed; a branch
  that is not pushed yet is pushed first, step 4); then step 2. Until the first change is merged, this machine then
  runs without it.
- **The pull request was closed without merging.** The user decides. To keep the branch, for later:
  `TOOLS switch-back --keep`. To drop it: `TOOLS switch-back --abandon`, only after the user's yes; it deletes the
  branch here and prints its last commit, with the line that brings it back. The branch on GitHub stays; the user
  can delete it on the pull request's page.

A branch that is not merged is never deleted without the user's yes.

## 7. Back to main

`TOOLS switch-back` fetches and, only when the branch is merged (or holds nothing that is not on `main`), switches
to `main`, brings it up to date and deletes the branch here without force. When the branch is not merged it changes
nothing and says so: go to step 6. It also stops on uncommitted changes (show them: the user decides) and when the
fetch fails (try again later).

On no branch (detached), it returns to `main` when the commit is also on a branch or on the remote; otherwise it
stops: show the user `git -C "<setup>" log --oneline -3`, and keep the commit with
`git -C "<setup>" branch <name>` before anything else, unless the user says to drop it (`--abandon`).

Done when the push succeeded and the user has the link (or the push's failure is shown) and the project holds no
second copy of the change; after a merge, when the setup is on `main` again and up to date.
