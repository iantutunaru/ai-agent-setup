# ChatGPT skills, round 1 (~10 min)

For SU-Q51: the README may call a skill "tested on ChatGPT" only after this round. Read-only: no row changes a
file. Cap: 3 rounds.

**Why.** The repo's skills were written for Claude. On this laptop 13 of them are now linked into the folder
ChatGPT reads (`C:\Users\<you>\.agents\skills`). OpenAI's pages say ChatGPT follows linked skill folders, but
they do not say whether the kind of link Windows makes without admin rights (a junction) counts, and the skills
find their scripts through a name only Claude fills in. This round shows whether ChatGPT sees the skills and can
run their scripts.

**Where to start.** Close the ChatGPT desktop app completely and open it again, so it reads the skills folder
afresh. Start a new task of the kind that works on a folder on the PC and can run commands (OpenAI's pages call
it Codex, or Work, inside the ChatGPT desktop app). Choose the folder `D:\<projects>\chatgpt-skill-test`; it holds
`draft.txt` and `page.html`. The screen names here are from OpenAI's pages, not from the app itself, so say
where a name differs.

| Row | Do | Bring back |
|---|---|---|
| R1 | In the message box type `@`. If no list of skills shows, type `$` instead. Look for `web-rulebook`, `writing-check` and `plain-language`. | Which key showed the list, and whether all three are in it. |
| R2 | Send: `Use the web-rulebook skill: is there a rule on how long a line of text should be? Give the entry ids.` | One id from its answer (pass looks like `type-135` or `type-229`), or the error line if a command failed. |
| R3 | Send: `Use the writing-check skill on draft.txt.` | How many issues it reports from `check_text.py` (pass is 1, a dash on line 3), or the error line. |
| R4 | Send: `Use the web-check skill on page.html, quick depth. Open it in your browser and measure it.` | Whether the report says `measured` with numbers, or `from the code`, or it stopped; and the error line if one showed. |
| R5 | Send, without naming a skill: `Put this in plain language: "Pursuant to our records, remittance of the outstanding balance is requested at your earliest convenience."` | Whether the app showed that it used a skill, and which one. |
| R6 | Send: `Use the humanizer-en skill on draft.txt and show me the result. Do not change the file.` | Worked, or the error line. |
| R7 | Anything odd: a skill listed twice, a question about permissions, a skill that started unasked. | A few words. |

Reply in one line, for example: `R1 @, all three · R2 type-135 · R3 1 issue · R4 from the code · R5 plain-language · R6 worked · R7 nothing`.

**Automatic (done, 2026-11-21).**

- `install-chatgpt.ps1` run twice against a scratch folder (12 of 13 linked beside a same-named real folder left
  untouched, a stale link removed, an own skill left alone), then on the laptop: 13 of 13 linked.
- `python -I %USERPROFILE%\.agents\skills\web-rulebook\rb.py topics` through the link prints the 16 topics, so
  the script finds the rulebook from the linked place.
- `check_text.py draft.txt` through the link: `1 issue(s)`, the dash on line 3. `audit_text.py`: 2 sentences,
  one of 45 words, Flesch 46.
- `rb.py find characters line --use check` lists `type-135` (52 to 78 characters a line) and `type-229` (45 to
  75), each with a conflict mark.

## Results

Run by the user on 2026-11-21 in the ChatGPT desktop app. The user's reply: "all passed", with the chat's
transcript. The rows below are read from that transcript and from the files the app left in its work folder
(`Documents\Codex\2026-11-21\use-the-web-rulebook-skill-is\`), not from the reply alone.

| Row | What came back | What it settles |
|---|---|---|
| R1 | Passed, per the user. Which key showed the list was not reported. | Still unknown: `@` or `$` in the desktop app. |
| R2 | Pass. The app read `~/.agents/skills/web-rulebook/SKILL.md` and ran `python -I 'C:/Users/<you>/.agents/skills/web-rulebook/rb.py'` 20 times (`topics`, `find`, `show`, `titles`). It cited `type-229`, `type-135`, `type-230` and `type-136`, each printed by `show`. | ChatGPT sees a skill linked by a junction, and puts the skill's folder in place of the unfilled `${CLAUDE_SKILL_DIR}`. |
| R3 | Pass, with a remark. It ran `check_text.py` and `audit_text.py` on `draft.txt`, wrote a revised draft into its own work folder and reported that one: 0 issues, passive 0%, reading ease 90. It did not report the count for the original draft, which the row asked for. | The scripts run. It looked for `AGENTS.md` and `style/writing-rules.md` in the project, loaded `humanizer-en` as the skill says, and `business-writing` by itself. It tried `humanizer-en/scripts/post_edit_audit.py`, which is not installed (`README-sources.md`), and went on without it. |
| R4 | Pass, by another route than the row expected. It did not use the app's built-in browser: it wrote a Node script that starts the installed Chrome without a window and passes the skill's `measure.js` to it (its `work/measure-page.mjs`, line 71). The first try ended in a crash of Chrome's graphics process; it tried again with a fresh profile. | Claude read its saved results: `page.script` 2026-11-21b, sideways overflow 445 at 375 and 0 at 1280, lowest contrast 2.84, 37 to 110 characters a line, `placeholderOnly` 1, one image without alt. These are the values of `web-check/tests/expected.md`. Its report has the skill's sections. This route needs Chrome and Node on the machine. Not settled: whether the app's own browser can run the script. |
| R5 | Pass. It said it used `plain-language` without being told to. | A skill starts by itself from its description. |
| R6 | Pass. The result was shown, and the candidate text went to the app's work folder. `draft.txt` still has its dash and its time stamp of 15:58, before the round. | `humanizer-en` runs without its missing script. |
| R7 | Nothing reported. | |

Not exercised in this round: `web-look`, `web-text`, `guided-session`, `stage-close`, `corporate-communication`,
`orwells-rules`, `gov-uk-style`. `business-writing` was only loaded as a helper in R3.
