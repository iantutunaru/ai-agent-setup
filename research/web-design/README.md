# Web design rulebook: how it was made

This folder holds the rulebook in [rulebook/](rulebook/): 1,718 short entries on how to build web pages, made
from the owner's notes on 26 books, most of them about web design. Each entry restates the advice in new words
and gives the book and page it rests on. The notes, the tools that made them and the books' own text are not published; only the
rulebook is.

Open this page to see how an entry came to be and what the work left out (the known gaps at the end). What an
entry is and what each of its lines means: [rulebook/README.md](rulebook/README.md). To use the rulebook, ask the
web skills: [web-rulebook](../../global/skills/web-rulebook/SKILL.md) holds the lookup tool that
[web-look](../../global/skills/web-look/SKILL.md), [web-check](../../global/skills/web-check/SKILL.md) and
[web-text](../../global/skills/web-text/SKILL.md) call. For each skill, what ran and what did not:
[docs/tried.md](../../docs/tried.md).

## How it was made

1. Each book was read by an agent, which wrote its findings in its own words, each with the page it rests on.
2. Each finding carried a few words quoted from its page, and a script confirmed that those words stand on
   that page. This shows the page is right, not that the finding says what the page says; step 4 covers that.
3. The findings were merged by topic into candidate entries.
4. Each candidate was read again on its book page before it became an entry.
5. Entries in two topics that gave the same advice were joined into one.
6. Studies that the books name were looked up at a current source, where one exists.

The reading closed on 2026-11-19: 25 books read, 4,967 findings. The rulebook was whole on 2026-11-21: all 1,866
candidates were read on their pages, and 1,718 entries stand in 16 topic files, beside a list of dropped findings
and a list of taste. The work was planned in the owner's web project (its ticket ids start with AW), so entries
and these pages cite ids such as AW-T19-Q34.

## The books

| Group | Book | Findings |
|---|---|---|
| A | Krug, Don't Make Me Think, Revisited (2014) | 227 |
| A | Nielsen, Веб-дизайн (Russian; imprint 2001) | 634 |
| A | Weinschenk, Neuro Web Design (2009) | 93 |
| A | Walter, Designing for Emotion (2011) | 91 |
| A | Beaird and George, The Principles of Beautiful Web Design (2014) | 305 |
| A | Boulton, A Practical Guide to Designing for the Web (2009) | 198 |
| A | Lupton, Thinking with Type (2010) | 216 |
| A | Gentry, Hello Design World (2017) | 167 |
| A | Кирсанов, Веб-дизайн (1999, Russian) | 576 |
| A | Киссейн, Основы контентной стратегии (2012, Russian) | 100 |
| A | Брингхерст, Основы стиля в типографике (2006, Russian) | 508 |
| B | Талер и Санстейн, Nudge (2017, Russian) | 242 |
| B | Heath, Made to Stick (2007, 2008) | 162 |
| C | Goldstein, Lazaris, Weyl, HTML5 & CSS3 for the Real World (2015) | 64 |
| C | Lawson and Sharp, Introducing HTML5 (copyright 2011) | 53 |
| C | Gillenwater, Stunning CSS3 (2011) | 102 |
| C | Lindley, JavaScript Enlightenment (2012) | not read |
| C | Дакетт, Javascript и jQuery (2017, Russian) | 72 |
| C | Седерхольм, Пуленепробиваемый веб-дизайн (2012, Russian) | 90 |
| C | Роббинс, Веб-дизайн для начинающих (2021, Russian) | 443 |
| C | Cabarga, Logo, Font & Lettering Bible | 122 |
| D | Godin, Linchpin (2010) | 148 |
| D | Альтушер, Выбери себя! (2018, Russian) | 121 |
| D | Клеон, Кради как художник (2019, Russian) | 79 |
| D | Freeman, Introducing HTML5 Game Development (2012) | 35 |
| D | Monteiro, Design Is a Job (2012) | 119 |
| skipped | Head First, mobile websites (2013, Russian) | not read |

Group C was read in part (gap 1). Group D are books that are not about websites. They were read for ideas, not
rules: their 502 findings are not in the rulebook.

Of the 4,967 findings, 4,413 were backed as practice, 268 as a named study and 286 as taste; 28 were the reading
agent's inference rather than read on the page. 226 came from a second pass over the pictures of six books
(Krug, Beaird, Boulton, Lupton, Gentry, Kirsanov).

## Known gaps

Answer "anything left?" from this list.

1. **Group C was read in part, by decision.** Read: the chapters on forms, accessibility, flexible layouts and
   type, plus galleries, filters and web images. Not read: the language and syntax chapters, Goldstein's
   appendix on structured data, and Robbins' chapters on colour, tables and SVG.
2. **Studies are named as the books name them**, unless the entry has a "Current source" line. Without that
   line, the study stands as the book reports it. An entry about a technique or a device that no current source
   has confirmed yet carries a "Needs source" line (88 entries).
3. **Findings from pictures were checked on the picture for a sample only.** The measures and positions a
   finding read off a picture were compared with the picture itself for 9 of the 226 such findings.
4. **The reading agents chose the topics** from a fixed list. No second reader has checked those choices.
5. **One book was not read and one was skipped.** Lindley was left out by decision, and the Head First book on
   mobile websites was skipped.
