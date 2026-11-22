# What the install scripts change

The install steps are on the [front page](../README.md#install). This page says what each install script does on
your PC, what to do on a second PC, how to undo the ChatGPT install, and how to take a single skill.

## Claude Code: install.ps1

The install first backs up `settings.json` and `CLAUDE.md` from `%USERPROFILE%\.claude` into
`%USERPROFILE%\.claude\agent-setup-backups\`. Then it:

- makes `.claude\setup` a link to the repo;
- puts one link per skill of the repo's `global\skills` into `.claude\skills`. Skills of your own there stay where
  they are, outside the repo, and a folder of yours with the name of one of these skills is kept and named. An
  older install made `.claude\skills` one link to `global\skills`: that link is replaced by a folder, and
  Anthropic's own skills that a Claude program wrote through it into `global\skills\synced` move to
  `.claude\skills\synced`;
- makes `local/personal.md` and `local/settings.personal.json` from the examples when they are missing, and
  says so;
- writes `.claude\CLAUDE.md` as two import lines: the rules (`global/CLAUDE.md`, which in turn imports the
  shared rules and the Claude part) and your personal file `local/personal.md`;
- merges `global/settings.json` and then `local/settings.personal.json` into `.claude\settings.json`, with the
  repo's parent folder as your projects folder.

## A second PC

On a second PC, clone and install there too, and copy your two files into its `local/` by hand: git does not
carry them. Until a PC has them and has run the install, the session-start hook says so in one line at the start
of each chat. The hook also links a skill that arrives with a pull and removes the link of one that leaves, and
asks for the install again while `.claude\skills` is still an older install's single link.

## ChatGPT: install-chatgpt.ps1

The script:

- puts one link per skill into `%USERPROFILE%\.agents\skills\`. It leaves your other skills there alone, and
  does not replace a folder of yours that has the same name as one of these skills;
- makes `%USERPROFILE%\.codex\setup` a link to the repo;
- builds `%USERPROFILE%\.codex\AGENTS.md`, the rules file ChatGPT loads in every chat, from the shared rules,
  the ChatGPT part, both profiles and your personal file `local/personal.md`, which it first makes from the
  example when it is missing. ChatGPT cannot import files, so they are written into one marked block; text of
  your own in that file stays, above the block, and the old file is backed up;
- adds a hook to `%USERPROFILE%\.codex\hooks.json`, beside any hooks of your own, that pulls the repo, refreshes
  the skill links and rebuilds the rules file when a chat starts.

The hook links a skill that arrives with a pull and removes the link of one that leaves; it says so in one line.

## Running it again, and undo

Run `install-chatgpt.ps1` again after you move the repo's folder. To undo it, delete the links, the marked block
in `AGENTS.md` and the hook's entry in `hooks.json`; the repo's files stay.

## One skill

Copy its folder from `global/skills/` into your assistant's skills folder: `%USERPROFILE%\.claude\skills\` for
Claude Code, `%USERPROFILE%\.agents\skills\` for ChatGPT. This works for the writing skills, `guided-session` and
`stage-close`. The web skills and the game design skills need the whole repo: they read files in `research/`.
