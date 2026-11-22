---
name: setup-init
description: Start a new project from the agent-setup template - three questions (five for a code project), the template files, a starter AGENTS.md and CLAUDE.md, git init and the first commit. Run it in the new, empty project folder.
disable-model-invocation: true
---

# Set up a new project

Works in Claude Code and in ChatGPT (the desktop app, Codex). `<setup>` below is the agent-setup repo's link:
`$HOME/.claude/setup` in Claude Code, `$HOME/.codex/setup` in ChatGPT; use the one that exists. The commands run
as written in bash and in PowerShell. Decisions behind this skill: SU-Q06, SU-Q11, SU-Q29, SU-Q59, SU-Q66, SU-Q70,
SU-Q142 to SU-Q145.

    TOOLS:  python "<setup>/tools/setup_tools.py"

## 1. Check the folder

`TOOLS repo-state` (in ChatGPT, with approval, as the pull): on `main`, `git -C "<setup>" pull --ff-only`, and if
it fails, show its line and go on with the files on disk; on a branch, no pull: say so in one line and go on with
the setup as it is (SU-Q95). The project
folder (the current one) is not a git repo and holds nothing, or only files the user put there; list those, they
stay untouched.

## 2. Ask

One grilling round (run the grilling skill first), a recommendation for each:

1. **Profile:** code (the assistant builds software, mods or tools) or docs (research, decisions, paperwork,
   outgoing text). Recommend from the folder name and any files in it.
2. **Name and description:** the project's name and one paragraph: what it is for, who uses the result, what
   "done" looks like. Ask in the same question what must never be sent, changed or committed (the Safety section).
3. **Id prefix:** 2-3 capitals for ticket and decision ids (`XY-T01`, `XY-Q01`). Recommend one no other project
   uses. The other projects are the sibling folders; `TOOLS prefixes` lists the prefixes they use.

Two more in the same round, each marked "only for a code project" and recommended from the folder's name and
files:

4. **Game:** is the project a game, or a mod of one, whose design is decided here (mechanics, balance,
   playtests)? Yes or no.
5. **Testing:** where will the user test by hand: the game, program or device, by name, or nowhere?

## 3. Write

1. `TOOLS copy-template <profile>` copies the template's base and profile files into the folder, hidden files
   included, and never overwrites a file that exists. The project then has `AGENTS.md` (the project's text, with
   its `Profile:` line) and `CLAUDE.md` (two import lines, so Claude Code loads the profile and `AGENTS.md`);
   both stay, whichever tool the user works in.
2. `TOOLS fill-prefix <PREFIX>` replaces `<P>` in every copied file. Fill every other placeholder in `AGENTS.md`
   and the decisions log by hand: name, paragraph, Safety section, dates. A value nobody knows yet is written as
   `none yet` (e.g. the test command; the first ticket sets it). The ticket-file skeleton in
   `docs/tickets/README.md` keeps its placeholders: it is the form for new tickets.
3. A code project, from questions 4 and 5:
   - A game: `TOOLS add-entry game-design` adds the **Game design** list to `AGENTS.md`.
   - A place to test: `TOOLS add-entry guided-sessions --where "<the place>"` adds the **Guided sessions** line
     and writes `docs/sessions.md`.

   Every field and part is written as `none yet`. Replace one only with what the user's answers said; the first
   ticket that learns the rest fills it in.
4. Log the answers as `<P>-Q01..Q03` in `decisions.md` (docs), or `<P>-Q01..Q05` in `docs/decisions/process.md`
   (code); a "no" and a "nowhere" are logged too.
5. `git init -b main`, add everything, commit `Project skeleton from the agent-setup template`. In ChatGPT ask
   approval for the `git init` (the "Git" line of its rules): made inside the sandbox, `.git` belongs to another
   Windows user and the user's own git refuses the project (SU-Q70).

## 4. Hand over

Tell the user, as numbered steps: publish the repo in GitHub Desktop (File, Add local repository, then Publish
repository, private: SU-Q13); then open the first chat (a code project: write ticket `<P>-T01` first).

Done when `git log` shows the one commit and `TOOLS check` ends with `ok: nothing left to fill` (it lists every
placeholder still open in `AGENTS.md` and the decisions log, and every file that still holds `<P>`; it reads only
text files git does not ignore).
