# Hand-over: one shared repo for the user and friends

The design is settled in three rounds on 2026-11-21: SU-Q84 to SU-Q100 in `decisions.md` (read that section
first; it holds the reasons and what was not taken), with SU-Q101 to SU-Q104 from ticket 1 and SU-Q105 to
SU-Q113 from the round before tickets 2 to 6. Tickets 1 to 6 are built; ticket 7 is the user's own. This file is the first of the per-work
hand-overs SU-Q92 asks for; the other open work has its own files beside it in `docs/handoffs/` since ticket 4.

**Model:** Opus, high effort. **Load:** medium (scripts, tests on scratch folders, two PCs).

## What is left, in order

1. **The user pushes `main`** from the main PC: six commits (the log of SU-Q105 to SU-Q113, then tickets 2, 3,
   5, 4 and 6). The push starts the tests on GitHub for `main` for the first time. It is the last push to
   `main` that works once ticket 7 is done.
2. **The laptop** ("For the user: the laptop" below): rename, pull, the two personal files, both installs.
3. **Round 3 in ChatGPT** (`docs/handoffs/chatgpt-round3.md`), which now also shows whether ChatGPT's hook can
   make the skill links and start Python.
4. **Ticket 7**, when both PCs run from `main`: the settings below, the invites, the first friend's pull
   request. The chat that records that trial updates the table "On GitHub" in `docs/tried.md` and the line in "For
   whoever maintains it" in `CONTRIBUTING.md` that links this file, then deletes this file (SU-Q92).

What the tests of tickets 2 to 6 left unknown is listed under "Not known" and in each "Built in ticket" part
below: an approval by a second person turning `core-approvals` green; the pull request link in
`/setup-promote`'s output against GitHub; the new hook lines in a real chat; everything inside the ChatGPT app;
whether the Claude program writes into the plain `~/.claude/skills/synced`; the laptop's upgrade from the old
single link.

## What is settled

- One private repo for the user and a couple of friends; everyone installs from it (SU-Q84, SU-Q85, SU-Q87).
- A change arrives as a pull request. One approval from someone other than its author; a change to the files
  every chat loads or every machine runs waits for everyone's yes (SU-Q89). GitHub enforces it: `main` protected,
  the user included (SU-Q88, SU-Q94).
- Rules, profiles, skills, template and tools are one set. Each person's own files live in a folder of the clone
  that git ignores; a personal file wins over the shared rules on preferences only (SU-Q86, SU-Q90, SU-Q99).
- Every change is made on a branch in the live clone; the assistant pushes the branch, the person opens the pull
  request (SU-Q93, SU-Q95).
- `decisions.md` stays, with its history; hand-overs become one file per line of work (SU-Q91, SU-Q92, SU-Q97).
- Claude gets one link per skill, so a person's own skills stay outside the repo (SU-Q98).
- GitHub runs the tests on every pull request (SU-Q96).
- The order: rebuild, protection on, friends invited straight after (SU-Q94).

## Facts, with how far each was checked

Measured or read in the design chat on 2026-11-21:

- The repo is private, on the user's personal account, one collaborator, no forks (`gh repo view`, the
  collaborators API). **[V]**
- The account is on GitHub Pro. After the upgrade the branch protection
  API for `main` answers "Branch not protected" (404); before it answered "Upgrade to GitHub Pro" (403). So
  protection is available and not set. **[V]**
- A repo owned by a personal account has two permission levels, owner and collaborator, and "Collaborators can't
  have read-only access" (GitHub Docs, "Permission levels for a personal account repository"). So every invited
  friend can push branches; only protection keeps them off `main`. **[V]**, read by a helper agent.
- GitHub Pro lists "Required pull request reviewers", "Protected branches" and "Code owners" for private repos
  (docs.github.com/en/get-started/learning-about-github/githubs-plans). **[V]**, read by a helper agent.

Measured in the ticket 1 chat on 2026-11-21 (SU-Q101 to SU-Q104):

- Claude Code 2.1.330 skips an `@` import whose file is missing without a word; the other imports load. Tested
  with `claude.exe -p` on a project `CLAUDE.md`, relative and `~/` paths. **[V]**; for `~/.claude/CLAUDE.md`
  **[I]**, the same import code. A project `CLAUDE.md` in a folder under `%TEMP%` was not loaded at all in that
  test, so such tests run in a folder outside it.
- A PC on the old setup, pulling ticket 1 through its own (old) session-start hook, measured on a scratch clone:
  the pull goes through while the hook runs; `global/personal.md` and `global/settings.personal.json` leave the
  folder; `~/.claude/CLAUDE.md` still imports the old path, so the first chat after the pull has no lines about
  the user and no warning. From the next chat the new hook prints its one line (SU-Q101). ChatGPT's builder
  makes `local/personal.md` from the example and says so. `install.ps1` run again before the person's files are
  copied keeps the auto mode description the PC had (SU-Q102); after the copy and one more run the hook is
  quiet. **[V]**
- The personal files are read from `local/` by `install.ps1`, `global/hooks/build-agents-md.ps1` (through
  `global/hooks/local-files.ps1`) and checked by `session-start.sh`; `tools/tests/test_personal_files.py` fails
  when a current file names the old places. **[V]**

Found out in the coordinating chat of tickets 2 to 6 on 2026-11-21 (SU-Q105 to SU-Q113):

- Claude Code 2.1.328 lists a skill that sits behind a junction inside a plain `skills` folder, beside one in a
  plain folder (a scratch profile through `CLAUDE_CONFIG_DIR`, the `skills` of the start-up record of
  `claude.exe -p --output-format stream-json --verbose`). **[V]** for the listing; a model loading the linked
  skill's text was not tested there.
- A code owners file cannot demand every owner: "an approval from any of the owners is sufficient" (GitHub
  Docs, "About code owners"). **[V]** So everyone's yes is a check of its own (SU-Q105).
- The repo allows merge, squash and rebase, does not delete merged branches, and has Actions enabled (GitHub's
  API). GitHub Pro includes $18 of Actions compute a month for private repos; a Linux minute costs $0.006
  (GitHub Docs, "GitHub Actions billing"). **[V]**

Built and measured in ticket 2 on 2026-11-21 (SU-Q98, SU-Q110, SU-Q111):

- `~/.claude/skills` is a plain folder with one junction per skill beside a person's own skills;
  `global/hooks/skill-links.ps1` does the linking for both installs and both session-start hooks. Tried on
  scratch profiles by the worker (a fresh profile; an old single link; a person's own skill and a folder with a
  repo skill's name; a skill added and then removed through a pull, for both hooks) and again by the
  coordinator (an old single link with a `synced` folder: the link replaced, `synced` moved, the 19 skills in
  Claude Code 2.1.328's start-up record, the hook silent afterwards). `tools/tests/test_skill_links.py` repeats
  these on temporary folders; it needs PowerShell and junctions and is skipped off Windows. **[V]**
- Run on the main PC's real profile: `install.ps1` replaced the single link, moved `synced` (228 files) to
  `~/.claude/skills/synced` and linked 19 skills; `install-chatgpt.ps1` found its 19 links in place. A new
  `claude -p` chat there listed the 19 skills and loaded `plain-language` through its link (the Skill tool
  returned its text). Both hooks, run by hand afterwards, printed nothing about links. **[V]**
- A PC still on the old single link (the laptop, until its install runs again) keeps working; its Claude hook
  says so in one line in every chat and changes nothing. **[V]** on a scratch profile.

Built and measured in ticket 3 on 2026-11-21 (SU-Q93, SU-Q95, SU-Q108, SU-Q112):

- `tools/setup_tools.py` has the branch steps as commands (`branch-name`, `repo-state`, `start-branch`,
  `push-branch`, `switch-back`); `/setup-promote` uses them and never pushes `main`; both session-start hooks
  pull only on `main` and otherwise print one line (the branch; "merged" once its tip is in `origin/main`; "could
  not be checked" when the fetch fails; detached). Walked on scratch repos by the worker and again by the
  coordinator: branch, push to a bare remote, the hook's line, a `--no-ff` merge pushed from a second clone, the
  "merged" line, a refused push, switch back, branch gone, hook silent. `tools/tests/test_branch_workflow.py`
  repeats it (30 tests, 5 of them need Windows). **[V]**
- Merged is read from git alone: the branch's last commit is in `origin/main` and not on main's first-parent
  line. That holds for merge commits (SU-Q108); a squash or rebase merge would read as "not merged" or "no
  commits", so the repo's merge setting on the user's list matters.
- Not seen: the pull request link in `push-branch`'s output. A bare remote prints none. GitHub prints
  `remote: Create a pull request for '<branch>' on GitHub by visiting:` and the URL on the next line (seen on
  the `ci-trial` push); whether `push-branch` picks it up shows at the first real `/setup-promote`.
- Not run: a real chat in either app with the new hook lines; whether Python starts inside ChatGPT's hook (if
  not, the hook prints its fallback line).

Built in ticket 5 and tried on GitHub on 2026-11-21, from the branch `ci-trial` and the user's draft pull
request 1, both gone again (SU-Q96, SU-Q105 to SU-Q107):

- `.github/workflows/tests.yml` runs the four suites on every push and pull request, as the checks
  `tests (ubuntu-latest)` and `tests (windows-latest)`. Both pass: Linux runs the 76 tools tests of that day
  with the 20 that need PowerShell and junctions skipped, Windows runs all of them. One test of ticket 2 had to
  change for GitHub's Windows machine, whose temp folder comes in its short 8.3 form. **[V]**
- `.github/workflows/core-approvals.yml` runs `tools/core_approvals.py`, which sets the commit status
  `core-approvals` on the pull request's last commit. Seen on the draft pull request: failure, "waiting for a
  yes on the current commit from" a made-up second owner; success after the commit that removed that owner
  ("the author is its only owner"); and a new run with a new status when the user submitted a comment review
  (`pull_request_review`), from the branch's own workflow file while `main` had none. **[V]**
- GitHub started the pull request's runs about 90 seconds after the second push; the run for the push itself
  started at once. **[V]**, one observation.
- Not seen, because it needs a second person with write access: an approval turning the status from failure to
  success. The first friend's first pull request shows it (ticket 7).
- A limit, **[I]** from GitHub's docs by the ticket 5 worker: a pull request that edits the check's own
  workflow or script is judged by its edited form. The check stops a merge by oversight, not a collaborator who
  works around it; GitHub's own rule (one approval from a code owner) applies on top.

Built in ticket 4 on 2026-11-21 (SU-Q91, SU-Q92, SU-Q109, SU-Q113):

- `HANDOFF.md` is gone. Its open work is in `docs/handoffs/game-programming-skills.md` and
  `docs/handoffs/chatgpt-round3.md`, the laptop's steps are below, the lasting gotchas are in the repo's new
  `AGENTS.md` (`Profile: code`, with a two-line `CLAUDE.md`), and the user's own carried-over items are in
  `local/handoff.md` on the main PC, which git ignores. The coordinator checked that none of those items is in
  a tracked file and that the facts of the old file are in the new ones (by search for a sample of them).
- `tools/tests/test_decision_ids.py` fails on a duplicate `SU-Q` id; `decisions.md` holds SU-Q01 to SU-Q113,
  each once. **[V]**
- A new `claude -p` chat started in this repo named `local/handoff.md` and the code profile from its loaded
  instructions, without opening a file: Claude Code loads the root `CLAUDE.md` and `AGENTS.md`. **[V]** Not
  seen: ChatGPT loading the root `AGENTS.md`.
- Ticket 6 (SU-Q85): the README is written for a group ("Join", "Working together"; since SU-Q116 the second is
  in `CONTRIBUTING.md`); its tried table (now `docs/tried.md`, table "On GitHub") has a row
  for the tests on GitHub and one for the approvals check and the protection of `main`, saying what the trial
  showed and what is not set or not tried. `tools/tests/test_readme.py` checks the two new sections.

Not known; find out before building on it:

- Whether a ChatGPT chat follows a git line of its rules file (round 3 of the ChatGPT setup, still open). With
  protection on, a wrong push to `main` is refused by GitHub either way.
- Whether ChatGPT's hook can make junctions inside the app. Run by hand as the user it does; whether the app
  runs it as the user is still **[I]** (round 3). If it cannot, it prints one line and the chat goes on.
- Whether Claude Code offers a skill that its hook linked at the start of that same chat, or only from the next.
- Whether the Claude program now writes Anthropic's skills into the plain `~/.claude/skills/synced` (SU-Q111
  assumes it). To see: the folder's dates on the main PC after the program's next refresh, and that
  `global/skills/synced` does not come back.

## The tickets, in order

Each is one chat unless it turns out small. Each ends with its tests, the README lines it changed, a commit, and
this file updated (a done ticket is struck from the list, not kept as history). Until ticket 7 the work is pushed
to `main` as today.

7. **Protection on, friends in** (SU-Q94, the user's steps). When tickets 1 to 6 are on `main` and both of the
   user's PCs run from it: switch protection on (the list below), invite the friends (the repo's Settings,
   Collaborators). Until one has accepted, nothing can be merged. The first pull request by a friend is the
   trial: record how it went here and in the table "On GitHub" in `docs/tried.md`.

## The settings for ticket 7, for the user to click

Nothing here is set yet. The names are GitHub's own, as its docs gave them on 2026-11-21 (read by the ticket 5
worker); the page may word one differently.

**The branch rule.** The repo's Settings, Branches, "Add classic branch protection rule", branch name pattern
`main`. Tick:

- "Require a pull request before merging", and inside it "Require approvals" with 1, "Dismiss stale pull request
  approvals when new commits are pushed" and "Require review from Code Owners".
- "Require status checks to pass before merging", and add these three by searching for them:
  `tests (ubuntu-latest)`, `tests (windows-latest)`, `core-approvals`. GitHub offers a check only after it has
  reported recently; after the trial of 2026-11-21 all three have. Leave "Require branches to be up to date
  before merging" off.
- "Do not allow bypassing the above settings", so the rule holds for the user too (SU-Q88).
- Leave "Allow force pushes", "Allow deletions" and "Require linear history" off (linear history would refuse
  merge commits).

**How a pull request lands** (SU-Q108). Settings, General, "Pull Requests": "Allow merge commits" on, squash
merging and rebase merging off, "Automatically delete head branches" on. The hooks and `/setup-promote` read
"merged" from a merge commit; with squash or rebase they would not see it.

**The first friend.** A friend is named in `.github/CODEOWNERS` only after accepting the invite (a line naming
someone without write access is invalid). Their first pull request adds their login to every line of that file,
and the user approves it. Until then the user is the only code owner and cannot approve their own change, so a
core change by the user cannot be merged. That first pull request is also the first time an approval can be seen
turning `core-approvals` green.

**The same as commands, not run and not tested.** With the three checks and the rule above in a file
`protection.json` (`required_status_checks` with `strict: false` and the three contexts, `enforce_admins: true`,
`required_pull_request_reviews` with `dismiss_stale_reviews`, `require_code_owner_reviews` and
`required_approving_review_count: 1`, `restrictions: null`, `allow_force_pushes: false`,
`allow_deletions: false`):
`gh api --method PUT repos/iantutunaru/agent-setup/branches/main/protection --input protection.json`, and
`gh api --method PATCH repos/iantutunaru/agent-setup -F allow_merge_commit=true -F allow_squash_merge=false
-F allow_rebase_merge=false -F delete_branch_on_merge=true`.

## For the user: the laptop

Ticket 7 waits for the laptop (SU-Q113). Not seen from the main PC: whether the laptop's folder is renamed
already and its remote re-pointed (the GitHub repo and the main PC are renamed). Skip a step that is done. In
this order, on the laptop:

1. **Rename the folder.** Close every Claude and ChatGPT chat that works in the folder, then rename the folder
   (`D:\<projects>\claude-setup`) to `agent-setup`.
2. **Point it at the renamed repo.** In the folder:
   `git remote set-url origin https://github.com/iantutunaru/agent-setup.git`.
3. **Pull.** In the folder, on `main` with nothing uncommitted (`git status`): `git pull --ff-only`. The links in
   `~/.claude` and `~/.codex` still name the old folder until step 5, so the session-start hooks cannot pull for
   it.
4. **Copy the two personal files by hand, once** (SU-Q90). Copy `personal.md` and `settings.personal.json` from
   the main PC's `local\` folder of the clone into a `local\` folder in the laptop's clone (make the folder). The
   same two files serve both PCs: the install fills in each PC's projects folder.
5. **Run both installs** from the folder: `install.ps1`, then `install-chatgpt.ps1`. They re-point the links to
   the renamed folder (SU-Q69); `install.ps1` replaces the old single skills link with one link per skill
   (SU-Q98) and merges the personal settings; `install-chatgpt.ps1` links the skills for ChatGPT, the three game
   design skills among them, and rebuilds its rules file.
6. **Restart the ChatGPT app**, and trust the hook if it asks. The hook's entry in `~/.codex/hooks.json` names
   the script through `~/.codex/setup`, so the rename does not change it. Not known: whether ChatGPT asks for
   trust again anyway.

Do steps 1 to 5 in one sitting. From the rename until the installs have run, `~/.claude/setup`, `~/.codex/setup`
and the skill links name a folder that is gone: a Claude chat there gets no shared rules (Claude Code skips the
missing import without a word, ticket 1), no repo skills and no hook. That is read from the scripts and the
settings, not tried. Without the rename, a laptop that has pulled but not run the installs gets one line in every
Claude chat asking for the install (the old single skills link) and, from the second chat after the pull, one
saying the personal file is not set up.

On the laptop, Git for Windows' default `core.autocrlf=true` writes CRLF wherever a project has no `eol` rule.

## Gotchas

- The live clone is the setup: a half-built ticket on `main` breaks the next chat on that PC. Build and
  try on a scratch folder, and run the install on the real profile only when the scratch run passed.
- Remove a junction with `cmd /c rmdir <link>`; never `Remove-Item -Recurse` on a folder that holds junctions
  (the repo's `AGENTS.md`, "Gotchas", lists the others that still apply).
- `git push` to `main` works until ticket 7 and is refused after it, for the user too.
- The commits of tickets 2 to 6 sit on the main PC's `main` until the user pushes them.
