# session-start.ps1: ChatGPT's SessionStart hook (SU-Q64), the counterpart of session-start.sh for Claude Code.
# At the start of a chat it fast-forwards the agent-setup repo, refreshes the skill links in
# %USERPROFILE%\.agents\skills (SU-Q110), rebuilds %USERPROFILE%\.codex\AGENTS.md when the rules changed, and
# prints one line naming the chat's model (the rules' ticket check reads it). What it prints becomes context for
# the model, so it prints little: the model line, plus one warning line when the repo has uncommitted changes,
# cannot be read by git or cannot be pulled, one while the repo is not on main (SU-Q95), and one line when a skill
# link was added or removed or could not be.
# It never fails the chat: every error ends in exit 0.
# Installed into %USERPROFILE%\.codex\hooks.json by install-chatgpt.ps1. Windows PowerShell 5.1 compatible.

param(
    [string]$CodexDir  = (Join-Path $env:USERPROFILE '.codex'),    # override only for testing
    [string]$AgentsDir = (Join-Path $env:USERPROFILE '.agents')    # override only for testing
)

$ErrorActionPreference = 'Continue'
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)       # <repo>\global\hooks -> <repo>

function Run-Git([string[]]$gitArgs, [int]$seconds, [string]$exe = 'git') {
    # git (or another program) with a time limit; returns exit code and output, or code -1 when it ran out of time
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $exe
    $psi.Arguments = ($gitArgs | ForEach-Object { if ($_ -match '[\s"]') { '"' + ($_ -replace '"', '\"') + '"' } else { $_ } }) -join ' '
    $psi.WorkingDirectory = $repo
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    $psi.EnvironmentVariables['GIT_TERMINAL_PROMPT'] = '0'
    try { $p = [System.Diagnostics.Process]::Start($psi) } catch { return @{ Code = -2; Out = "$exe not found" } }
    $outTask = $p.StandardOutput.ReadToEndAsync()
    $errTask = $p.StandardError.ReadToEndAsync()
    if (-not $p.WaitForExit($seconds * 1000)) {
        try { $p.Kill() } catch {}
        return @{ Code = -1; Out = "no answer in $seconds seconds" }
    }
    $p.WaitForExit()
    return @{ Code = $p.ExitCode; Out = (($outTask.Result + "`n" + $errTask.Result).Trim()) }
}

try {
    # 1. the model, from the hook's input (one JSON object on stdin)
    $model = ''
    if ([Console]::IsInputRedirected) {
        try {
            $raw = [Console]::In.ReadToEnd()
            if ($raw.Trim()) { $model = [string]((ConvertFrom-Json $raw).model) }
        } catch {}
    }
    if ($model) { Write-Output "agent-setup: model $model" }

    # 2. pull, as session-start.sh does
    if (Test-Path -LiteralPath (Join-Path $repo '.git')) {
        $status = Run-Git @('status', '--porcelain') 10
        if ($status.Code -ne 0) {
            # git refuses the repo (e.g. "dubious ownership" when this runs as another Windows user), is missing
            # or gave no answer: say so instead of skipping the pull quietly (SU-Q72)
            $first = ($status.Out -split "`n")[0]
            Write-Output "agent-setup: git could not read $repo ($first). The setup was not pulled and may be out of date: tell the user."
        } else {
            if ($status.Out) {
                Write-Output "agent-setup: uncommitted changes in $repo. Run the setup-promote skill to commit them on a branch and push it for a pull request; main is never pushed."
            }
            $branch = Run-Git @('symbolic-ref', '--short', '-q', 'HEAD') 10
            if ($branch.Code -eq 0 -and $branch.Out -eq 'main') {
                $upstream = Run-Git @('rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}') 10
                if ($upstream.Code -eq 0) {      # no upstream yet (repo not published): nothing to pull
                    $pull = Run-Git @('pull', '--ff-only', '-q') 10
                    if ($pull.Code -ne 0) {
                        $first = ($pull.Out -split "`n")[0]
                        Write-Output "agent-setup: could not pull ($first). Run the setup-sync skill to check."
                    }
                }
            } else {
                # a setup change on a branch (SU-Q95, SU-Q108): no pull. setup_tools.py fetches (10 seconds, as the
                # pull) and says in one line whether the branch is merged; 11 seconds here leave Python time to start.
                $state = Run-Git @((Join-Path $repo 'tools\setup_tools.py'), 'repo-state', '--hook', 'chatgpt') 11 'python'
                $line = ($state.Out -split "`n" | Where-Object { $_ -like 'agent-setup:*' } | Select-Object -First 1)
                if ($line) {
                    Write-Output $line.Trim()
                } else {
                    $on = if ($branch.Code -eq 0 -and $branch.Out) { $branch.Out } else { 'no branch (detached HEAD)' }
                    Write-Output "agent-setup: the setup is on $on, not on main, so it was not pulled and gets no updates from main; whether it is merged could not be checked (Python: $(($state.Out -split "`n")[0]))."
                }
            }
        }
    }

    # 3. one link per skill, as the install made them: a skill that arrived with the pull is linked, the link of
    #    one that left is removed. Whether this hook runs as the user is not proven (it may run where it cannot
    #    make links), so a failure is one line, never an error.
    $skillsDir = Join-Path $AgentsDir 'skills'
    try {
        . (Join-Path $PSScriptRoot 'skill-links.ps1')
        $line = Get-SkillLinkHookLine (Sync-SkillLinks (Join-Path $repo 'global\skills') $skillsDir) $skillsDir
        if ($line) { Write-Output $line }
    } catch {
        Write-Output "agent-setup: could not refresh the skill links in $skillsDir ($($_.Exception.Message))."
    }

    # 4. the rules file, rebuilt only when its sources changed
    & (Join-Path $PSScriptRoot 'build-agents-md.ps1') -CodexDir $CodexDir
} catch {
    Write-Output "agent-setup: session-start hook stopped early ($($_.Exception.Message))."
}
exit 0
