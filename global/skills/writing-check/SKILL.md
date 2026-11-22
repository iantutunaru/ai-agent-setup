---
name: writing-check
description: Write and check outgoing text before the user sends it - emails, messages, letters, listings, reports, forms. Use when drafting any text other people will read, and before handing it over; runs the dash and banned-word check and the readability audit against the shared and the project's writing rules.
---

# Writing check

Text others will read is drafted here and sent by the user. It should read as if the user wrote it. The shared
rules are `writing-rules.md` beside this file; a project adds its own audience, voice and words in
`style/writing-rules.md` (or the file its `AGENTS.md` (`CLAUDE.md` in a project not yet moved) names under "Where things are" as
**Writing rules**). Merged from two projects' tools (SU-Q27).

## 1. Draft

Load `humanizer-en` (or `humanizer:humanizer`) while writing. Read both rules files first. Russian and Greek are
written natively, never translated sentence by sentence, and the user proofreads them.

## 2. Check

The path in front of each script's name below is this skill's folder. A tool that shows it as a `${...}` name has
not filled it in: put the folder this file is in there.

Run from the project folder (add `--rules <path>` when the project's file is not `style/writing-rules.md`):

    python -I "${CLAUDE_SKILL_DIR}/check_text.py" <files>

Dashes and banned words, from both rules files; HTML tags are ignored. It must report `0 issue(s)`.

    python -I "${CLAUDE_SKILL_DIR}/audit_text.py" <English files>

Targets: no sentence over 25 words, passive voice 10% or less, Flesch Reading Ease 60 or more; legal footers and
signatures are exempt. It is advisory (exit 0), so read its numbers: `--skip-class <name>` drops a project's own
non-prose HTML blocks.

## 3. Read

Read the text against the patterns and structure in both rules files: the checks catch words, not shapes.

Done when `check_text.py` reports 0 issues, every audit target is met or each miss is shown to the user with its
reason, and the read-through found nothing left to fix.
