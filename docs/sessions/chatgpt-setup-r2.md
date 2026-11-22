# The whole setup in ChatGPT, round 2 (~15 min)

For SU-Q49 stage 2 and SU-Q51: the README may say the rules, the hook and the setup skills work in ChatGPT only
after this round. Rows R2 to R5 write only inside the empty test folder `D:\<projects>\chatgpt-setup-test`. Cap: 3
rounds.

**Why.** Until now ChatGPT got this repo's skills but none of its rules. On this laptop `install-chatgpt.ps1`
has now also written a rules file (`C:\Users\<you>\.codex\AGENTS.md`), a hook that pulls the repo when a chat
starts (`C:\Users\<you>\.codex\hooks.json`) and links for the three setup skills. Everything a script can check
is checked (see "Automatic"). What only the app can show: whether it loads the rules file, runs the hook once
you trust it, keeps the setup skills from starting unasked, and can set up a project with them. One row is
for Claude: the rules file Claude loads now imports two other files, and only a new chat shows whether that
works.

**Where to start.** Close the ChatGPT desktop app completely and open it again. The screen names below are from
OpenAI's pages, not from the app itself, so say where a name differs.

| Row | Do | Bring back |
|---|---|---|
| R1 | In ChatGPT open Settings, then Hooks (or "Review hooks" under the message box). Find the hook whose command ends in `session-start.ps1` and trust it. | Whether it was listed, and whether trusting it worked. |
| R2 | Start a new Codex chat on the folder `D:\<projects>\chatgpt-setup-test`. Send: `Without opening any file: what is your rule about dashes in text other people read, which two profiles do you know, and is there a line in your context that begins "agent-setup: model"? Quote it.` | Its answer on dashes (pass: no em or en dashes), whether it names the code and docs profiles, and the model line or "no such line". |
| R3 | Same chat. Send: `$setup-init` (or type `@` and pick setup-init). It should ask three numbered questions, each with a recommendation. Answer: docs profile; name `Test project`, any one-line description, nothing special for safety; prefix `ZT`. | Whether the three questions came with recommendations, and its last message (pass: it names one commit and "nothing left to fill"), or the error line. |
| R4 | Same chat. Send, without naming a skill: `Bring this project up to date with the shared setup.` | Whether it started the setup-sync skill by itself (pass: it does not; it may suggest it), in a few words. |
| R5 | Same chat. Send: `$setup-sync`. In a project that new it should find little or nothing to change. | What it proposed, or the error line. Answer "no" to anything it wants to change. |
| R6 | In Claude Code open a new chat in any project. Send: `Do not open files. Which top-level headings do your loaded global rules have, in order?` | The headings (pass: "Shared rules (every project)", "Claude Code part", "About the user"). **Do not push before this row passes** (SU-Q67). |
| R7 | Anything odd: a question about permissions, a hook warning at the start of a chat, a skill listed twice. | A few words. |

Reply in one line, for example: `R1 listed, trusted · R2 no dashes, both profiles, model gpt-6.2-sol · R3 3
questions, one commit · R4 did not start · R5 nothing proposed · R6 three headings · R7 nothing`.

**Automatic (done, 2026-11-21).**

- `install-chatgpt.ps1` against a scratch folder, 25 checks pass: a fresh install (16 skill links, the repo
  link, a rules file of 12.3 KB of ChatGPT's 32 KiB, one hook entry); a second run rewrites nothing; a machine
  with its own rules file, its own hooks and a same-named skill folder keeps all three, with backups; a changed
  block of the rules file is rebuilt once and the user's text around it stays; the hook script, called through
  the link with the JSON ChatGPT sends, prints `agent-setup: model gpt-6.2-sol` and ends with exit code 0.
- Then on the laptop: 16 of 16 skills linked (the three setup skills new), `~/.codex/setup` linked,
  `~/.codex/AGENTS.md` built (12,326 bytes), the hook written to `~/.codex/hooks.json`. Neither file existed
  before, so nothing of the user's was replaced.
- `python -m unittest discover -s tools/tests`: 17 tests pass (template copy that never overwrites, prefix
  fill, the open-placeholder check, sibling prefixes, base lines, the move of a project's text from `CLAUDE.md`
  to `AGENTS.md`).
- Not possible from here: starting a new Claude chat or a ChatGPT chat to see what it loads. A helper agent
  inside the building chat only sees that chat's already loaded rules, which is why R6 is a row.

## Results

Run by the user on 2026-11-21 on the laptop: rows R2 to R5 in one chat of the ChatGPT desktop app (GPT-6.2 Sol),
R6 in a new Claude Code chat. The user's reply: "all passed", with both transcripts. The rows below are read
from the transcripts, not from the reply alone.

| Row | What came back | What it settles |
|---|---|---|
| R1 | Passed, per the user. The hook ran in the chat of R2, which it can only do once trusted. | The hook written by the install is listed, can be trusted, and runs. |
| R2 | Pass. Dashes: "no em dashes or en dashes in text other people will read". Profiles: Code (`Profile: code`) and Documents (`Profile: docs`). It quoted `agent-setup: model gpt-6.2-sol`. | ChatGPT loads `~/.codex/AGENTS.md` with the shared rules and both profiles, and the hook's output reaches the model. The 12.3 KB file was not cut short where these three answers sit. |
| R3 | Pass. It read the skill, found `~/.codex/setup`, loaded `grilling` and asked three numbered questions, each with a recommendation. With the answers (docs, Test project, ZT) it ran `copy-template docs`, `fill-prefix ZT`, filled `AGENTS.md` and `decisions.md`, ran `check` ("ok: nothing left to fill") and made one commit, `97e1ec3`, of five files. | `setup-init` works in ChatGPT, through the script, in PowerShell. Two remarks: the pull of step 1 failed with git's "detected dubious ownership in repository at 'D:/<projects>/claude-setup'" and it went on with the files on disk, as the skill says; after `git init` its sandbox stopped running git in the new folder until it passed `-c safe.directory=<folder>` on an approved command. |
| R4 | Pass. It did not start the skill; it answered that the shared rules require `setup-sync` to be named and told the user to send `$setup-sync`. | `agents/openai.yaml` with `allow_implicit_invocation: false` holds, and the rule's last sentence is read. |
| R5 | Pass. The pull succeeded this time ("already current"). `instructions` and `base-lines` found nothing; it proposed one change, as a grilling question with a recommendation: remove "A settled decision stands unless the user reopens it" from the project's `AGENTS.md`, because `global/rules.md` says the same. On "no" it kept the line, logged the answer as `ZT-Q04` and committed (`834c9d8`). | `setup-sync` works in ChatGPT. Its one finding is real: the template's `AGENTS.md` repeats a shared rule, so every new project meets this proposal at its first sync. |
| R6 | Pass. The new Claude chat named three top-level headings in order: "Shared rules (every project)" (`global/rules.md`), "Claude Code part" (`global/rules-claude.md`), "About the user" (`global/personal.md`). | Claude Code loads the import inside an import (SU-Q67). The push gate is cleared. |
| R7 | Nothing reported. | |

Open after this round:

- **ChatGPT's sandbox works as its own Windows user.** Seen after the round: in the test project the `.git`
  folder and `AGENTS.md` are owned by `<PC>\CodexSandboxOffline`, the project folder itself (made
  before the round) by the user's account. Git refuses a repo owned by someone else ("dubious ownership"), which
  explains both remarks of R3, and it cuts both ways: inside the sandbox git refuses the setup repo, and the
  user's own git (GitHub Desktop, Claude) refuses a project that `setup-init` made in ChatGPT, until a
  `safe.directory` entry or a change of owner. The project's two commits were read from here with a one-off
  `git -c safe.directory=<folder> log`. Not known: why the pull of R5 worked (an approved command may run as the
  user), and whether the session-start hook's own pull is affected (the chat quoted no "could not pull" line, but
  it was asked only for the model line).
- **The template repeats a shared rule** (R5): the sentence in `template/code/AGENTS.md`, `template/docs/AGENTS.md`
  and the two decisions files. Whether to drop it from the template is the user's call.
- Not exercised: `setup-promote` in ChatGPT, the move of an existing project (`move-instructions`) in either
  tool, and a chat on GPT-6.2 Astra.

Found later the same day (the facts, with how each was tested, are in `HANDOFF.md` under "ChatGPT's sandbox and
git"): the pull of R5 worked because it was an approved command, which runs as the user; the sandbox stopped
after `git init` because it could not protect a `.git` owned by its own user, not because of git; and the hook
is not started through the sandbox.
