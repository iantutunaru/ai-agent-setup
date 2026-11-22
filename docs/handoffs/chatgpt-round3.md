# Hand-over: round 3 in ChatGPT, and what is still open about ChatGPT

Done: ChatGPT (the desktop app, Codex) gets the rules, the pull at session start, the template, the skills and the
three setup skills (SU-Q49 stage 2, SU-Q59 to SU-Q69); round 2 in the app passed every row, and its two open
points are settled and fixed (SU-Q70 to SU-Q74), checked by script.

Left: round 3 in the app, run by the user, and the ChatGPT items below that no round has covered yet.

## Left

**Round 3 was run and read on 2026-11-21** (results in `docs/sessions/chatgpt-setup-r3.md`): R2, R3, R4 and
R5 pass; R1 failed only as asked. The laptop's session log shows the hook ran at the chat's start, rebuilt the
rules file and put `agent-setup: model gpt-6.2-sol` into the context as a developer message
(`hooks.additional_context`); the model answered "I can't quote hidden context". Run by hand the hook took 2.6
of its 60 seconds. `git init`, the commit and the setup repo's pull went through approvals; the project's `.git`
belongs to the user. The README row is updated. The hook ran without being trusted again after its text changed.

1. **What round 3 left open** (a later round, by the user, a few minutes):
   - Whether a chat acts on the hook's model line, which ChatGPT's rules use for a ticket's model check, when it
     will not quote it. A row that asks for the fact, not the quote: "Which model does the session-start hook
     name, and does it match the model you run on?" Check the answer against the session log
     (`hooks.additional_context` in `~/.codex/sessions/<date>/rollout-*.jsonl`). If the chat cannot use the
     line, the ticket check in `global/rules-chatgpt.md` needs another source for the model: a question round.
   - The hook's own line "It applies from the next chat" is not quite what the app does: the app sent the
     rebuilt rules file again at the next turn of the same chat. Harmless; a wording question only.
   - Why the hook ran a second time in the round's chat (start of the fourth turn, after 80 idle seconds): its
     matcher is `startup|resume`; which source fired is not in the log.
   Still not exercised: `setup-promote` in ChatGPT, `move-instructions` on a real project, a chat on Astra.
2. **Also for the round, from the shared repo's tickets 2 and 3** (the detail stays in
   `docs/handoffs/shared-repo.md`):
   - whether ChatGPT's hook can make the skill junctions inside the app (SU-Q110); by hand, as the user, it does;
     in round 3 the links were already current, so the hook had none to make;
   - whether Python starts inside ChatGPT's hook, for its line while the setup is on a branch; if not, the hook
     prints its fallback line. Round 3 ran on `main`, so the hook did not call Python.
   Round 3 makes both likely to work **[I]**: the hook runs as the user, outside the sandbox (it read the setup
   repo and wrote `~/.codex/AGENTS.md`, which the sandbox cannot). A trial needs a new skill arriving with a
   pull, and the setup on a branch, at a chat's start.
3. **ChatGPT on the main PC**: `install-chatgpt.ps1` ran there on 2026-11-21 (ticket 1 of
   `docs/handoffs/shared-repo.md`): skills linked, `~/.codex/AGENTS.md` built, the hook written to a new
   `~/.codex/hooks.json`. Left: restart the app and trust the hook. The install warns that the Git on that PC's
   path is 2.49, older than 2.53. On Windows 11 24H2 or newer the app may use the MXC sandbox, which has no
   second Windows user; nothing here was tested on it.
4. Still open from round 1 (`docs/sessions/chatgpt-skills-r1.md`): which key lists the skills in the desktop
   app, whether the app's own browser can run `measure.js`, and seven skills not exercised. The three game
   design skills came after that round and are not exercised in ChatGPT either.

## Facts, with how far each was checked

Read by the stage 2 chat itself on 2026-11-21 ([V], the page text was in the chat):

- ChatGPT reads `~/.codex/AGENTS.md`, then one `AGENTS.md` per folder from the project root down; all together
  stop at `project_doc_max_bytes`, 32 KiB by default; no import. `project_doc_fallback_filenames` can add other
  file names (not used, SU-Q59). learn.chatgpt.com/docs/agent-configuration/agents-md
- Hooks: `%USERPROFILE%\.codex\hooks.json`; `SessionStart` with a matcher on `startup`, `resume`, `clear`,
  `compact`, `fork`; plain text on stdout becomes context for the model; the hook's input is one JSON object on
  stdin with `model`; a new or changed hook runs only after the user trusts it (Settings, Hooks).
  learn.chatgpt.com/docs/hooks
- `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; skills are named with `@` in the desktop
  app and `$` in Codex. learn.chatgpt.com/docs/build-skills
- Models: GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, GPT-6 Luna; efforts Light or Low, Medium, High, Extra High,
  Max. Credits per million input tokens: Astra 200, Sol 50, Luna 2.5.
  learn.chatgpt.com/docs/models, /docs/model-selection, /docs/pricing
- The Windows desktop app's agent runs commands in PowerShell. learn.chatgpt.com/docs/windows/windows-app
- Claude Code reads a project's `AGENTS.md` when `CLAUDE.md` imports it (`@AGENTS.md`), and imports may nest
  four levels. code.claude.com/docs/en/memory
- Codex install of the question round skill: `codex plugin marketplace add mattpocock/skills`, then
  `codex plugin add mattpocock-skills@mattpocock`. github.com/mattpocock/skills

Seen on the laptop on 2026-11-21:

- `~/.codex/models_cache.json`: context 500,000 for `gpt-6.2-sol` and 272,000 for `gpt-6.2-astra`, 95% usable;
  the round 1 session log shows 475,000 for its Sol chat.
- That session log lists the skill `grilling` from `~/.codex/skills` (a plain copy from September, not the
  plugin), and describes the app's question tool as available in Plan mode only.
- `humanizer-en` has twelve front matter fields and loaded in round 1, so ChatGPT tolerates fields it does not
  know, `disable-model-invocation` among them.
- `~/.codex/config.toml` sets `gpt-6.2-sol` at high effort. `codex.exe` is under
  `%LOCALAPPDATA%\OpenAI\Codex\bin\`, not on the path.
- After SU-Q70 the laptop's `~/.codex/AGENTS.md` was rebuilt (13,093 bytes) and holds the Git line.

### ChatGPT's sandbox and git

Found on 2026-11-21 in the follow-up chat after round 2. "Tested" means run there with
`codex.exe sandbox -C <folder> -P :workspace -- cmd /c <command>` (codex-cli 0.171.0-alpha.13), which runs one
command the way a chat's sandbox does, on scratch folders that are gone again:

- **Two kinds of command.** A command the chat runs by itself runs inside the sandbox as the local Windows user
  `CodexSandboxOffline` (tested with `whoami`; git's own message in the round's session log names that user). A
  command the chat asks approval for (`sandbox_permissions: "require_escalated"` in the session log) runs outside
  the sandbox as the user: the round's second pull was such a command and succeeded on a repo the user owns,
  with no `safe.directory` entry in any git config. That is why the pull failed in R3 and worked in R5. Session
  log: `~/.codex/sessions/2026/11/21/rollout-2026-11-21T19-36-05-*.jsonl`.
- **Why a second user.** Windows 10 has no MXC, so the app uses the "elevated" sandbox, which "uses dedicated
  lower-privilege sandbox users" [V] learn.chatgpt.com/docs/windows/windows-sandbox. `~/.codex/config.toml` has
  `[windows] sandbox = "elevated"`; `~/.codex/.sandbox/sandbox.2026-11-21.log` says "MXC availability: false".
  MXC needs Windows 11 24H2 or newer (same page).
- **The sandbox hands git an exception for the project folder, and the laptop's git is too old to take it.**
  Every sandboxed command gets `GIT_CONFIG_KEY_0=safe.directory` with the working folder as its value, written
  with backslashes, and a second entry `<folder>/*` (tested: `set GIT`). Git 2.44.0 (`D:\Program Files\Git`, the
  one on the path) does not match it: `git status` in the working folder's own repo fails with "dubious
  ownership"; the same value with forward slashes works. Git 2.53.0 and 2.56.1 (the copies inside GitHub
  Desktop) accept the injected form: the same command works. All tested. The lowest version that works was not
  determined; Git 2.46.0's release notes name the `/*` form ("optionally allow leading path matches") [V]
  raw.githubusercontent.com/git/git/v2.46.0/Documentation/RelNotes/2.46.0.txt.
- **`.git` is read-only inside the sandbox**, by design: "`<writable_root>/.git` is protected as read-only" [V]
  learn.chatgpt.com/docs/agent-approvals-security. Tested: a sandboxed `git add` ends in "index.lock: Permission
  denied". So a commit always goes through an approval and runs as the user.
- **The setup repo inside the sandbox.** It lies outside the project folder, so the injected exception does not
  cover it ("dubious ownership" with any git version), and the sandbox has no network (tested: `git ls-remote`
  cannot connect; "Codex asks for approval to edit files outside the workspace or to run commands that require
  network access" [V], same page). A pull or push of the setup repo therefore always needs an approved command,
  and then runs as the user.
- **`git init` inside the sandbox is the one harmful case.** No `.git` exists yet, so nothing protects it: the
  new `.git` belongs to `CodexSandboxOffline` (tested, and seen on `D:\<projects>\chatgpt-setup-test`). Two effects.
  The user's own git refuses the project ("dubious ownership", tested as the user). And on `D:` the sandbox
  itself stops: its setup cannot protect a `.git` it does not own ("deny ACE failed on ...\.git ... os error 5",
  then "setup refresh had errors" for every later command; in the sandbox log at 19:38:42 local time,
  reproduced on a scratch folder on `D:`). That, not git, is why the R3 chat ran everything after `git init` as
  approved commands. Under the user's profile folder the second effect does not occur (tested): the user has
  full control there, while on `D:` the user's rights come from "Authenticated Users: Modify".
- **Git checks who owns the project folder and `.git`**, not the files in them (its messages name those two):
  the files ChatGPT wrote in the test project belong to the sandbox user and do no harm. A project folder that
  the sandbox itself creates would be refused like a sandbox-made `.git`.
- **Repair of such a project, without admin rights** (tested on the scratch folder on `D:`): rename `.git`, copy
  it back with `robocopy <renamed> .git /E`, delete the renamed one. The copy belongs to the user; the user's
  git and the sandbox both work again.
- **The session-start hook.** The sandbox log has a "START" line for every sandboxed command and none between
  the chat's start (19:36:05) and its first tool call (19:36:41), while the hook's line reached the chat at
  19:36:10: the hook is not started through the sandbox. That its pull ran as the user is [I] from this. The
  chat's context held only the model line, which proved nothing, because the hook was silent when git refused
  the repo: run inside the sandbox, `session-start.ps1` printed no warning (tested), since a failed `git status`
  and a failed upstream check were both skipped quietly. Since SU-Q72 it prints `agent-setup: git could not
  read ...` there (tested), so row R1 of round 3 settles it. NOT FOUND on learn.chatgpt.com/docs/hooks: whether
  hooks run inside the sandbox. Round 3's session log (`rollout-2026-11-21T22-44-00-*.jsonl`) settles it in
  practice: the hook printed no "could not read" line and rebuilt `~/.codex/AGENTS.md`, neither possible inside
  the sandbox, so it runs as the user **[I]**, strong. Its output arrives as a developer message, which the model
  would not quote.
- **The sandboxed git reads the user's `~/.gitconfig`** (tested; `USERPROFILE` stays the user's), so a global
  `safe.directory` entry would count inside the sandbox too. None exists today (`git config --get-all
  safe.directory`).
- **What OpenAI recommends for git inside the sandbox:** NOT FOUND. Its pages (windows-sandbox, sandboxing,
  agent-approvals-security) say that git inherits the sandbox's limits and that `.git` is protected; none
  mentions `safe.directory` or who owns the files.

### Not found, or not tried

- How long OpenAI keeps a chat's cache (why "never resume after a pause" is not in the ChatGPT part, SU-Q62).
- Which shell runs a hook command on Windows. The command is written to work from any (`powershell -File` with
  a full path), and it ran in round 3 (session log).
- Whether ChatGPT counts the global rules file (12.3 KB) toward the 32 KiB; the install prints the size.
- None of the ChatGPT models or budget numbers is measured on the user's work (SU-Q61, SU-Q62).

## Gotchas

- One command inside ChatGPT's sandbox, without a chat: `codex.exe sandbox -C <folder> -P :workspace -- cmd /c
  <command>` (`codex.exe` is under `%LOCALAPPDATA%\OpenAI\Codex\bin\<hash>\`). It marks the folder with the
  sandbox's permissions, so use a scratch folder. On `D:` it shows what a project there meets; under the
  user's profile the user has full control and the `git init` breakage does not show.
- A project whose `.git` was made inside ChatGPT's sandbox: rename `.git`, `robocopy <renamed> .git /E`,
  delete the renamed one. No admin rights needed; the copy belongs to the user.
- The gotchas about both tools (`${CLAUDE_SKILL_DIR}`, `stage-close/cleanup.py` under ChatGPT) are in this
  repo's `AGENTS.md`.
