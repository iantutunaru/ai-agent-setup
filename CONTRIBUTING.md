# Contributing to agent-setup

How this copy relates to the owner's own repo, how a change is made, the tests, the notes for whoever maintains
it, and where things are. How to install it and what the setup does are on the [front page](README.md).

## This copy

agent-setup is the owner's own setup. It is developed in a private repo, and this public copy is updated from it
by hand, so it can lag behind. To make the setup yours, fork it and change your fork as you like. Issues and pull
requests here are read, but there is no promise that they are merged.

## Working together

This is how the owner, and any collaborators the owner adds, change the repo. Every PC that installed it loads
what is on `main`, so every change is read by someone other than its author before it lands there, once there is
a second person. How much of this GitHub enforces so far, and what has been tried, is in the table "On GitHub" in
[docs/tried.md](docs/tried.md). In a fork of your own you can keep these steps or drop them.

- **A change goes on a branch.** A branch is a separate line of commits beside `main`, the line every PC runs.
  `/setup-promote` makes the branch, commits your change on it, pushes the branch to GitHub and shows a link.
  Open the link and create the pull request yourself: a pull request asks for your branch to be merged into
  `main`, and is where the others read, comment and approve. Until the merge your PC runs your change and gets
  no updates from `main`. After the merge, run `/setup-promote` again: it switches your setup back to `main` and
  pulls.
- **Who approves.** Every change needs one approval from someone other than its author. A change to the shared
  core waits for a yes from every owner. The shared core is what every chat loads or every PC runs, as listed in
  [.github/CODEOWNERS](.github/CODEOWNERS): the rules files (`global/rules*.md`), the profiles, the shared Claude
  Code settings (`global/settings.json`), the hooks, both install scripts, the `tools/` folder and the `.github/`
  folder. GitHub checks this with a check named `core-approvals`, which stays red until every owner named for a
  changed file, other than the author, has approved the latest commit. The check stops a merge made by
  oversight, not someone who works around it: a pull request that edits the check itself is judged by its edited
  form.
- **The tests.** GitHub runs the four test suites (listed under "The tests" below) on every push and every pull
  request, on a Linux and a Windows machine. A failing test blocks the merge once `main` is protected. Run them on your PC before you
  commit.
- **How a pull request lands.** As a merge commit: your commits stay as you wrote them, and one more commit joins
  them to `main`. GitHub then deletes the merged branch. The session-start hook and `/setup-promote` tell that a
  branch is merged from that merge commit.
- **Decisions and hand-overs.** Every decision goes into [decisions.md](decisions.md) with an id `SU-Qnn`, one
  sequence for everyone; a new decision takes the next free id. When two pull requests take the same id, the one
  merged second renumbers its new ids, and a test fails on a duplicate. Work that continues in a later chat is
  handed over in one file per open line of work in [docs/handoffs/](docs/handoffs/), deleted when that work is
  merged.
- **What is yours alone.** Your files in `local/`, which git ignores, and any skill you copy or write into your
  skills folder beside the links: it stays yours and never enters the repo.

## The tests

From the repo's folder. GitHub runs the same four on every push and pull request
(`.github/workflows/tests.yml`):

```powershell
python -m unittest discover -s global/skills/stage-close/tests
```

```powershell
python -m unittest discover -s global/skills/web-rulebook/tests
```

```powershell
python -m unittest discover -s global/skills/balance-check/tests
```

```powershell
python -m unittest discover -s tools/tests
```

The page measuring script of `web-check` is tried by hand on `global/skills/web-check/tests/fixture.html`; the
expected numbers are in `tests/expected.md` beside it. How the web skills are tried with agents:
`global/skills/web-rulebook/tests/TRIALS.md`.

## For whoever maintains it

- Reasons for how things are: [decisions.md](decisions.md). Skills and rules cite its ids (`SU-Q14`).
- Where the skills from GitHub and from a project came from, and what was left out:
  [global/skills/README-sources.md](global/skills/README-sources.md).
- The game design skills: where the books live, how to add to a skill from them, and the fields of the entry
  they read: [research/game-design/README.md](research/game-design/README.md).
- A new skill changes several places in the front page and its side pages; the list is in step 3 of
  [setup-promote](global/skills/setup-promote/SKILL.md). The last test above checks them against the skill
  folders: the skill count and one table row per skill in [README.md](README.md), "Install" there, "Working
  together" and the tests list here, one row per skill in [docs/tried.md](docs/tried.md) with a status word in
  every cell, the small status table on the front page against it, and every link from the four pages to a file
  in the repo.
- Every tracked file is public. `tools/tests/test_public_guard.py` fails on a machine path with a user or PC
  name, on an email address outside a short allow list, and on any term in your own `local/private-terms.txt`.
- The approvals check: [tools/core_approvals.py](tools/core_approvals.py), run by
  `.github/workflows/core-approvals.yml`. It reads [.github/CODEOWNERS](.github/CODEOWNERS) and understands only
  the forms that file's header lists; any other form turns it red and names the line. The settings of `main`'s
  protection and of how a pull request lands are listed, for the owner to set, in
  [docs/handoffs/shared-repo.md](docs/handoffs/shared-repo.md) until they are on.
- `global/skills/synced/` is not part of this repo: a Claude program writes Anthropic's own skills into
  `~/.claude/skills/synced`, which an older install's single link put inside the repo. `install.ps1` moves it out
  (SU-Q111), and git ignores the folder (SU-Q37) in case an older install still writes there.
- How the rulebook was built, and its known gaps: [research/web-design/README.md](research/web-design/README.md).

## Layout

```
global/                      seen by every project on the machine, through the install scripts
  rules.md                   the shared rules, for both assistants
  rules-claude.md            what differs in Claude Code: models, chat size, shell
  rules-chatgpt.md           the same for ChatGPT
  CLAUDE.md                  two import lines: what Claude Code loads
  personal.example.md        the example of a person's own file, copied into local/ by the installs
  skills/                    the skills
  settings.json              shared Claude Code settings, merged by install.ps1
  settings.personal.example.json  the example of a person's auto mode description, copied into local/
  hooks/                     the scripts that pull this repo at session start, the builder of ChatGPT's rules
                             file, the helper that makes the files in local/, and the code that links each
                             skill (both installs and both hooks use it)
local/                       your own personal.md, settings.personal.json and private-terms.txt; git ignores
                             this folder
profiles/                    code.md and docs.md: a project names one
template/                    copied into a new project by /setup-init: base/ always, then code/ or docs/;
                             entries/ holds the forms `setup_tools.py add-entry` writes into a project
tools/setup_tools.py         the steps of the setup skills that must run the same in bash and PowerShell
tools/core_approvals.py      the core-approvals check, which GitHub runs on every pull request
tools/tests/                 the tests of the scripts, the decision ids, the front page with its side pages,
                             and the public guard
.github/                     what GitHub runs and reads: the tests, the approvals check, the code owners file
                             (the shared core and its owners) and the pull request template
install.ps1                  links the repo into Claude Code (once per machine, safe to re-run)
install-chatgpt.ps1          sets the repo up for ChatGPT (run again after moving the repo)
research/web-design/         how the rulebook was made (README.md) and the rulebook itself (rulebook/: one file
                             per topic, taste.md, dropped.md and _joined.json)
research/game-design/        where the game design books live, and the Game design entry the game skills read
docs/install.md              what each install script changes on a PC, the second PC, undo, one skill
docs/tried.md                what has been tried where, skill by skill
docs/img/                    the front page's banner, in a light and a dark form
docs/sessions/               checklists and results of test rounds
docs/handoffs/               one hand-over per line of work that is still open
decisions.md                 every decision about this setup, with ids SU-Qnn
LICENSE                      the MIT licence, and what it does not cover
README.md                    the front page: what this is, how to install it, the skills
CONTRIBUTING.md              this file: this copy, how a change lands, the tests, the layout
AGENTS.md                    what a chat working on this repo reads first: where things are, how a change is made
CLAUDE.md                    two import lines, so Claude Code loads the code profile and AGENTS.md
```
