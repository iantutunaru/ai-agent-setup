# What has been tried where

What each skill and each part of the setup has done on each assistant, as the repo records it. The front page
sums this up in a small table, one row per skill group ([README.md](../README.md#which-assistants)).

Every cell starts with one of three words, decided from the cell's own text (SU-Q127):

- **tried**: the cell names a run on that assistant and names nothing as still not run.
- **partly tried**: it names a run and also names something not run or not seen.
- **not tried**: it names no run on that assistant. "Installed" and "built for it" alone are not tried: they
  say the skill exists, not that it ran.

A run found in one of the owner's private projects is given as the number of projects, the dates and the short
commit hashes (SU-Q130); you cannot open those projects. A hash without a project is in the history of the
owner's private working repo, from which this copy was made; this copy does not carry that history.

## By assistant

| Skill | Claude Code | ChatGPT desktop app |
|---|---|---|
| web-rulebook | tried: built for it; trial cases in its `evals/`; two trial runs, 2026-11-21 (`dcdba71`) | tried: tested: answered with entry ids from the lookup script |
| web-check | tried: built for it; trial cases in its `evals/`, one full page audit; the pilot's three runs and a rerun (`dd51636`, `bf2918a`) and the first full audit (`23a2acc`), all 2026-11-21 | tried: tested: measured a page at two widths. It drove the installed Chrome through a Node script of its own, so it needs Chrome and Node |
| web-look, web-text | tried: built for it; trial cases in each skill's `evals/`; one trial run each, 2026-11-21 (`4f21e74`, `74b885d`) | not tried: not tested; they use the same lookup script as web-rulebook |
| writing-check | tried: built for it; run on real texts in three of the owner's private projects, 2026-11-12 to 2026-11-16 (`0798b01`, `2b1165f`, `d0020d5`, `2d53e24`), and on this repo's README, 2026-11-21 (`31fb743`) | tried: tested: ran both scripts |
| humanizer-en | not tried: installed; writing-check loads it | tried: tested |
| plain-language | not tried: installed; no test on record | tried: tested: started by itself |
| business-writing | not tried: installed; no test on record | partly tried: loaded as a helper; not tested by itself |
| corporate-communication, orwells-rules, gov-uk-style | not tried: installed; no test on record | not tried: not tested |
| guided-session | tried: built for it; run in one of the owner's private projects, 2026-11-14 to 2026-11-16 (`a4bb05c`, `b3b739c`, `0930584`) | not tried: not tested |
| design-lenses, balance-check, playtest-plan | partly tried: built in one game project and used there in their first form. The general versions (2026-11-21) have no run on record; checked so far: balance-check's script has unit tests, and the first project's entry holds every field the skills read | not tried: not tested |
| stage-close | partly tried: built for it; its cleanup script has unit tests. The runs on record are of projects' own earlier copies, from before the shared skill (`11986b8`, 2026-11-12): two of the owner's private projects, 2026-10-24 to 2026-10-28 (`82f9fad`, `6f2c355`, `b62684fb`, `9477dc48`). No stage close of the shared form is on record | not tried: not tested |
| /setup-sync | tried: built for it; run on 11 projects | partly tried: tested on a new project: surveyed it, asked about its one finding, logged the answer. Moving an existing project is not tested |
| /setup-promote | partly tried: built for it; one run on record of its older form, which pushed `main`. The branch form (2026-11-21): walked through on scratch repos (branch, push, the hook's line, a merge from a second clone, the "merged" line, switch back, branch gone), and its commands have unit tests. Not seen yet: a run against GitHub, and the pull request link in its output | not tried: not tested |
| /setup-init | not tried: built for it; no run on record | tried: tested: three questions, the template files, one commit |
| the rules file and the session-start hook | partly tried: built for it; a new chat loads all three rule files. The hook's skill links (2026-11-21): tried on scratch profiles and on the owner's main PC, where a new chat listed the 19 skills and loaded one through its link. Its lines while the setup is on a branch or merged: tried on scratch repos, not yet in a real chat | partly tried: tested: the rules and both profiles were loaded, and the hook's line reached the chat. Round 3 (2026-11-21, laptop): the hook ran at a chat's start, rebuilt the rules file and put its model line into the chat as a developer message (session log), but the chat would not quote that line; run by hand it took 2.6 of its 60 seconds. The chat followed the Git line: `git init`, the commit and the pull of the setup repo went through approvals, and the project's `.git` belongs to the user. Not run in the app: the hook's skill links and branch lines; whether Python starts inside its hook, and whether it can make the links there, is not known |

## On GitHub

These two are about how changes reach `main`, not about an assistant (SU-Q128). Both trials were run in the
owner's private working repo, not in this copy. Neither was tested from ChatGPT; GitHub runs the tests on every
push, from either app.

| Part | On GitHub |
|---|---|
| the tests on GitHub | tried: tried 2026-11-21 from a test branch: both checks, `tests (ubuntu-latest)` and `tests (windows-latest)`, passed. Linux skips the tests that need PowerShell and junctions; Windows runs them all. They block a merge only once `main` is protected, which it is not yet |
| the approvals check and the protection of `main` | partly tried: tried 2026-11-21 on a draft pull request: `core-approvals` was red while it waited for a second owner added for the trial, green once the author was the only owner left, and ran again when the owner left a comment review. Not tried yet: an approval by a second person turning it green; the protection rule and the merge settings, which are not set, so GitHub enforces none of "Working together" yet; a second person's first pull request |

## Where each column comes from

The ChatGPT column comes from one test round on 2026-11-21, recorded in
[sessions/chatgpt-skills-r1.md](sessions/chatgpt-skills-r1.md). The rules file, the hook and the setup skills
come from a second round the same day: [sessions/chatgpt-setup-r2.md](sessions/chatgpt-setup-r2.md). A third
round, on git inside ChatGPT's sandbox, ran on the laptop the same day:
[sessions/chatgpt-setup-r3.md](sessions/chatgpt-setup-r3.md). The two rows about GitHub come from one trial on
2026-11-21, from a test branch, deleted afterwards, and a draft pull request, closed (SU-Q107). The runs in
Claude Code come from the commits each cell cites.
