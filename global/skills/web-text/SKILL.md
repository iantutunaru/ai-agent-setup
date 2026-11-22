---
name: web-text
description: Write and check the words of a web page against the user's web design rulebook. Use whenever text that will appear on a website is written, changed or translated - headings, button and link labels, menu items, form labels and error messages, listing and product descriptions, page titles, empty states, the wording in an i18n or strings file - also when that text is only a small part of a build task. For emails, letters and other text the user sends, use writing-check instead.
---

# Web text

Text on a page is scanned, not read, by someone in the middle of a task. The rulebook holds about 330 entries on
what such text says and how it is put; this skill loads them before the words are written and checks the words
against them after.

The rulebook is asked through one tool (the `web-rulebook` skill explains its marks):

    RB:  python -I "${CLAUDE_SKILL_DIR}/../web-rulebook/rb.py"

The path in front of the script's name is this skill's folder. A tool that shows it as a `${...}` name has not
filled it in: put the folder this file is in there.

## 1. Frame

- **What text:** which page and which parts of it (heading, labels, errors, a description), and what the
  visitor is doing when they meet it.
- **Languages.** Each language is written natively, never translated sentence by sentence; the user proofreads
  the languages the assistant does not write for them every day.
- **The project's words:** its writing rules (its `AGENTS.md`, or `CLAUDE.md` where not yet moved, "Where things
  are"), and the names it already uses on the site for the same things. Find them in its text files before
  coining a new one.

## 2. Load the entries

- **One label or one sentence:** `RB find <word> --use text` for its nouns (button, error, link, price, date).
- **A part of a page or more** (a form, a dialog, a strings file): `RB titles text all`. It is written to a
  file; read every title (about 330), then run `RB find` for the nouns as well.
- **A whole page's words, or a page that is mostly text:** also `RB topic text content`, every `text` entry of
  the content topic in full.

Words depend on where they stand: for labels, errors and buttons also run `RB find <word> --use check` for
the same nouns, which reaches the entries on required marks, on where a message sits and on what a button is.

Then `RB show <ids>` for every entry whose title could bear on this text. Pick widely.

## 3. Write

Write to the entries shown. Two limits come from the rulebook's own marks:

- A **persuasion** entry is used only as far as the page's facts carry it: a real deadline, a real count, a
  real customer. Where the fact is missing, the entry does not apply; ask the user for the fact.
- A **practice** may be bent for the project's voice, a settled pick or a writing rule of the project or the
  shared list (no dashes, for one); a **rule** is bent only on the user's explicit decision.

## 4. Check

1. Give every entry shown in step 2 one line, judged by the statement's own words: **met**, **bent** (why, and
   what it costs the reader), **missing** (the entry asks for text nobody asked for, such as the line a visitor
   sees after sending: offer it under "For you to check"), or **does not apply** (also when only a general
   principle connects the entry to this text). A Conflict line is passed on with an entry that is bent or that
   decided a word; a met entry is listed without it.
2. Run the `writing-check` skill's two scripts and its read-through on the text as plain text, also when it
   lives inside a code file. The audit's sentence-length target is for prose: on labels and short messages a
   miss is reported with that reason.
3. Read each piece once more where it will stand: a label beside its field, a heading above its text, a link
   out of its sentence. Words that only work with their neighbours are a finding.

## 5. Hand over

```markdown
<the text, per language, each piece named by where it goes>

**Entries behind it:** content-000 (rule), forms-000 (practice), ...
**Bent:** navigation-000 (practice): <why, and what it costs the reader>
**Missing:** forms-000 (practice): <the text the entry asks for that was not in the request>
**Does not apply:** <ids>
**For you to check:** <the languages to proofread; facts asked for and not yet given; the lines offered for
what is missing>
```

(The ids here are placeholders; cite only ids that `RB show` printed in this chat.)

Done when every entry shown stands in exactly one of "Entries behind it", "Bent", "Missing" and "Does not
apply", every id
cited was printed in full by `RB show` in this chat, the
`writing-check` scripts report no issue or each miss is shown with its reason, and every language named in the
frame is written.
