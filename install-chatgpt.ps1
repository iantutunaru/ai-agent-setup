# install-chatgpt.ps1: set this repo up for ChatGPT (the desktop app, Codex command line and editor extension).
# Safe to re-run. It does four things (SU-Q48, SU-Q54, SU-Q60, SU-Q64, SU-Q65):
#   1. links each skill of global\skills into %USERPROFILE%\.agents\skills, the folder ChatGPT reads;
#   2. links the repo itself at %USERPROFILE%\.codex\setup, where the setup skills look for it;
#   3. builds the rules file %USERPROFILE%\.codex\AGENTS.md from global\rules.md, global\rules-chatgpt.md,
#      local\personal.md and profiles\ (ChatGPT cannot import files, so they are written into one block);
#      local\personal.md, the person's own file that git ignores, is made from global\personal.example.md when
#      it is missing (SU-Q90, SU-Q104);
#   4. adds a session-start hook to %USERPROFILE%\.codex\hooks.json that pulls this repo, refreshes the skill
#      links and rebuilds the rules file. ChatGPT runs a new or changed hook only after you trust it: Settings,
#      Hooks, in the app.
# It also warns when the git on the path is too old for ChatGPT's sandbox on Windows (SU-Q71).
# The hook links a skill added to global\skills and removes the link of one removed (SU-Q110). Run this again
# after the repo's folder is moved.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File "<repo>\install-chatgpt.ps1"
# Windows PowerShell 5.1 compatible. Junctions need no admin rights.

param(
    [string]$AgentsDir = (Join-Path $env:USERPROFILE '.agents'),   # override only for testing
    [string]$CodexDir  = (Join-Path $env:USERPROFILE '.codex')     # override only for testing
)

$ErrorActionPreference = 'Stop'
$repo       = $PSScriptRoot
$repoSkills = Join-Path $repo 'global\skills'
$target     = Join-Path $AgentsDir 'skills'
$utf8       = New-Object System.Text.UTF8Encoding $false
$stamp      = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$backup     = Join-Path $CodexDir "agent-setup-backups\$stamp"
$hookMarker = 'global/hooks/session-start.ps1'     # how this repo's own hook entry is recognised

# PS 5.1 bug: ConvertTo-Json serialises arrays as {value, Count} while this type data is loaded.
Remove-TypeData System.Array -ErrorAction SilentlyContinue

. (Join-Path $repo 'global\hooks\skill-links.ps1')     # Get-LinkTarget, Test-SamePath, Sync-SkillLinks

function Say($msg) { Write-Host "  $msg" }

function Save-Backup($path) {
    New-Item -ItemType Directory -Force -Path $backup | Out-Null
    Copy-Item -LiteralPath $path -Destination $backup
    Say "saved the old $(Split-Path -Leaf $path) to $backup"
}

Write-Host "agent-setup for ChatGPT, from $repo"
if (-not (Test-Path -LiteralPath $repoSkills)) { throw "global\skills missing: run this from the agent-setup repo." }
New-Item -ItemType Directory -Force -Path $CodexDir | Out-Null

# 1. one junction per skill (skill-links.ps1, shared with install.ps1 and both session-start hooks)
$links = Sync-SkillLinks $repoSkills $target
Format-SkillLinkLines $links $target | ForEach-Object { Say $_ }
$linkFailed = @($links | Where-Object { $_.Action -eq 'failed' }).Count -gt 0

# 2. %USERPROFILE%\.codex\setup -> repo
$setupLink = Join-Path $CodexDir 'setup'
$current = Get-LinkTarget $setupLink
if ($null -eq $current) {
    New-Item -ItemType Junction -Path $setupLink -Target $repo | Out-Null
    Say "junction $setupLink -> $repo"
} elseif ($current -eq '') {
    throw "$setupLink exists and is not a link; move it away first."
} elseif (Test-SamePath $current $repo) {
    Say "junction $setupLink ok"
} else {
    cmd /c rmdir "$setupLink" | Out-Null
    New-Item -ItemType Junction -Path $setupLink -Target $repo | Out-Null
    Say "junction $setupLink re-pointed -> $repo (was $current)"
}

# 3. the rules file
$agentsMd = Join-Path $CodexDir 'AGENTS.md'
if (Test-Path -LiteralPath $agentsMd) {
    $had = [IO.File]::ReadAllText($agentsMd, $utf8)
    if ($had.Trim() -and ($had.IndexOf('<!-- agent-setup:begin') -lt 0)) {
        Save-Backup $agentsMd      # a rules file of the user's own: kept on top of the built block, and backed up
    }
}
& (Join-Path $repo 'global\hooks\build-agents-md.ps1') -CodexDir $CodexDir -Quiet
$bytes = (Get-Item -LiteralPath $agentsMd).Length
Say "rules file $agentsMd built ($bytes bytes of ChatGPT's 32768 for all rules files together)"

# 4. the session-start hook
$hooksPath = Join-Path $CodexDir 'hooks.json'
$script    = ((Join-Path $setupLink 'global\hooks\session-start.ps1') -replace '\\', '/')
$command   = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$script`""
$ours = [pscustomobject]@{
    matcher = 'startup|resume'
    hooks   = @([pscustomobject]@{
        type          = 'command'
        command       = $command
        timeout       = 60
        statusMessage = 'Updating agent-setup'
    })
}
$oldJson = ''
if (Test-Path -LiteralPath $hooksPath) {
    $oldJson = [IO.File]::ReadAllText($hooksPath, $utf8)
    $hooksDoc = $oldJson | ConvertFrom-Json
} else {
    $hooksDoc = [pscustomobject]@{}
}
if ($null -eq $hooksDoc.PSObject.Properties['hooks']) {
    $hooksDoc | Add-Member -NotePropertyName hooks -NotePropertyValue ([pscustomobject]@{})
}
$kept = @()
if ($hooksDoc.hooks.PSObject.Properties['SessionStart']) {
    # drop the entry this repo installed earlier, keep everything else
    $kept = @($hooksDoc.hooks.SessionStart | Where-Object { -not (($_ | ConvertTo-Json -Depth 32 -Compress) -like "*$hookMarker*") })
}
$hooksDoc.hooks | Add-Member -NotePropertyName SessionStart -NotePropertyValue (@($kept) + @($ours)) -Force
$newJson = ($hooksDoc | ConvertTo-Json -Depth 32) + "`n"
if ($newJson.Replace("`r`n", "`n") -ne $oldJson.Replace("`r`n", "`n")) {
    if ($oldJson) { Save-Backup $hooksPath }
    [IO.File]::WriteAllText($hooksPath, $newJson, $utf8)
    Say "session-start hook written to $hooksPath"
    $hookChanged = $true
} else {
    Say "session-start hook ok"
    $hookChanged = $false
}

# 5. the git on the path: on Windows, ChatGPT's sandbox runs commands as another Windows user and hands git an
#    exception for the project folder. Git 2.44.0 does not accept its form; 2.53.0 and 2.56.1 do (tested
#    2026-11-21, SU-Q71; the lowest version that works is not determined).
$gitOldest = [version]'2.53'
$gitLine = ''
try { $gitLine = [string](& git --version) } catch {}
$gitOld = $false
if ($gitLine -match '(\d+)\.(\d+)') {
    $gitHas = [version]"$($Matches[1]).$($Matches[2])"
    if ($gitHas -lt $gitOldest) {
        $gitOld = $true
        Say "WARNING git $gitHas is older than $gitOldest, the oldest version tested with ChatGPT's sandbox"
    } else {
        Say "git $gitHas ok"
    }
} else {
    Say "WARNING git was not found on the path: the session-start hook cannot pull the repo"
}

Write-Host "done. Next:"
$step = 1
Write-Host "  $step. Restart the ChatGPT desktop app."
if ($hookChanged) {
    $step++
    Write-Host "  $step. Trust the new hook once: Settings, Hooks (or 'Review hooks' under the message box). Until then"
    Write-Host "     ChatGPT skips it, and the repo is not pulled at the start of a chat."
}
if ($linkFailed) {
    $step++
    Write-Host "  $step. Some skills could not be linked (the FAILED lines above): fix the cause and run this again."
}
if ($gitOld) {
    $step++
    Write-Host "  $step. Update Git for Windows (git-scm.com). With git $gitHas, every git command a ChatGPT chat runs in a"
    Write-Host "     project is refused inside its sandbox (`"dubious ownership`") and repeated with an approval."
}
