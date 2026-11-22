# Where the skills came from

Each of the 19 skills came from one of three places: GitHub, one of the owner's projects, or this repo itself.
This page gives each one's source, the parts left out, and the skills looked at but not installed.

## From GitHub

Added on 2026-11-03. Each was read in full before it was installed. All are Markdown only, with no scripts.

| Skill | Source | Licence | What was left out |
|---|---|---|---|
| humanizer-en | github.com/matematicsolutions/matematic-humanizer | MIT | Its `post_edit_audit.py` was not installed. The skill falls back to a check by hand. |
| plain-language | github.com/surendranb/writing-skills | MIT | Nothing. |
| business-writing | github.com/surendranb/writing-skills | MIT | Nothing. |
| corporate-communication | github.com/surendranb/writing-skills | MIT | Nothing. |
| orwells-rules | github.com/surendranb/writing-skills | MIT | Nothing. |
| gov-uk-style | github.com/surendranb/writing-skills | MIT | Nothing. |

`humanizer-en` carries two MIT notices: the adapted skill's (Siqi Chen, github.com/blader/humanizer) and its
direct source's (Wieslaw Mazur / MateMatic Solutions, in `LICENSE-MateMatic`). `gov-uk-style/references/REFERENCE.md`
condenses the GOV.UK style guide, which is Crown copyright and available under the
[Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

One more came from GitHub and is gone. `design-critique`, from github.com/anthropics/knowledge-work-plugins (the
design plugin), came out on 2026-11-21 (SU-Q40). `web-check` took its place and kept its useful frame.

## Looked at, not installed

- **iso-24495-1.** It applies to every reply and requires bold lead-ins on bullets. That conflicts with the
  rule against bold labels.
- **iso-24495-text-audit.** It needs Bun and TypeScript scripts, and it reads only `.md` and `.txt` files.

## Ours, promoted from a project

Promoted on 2026-11-21 (SU-Q75 to SU-Q77): `design-lenses`, `balance-check` and `playtest-plan`. They were first
written in the owner's first game project. They draw on the owner's game design books, which are not in
the repo. Where the books live, and the project entry the three skills read:
[research/game-design/README.md](../../research/game-design/README.md).

## Written for this repo

The other ten skills began in this repo, some from the owner's projects' own earlier copies. Each line
gives the decision behind it in [decisions.md](../../decisions.md).

- **writing-check:** one global skill for the checking scripts and the shared writing rules (SU-Q27,
  2026-11-12). It merges two projects' tools.
- **guided-session:** one skill in place of three projects' own versions (SU-Q10, 2026-11-12).
- **stage-close:** one generic version in place of three projects' own copies (SU-Q10, 2026-11-12).
- **setup-init:** starts a new project from the template (SU-Q06, SU-Q10, 2026-11-12).
- **setup-sync** and **setup-promote:** keep a project in line with this repo and move a project's improvement
  into it (SU-Q02, SU-Q10, 2026-11-12).
- **web-rulebook, web-look, web-check, web-text:** four skills over the web design rulebook (SU-Q39 to SU-Q43,
  2026-11-21), decided in a chat of the owner's web project. The rulebook and its making:
  [research/web-design/README.md](../../research/web-design/README.md).

## Not ours: `synced/`

`synced/` holds Anthropic's own skills (docx, pdf, pptx, xlsx and others). A Claude program writes and refreshes
them in `~/.claude/skills/synced`. They were first seen on 2026-11-19. While `~/.claude/skills` was one junction
to this folder, they landed here; `install.ps1` now moves them out (SU-Q111). Git ignores the folder (SU-Q37)
until every PC has run that install.
