---
name: web-rulebook
description: Look up what the user's web design rulebook says - 1,700 entries from their 26 design books, each marked rule (study or current source behind it) or practice. Use for any question of the kind "is there a rule on X", "what do the books say about X", "why is it done this way" about a web page's layout, type, colour, forms, navigation, images, search, phone behaviour, speed, accessibility, trust, persuasion or testing, and before stating any web design advice as fact. The skills web-look, web-check and web-text call its lookup tool.
---

# Web rulebook

The rulebook is too large to read (about 330,000 tokens), so it is asked, never opened. One tool hands out the
part a job needs:

    python -I "${CLAUDE_SKILL_DIR}/rb.py" topics                       the 16 topics: what each holds, entry counts
    python -I "${CLAUDE_SKILL_DIR}/rb.py" find <word> [<word>...]      entries holding every word; a phrase in quotes
                                                                       (--any: any word; --use look|check|text;
                                                                       --topic <topic>)
    python -I "${CLAUDE_SKILL_DIR}/rb.py" titles <use> <topic>...      a topic's titles for one use (or `any`, `all`)
    python -I "${CLAUDE_SKILL_DIR}/rb.py" show <id> [<id>...]          the full text of entries
    python -I "${CLAUDE_SKILL_DIR}/rb.py" topic <use> <topic>          every entry of a topic, in full
    python -I "${CLAUDE_SKILL_DIR}/rb.py" ideas [site|pitch] [<word>]  the project's own ideas list, if it has one
    python -I "${CLAUDE_SKILL_DIR}/rb.py" taste <word>                 the taste and unconfirmed list

The path in front of the script's name is this skill's folder. A tool that shows it as a `${...}` name has not
filled it in: put the folder this file is in there.

A use is the moment an entry serves: `look` before a page is drawn, `check` when one is built or checked, `text`
when its words are written. Output too long for a tool result is written to a file whose path is printed; read
that file.

## Answering a question

1. **Find.** Run `find` with the question's nouns, one or two at a time, and again with another word for the same
   thing (label and caption, phone and touch, button and link): the entries use the books' words, and a subject
   is spread over several topics. `topics` shows where else to look; `titles any <topic>` lists a whole topic.
   The search is done when a further word for the same thing brings no id that bears on the question and is
   new. `find` does not read the ideas and taste lists: run `ideas` and `taste` with the same words before
   saying that nothing was found.
2. **Read.** `show` every entry that bears on the question. Titles are a table of contents: an answer rests on
   the statement, never on the title.
3. **Answer** with each entry's id and kind, as the tool's last lines say. Done when every claim in the answer
   carries an id that `show` printed in this chat, and every Conflict line of those entries is passed on. A
   Conflict line is passed on as it stands; the entry it names ("in type-000") is shown only when the answer
   says more about that entry than the line does.

## What the marks mean

- **rule**: a book reports a study or a measurement of the statement, or a current primary source confirms it
  (the "Current source" line gives the address). A "Study" line is the study as the book reports it.
- **practice**: an author's working rule with no study behind it. It is a default; a design may bend it when
  the user picks so, knowing what it loses.
- **Needs source** with **Current source: none found**: the lookup found no current page that answers, so
  the entry is unconfirmed. Say so when citing it. Beside a "confirmed by" line, what the Needs source line
  names is the part still open.
- **Joined**: `show` on an id that was joined into another entry prints that entry and says which id to cite.
  Advice often moved to another topic that way (text alternatives from accessibility to images), which is one
  more reason to search by word and not by topic alone.
- **Conflict**: another entry or a current source says otherwise. Both sides go into the answer. A "Current
  source: overturned by" line means a current source speaks against part of the statement; the Conflict line
  says which part, and the kind stays as printed. A Conflict line that names a candidate "not kept" has no
  entry behind it: `taste <its finding id>` prints the claim and whether a current source overturned it; say
  that with the line.
- **idea**: from the project's own ideas file (`docs/web-ideas.md`, or the file named in `WEB_IDEAS_FILE`),
  not from the rulebook; a project without one has no ideas. Never a rule, nothing in it proven, its book page
  not read. Offer it as an idea, by its `idea-` id.
- **taste**: an author's preference, or a claim a current source overturned. It supports nothing; say "designers
  differ here".
- **Nothing found** means the books in the rulebook do not speak of it. It is no rule for and no rule against;
  say so first, and say plainly when advice comes from general knowledge and not from the rulebook. Entries on
  a neighbouring subject may follow, each named as a neighbour and never as a rule on the subject asked about.
  When the entries answer only a part of the question ("on a phone"), the answer names the part they leave
  open, in the same words.

## Walking back to the book

`show <id> --sources` adds the findings behind an entry with their pages, and who read the page. A finding id
(`KRUG-153`) names the book; the page stands beside it in the Sources line. The reading notes behind the findings are not
published.

The topic files were written by a build (`research/web-design/rulebook/README.md`). A wrong entry is reported
to the user with its id; the files are never edited by hand.
