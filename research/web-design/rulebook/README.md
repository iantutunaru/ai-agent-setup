# Web design rulebook

One file per topic, built from the owner's notes on the web design books (how: [../README.md](../README.md)).
Whole since 2026-11-21: every one of the 1,866 candidate entries is read on its page, its current sources are
looked up, and the duplicates pass has joined the same advice standing in two topics. The rulebook holds
**1,718 entries** (133 rule, 1,585 practice; 88 still need a current source), 109 candidates joined into others,
22 dropped, 17 to taste. By topic: accessibility 55, colour 91, content 242, forms 97, images 139, layout 196,
logo 43, navigation 138, persuasion 163, phone 40, search-and-filters 58, spacing 34, speed 42, testing 93,
trust 41, type 246. The work was planned in the owner's web project, whose ticket and decision ids start with AW
(such as AW-T19-Q4); the lines below cite them as the reason for a choice. That project is not published.

The topic files were written by a script from the reading's results. Do not edit them by hand in this copy:
an entry's id and lines are what the web skills cite.

## An entry

```markdown
### forms-012 · Put the label above its field
- **Statement:** what to do or what holds, the case, the reason the books give.
- **Kind:** rule | practice
- **Use:** look, check, text
- **Sources:** KRUG-009 (page s49), ROBBINS-171 (page 212)
- **Also in (not read):** GENTRY-044
- **Study (as the book reports it):** ...
- **Current source:** confirmed by <address> (read <date>)
- **Asked of the source:** what the current source was asked to confirm
- **Needs source:** what a current source would have to confirm
- **Conflict:** which entry says otherwise, and what
- **Read:** 2026-11-20, passage; candidate forms E19, joined by phone E40
```

- **rule**: a book reports a study or a measurement of the statement itself (AW-Q46). The study is named as the
  book reports it. **practice**: an author's working rule with no study behind it, a default that a pick on an
  option sheet may override.
- **Sources** are the findings the entry rests on, each with its book page. A finding id starts with the book's
  short name (`KRUG-009`); [../README.md](../README.md) lists the books. A page that starts with `s` is a
  section of an ebook. The book behind each source was read: the passage around the finding, or the page
  (`page`), or the page image (`image`), as the Read line says. The Read line also says who read. With no name
  it was Claude, the coordinating chat, alone. "Opus agent, each part checked by Claude": an agent found the
  book sentence for every part of the statement, a script found every such sentence on its page, and Claude read
  each part beside its sentence and settled every change (AW-T19-Q11). "read again": a second reading by an
  agent, its differences settled by Claude (AW-T19-Q13). A page range followed by "the notes cite" was widened
  by the reader to the page next to the cited one, where a detail of the statement stands (AW-T19-Q14).
- **Also in** lists findings the merge found to say the same. They were not read and carry no weight.
- **Current source**: the current source looked up for the entry's study or "Needs source" line: `confirmed
  by`, `overturned by` (the entry then went to the taste list) or `none found`, with the date it was read or
  searched (AW-Q42, AW-T19-Q4).
- **Needs source**: the entry is about a technique or a device and is not confirmed until a current primary
  source is named (AW-Q42). Until then, treat it as unconfirmed.
- **Use**: `look` before a page is drawn, `check` when a built page is checked, `text` when web text is written.
- Advice a book gives only for an organisation's own network (an intranet) stays, worded as such, so a check of
  a public page can skip it (AW-T19-Q26).
- An id (`forms-012`) is given once and never changes.

Beside the topic files:

- `dropped.md`: findings in no entry, each with its reason.
- `taste.md`: preferences and claims that did not hold, never stated as proven.
- `_joined.json`: maps the id of an entry that was joined into another to the id that now holds it, so an old
  citation still leads somewhere.

An ideas list is not part of the rulebook. If a project keeps its own ideas file (`docs/web-ideas.md`), web-look
puts its matching ideas on the table.

## Joined entries

A joined entry's advice now stands in its target, often in another topic (63 of the 93 joins of the duplicates
pass crossed topics, for example phone's "a page will not look the same everywhere" into accessibility-048, four
accessibility entries into images). The target's Read line names it ("joined by phone E01"), its Sources and Also
in take in the joined entry's findings, and its statement takes in what the joined entry added. The old topic
keeps no pointer; `_joined.json` does. The joined entry's id is not reused, so a topic's ids have gaps. A check
that wants everything about one subject should search every topic file, not only the one named after it.
