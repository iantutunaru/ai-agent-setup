#!/usr/bin/env bash
# SessionStart hook (SU-Q14): fast-forward the agent-setup repo at the start of every session.
# Prints nothing when all is well; one warning line when the repo has uncommitted changes or can't be pulled, one
# while the repo is not on main (SU-Q95), one when the person's own file is not set up, one when a skill link was
# added or removed after the pull, and one while ~/.claude/skills is still the old install's single link.
repo="$HOME/.claude/setup"
[ -e "$repo/.git" ] || exit 0
cd "$repo" || exit 0

if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  echo "agent-setup: uncommitted changes in $repo. Run /setup-promote to commit them on a branch and push it for a pull request; main is never pushed."
fi

branch=$(git symbolic-ref --short -q HEAD 2>/dev/null)
if [ "$branch" = main ]; then
  # No upstream yet (repo not published): nothing to pull.
  if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
    if ! out=$(GIT_TERMINAL_PROMPT=0 timeout 10 git pull --ff-only -q 2>&1); then
      echo "agent-setup: could not pull ($(printf '%s' "$out" | head -n 1)). Run /setup-sync to check."
    fi
  fi
else
  # A setup change on a branch (SU-Q95, SU-Q108): no pull. setup_tools.py fetches (10 seconds, as the pull) and says
  # in one line whether the branch is merged; 11 seconds here leave Python time to start.
  py=$(command -v python || command -v python3)
  out=$(timeout 11 "${py:-python}" "$repo/tools/setup_tools.py" repo-state --hook claude 2>/dev/null)
  code=$?
  line=$(printf '%s' "$out" | tr -d '\r' | grep '^agent-setup:' | head -n 1)
  if [ -n "$line" ]; then
    echo "$line"
  else
    echo "agent-setup: the setup is on ${branch:-no branch (detached HEAD)}, not on main, so it was not pulled and gets no updates from main; whether it is merged could not be checked (Python stopped with code $code; 124 means no answer in 11 seconds)."
  fi
fi

# The person's own file (SU-Q90, SU-Q101). Claude Code skips an import whose file is missing without a word, so a
# PC that has pulled the move to local/ and not rerun install.ps1 would lose the lines about its user silently.
if [ ! -f "$repo/local/personal.md" ] || ! grep -qF 'setup/local/personal.md' "$HOME/.claude/CLAUDE.md" 2>/dev/null; then
  echo "agent-setup: the personal file is not set up (local/personal.md is missing or ~/.claude/CLAUDE.md does not import it), so this chat has no lines about the user. Tell the user to run install.ps1 in $repo again and fill in local/personal.md."
fi

# One link per skill (SU-Q98, SU-Q110). A cheap check here; PowerShell (skill-links.ps1, shared with the installs)
# runs only when a skill of the repo has no link, or a link into a setup's skills folder has lost its target.
skills="$HOME/.claude/skills"
if [ -L "$skills" ]; then
  # a PC that pulled the change and has not rerun the install: its skills still work through the one link
  echo "agent-setup: ~/.claude/skills is still one link to the setup's skills folder, from the old install. Tell the user to run install.ps1 in $repo again: it gives each skill its own link, so their own skills stay outside the repo."
else
  stale=""
  for dir in "$repo"/global/skills/*/; do
    name=$(basename "$dir")
    [ "$name" = synced ] && continue
    [ -f "$dir/SKILL.md" ] || continue
    [ -e "$skills/$name" ] || { stale=1; break; }
  done
  if [ -z "$stale" ] && [ -d "$skills" ]; then
    for entry in "$skills"/*; do
      if [ -L "$entry" ] && [ ! -e "$entry" ]; then
        case "$(readlink "$entry")" in */global/skills/*) stale=1; break ;; esac
      fi
    done
  fi
  if [ -n "$stale" ]; then
    q() { printf "'%s'" "$(printf '%s' "$1" | sed "s/'/''/g")"; }   # a PowerShell string in single quotes
    lib=$(cygpath -w "$repo/global/hooks/skill-links.ps1")
    from=$(cygpath -w "$repo/global/skills")
    into=$(cygpath -w "$skills")
    out=$(timeout 8 powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command \
      "try { . $(q "$lib"); Get-SkillLinkHookLine (Sync-SkillLinks $(q "$from") $(q "$into")) $(q "$into") } catch { Write-Output ('agent-setup: could not refresh the skill links in ' + $(q "$into") + ' (' + \$_.Exception.Message + ').'); exit 1 }" \
      2>/dev/null)
    code=$?
    line=$(printf '%s' "$out" | tr -d '\r' | grep '^agent-setup:' | head -n 1)
    if [ -n "$line" ]; then
      echo "$line"
    elif [ "$code" -ne 0 ]; then
      echo "agent-setup: could not refresh the skill links in $into (PowerShell stopped with code $code; 124 means no answer in 8 seconds). Tell the user to run install.ps1 in $repo again."
    fi
  fi
fi
exit 0
