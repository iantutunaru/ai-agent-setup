---
name: web-look
description: Prepare the options before a web look is drawn, from the user's web design rulebook. Use whenever a page, layout, component, colour, type or any other look of a website is about to be designed, mocked up, wireframed or put to the user as an option sheet - "design the home page", "how should the filters look", "option sheet for X", a design ticket. Each option then says which rules and practices it follows, which it bends and what that costs, and matching ideas from the project's own ideas list, if it has one, are put on the table.
---

# Web look

A look is picked by the user from options. This skill makes the options differ where the books leave a real
choice, and makes each option say what it follows and what it bends, so the pick is made knowing its cost.

The rulebook is asked through one tool (the `web-rulebook` skill explains its marks):

    RB:  python -I "${CLAUDE_SKILL_DIR}/../web-rulebook/rb.py"

The path in front of the script's name is this skill's folder. A tool that shows it as a `${...}` name has not
filled it in: put the folder this file is in there.

## 1. Frame

- **The question the sheet answers,** in one sentence ("where does the map go on the search page at PC
  width?"). One sheet, one question. A neighbouring question stays on the sheet only when the options' answer
  to the first one changes its answer; any other is a second sheet, named under "Left out".
- **The screens:** which widths the options are drawn for (phone 375 and PC 1280 unless the project names
  others).
- **What is settled:** the project's brand or design file and its decisions (its `AGENTS.md`, or `CLAUDE.md`
  where not yet moved, "Where things are"). A settled pick is drawn as it is in every option; it is never
  offered again as a choice.
- **The sheet's form:** the project's own rule for option sheets (how many options, at what size, where they
  are shown). Without one: 2 to 4 labelled options at contact-sheet size, with a recommendation.
- **The depth:** *quick* for one sheet. For the sheets of a whole stage, read [full-set.md](full-set.md) now:
  one agent per topic reads every `look` entry against all the sheets at once.

## 2. Load the entries (quick depth)

1. `RB topics`: choose the topics the sheet lives in.
2. `RB titles look <topic> <topic>`: read every title. A line ending in `| conflict` marks an entry another
   entry or a current source speaks against: those are where options come from.
3. `RB find <word> --use look` for each noun on the sheet (map, card, price, photo, filter): a subject is spread
   over topics.
4. `RB find <word> --use check` for what the built page will be measured on: tap sizes, text sizes, characters
   a line, contrast. An option that cannot pass its later check is a wasted option.
5. `RB show <ids>` for every entry whose title could bear on the sheet. Pick widely.
6. `RB ideas site <word>` for the sheet's nouns, and `RB taste <word>`.

## 3. Sort what was loaded into fixed, open and settled

- **Fixed:** rules, and practices nothing here pulls against. Every option follows them; they are the sheet's
  common ground, listed once, not repeated per option.
- **Open:** entries whose Conflict line bears on the sheet's question; two entries that cannot both be met on
  this sheet; taste lines ("designers differ here"); ideas. Each open point is a question the options answer
  differently.
- **Settled:** covered by one of the project's picks. Where an entry speaks against a pick, note it for the
  sheet's foot with its evidence and change nothing: reopening a pick is the user's decision.

The options differ on the open points. Two options that follow and bend the same entries are one option drawn
twice: merge them, or find the open point that separates them.

## 4. Put the ideas on the table

Show the matching ideas to the user by id and title before drawing, each marked "idea, not proven, its book
page not read" and with nothing added: an idea speaks for no option until the user takes it. The ideas come
from the project's own ideas file, if it has one (`docs/web-ideas.md`); a project without one has no ideas,
and this step is skipped. An idea the user takes is read on its page first, for each finding in the idea's
Sources (`RB show <idea id> --sources`), where the project has the book at hand. If the page carries the idea,
it becomes an option or a part of one, still marked as an idea. If it does not, tell the user what the page
says instead. Where the book is not at hand, the idea stays marked unread on the sheet. An idea's "Would
change" line is used only from the project's own ideas file.

## 5. Draw the options, each with its lines

Under every option on the sheet, or beside the sheet in the same order:

```markdown
**Option B: the map beside the list**
- Answers: <the open point, and this option's answer to it>
- Follows: layout-000 (practice), search-and-filters-000 (rule)
- Bends: phone-000 (practice): <what the visitor loses, in one sentence>
- At risk: layout-000 (rule): <what must be measured on the drawing before this option stands>
- Idea: idea-000 (not proven), taken by the user
```

(The ids here are placeholders; a sheet cites only ids that `RB show` printed in this chat.)

- An option that goes against a **rule** is drawn only when the user asked for it, and its Bends line carries
  the rule's study or source, so the evidence is on the sheet.
- **The recommendation** names one option and its reason in entries. A rule outweighs a practice, a practice
  outweighs taste. Where only taste separates the options, say so: the recommendation is then the assistant's own
  judgement of fit and is labelled as that.
- **Common ground:** the fixed entries, once, at the sheet's head or foot.
- **Left out:** the questions moved to a later sheet and the options considered and dropped, each with the
  entry that decided it.

## 6. After the pick

Write the picked option into the project's brand or design file as rules a build can follow, with the ids it
follows and the ids it bends, and log the pick where the project logs decisions. The bent ids matter later:
`web-check` then lists them under "Against a pick or a limit" instead of raising them as findings.

Done when every option carries its Answers, Follows and Bends lines with ids shown in this chat, every open
point found in step 3 gets different answers from at least two options or is named on the sheet as left out, and the
recommendation states whether it rests on a rule, a practice or taste.
