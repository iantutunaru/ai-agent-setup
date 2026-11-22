# Decisions

The user's decisions about the shared setup (the agent-setup repo, called claude-setup until SU-Q68), `SU-Qnn`,
newest at the bottom, ids never reused. A settled decision stands unless the user reopens it. Entries before
SU-Q68 keep the old name.

**In this public copy** the names of the owner's other projects, PC and user names, folder paths and
account details are replaced by neutral words or placeholders such as `<projects>`. Entries that speak of
those names (SU-Q47, SU-Q130, SU-Q136) describe the owner's private repo, where the names still stand. The
same holds for the records in `docs/sessions/` and `docs/handoffs/`.

## Round 1 to 3 (2026-11-12): the design

- **SU-Q01 Where the shared setup lives.** Anything universal goes to the user level (`~/.claude`), so it is never
  copied. The project level keeps only what must sit in the project folder. The repo holds both: `global/` (linked
  into `~/.claude`) and `template/` (copied into a project).
- **SU-Q02 Which way improvements flow.** This repo is the one source. An improvement found in a project is
  promoted here (`/setup-promote`: Claude copies it in, commits, pushes); other projects pull it (`/setup-sync`).
  No automatic two-way sync.
- **SU-Q03 Hosting.** Git repo `claude-setup`, kept in a folder on the main PC.
- **SU-Q04 Machines.** The user also has a laptop, so the repo is a private GitHub repo from day one.
- **SU-Q05 Existing projects.** The active ones (changed in the last ~3 weeks) are migrated now; dormant ones when
  next opened, through `/setup-sync`.
- **SU-Q06 New projects.** A global `/setup-init` skill: open an empty folder, run it; Claude copies the template,
  runs `git init`, asks 2-3 questions, writes the starter project `CLAUDE.md`.
- **SU-Q07 Plumbing into `~/.claude`.** Windows junctions (no admin needed): `~/.claude/setup` -> this repo,
  `~/.claude/skills` -> `global/skills`. `~/.claude/CLAUDE.md` is one import line,
  `@~/.claude/setup/global/CLAUDE.md`. Edits apply at once, no copy step. A plugin can be added later if cloud
  sessions need the global layer.
- **SU-Q08 Layers of rules.** Three: the global `CLAUDE.md` (universal rules only), two profiles
  (`profiles/code.md`, `profiles/docs.md`) that a project imports with one line, and the project's own `CLAUDE.md`
  with only project-specific content.
- **SU-Q09 Reconciling drift.** Claude merges from a game project (code) and a documents project (documents),
  taking the newest wording of each block; every block where the versions really disagree goes to the user as a
  grilling round.
- **SU-Q10 Global skills.** `stage-close` (one generic version, paths read from the project `CLAUDE.md`),
  `guided-session` (merges `re-session`, `car-session`, `playtest`), the writing tools with the docs profile, and
  `/setup-init`, `/setup-sync`, `/setup-promote`. Project domain skills stay in their projects. Old copies are
  deleted when a project is migrated.
- **SU-Q11 Project template.** Base `.gitignore`, `.gitattributes` with `* text=auto eol=lf` and binary rules, a
  `CLAUDE.md` skeleton (profile import, title, project paragraph, safety rules, "Where things are"); code projects
  get `docs/tickets/README.md` and `docs/decisions/`, document projects a root `decisions.md`. The `PYTHONUTF8` env
  block moves to the global settings. `/setup-sync` only adds missing base lines, never removes. Line endings: LF.
- **SU-Q12 Existing layouts.** Existing projects keep their ticket and decision paths; their "Where things are"
  section tells the generic skills where to look. Only new projects get the standard layout.
- **SU-Q13 Creating the GitHub repo.** Claude prepares the repo locally; the user publishes it with GitHub Desktop
  ("Publish repository", private). Later pushes are plain `git push` through the Git credential manager. No `gh`.
- **SU-Q14 Keeping machines current.** A global SessionStart hook runs `git pull --ff-only` on this repo and prints
  one warning line if it can't (offline, diverged, uncommitted changes). `/setup-sync` also pulls.
- **SU-Q15 Promotion.** `/setup-promote` commits and pushes this repo. The global `CLAUDE.md` tells Claude to
  suggest promotion when it makes a change that is not project-specific, and never to promote without asking.
- **SU-Q16 Global settings.** `global/settings.json` is a fragment merged key by key into `~/.claude/settings.json`
  (env block, the hook, plugins and marketplaces, `autoMode.environment`); machine-specific keys are left alone.
  The stale `autoMode.environment` (which named a game project as the only trusted repo) is rewritten to describe
  the real setup.
- **SU-Q17 Order of work.** (1) This chat: repo, install script, junctions, hook, the reconciliation round, global
  `CLAUDE.md` and profiles. (2) Next chat: the skills. (3) Migrating the 11 active projects, one subagent
  per project, one revertable commit each, approved by the user; nothing pushed to project remotes without asking.
  (4) Laptop: clone, run install.

## Round 4 (2026-11-12): reconciling the drifted blocks

- **SU-Q18 Chat budget.** Plan ~320k, quiet zone past ~250k, hand-over before ~320k (a game project's measured
  median peak ~254k). Plus: never resume a long chat after a pause; a goal is never cut to fit one chat. The
  hand-over goes where the project's `CLAUDE.md` says, by default the ticket's `## Handoff` section, else
  `HANDOFF.md`.
- **SU-Q19 Model choice.** The first game project's tiers go global (Critical: Fable high; Standard: Opus medium;
  Chores: Sonnet medium) with "never switch model mid-chat"; ticket headers name model and effort. The
  2-heavy-chats limit stays in the first game project.
- **SU-Q20 Grilling.** The strong form (every round runs the grilling skill first, also when a hand-over lists the
  questions), and every answer is logged in the decisions file the project's `CLAUDE.md` points to.
- **SU-Q21 Commits.** Claude commits its own finished work in small commits saying what changed and how it was
  checked; the user pushes, unless a project or skill says otherwise (e.g. `/setup-promote`).
- **SU-Q22 Placement.** Global: hard rules, grilling, budget, models, commits, official connectors, secrets,
  Claude never sends, no em/en dashes in anything others read, research labels, research "done" and known gaps,
  shell and files, start-of-chat reading, the promote suggestion. Code profile: roles, modular code, manual test
  steps, visual picks, tickets layout, worktree cleanup and `stage-close`. Docs profile: citations to document and
  page, [I] markers, originals never edited, writing tools, root `decisions.md`, related projects.

## Round 5 (2026-11-12): the skills (Stage 2)

- **SU-Q23 Stage-close details per project.** A short "Stage close" list under the project's "Where things are"
  in its `CLAUDE.md`: ticket index, decision ids, retro place, cleanup command, test commands, push or not, branch
  or main checkout. No separate file.
- **SU-Q24 Cleanup script.** The global `stage-close` ships a generic `cleanup.py` (dry run by default, deletes only
  with `--yes`): merged worktrees and branches, session scratchpads a doc still cites, broken doc links, tickets
  missing from the index. A project with its own script keeps using it.
- **SU-Q25 Guided-session details per project.** In a project file (e.g. `docs/sessions.md`) named under "Where
  things are"; the global `guided-session` skill holds the common protocol.
- **SU-Q26 Failed rows.** A 3-round cap per target in every project. Failed rows go to the user as a fix list with
  recommendations. The fix continues in the same chat while under the quiet zone (~250k), else in a fresh chat
  after a hand-over. A project may require a fresh chat every time (a game project does).
- **SU-Q27 Writing check.** A global `writing-check` skill holds `check_text.py`, `audit_text.py` and the shared
  writing rules. A project's `style/writing-rules.md` keeps only its own additions; the script reads both.
- **SU-Q28 `/setup-sync` is the migration tool.** It pulls this repo, adds the profile import, the "Where things
  are" entries the global skills need and missing base lines, lists project copies of global skills and rules that
  duplicate the global file for deletion, and shows the whole diff before one commit. Stage 3 runs it per project.
- **SU-Q29 `/setup-init` questions.** Profile (code or docs), name and one-paragraph description, id prefix.
  Publishing to GitHub stays the user's step in GitHub Desktop.
- **SU-Q30 Template tickets README.** Only the ticket mechanics (naming, statuses, one ticket per chat, scope,
  roadmap changes, side by side, one source per fact, close, table columns); everything else points at the global
  rules.
- **SU-Q31 Repo name.** The user renamed the GitHub repo to `claude-setup` (2026-11-12); the remote here points at
  `https://github.com/iantutunaru/claude-setup.git`.
- **SU-Q32 Going live.** The skills are committed now. A global skill overrides a project skill of the same name
  (code.claude.com/docs/en/skills, "personal over project"), so `stage-close` stops and asks for `/setup-sync` when
  the project's `CLAUDE.md` has no "Stage close" entry. `guided-session` has a new name, so the old `re-session`,
  `car-session` and `playtest` keep working until Stage 3 deletes them.
- **SU-Q33 Decision prefix.** This repo's ids are `SU-Qnn`, renamed from `CS-Qnn` (2026-11-12) because another
  project already uses `CS-Q` and the global skills cite these ids inside every project. Numbers unchanged;
  commit messages before the rename say `CS-Q`.

## Round 6 (2026-11-12): migrating the active projects (Stage 3)

The survey of all 11 projects raised 46 questions; the user took every recommendation. Each project logs its own
answers in its own decisions log; the ones about this repo and the shared defaults are here.

- **SU-Q34 setup-sync guards.** Step 4 requires a clean tree before `git add --renormalize .` (it stages every
  modified file, so the user's edits would land in the sync commit; found in a documents project). The base
  attribute block goes at the top of `.gitattributes`, because a later `*` line overrides earlier project rules
  (measured in another game project: appended, it turned `*.CT -text` back into text). Before proposing `eol=lf`,
  the survey looks for files a game, device or tool reads byte for byte and asks about them (a game project's data,
  a game modding project's files).
- **SU-Q35 Template base additions.** `*.cmd text eol=crlf` beside `*.bat` (a web app project's setup script) and
  `.vs/` (Visual Studio local state, seen untracked in that project) in the base `.gitignore`.
- **SU-Q36 Shared defaults applied in Stage 3.** Approval: an agent applies without committing, Claude checks the
  diff against the answers, the user sees a summary and the `CLAUDE.md` diff in batches, then one commit per
  project. Chat-size lines with no decision behind them are dropped for the global rule (only a game modding
  project keeps 335k, by its own decision; the first game project's decision already equals the global caps). Old
  "Sonnet for routine, Opus for design" lines give way to the global tiers; existing ticket headers stay. Every
  project `CLAUDE.md` gets the template shape (Safety, Where things are). Project `settings.json` files that only
  set UTF-8 are deleted. Projects with tickets but no stages get no Stage close entry, logged so the next sync does
  not propose it. Done tickets and old decision rows that name the old skills stay as history.

## 2026-11-19: the program's own skills folder

- **SU-Q37 `global/skills/synced/` is gitignored.** A Claude program writes Anthropic's own 13 skills (228 files,
  4.5 MB) into `~/.claude/skills/synced/`, which the junction puts inside this repo; seen 2026-11-19, created
  17:31, its manifest refreshed 20:11 the same day. The folder stays on disk and the program keeps it up to
  date; git does not see it, so the session-start warning stops. Not taken: committing it (it changes at every
  refresh, and the subfolder's name is two long ids, probably the account's and the organisation's) and
  deleting it (the program most likely writes it again). Not known: which program writes it, and whether it
  comes back after a delete. Decided in a chat of the owner's web project (AW-T18, chat 4).

## 2026-11-20: Fable only where it can change the plan

- **SU-Q38 Model choice, reworded (reopens SU-Q19).** Opus at high effort is the default chat, also for planning,
  design rounds with a fixed aim and debugging; Fable at high only where critical thinking can change the plan (a
  round that re-evaluates the approach, reverse engineering, measure-first work with no known method, a problem
  Opus has not solved in three chats), and a ticket that names Fable says why; Sonnet at medium for mechanical
  work. Agents: Opus at medium where a coordinating chat checks every part, Sonnet only where a script checks every
  output, Fable only when the user asks; a batch's size is told first. Rests on the user's measure (Fable costs 5
  to 10 times more of the limits a chat; its advantage is critical thinking) and on two tests in the owner's web
  project, AW-T19: an Opus agent at medium read book pages as strictly as the Fable coordinator (phone, 48
  entries), and an Opus coordinator at high settled 42 of 45 entries as the Fable one did, one difference against
  Fable and two for it (trust). A Sonnet agent read as faithfully but left the cross-entry work (joins,
  missing-source and conflict lines, titles) to the coordinator. Not taken: keeping Fable for every design round
  and plan. Decided in a chat of the owner's web project (AW-T19, chat 5, AW-T19-Q24).

## 2026-11-21: the web design skills

Decided in a chat of the owner's web project (ticket AW-T19, round 13, AW-T19-Q60 to Q69); the rulebook they work
from is `research/web-design/rulebook/` (1,811 entries when they were built, about 330,000 tokens in full; 1,718
entries after the duplicates pass of the same day).

- **SU-Q39 Four web skills, one per moment and one lookup.** `web-look` before a look is drawn (options that say
  which entries they follow and bend; the ideas list on the table), `web-check` when a page part is built or a
  page checked (measured, a verdict per entry, findings with ids), `web-text` when a page's words are written,
  and `web-rulebook`, which answers "is there a rule on X?" and holds the lookup tool the other three call.
  Not taken: three skills each carrying a copy of the tool.
- **SU-Q40 `design-critique` is removed.** Anthropic's generic skill gave opinions with no source, named a Figma
  connector this set-up lacks and linked to a file that is not there. Its frame (first impression, what works,
  findings by effect, feedback matched to the stage) is in `web-check`. Accepted loss: a ready frame for
  critiquing something that is not a web page. Not taken: leaving it (two skills answer "review this design"),
  wrapping it.
- **SU-Q41 The rulebook stays one master copy, asked through `rb.py`.** No skill opens the topic files and no
  compact copy sits in the skills folder (it would fall out of step at every rebuild). `rb.py` reads the master
  and prints titles by use and topic, chosen entries without their provenance lines, a whole topic in parts, a
  word search, the ideas and the taste list; it follows an id that was joined into another entry, and its
  output says how to cite. The citing rules live in the tool's output, not in the four skill files.
- **SU-Q42 Two depths.** Quick: titles of the topics touched plus a word search for the part's nouns (a subject
  is spread over topics), then the full text of the entries that could apply. Full: one Opus agent at medium
  effort per topic reads every entry of its use against the page or the sheets, and the coordinating chat
  checks every finding before it counts (`web-check/full-audit.md`, `web-look/full-set.md`).
- **SU-Q43 `web-check` measures before it judges, and `web-text` ends in `writing-check`.** `measure.js` runs in
  the open page and reports numbers only (text sizes, contrast, characters a line, leading, tap targets,
  headings, images, forms, links, speed); what a number should be is the entry's to say, so the script holds no
  thresholds and no entry ids. Nothing is installed; whether Lighthouse or axe is added is decided after the
  first real audit shows what the script misses. `web-text` stands beside `writing-check` and runs its scripts
  as its last check, so the sentence-level rules stay in one place.

## 2026-11-21: a README for other people, and ChatGPT

- **SU-Q44 Who the repo is for.** The user and friends the user invites to the private repo, some of whom use
  ChatGPT instead of Claude. The README is written for a stranger who knows nothing about the user or the
  projects. The repo stays private (SU-Q04 stands). Not taken: going public, which would first need a licence, a
  pass over the personal details in `HANDOFF.md`, `decisions.md`, `global/settings.json` and `global/CLAUDE.md`,
  and a decision on publishing the book notes; it is a separate decision for later.
- **SU-Q45 Shape of the README.** One README: what this is in a few plain sentences; what you get (rules,
  profiles, skills, template); the skills in four groups (writing, web design, running a project, setup), each
  with a short paragraph (what it does, when it starts by itself, what it needs from the project, one example of
  what to say), the six skills from GitHub described the same way with their source; what it needs that is not
  in the repo (the two plugins); install, day to day, layout; a last section for whoever maintains it (tests,
  decision ids). It says "you" to the reader. Not taken: adding six rows to the old table.
- **SU-Q46 Friends work from their own copy.** The README gives two paths: take one skill (copy its folder), or
  take the whole setup (your own private repo made from this one, the personal parts replaced, then the
  install). The personal parts move into two small files: the lines about the user (imported by the rules file)
  and the auto mode block (merged by `install.ps1` after the shared settings), so a friend replaces two files
  and can still pull later improvements. Not taken: friends working from the user's repo, where a collaborator's
  push changes the rules the user's own Claude loads and the trust settings describe the user's PC.
- **SU-Q47 What friends can see.** `HANDOFF.md` and `decisions.md` stay as they are (project names and the
  setup's history, no project contents). The README tells a friend making a copy to start with an empty
  hand-over and decisions log. Part of the cleanup before any public step (SU-Q44).
- **SU-Q48 Which ChatGPT.** The ChatGPT desktop app and Codex (command line, editor extension), which read skill
  folders from disk (`$HOME/.agents/skills`, a project's `.agents/skills`; learn.chatgpt.com/docs/build-skills,
  read 2026-11-21). Not the chat window on the web or phone: skills there are for Business, Enterprise,
  Healthcare and Edu plans and are added by hand (help.openai.com/en/articles/20001066-skills-in-chatgpt). The
  README says so in one line, and that a writing skill's text can be pasted into a chat.
- **SU-Q49 The whole setup on ChatGPT, in two stages.** Stage 1: the new README and the skills usable from
  ChatGPT through a second install script. Stage 2, its own chat from a hand-over, starting with its own
  question round: the rules as an `AGENTS.md` built by the install script (`AGENTS.md` cannot import a file and
  is capped at 32 KiB; learn.chatgpt.com/docs/agent-configuration/agents-md), the pull at session start, the
  project template, the three setup skills for both tools, and a ChatGPT version of the rules that name Claude
  things (model tiers, the grilling plugin, the chat budget). Not taken: skills only; ChatGPT's own import from
  Claude Code (learn.chatgpt.com/docs/import), a copy made once.
- **SU-Q50 One skills folder for both tools.** The wording is adjusted instead of keeping a converted copy:
  "the project's `CLAUDE.md`" names both files, and a line says what `${CLAUDE_SKILL_DIR}` means where a tool
  does not fill it in. The three setup skills are Claude only until stage 2 and must not start unasked on
  ChatGPT (`agents/openai.yaml`, `policy.allow_implicit_invocation: false`).
- **SU-Q51 Tested before the README says it works.** The user runs a short round in the ChatGPT desktop app on
  this PC (skills listed through the link, `writing-check` runs its script, `web-rulebook` answers with ids,
  `web-check` measures a page in the app's browser). The README marks each skill per tool as tested, not tested
  or not supported.
- **SU-Q52 No drive path in the shared files.** `install.ps1` fills in the projects folder from the machine it
  runs on (the folder the repo sits in), in the personal settings file of SU-Q46; the path leaves the rules file
  and the README. Found on a PC with drives C and D only, where the merged auto mode block named
  the main PC's projects folder (on drive E) as the trusted folder (SU-Q03's path is the other PC's).
- **SU-Q53 The repo keeps its name.** `Claude-Setup`; the README's first lines say it serves both tools.
- **SU-Q54 ChatGPT gets the skills linked one by one.** The ChatGPT install script links each skill folder
  into `$HOME/.agents/skills` instead of linking the whole folder, so ChatGPT sees neither Anthropic's `synced/`
  skills (SU-Q37) nor the three setup skills, and its own skills there stay untouched. After a new skill is
  added the script is run again. The setup skills' "do not start unasked" file (SU-Q50) is written in stage 2,
  when they are ported.
- **SU-Q55 The ChatGPT install runs on the laptop.** Once tried on a scratch folder; it creates
  `~/.agents/skills` with the links and touches nothing else of ChatGPT's.
- **SU-Q56 The two personal files.** `global/personal.md` (the user's background, "Talk to the user in English")
  and `global/settings.personal.json` (the auto mode block, the projects folder filled in by `install.ps1`).
  `~/.claude/CLAUDE.md` becomes two import lines, the shared rules and the personal file. Not taken: importing
  the personal file from inside the rules file, an import nested in another, which this setup has never used.
- **SU-Q57 Stage 4 is done.** The PC with drives C and D is the laptop; the setup is installed on it. Its
  hand-over gives way to the hand-over for ChatGPT stage 2; the open items for the user move across unchanged.
- **SU-Q58 The repo will be renamed (reopens SU-Q53).** To a more neutral name, in a separate chat later. Until
  then the name stays `Claude-Setup` and the files keep saying `claude-setup`.

## 2026-11-21: the whole setup on ChatGPT (stage 2 of SU-Q49), and the new name

One round of eight questions and three follow-ups; the user took every recommendation. What the answers rest on
was read the same day on OpenAI's pages (learn.chatgpt.com/docs: `agent-configuration/agents-md`, `hooks`,
`build-skills`, `models`, `model-selection`, `pricing`, `windows/windows-app`), on Anthropic's
(code.claude.com/docs/en/memory) and in the laptop's own ChatGPT files (`~/.codex/models_cache.json`, the session
log of the test round).

- **SU-Q59 One project file for both tools.** A project's text lives in `AGENTS.md`; its `CLAUDE.md` shrinks to
  two import lines, the profile and `@AGENTS.md` (the pattern Anthropic's page gives for sharing one file with
  other tools). ChatGPT cannot import, so its built rules file carries both profiles and the project's
  `AGENTS.md` names which one applies (`Profile: code` or `Profile: docs`). New projects get both files from
  the template; an existing project moves when `/setup-sync` next runs in it, shown to the user first. Not
  taken: keeping `CLAUDE.md` as the one file and setting ChatGPT to read it (`project_doc_fallback_filenames`),
  which leaves a ChatGPT-only friend with files named after Claude and an install that edits ChatGPT's config.
- **SU-Q60 Shared rules written once.** `global/rules.md` holds what both tools follow; `global/rules-claude.md`
  and `global/rules-chatgpt.md` hold what differs (the grilling skill's name, chat budget, models, shell notes).
  The ChatGPT install builds `~/.codex/AGENTS.md` from the shared rules, the ChatGPT part, `global/personal.md`
  and both profiles. Not taken: a full second copy of the rules for ChatGPT, which drifts.
- **SU-Q61 Models in ChatGPT.** GPT-6.2 Sol at High is the default; GPT-6.2 Astra at High only where critical
  thinking can change the plan, and a ticket that names it says why; GPT-6 Luna at High for mechanical work
  that lint and tests catch. Agents: Sol at Medium where the coordinating chat checks every part, Luna where a
  script checks every output, Astra only when the user asks. A ticket header written for Claude translates:
  Opus to Sol, Fable to Astra, Sonnet to Luna. Rests on OpenAI's pages only (Astra costs 4 times Sol's credits
  per token, Luna a twentieth; "for Luna, start with High"); nothing has measured these models on the user's
  work, and the rules say so.
- **SU-Q62 Chat budget in ChatGPT.** Sol: plan 320k, quiet zone past 250k, as in Claude (its usable context on
  the laptop is 475,000 tokens). Astra: hand-over before about 230k, quiet zone past about 180k, the same
  proportion inside its 258,400. Both are starting values: no ChatGPT chat of the user's has been measured.
  "Never resume a long chat after a pause" rests on Claude's cache pricing and stays out of the ChatGPT part
  until OpenAI's cache lifetime is known (NOT FOUND on its pages). Not taken: no numbers at all.
- **SU-Q63 "The assistant" instead of "Claude".** In the user's own files (rules, profiles, own skills) the one
  doing the work is "the assistant". The six skills taken from GitHub keep their text. Not taken: leaving
  "Claude" and telling ChatGPT in one line that it means ChatGPT there.
- **SU-Q64 The pull at session start in ChatGPT.** `install-chatgpt.ps1` adds a session-start hook to
  `~/.codex/hooks.json`: it pulls the setup repo, warns about uncommitted changes and rebuilds
  `~/.codex/AGENTS.md` when the rules changed. The user trusts the hook once in the app (Settings, Hooks) and
  again if its definition changes. Not taken: no hook, the install rerun by hand after every pull.
- **SU-Q65 Where ChatGPT finds the setup repo.** A link `~/.codex/setup`, as Claude has `~/.claude/setup`; the
  setup skills name both and use the one that exists. Not taken: one neutral link for both tools, a second
  link on every Claude machine.
- **SU-Q66 Setup skills that run in both shells.** The bash-only steps (`cp -rn`, the `grep` pipelines) move
  into one tested Python script, `tools/setup_tools.py`, that both tools call; the `git` lines stay as text.
  Not taken: every command written twice in the skill text.
- **SU-Q67 `global/CLAUDE.md` stays as Claude's entry file (reopens the "not taken" of SU-Q56).** It holds two
  import lines, the shared rules and Claude's part, so `~/.claude/CLAUDE.md` is unchanged, no PC needs a
  reinstall and no chat runs without rules while a PC has pulled but not reinstalled. It is an import inside an
  import; Anthropic's page allows four levels. Checked on the laptop before the push. Not taken: three direct
  import lines in `~/.claude/CLAUDE.md`, where the main PC loads no global rules between its pull and its
  reinstall.
- **SU-Q68 The new name is agent-setup (settles SU-Q58).** It names neither vendor and matches the words both
  tools use on disk (`AGENTS.md`, `~/.agents/skills`). The skill names `/setup-init`, `/setup-sync` and
  `/setup-promote` stay. Not taken: assistant-setup, ai-setup.
- **SU-Q69 The rename is done in the stage 2 chat (reopens SU-Q58's "separate chat").** The name stood 37 times
  in 14 files, 12 of which that chat rewrote anyway. Left for the user, as steps in the hand-over: rename the
  repo on GitHub, rename the folder, then run both install scripts again, because the links into `~/.claude`,
  `~/.agents` and `~/.codex` point at the folder's path.

## 2026-11-21: git inside ChatGPT's sandbox, and the template's repeated sentence

One round of five questions, after the facts were found: `HANDOFF.md`, "ChatGPT's sandbox and git" (tested with
`codex.exe sandbox` on scratch folders; pages read on learn.chatgpt.com/docs: `windows/windows-sandbox`,
`sandboxing`, `agent-approvals-security`, `hooks`; the session and sandbox logs of the round of
`docs/sessions/chatgpt-setup-r2.md`). The user took every recommendation ("Yes to all").

- **SU-Q70 Git in ChatGPT: creating a repo is an approved command.** `global/rules-chatgpt.md` gets a "Git"
  line: a command that creates a repo or its folder (`git init`, `git clone`, `git worktree add`) and every git
  command on the setup repo run as approved commands, which run as the user; on "dubious ownership" the command
  is run again with approval. Step 4 of `setup-init` points at the line. No `safe.directory` entry is added to
  the user's git config, by the install or by the assistant. Rests on: a `.git` made inside the sandbox belongs
  to the sandbox's Windows user, so the user's git refuses the project and on `D:` the sandbox stops working in
  it. Not taken: a line in `setup-init` only, which misses every other `git init` or clone; a `safe.directory`
  step in `install-chatgpt.ps1`, which leaves the sandbox stopped and weakens git's ownership check.
- **SU-Q71 Git on the laptop is updated, and the install warns about an old one.** The user installs the
  current Git for Windows over 2.44.0. `install-chatgpt.ps1` prints a warning when the git on the path is older
  than 2.53. Rests on: the sandbox hands git a `safe.directory` exception for the project folder that Git
  2.44.0 does not accept, while 2.53.0 and 2.56.1 do (all three tested); the lowest version that works is not
  determined, so the warning names the oldest one tested. Not taken: leaving the old git, where every git
  command of a ChatGPT chat fails once and is repeated with an approval.
- **SU-Q72 The session-start hook says when git cannot read the setup repo.** `session-start.ps1` prints one
  warning line in that case, where it was silent, and skips the pull. Not known: whether ChatGPT asks the user
  to trust the hook again after the script's text changes (SU-Q64 covers a changed definition).
- **SU-Q73 The template's `AGENTS.md` files lose the repeated sentence.** "A settled decision stands unless the
  user reopens it" goes from `template/code/AGENTS.md` and `template/docs/AGENTS.md`, because `global/rules.md`
  says it and a new project's first `setup-sync` proposed removing it. The template's decisions files
  (`docs/decisions/README.md`, `decisions.md`) keep it: the sync's check reads the project's file and what it
  imports, and the sentence tells a reader of the log alone how to treat its entries. Not taken: removing it
  from all four files; keeping it everywhere.
- **SU-Q74 A third round in the app.** After the fixes the user runs a short round in ChatGPT
  (`docs/sessions/chatgpt-setup-r3.md`): what the hook prints in a new chat, `setup-init` in a new folder on
  `D:`, and GitHub Desktop opening that project. Until it is run, the fixes are checked by script only.
- **SU-Q75 The game skills become global.** Reopens SU-Q10's "project domain skills stay in their projects" for
  the first game project's eight skills: all eight move to `global/skills/`. The three design skills
  (`design-lenses`, `balance-check`, `playtest-plan`) move first, in the chat that decided it; the five game
  programming skills (`bot-ai`, `sim-patterns`, `unit-movement`, `lockstep-desync`, `frame-budget`) follow in
  their own chats (SU-Q78). Not taken: the three design skills only; the three plus the general parts of
  `bot-ai` and `unit-movement`.
- **SU-Q76 One "Game design" entry carries a project's facts.** The skills read a **Game design** list under
  "Where things are" in the project's `AGENTS.md`, defined once in `research/game-design/README.md`, and stop
  with a pointer to `/setup-sync` when it is missing, as `stage-close` does (SU-Q10, SU-Q12). `setup-sync` writes
  the entry; a project's own copies of these skills are deleted when it gets the entry (a global skill overrides
  a project skill of the same name, SU-Q32). `balance-check` carries `verdict.py`, a standard-library port of the
  first project's win-rate statistics, so its verdict needs no project tool. Not taken: a thin project skill beside
  each global one.
- **SU-Q77 Neutral examples, the books' places in one file.** The `references/` digests keep their book and
  chapter tags; examples naming the first project become neutral ones, and its two real cases stay as worked
  examples without names or ids. Where the books live and how to extract them: `research/game-design/README.md`.
  Not taken: keeping the project's examples as they were.
- **SU-Q78 The game programming skills become engine-neutral.** Each keeps its general method (lockstep rules,
  paths and crowds, bot decisions, data-driven patterns, finding frame time), with engine facts in
  `references/engines/<engine>.md`: `threejs.md` from the first project's measured findings, `unity.md` from
  what has been measured in Unity, saying where nothing has. About 29,000 words across five skills, so one chat
  per skill or two, from tickets in `HANDOFF.md`. Not taken: the method only, dropping the three.js parts;
  copying them with only the names taken out.

## 2026-11-21: a check after the game skills

One round of five questions in a chat that checked the README and the rest against the three new skills; the
user took every recommendation. Found right: the count (19), the README's Game design section, tried table,
install note, layout and tests list, the four test suites, the project's entry (all 13 fields) and its commit.

- **SU-Q79 `HANDOFF.md` is brought to today's state.** Its opening said nothing was pushed and the old name
  stood, while GitHub's `main` held the game skills commit under the new name and the main PC was renamed and
  installed. The opening and "Left" now say what was seen from the main PC; the laptop's rename stays as one
  item, because it could not be seen from there.
- **SU-Q80 A new skill gets a list and a test.** `setup-promote` has a row for a whole new skill and, in step 3,
  the places it changes (the README's count, section, tried table, install note, tests list and layout;
  `README-sources.md`; the entry in `setup-sync`; `HANDOFF.md`; the rerun of `install-chatgpt.ps1`).
  `tools/tests/test_readme.py` fails when the README's count, sections, tried table or tests list do not match
  the skill folders. Not taken: the list alone (nothing catches a chat that forgets); the test alone (it cannot
  check `HANDOFF.md` or the install rerun).
- **SU-Q81 Every field of the Game design entry is read.** The field **Also** was read by no skill; all three
  now read it in step 0, and the field table in `research/game-design/README.md` has its row. The table's
  `design-lenses` row is corrected to Batch only, as its step 0 says. Not taken: dropping the field, which holds
  the first project's worked example and gate (SU-Q77).
- **SU-Q82 The first real use is the trial.** The README's tried row says the general versions have no run on
  record (the first project used their first form). No test chat: the chat that first uses each skill in the
  first project notes how step 0 went and updates the row (`HANDOFF.md`, "Left").
- **SU-Q83 The game skills' origin is in the maintainer's pointers.** One line in
  `global/skills/README-sources.md` (ours, promoted from a project, sources in
  `research/game-design/README.md`) and one in the README's "For whoever maintains it".

## 2026-11-21: one shared repo for the user and friends

The user asked how the user and friends can all work in one repo instead of each in a copy. Facts first, read or
measured that day: the repo is private on the user's personal GitHub account, the user is its only collaborator,
no forks, 121 commits all by the user; the session-start hook pulls `main` in every chat, so whoever can push to
`main` writes rules for every machine; a repo owned by a personal account has no read-only collaborators (every
collaborator can push; GitHub Docs, "Permission levels for a personal account repository"); GitHub's API refused
branch protection on this repo ("Upgrade to GitHub Pro or make this repository public"). Round 1, four questions:

- **SU-Q84 Who shares it.** The user and a couple of friends the user invites, as SU-Q44 describes them. Not a
  wider or unknown group.
- **SU-Q85 One repo, changes by pull request (reopens SU-Q46).** Everyone installs from the same repo; a change
  arrives as a pull request and is merged after someone other than its author has read it. This answers what
  SU-Q46 held against sharing (a collaborator's push changes the rules the user's assistant loads). Not taken:
  everyone pushing to `main`, where an unread change reaches every machine in the next chat; own copies with
  improvements sent back (SU-Q46), where the copies drift.
- **SU-Q86 Everything is shared, with each person's own file on top.** Rules, profiles, skills, template and
  tools are one set for all; what differs per person (language, background, model and chat size preferences)
  sits in that person's own short file. A change to a hard rule needs the group's agreement. Not taken: sharing
  only skills, template and tools, because the skills lean on the rules.
- **SU-Q87 The repo stays private.** SU-Q04 and SU-Q44 stand. Not taken: going public, which needs a licence, a
  pass over the history in `HANDOFF.md` and `decisions.md`, and a decision on the book notes. How "nothing
  reaches `main` unread" is enforced on a private repo is a question of the next round.

Round 2, six questions. Facts read the same day: GitHub Pro adds protected branches, required pull request
reviewers and code owners on private repos; GitHub Team adds the same at $4 per person per month; a free
organization lists none of them (docs.github.com/en/get-started/learning-about-github/githubs-plans and
github.com/pricing, read by a helper agent). Whether a ChatGPT chat follows a git line of its rules file is
untested (round 3 of the ChatGPT setup, SU-Q74).

- **SU-Q88 GitHub enforces the gate.** The user upgraded the personal account to GitHub Pro on 2026-11-21.
  `main` will be a protected branch: no direct push, a pull request with
  one approval. Checked after the upgrade: the API's answer for this repo's branch protection changed from
  "Upgrade to GitHub Pro" (403) to "Branch not protected" (404), so protection is available and not yet set. Not
  taken: agreement only with a local check, where one wrong push by a person or an assistant reaches every
  machine; an organization on GitHub Team, which costs more for nothing three people need.
- **SU-Q89 Who approves.** Any change needs one approval from someone other than its author. A change to the
  files that load in every chat or run on every machine (`global/rules*.md`, `profiles/`,
  `global/settings.json`, `global/hooks/`, both install scripts, `tools/`) waits until everyone has said yes
  (SU-Q86). Not taken: the user approves everything.
- **SU-Q90 Each person's own files live in a folder git ignores.** The repo holds example files; the install
  creates a person's files from them in that clone. Nothing personal enters the shared history from then on.
  The cost: a second PC gets the two small files by hand once. Not taken: `people/<name>/` tracked in the repo
  (everyone reads everyone's account and machine description); a private repo per person. Reopens the place of
  the two personal files in SU-Q56.
- **SU-Q91 The decisions log stays, the user's own hand-over items leave.** `decisions.md` is the shared log:
  rules and skills cite its ids (SU-Q47 on what it shows stands). The user's carried-over items in `HANDOFF.md`
  (other projects, the PCs' paths) move to the user's own ignored folder.
- **SU-Q92 Hand-overs and decision ids with several authors.** One hand-over file per line of work in
  `docs/handoffs/`, deleted when that work is merged, instead of one `HANDOFF.md` every pull request edits. One
  `SU-Q` sequence; the pull request that merges second renumbers its new ids, and a unit test fails on a
  duplicate id.
- **SU-Q93 Every change is made on a branch (reopens SU-Q15).** The assistant commits and pushes the branch,
  never `main`; the person opens the pull request from the link git prints, because a pull request is a message
  to other people and the assistant never sends. `/setup-promote` follows this.

Round 3, seven questions. Read for it: `session-start.sh` leaves silently when the checked-out branch has no
upstream; `install.ps1` makes `~/.claude/skills` one link to the repo's skills folder and moves a person's
existing skills into the repo.

- **SU-Q94 The order: rebuild now, protection on, friends invited straight after.** The user's own order. The
  rebuild is pushed as today; when it is on `main`, protection goes on and applies to the user too; the friends
  are invited at once. The recommendation was to invite the first friend before switching protection on,
  because one required approval with a single collaborator lets nothing merge; the user keeps that window short
  instead. Until a friend has accepted, nothing can be merged, so the rebuild must be complete on `main` first.
- **SU-Q95 A change is made on a branch in the live clone.** The person's own machine runs the change at once
  and tries it in real chats before anyone reads it; while on the branch that machine gets no updates from
  `main`. The session-start hook says in one line when the setup is not on `main`; after the merge the skill
  switches back and pulls. Not taken: a second clone for changes, where a change cannot be tried before it is
  merged.
- **SU-Q96 GitHub runs the tests on every pull request.** The four suites; a failing test blocks the merge. Not
  known until tried: whether they pass on GitHub's Linux machines or need a Windows one.
- **SU-Q97 The history stays.** Old versions of the personal files and of `HANDOFF.md` remain readable to
  invited friends. Not taken: a fresh repo without history. It is part of the cleanup before any public step
  (SU-Q44).
- **SU-Q98 Claude gets one link per skill.** As ChatGPT has (SU-Q54): a person's own skills stay beside the
  links, outside the repo, and `install.ps1` no longer moves them in. The session-start hook refreshes the links
  after a pull. Reopens the one link of SU-Q10's install. To test before building: whether Claude Code reads
  skills through per-skill links.
- **SU-Q99 Which file wins.** The project over the person, the person over the shared rules, and the person only
  on preferences: language, background, which model, chat size. A personal file cannot switch off a hard rule.
- **SU-Q100 Built in fresh chats.** This chat logs the design and writes the hand-over with the build as
  tickets (`docs/handoffs/shared-repo.md`); the build runs in new chats, Opus at high effort.

## 2026-11-21: the personal folder (ticket 1 of the shared repo)

Found out first, in the build chat of ticket 1: Claude Code 2.1.330 (the desktop app's own `claude.exe`, run with
`-p`) skips an `@` import whose file is missing without a word. A project `CLAUDE.md` importing an existing file,
a missing one (a relative path, and once a `~/.claude/setup/...` path) and another existing file loaded both
existing files; no error, no message, exit code 0. Inferred, not tested: `~/.claude/CLAUDE.md` takes the same
path. So a PC that has pulled the change but not rerun `install.ps1` loses the lines about its person silently.
One round, four questions; the user took every recommendation:

- **SU-Q101 A warning while a PC has pulled but not reinstalled.** Claude's session-start hook prints one line
  when `local/personal.md` is missing or `~/.claude/CLAUDE.md` does not import it: run `install.ps1` again and
  fill in `local/`. On ChatGPT the rules file builder, which runs after the pull, creates the file from the
  example and says so. Not taken: no warning, where the only sign is an assistant that no longer knows its user.
- **SU-Q102 An untouched example changes nothing.** The installs do not merge a `local/settings.personal.json`
  that is still the example, and say so; the example `personal.md` reads, unfilled, as "nothing set, the shared
  defaults apply". This keeps the auto mode description a PC already has when the install runs before the
  person's own file is copied in. Not taken: merging the example's placeholders.
- **SU-Q103 A personal file names only what differs from the shared defaults.** The user's own file holds
  language and background; model and chat size stay with the shared defaults in `rules-claude.md` and
  `rules-chatgpt.md`, so a change to the defaults (which waits for everyone's yes, SU-Q89) reaches the user too.
  Not taken: copying today's values into the user's file.
- **SU-Q104 `install-chatgpt.ps1` creates only `local/personal.md`.** ChatGPT never reads
  `settings.personal.json` (it feeds Claude's auto mode); `install.ps1` creates both. Not taken: both installs
  create both files, as the hand-over first worded it.

## 2026-11-21: the build of tickets 2 to 6 (one round before the workers start)

Found out first, in the coordinating chat. Claude Code 2.1.328 (`~/.local/bin/claude.exe`), started with
`CLAUDE_CONFIG_DIR` on a scratch profile whose `skills` folder was a plain folder holding one skill behind a
junction and one in a plain folder, listed both in the `skills` of its start-up record
(`-p --output-format stream-json --verbose`). So SU-Q98 stands. Not tested there: a model loading the linked
skill's text (the scratch profile is not logged in). A code owners file cannot demand every owner: "an approval
from any of the owners is sufficient" (GitHub Docs, "About code owners", read 2026-11-21). The repo allows all
three merge methods, does not delete merged branches and has Actions enabled (GitHub's API, read the same day).
GitHub Pro includes $18 of Actions compute a month for private repos, a Linux minute costs $0.006 (GitHub Docs,
"GitHub Actions billing"). One round, nine questions; the user took every recommendation:

- **SU-Q105 Everyone's yes on a core change is a check GitHub runs.** A script in a workflow keeps a pull
  request that touches the shared core red until every owner named for it in the code owners file, other than
  the author, has approved; as a required check it blocks the merge. If GitHub's side cannot be made to work in
  the trial, the fallback is the checklist line and the user is told. If the check breaks, the user can untick
  it in the repo's settings. Not taken: only a checklist line in the pull request, where "everyone" rests on
  the person who merges; that is agreement, which SU-Q88 did not take.
- **SU-Q106 `.github/` joins the shared core (adds to SU-Q89's list).** The workflows, the code owners file and
  the pull request template decide what gets checked.
- **SU-Q107 The workflows are tried from a branch `ci-trial`.** The assistant pushes that branch, never `main`,
  and deletes it on GitHub after the trial; the user opens and closes one draft pull request from it for the
  check of SU-Q105.
- **SU-Q108 A pull request lands as a merge commit; GitHub deletes the merged branch.** The branch's commits
  stay as written, and plain git can tell that a branch is merged, so the hook can say so and the branch is
  deleted without force. Both are settings on the user's list for ticket 7. Not taken: squash, where git cannot
  tell and the skill would have to ask or need `gh` on every PC.
- **SU-Q109 This repo gets its own `AGENTS.md`** (`Profile: code`) with a two-line `CLAUDE.md`, as the template
  gives. It names `docs/handoffs/`, `decisions.md`, the branch rule, the tests, the scratch-first rule for
  installs and hooks, the lasting gotchas from `HANDOFF.md`, and `local/handoff.md` for a person's own open
  items. Not taken: a pointer in the README only.
- **SU-Q110 ChatGPT's links are refreshed by its hook too (adds to SU-Q98).** Both session-start hooks refresh
  the per-skill links through the same code, because a new skill now arrives through someone else's pull
  request. Proof inside the ChatGPT app joins round 3.
- **SU-Q111 `synced/` moves out of the repo (follows SU-Q37).** `install.ps1` moves the copy in
  `global/skills/synced` to `~/.claude/skills/synced`, where the Claude program writes it once that folder is
  plain. The ignore line stays until both of the user's PCs have run the new install.
- **SU-Q112 A setup change's branch is named `<name>/<topic>`,** the name from git's user name, shown before
  the branch is made. Not taken: `promote/<topic>`, which does not say whose branch it is.
- **SU-Q113 The laptop's steps from `HANDOFF.md` go into `docs/handoffs/shared-repo.md`,** under "For the
  user": ticket 7 waits for the laptop.

## 2026-11-21: the README as a front page (before ticket 7)

Round 1 of a question round on the README and docs, with github.com/mattpocock/skills as the user's example of
a good one. Measured that day: this README is 404 lines on one page; the example's is 258, with its
contributing, glossary, changelog and scope pages in their own files.

- **SU-Q114 The front page is for the invited friend.** The first screen says what this is, what they get and
  how to join; the rest is linked. The friend reads it once, cold, before an assistant can help. Not taken:
  the daily member first, or all three readers at once as before.
- **SU-Q115 "Docs" means the README and the pages it is split into.** Left as they are: `decisions.md`, the
  hand-overs, the session records (evidence, kept as written), `AGENTS.md` and the `SKILL.md` files (written
  for assistants). `global/skills/README-sources.md` and the two `research/` READMEs are a possible second
  step, not part of this change.
- **SU-Q116 The README is split into a front page and side pages.** `README.md`: the pitch, what you get, which
  assistants, the join steps, the skills list, day to day. `CONTRIBUTING.md`: "Working together", the tests,
  the maintainer notes, the layout. `docs/install.md`: what each install script changes on the PC, the second
  PC, undo, one skill. `docs/tried.md`: the full tried table; the README keeps a small status table that links
  to it. `tools/tests/test_readme.py`, step 3 of `setup-promote` and the lines in
  `docs/handoffs/shared-repo.md` that name "the README's last two tried rows" follow the move. Not taken: one
  page restyled, still about 400 lines.
- **SU-Q117 The skills are listed as one table per group:** Skill, What it does, Say. The groups stay (Writing,
  Web design, Game design, Running a project, Setup), each with a two-line intro for what the group shares;
  the name links to the skill's `SKILL.md`. Not taken: the paragraph per skill, whose detail is in each
  `SKILL.md`.
- **SU-Q118 The README gets a "why" part of four short blocks,** each a problem and the rule or skill that
  answers it, two or three lines, linked: copies drift apart; the assistant guesses; the assistant decides or
  sends for you; chats grow too long. No book quotes. Not taken: the single paragraph.
- **SU-Q119 Visual devices taken from the example:** a fold-out per assistant for the install steps; GitHub's
  note boxes for the few things that bite (the invite first, Git 2.53 for ChatGPT, trusting the hook once); a
  tests badge at the top; a banner, the "agent-setup" wordmark as an SVG in the repo in a light and a dark
  form. No emoji in headings. Not known when decided: whether a badge and an SVG from the repo show on a
  private repo's page; both are checked on the branch's page on GitHub before the pull request, and what does
  not show is dropped.
- **SU-Q120 The voice stays plain, addressed to "you",** with shorter sentences and less in brackets. Not
  taken: the example's first person, since the group shares the page and it says only what was tried.

Round 2, the same day:

- **SU-Q121 The banner is a mark, the wordmark and one line.** The mark is one square linked to three smaller
  ones (one copy, many projects); the line is "One set of rules and skills for every project." Chosen from
  three sketches shown in the chat; not taken: the wordmark alone, or the wordmark with the line and no mark.
  The letters are drawn in the reader's own monospace font, so their shape varies from PC to PC; the look is
  checked on the branch's page.
- **SU-Q122 The README's small status table is held to the full table by a test.** One row per skill group and
  for the setup parts, one column per assistant, each cell one of three fixed words: tried, partly tried, not
  tried. Each cell of the full table in `docs/tried.md` starts with one of the three words, and a test fails
  when the small table disagrees. The assistant proposes each word from what the cell records and lists for
  the user the cells the record does not settle. Not taken: a line and a link only; a table kept by hand,
  which can drift.
- **SU-Q123 The git basics stay where the word is first used,** a sentence each: clone in the join steps,
  branch and pull request in `CONTRIBUTING.md`. The recommendation the user agreed to named one exception,
  dropping them if the friends use git daily; the user did not say they do. Not taken: a glossary.
- **SU-Q124 The front page's order:** banner, tests badge, the pitch and what you get; which assistants, with
  the small status table; Join (what you need, the steps in one fold-out per assistant, a link to
  `docs/install.md`); Why; the skills; Day to day, with a link to `CONTRIBUTING.md`; More. The friend has the
  invite already, so joining comes before the reasons. `CONTRIBUTING.md` sits in the repo's root, not in
  `.github/`, which is shared core; `install.md` and `tried.md` sit in `docs/`.
- **SU-Q125 The README test follows each part to its new file and gains a link check:** every link from the
  four pages to a file in the repo points to a file that exists.
- **SU-Q126 A new chat on Opus at high effort writes the pages,** from a hand-over
  `docs/handoffs/readme-front-page.md`. The assistant pushes the branch, the user reads the four pages as
  GitHub shows them, sends notes in the chat and opens the pull request; it merges before ticket 7. Not taken:
  writing it in the question round's chat, which ran on Fable.

Round 3, the same day, on the status words of SU-Q122:

- **SU-Q127 What the three words mean, decided from the cell's own text.** Tried: the cell names a run on that
  assistant and names nothing as still not run. Partly tried: it names a run and also names something not run
  or not seen. Not tried: it names no run on that assistant. "Installed" and "built for it" alone are not
  tried: they say the skill exists, not that it ran.
- **SU-Q128 The two GitHub rows get their own table.** "The tests on GitHub" and "the approvals check and the
  protection of `main`" are about the group's process, not an assistant: in `docs/tried.md` they form a short
  table "On GitHub" with one column. The front page's small table has six rows: the five skill groups, and the
  rules with the session-start hook. Not taken: keeping them in the per-assistant table, where their ChatGPT
  cells would read "not tried" for something that does not depend on the assistant.
- **SU-Q129 Cells that name no run in Claude Code are filled from the projects' histories.** One reading agent
  looks through the user's other projects on this PC for recorded runs of `writing-check`, `humanizer-en`,
  `guided-session` and `stage-close`; each cell then cites what was found, with project and date, and what is
  not found stays "not tried". The web skills count as tried in Claude Code from this repo's own history (the
  commits "what its trial run showed"). Not taken: strict "not tried" without looking; runs recorded from the
  user's memory.
- **SU-Q130 The tried cells name no project of the user's.** A run found in another project is given as the
  number of projects, the dates and the short commit hashes: the user can find each run again from its hash,
  and a friend, who cannot see those repos, learns nothing about them. What the agent of SU-Q129 found, each
  commit and file read afterwards by the chat: `writing-check` tried (three projects, 2026-11-12 to
  2026-11-16, and this repo), `guided-session` tried (one project, 2026-11-14 to 2026-11-16), `stage-close`
  partly tried (only projects' own earlier copies, October 2026), `humanizer-en` not tried. Not taken: names
  where the repo already has them; names everywhere.

Round 4, the same day, in the chat that writes the pages:

- **SU-Q131 The pitch and the four "why" blocks go in as drafted in that chat.** The pitch keeps the facts of
  today's opening (who shares the repo, one copy, Claude Code first, ChatGPT and Codex too); each "why" block
  says what its rule says and links it. Changed later only on the user's notes from reading the branch's page.
- **SU-Q132 The git basics stay** (SU-Q123): the user did not say both friends use git daily, and keeping them
  costs three sentences. Not taken: dropping them for shorter pages.
- **SU-Q133 The comment at the top of `.github/workflows/tests.yml` follows the tests list to
  `CONTRIBUTING.md`, in the same pull request;** the user is the only owner of `.github/` today. The second
  step of SU-Q115 (`global/skills/README-sources.md`, the two `research/` READMEs) is proposed as its own
  session once the branch is pushed. Not taken: a comment that points to the wrong file; noting the second
  step nowhere, so it is lost when the hand-over is deleted.

## 2026-11-22: the sources page and the two research READMEs (SU-Q115, second step)

One question round in the chat that rewrites `global/skills/README-sources.md`, `research/web-design/README.md`
and `research/game-design/README.md` in the front page's voice (SU-Q120), after pull request 3 merged. The user
took every recommendation.

- **SU-Q134 The web design README keeps its record and gains a way in.** Its sections, tables and gap numbers
  stay (the page cites its own gaps, and the research rule keeps a visible known-gaps list), in shorter
  sentences; three or four opening lines say what the folder holds and when you would open it. "The user"
  becomes "the owner"; "Claude" stays where the page records what Claude did. Not taken: voice only, with no
  way in for a cold reader; a rebuild that moves the gaps to their own page.
- **SU-Q135 A dated status stays as written, and a line checked today says what changed since.** The web
  design README's "the skills ... are being built" is followed by where the four web skills are now. Not
  taken: leaving a page that says finished work is still going on.
- **SU-Q136 The research READMEs keep the owner's project names and folder paths** (the owner's web project and its
  AW ids, the books' folders): they say where each fact comes from and where the books are, and the same names
  stand in the other files of `research/web-design/`. SU-Q130 stays about the tried cells. Not taken: neutral words
  on these two pages only.
- **SU-Q137 The sources page gets a heading and parts:** a table of the skills from GitHub (skill, source,
  licence, added, what was left out), the skills looked at and not installed with their reasons, ours
  promoted from a project, and `synced/`. The file keeps its name, which the README, `CONTRIBUTING.md`,
  `setup-promote` and a test use. Not taken: the note as it was.
- **SU-Q138 The sources page names the origin of every skill.** A part "Written for this repo" gives each of
  the other ten skills with the decision id behind it, checked in `decisions.md`; what is not found there is
  marked not found. Not taken: a page that answers "where did it come from" for nine skills of 19.
- **SU-Q139 A book title the banned-word check flags stays.** `check_text.py` flags the first word of
  the title of Gillenwater's CSS3 book in the web design README's book table; the one hit is a known false
  hit, named in the commit message. An allow-list
  for `check_text.py` would be its own change. Not taken: shortening the title, which loses a fact.

## 2026-11-22: `check` reads only what git would track; `/setup-init` asks about games and testing

The user's two fixes, given at the start of the chat. Their report on `check`: in a project with 14 GB of
git-ignored game files it ran over two minutes and gave 595 false `<P>` hits in binary textures. Measured
here, read-only, on a game project (its ignored game folder is 14 GB): the new `check` ends in 0.2
seconds and names no file of that folder.

- **SU-Q140 `check` asks git which files to read.** Tracked files, and untracked files no ignore rule matches
  (`git ls-files --cached --others --exclude-standard`), so an ignored folder is never opened. In a folder that
  is not a repo yet, git answers through an empty scratch git folder with the project as its work tree; tried
  on a scratch folder: the same list, nothing written in the project. Only when git gives no list (not
  installed, or it refuses the folder) does `check` read every folder as before, and it says so in a `note:`
  line. Not taken: a list of folder names to skip, which each project would have to extend; reading
  `.gitignore` in Python, a second reading of git's rules that can differ from git's.
- **SU-Q141 `check` skips binary files by git's own test:** a NUL byte in the first 8000 bytes. Such a file is
  not read further. The cost: a text file saved as UTF-16 counts as binary, and a `<P>` in it is not found; the
  template's files are UTF-8. A text file is read in blocks, never whole. Not taken: a list of binary file
  extensions, which misses every extension not on it.

One question round on `/setup-init`, which reopens SU-Q29 (three questions). The user took every
recommendation.

- **SU-Q142 The two entries are written by a command, from one form each.** `setup_tools.py add-entry
  game-design` and `add-entry guided-sessions --where PLACE` put the entry into `AGENTS.md` under "Where things
  are", before the Stage close list, from the forms in `template/entries/`; an entry that is there is kept. A
  test keeps the Game design form's fields equal to the list in `research/game-design/README.md`. The same
  result in Claude Code and ChatGPT. Not taken: both entries in the code template's `AGENTS.md`, deleted on a
  "no" (a second copy of the field list, and every other project starts by deleting lines); typed by the
  assistant from the definitions each time (a dropped or misnamed field, and nothing to catch it).
- **SU-Q143 A place to test writes the line and a starter `docs/sessions.md`.** The starter has the six parts
  the notes of the six projects that have them share (tools between rounds, before a round, checklists and
  results, writes and undo, safety, overrides), each `none yet`; notes that are there are kept. Not taken: the
  line alone, which names a file that does not exist.
- **SU-Q144 The questions ask little.** "Is it a game, or a mod of one, whose design is decided here?" is yes
  or no. "Where will you test by hand?" takes the game, program or device by name, or "nowhere"; the name goes
  into the entry's line and the notes' first lines. Every field says `none yet` and is filled by the first
  ticket that learns it. Not taken: asking for pillars, fairness band, match length and tools in a folder that
  holds nothing yet.
- **SU-Q145 Only a code project gets the two questions,** in the same single round as the first three, marked
  "only for a code project". All six projects with session notes today are code profile (their profile lines,
  read 2026-11-22). A docs project that later needs rounds gets the entry from `/setup-sync`. A code project
  logs five answers, `<P>-Q01..Q05`. Not taken: both profiles; a second round after the profile is known.
- **SU-Q146 The game skills say what to do on `none yet`.** One sentence in step 0 of `design-lenses`,
  `playtest-plan` and `balance-check`: name the field, say what cannot be done without it, offer to set it now;
  `design-lenses` stops on `Vision: none yet` until the vision file exists, `balance-check` asks for the band on
  `Fairness: none yet`. Before, only `balance-check` covered it, for Batch. The assistant added the matching
  sentence to `guided-session` (a part of the notes that says `none yet` takes the skill's default), as the
  consequence of SU-Q143; it was not a question of the round. Not taken: leaving the skills as they were, with
  entries a new project cannot use on its first day.
- **SU-Q147 `check` passes over text in backticks when it looks for open placeholders.** Measured on the
  same game project: `check` said "1 to fill" for the Playtests field's file name pattern
  `docs/sessions/<ticket>-r<N>.md`; after the change it says "ok". The template's own placeholders are not in
  backticks, and `<P>` is still found by its own search. A fenced block is not passed over. Not taken: asking
  projects to write such patterns without angle brackets.
