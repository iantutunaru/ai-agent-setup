---
name: web-check
description: Build and check web pages against the user's web design rulebook, by measurement instead of by eye. Use before and after building or changing any page part (a form, card, menu, filter, listing, header), and whenever a page, component, mock-up or screenshot is to be checked, reviewed, critiqued or audited - "check this page", "review this design", "what do you think of this screen", an audit ticket. Findings carry the rulebook entry's id, the number measured and a fix.
---

# Web check

A finding here rests on two things that can be shown: a number read from the page, and a rulebook entry read in
this chat. Eye and memory supply neither, so the order is fixed: frame, measure, load the entries, give each a
verdict, report.

The rulebook is asked through one tool (the `web-rulebook` skill explains its marks):

    RB:  python -I "${CLAUDE_SKILL_DIR}/../web-rulebook/rb.py"

The path in front of the script's name is this skill's folder. A tool that shows it as a `${...}` name has not
filled it in: put the folder this file is in there.

## 1. Frame

Settle these before anything is opened, and put them at the top of the report:

- **What is checked:** which pages or which part, at which widths (phone 375 and PC 1280 unless the project
  names others), in which languages, and in which states: a form also has the state after a refusal and the
  state after sending, a menu its open state. Open each state and look; the script measures only what is on
  screen.
- **Its state:** a running page, a mock-up or screenshot, or a part not built yet.
- **The stage:** exploration (is the direction right), refinement (what is wrong), final (what is left). It
  decides which findings are worth the user's time: a rough sketch gets no list of polish. Where the user names
  none, take refinement (a first build is one) and say so.
- **Picks and limits:** the settled picks of the project the page belongs to (the brand or design file its
  `AGENTS.md` (`CLAUDE.md` in a project not yet moved) names under "Where things are"), and the limits the task itself sets ("no
  script yet", "one file"). Both stand; step 4 says what to do when an entry speaks against one.
- **The depth:** *quick* for one part, one change, one screen; *full* for the audit of a whole page or stage,
  or when a ticket says audit. Full runs one agent per topic: read [full-audit.md](full-audit.md) now and
  follow it from step 3 on.

**A part not built yet:** do step 3 first. The entries it loads are the part's requirements: build to them and
name them to the user by id. Where two of them pull apart, build to the rule, else to the project's pick,
else to the one a current source confirms, and give the other side in the report. Then run steps 2, 4 and 5
on the result. A fault step 4 finds in the fresh build is fixed, and the report's "Built" line says so.

## 2. Measure

For a running page, with a browser tool:

1. Open the page, set the first width with the browser's resize tool, and reload.
2. Read `${CLAUDE_SKILL_DIR}/measure.js` and pass its whole text to the browser's JavaScript tool. The result is
   one JSON object: page, text, contrast, lines, tap, headings, images, forms, links, speed, and `notMeasured`.
   For one part of a page, put `window.WEB_CHECK_ROOT = "<css selector>";` on a line before the script.
3. For every further width: resize, reload, and run `eval(sessionStorage.getItem('webCheckMeasure'))`. It
   returns a promise: the JavaScript tool waits for it by itself, but inside a larger snippet write
   `await eval(...)`, or the result is an empty object.
4. An `error` about a window with no size means the browser pane is hidden: set a size, reload, run again.
5. The file is 21 KB, about 6,000 tokens each time it passes through the chat. To keep it and its results out
   of the chat, start `python -I "${CLAUDE_SKILL_DIR}/receiver.py" <folder>`: it serves the file on
   127.0.0.1:8765 without caching and saves what the page posts to `/save/<name>` into the folder. Load the
   file with a script element (`s = document.createElement('script'); s.src =
   'http://127.0.0.1:8765/measure.js'; document.head.appendChild(s)`, waiting for its `onload`), run
   `r = await eval(sessionStorage.getItem('webCheckMeasure'))`, and post it: `await
   fetch('http://127.0.0.1:8765/save/measure-375.json', {method: 'POST', body: JSON.stringify(r, null, 1)})`.
   Stop the receiver after.
6. **Check `page.script` in every result against the version in the file's head comment.** A browser pane
   keeps its cache and its sessionStorage from earlier chats, so a cached address or the one-liner can run an
   older copy of the script without any sign: a whole audit round was once measured with the version before
   the last fix. An older value, or none: pass or load the file again.
7. **A picture that loads lazily is measured only once it is on screen.** `images.notLoaded` lists the ones
   that had not arrived: bring them into view (a photo strip sideways, the page downwards) and run again
   before reading `stretched`, `oversized` or `heaviest`.

The script gives numbers and no opinion; what a number should be is the entry's to say. Each section's `find`
line gives words for `RB find`. Its `notMeasured` list names what only a hand can check: do those by hand when an
entry loaded in step 3 asks for one (text enlarged to 200%, focus moving with the Tab key, hover, a slow line).
A focus style counts only when the page itself has the focus: click into it or press Tab with the browser
tool first (`document.hasFocus()` is then true). In a pane without the focus every field reports
`outline: none`, which is not a fault of the page.

Without a running page, nothing is measured and the report says so:

- **A mock-up or screenshot:** every verdict is `judged`, with what was seen and where in the picture. A size
  read off the picture is given as "about" and stays `judged`. What a picture cannot show (the markup, alt
  texts, what happens on a tap) is `cannot tell`.
- **No browser tool:** read the sizes and colours from the code and mark the evidence `from the code`. Where an
  entry names a number the code does not state, work it out from the code's values (a contrast ratio from the
  two colours, a tap size from the CSS) and say how; a number that cannot be worked out is `cannot tell`.

## 3. Load the entries (quick depth)

1. `RB topics`: choose the two or three topics this part lives in; step 3 reaches the others by word.
2. `RB titles check <topic> <topic>`: read every title of those topics.
3. `RB find <word> --use check`, one word or one quoted phrase a call, for each noun of the part (button, price,
   photo, filter) and for the `find` words of every measured section that shows something. With nothing
   measured, take those words from the script (`grep "find:" "${CLAUDE_SKILL_DIR}/measure.js"`) for the
   sections the part has. A subject is spread over topics, so the words reach entries the topic titles miss.
4. `RB show <ids>` for every entry whose title could bear on this part. Pick widely: a title that turns out not
   to apply costs one line in step 4, an entry never read cannot be found again. For scale, the trial runs
   read about 80 entries for one form and 80 to 120 for a whole screen.

## 4. Give every entry a verdict

Each entry shown in step 3 gets one of four verdicts, with its evidence:

- **met**, **not met**, **cannot tell** (say what would settle it), or **does not apply** (say why in three words).
- Evidence is `measured` (the number, the width, the script's field), `judged` (what was seen and where), or
  `from the code`. Where an entry names a number, compare it with the measured one; a measured number outranks
  an impression.
- **Judge by the statement's own words.** A verdict rests on what the statement asks, in its words. An entry
  that only a general principle connects to the page does not apply, however well its title fits. A
  statement that only describes or permits ("browsers differ", "a site can", an example read from a picture)
  asks nothing: it is met where the page does it and does not apply otherwise, never not met.
- An entry met by one element and not by another is not met; name the element. A hand check that could not be
  done (no browser, no hover) is cannot tell.

Then, for the entries not met:

- **Rule or practice.** A rule not met is a finding. A practice not met is a finding too, worded as a default
  the page leaves, with what that costs the visitor.
- **One fault, one finding.** Entries that ask the same thing of the same element share a row that cites them
  all; a row holding a rule sorts as a rule.
- **A Conflict line** on an entry not met goes into its row as it stands: both sides, no winner picked here.
  An id named only inside a quoted Conflict line is not cited by the report. A met entry is listed without its
  Conflict line, unless the page shows the very thing the line warns of (the browser's own error bubble in
  another language than the page): that is a finding under the entry, with the line as it stands and the
  evidence, worded as the cost of following the entry.
- **Against a pick or a limit:** list it apart with its effect and evidence and change nothing. Reopening a
  pick is the user's decision. One that stops the visitor is also named in the report's first lines, so the
  findings' count does not hide it.
- **Effect on the task the page is for:** *stops* (the visitor cannot finish, or is misled), *slows*, or
  *polish*. A fault off that task's path is at most *slows*.
- **A fix** for each finding: the smallest change that would meet the entry.

## 5. Report

```markdown
# Check: <page or part>, <date>

Checked: <running page | mock-up | from the code>, at <widths>, in <languages>. Stage: <stage>. Depth: <depth>.
Loaded: titles of <topics>; find <words>; <n> entries read in full.
Built: <only after a build: what was built, the choices made where entries pulled apart, what the check changed.>
Stops the visitor: <the findings and the limits with that effect, in one line each, or "nothing">.

## First impression
<What the eye meets first at each width, and whether that is what the page is for. One or two sentences.>

## Findings
| # | Effect | The entry asks, the page does | Entry | Evidence | Fix |
|---|---|---|---|---|---|
| 1 | stops | Every field is tied to a label; the email field has only a placeholder | forms-000 (practice) | measured: forms.placeholderOnly 1, at 375 and 1280 | Add a visible label above the field |

## Against a pick or a limit
| Pick or limit | Entry | Effect | Evidence |
|---|---|---|---|

## Met
<The entries met, by topic, with the number where one was measured: "type-000 (practice): 68 characters a line at 1280".>

(The ids in this template are placeholders; a report cites only ids that `RB show` printed in this chat.)

## Cannot tell
<Entry, and what would settle it.>

## Does not apply
<The ids by topic, each with its three words of why.>

## Not covered
<Topics not loaded, widths, languages or states not checked, and what the script cannot measure and no hand
checked. A fault seen that no entry covers goes here too, marked "outside the rulebook, general knowledge".>
```

Order the findings by effect, rules before practices within one effect; with no finding, write "None" under
the table's head. "Met" stays in: it tells the user what was looked at, and it is what a later check compares
against.

Done when every entry shown in step 3 stands in exactly one section of the report, every id the report cites
was printed in full by `RB show` in this chat (an id seen only in a title list is shown first or left out),
every finding has all six cells filled, and "Not covered" names everything framed in step 1 that was not
reached.
