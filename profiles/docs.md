# Documents profile

For projects where the work is research, decisions, paperwork, reports or outgoing text rather than code.
The project's `AGENTS.md` names it (`Profile: docs`); in Claude Code the project's `CLAUDE.md` imports it
(`@~/.claude/setup/profiles/docs.md`), in ChatGPT it is part of the built rules file. The shared rules apply as
well.

- **Every figure and claim cites where it comes from:** the document and page, the transcript and timestamp, or
  the source URL.
- **Inferences are marked [I]** until the user confirms them.
- **Originals are never edited.** Source files stay as received (a read-only `sources/` or `source/` folder).
  Evidence for anyone else is the original page copied unchanged, never a retyped or redrawn document.
- **Outgoing text** (emails, messages, letters, forms, reports others read) is written and checked with the
  `writing-check` skill. The project's own rules, if any, are in `style/writing-rules.md`.
- **Decisions log:** `decisions.md` at the project root, ids `<PREFIX>-Qnn`, newest at the bottom, ids never
  reused.
- **Related projects** are listed in the project's `AGENTS.md` under "Related projects (read, never edited from
  here)": this project reads them and never changes them.
