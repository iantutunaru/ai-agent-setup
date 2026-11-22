# install.ps1: link the agent-setup repo into ~/.claude (SU-Q07, SU-Q16). Safe to re-run.
# The person's own files live in local\ of the clone, which git ignores (SU-Q90); the install makes them from the
# examples in global\ when they are missing.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File "<repo>\install.ps1"
# Windows PowerShell 5.1 compatible. Junctions need no admin rights.

param([string]$ClaudeDir = (Join-Path $env:USERPROFILE '.claude'))   # override only for testing

$ErrorActionPreference = 'Stop'
$repo    = $PSScriptRoot
$claude  = $ClaudeDir
$stamp   = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$backup  = Join-Path $claude "agent-setup-backups\$stamp"
$utf8    = New-Object System.Text.UTF8Encoding $false
$importLine = '@~/.claude/setup/global/CLAUDE.md'      # the shared rules
$personalLine = '@~/.claude/setup/local/personal.md'   # the lines about the person (SU-Q56, SU-Q90)
$oldPersonalLine = '@~/.claude/setup/global/personal.md'   # where they were before SU-Q90
$projects = Split-Path -Parent $PSScriptRoot           # the folder the repo sits in holds the projects (SU-Q52)
$hookMarker = '.claude/setup/global/hooks/'
$local    = Join-Path $repo 'local'                   # the person's own files, ignored by git (SU-Q90)

# PS 5.1 bug: ConvertTo-Json serialises arrays as {value, Count} while this type data is loaded.
Remove-TypeData System.Array -ErrorAction SilentlyContinue

. (Join-Path $repo 'global\hooks\local-files.ps1')     # Initialize-LocalFile, Test-LocalFileIsExample
. (Join-Path $repo 'global\hooks\skill-links.ps1')     # Get-LinkTarget, Sync-SkillLinks and the move to them

function Say($msg) { Write-Host "  $msg" }

function Set-Junction($link, $target) {
    $current = Get-LinkTarget $link
    if ($current -eq $null) {
        New-Item -ItemType Junction -Path $link -Target $target | Out-Null
        Say "junction $link -> $target"
    } elseif ($current -eq '') {
        throw "$link exists and is not a link; move it away first."
    } elseif ((-not (Test-Path -LiteralPath $current)) -or ((Resolve-Path -LiteralPath $current).Path.TrimEnd('\') -ne (Resolve-Path -LiteralPath $target).Path.TrimEnd('\'))) {
        # also a link whose old target is gone, e.g. after the repo's folder was renamed (SU-Q69)
        cmd /c rmdir "$link" | Out-Null   # removes the link only, never the target's contents
        New-Item -ItemType Junction -Path $link -Target $target | Out-Null
        Say "junction $link re-pointed -> $target"
    } else {
        Say "junction $link ok"
    }
}

function Merge-Json($target, $source, $path) {
    foreach ($prop in $source.PSObject.Properties) {
        $name = $prop.Name
        $value = $prop.Value
        $here = if ($path) { "$path.$name" } else { $name }
        $existing = $target.PSObject.Properties[$name]
        if ($here -eq 'hooks') {
            if ($null -eq $existing) { $target | Add-Member -NotePropertyName hooks -NotePropertyValue ([pscustomobject]@{}); $existing = $target.PSObject.Properties['hooks'] }
            foreach ($event in $value.PSObject.Properties) {
                $old = @()
                if ($existing.Value.PSObject.Properties[$event.Name]) {
                    # drop entries this repo installed earlier, keep everything else
                    $old = @($existing.Value.($event.Name) | Where-Object { -not (($_ | ConvertTo-Json -Depth 32 -Compress) -like "*$hookMarker*") })
                }
                $new = @($old) + @($event.Value)
                $existing.Value | Add-Member -NotePropertyName $event.Name -NotePropertyValue $new -Force
            }
        } elseif ($null -ne $existing -and $existing.Value -is [System.Management.Automation.PSCustomObject] -and $value -is [System.Management.Automation.PSCustomObject]) {
            Merge-Json $existing.Value $value $here
        } else {
            $target | Add-Member -NotePropertyName $name -NotePropertyValue $value -Force
        }
    }
}

Write-Host "agent-setup install from $repo"
if (-not (Test-Path (Join-Path $repo 'global\CLAUDE.md'))) { throw "global\CLAUDE.md missing: run this from the agent-setup repo." }
New-Item -ItemType Directory -Force -Path $backup | Out-Null
Say "backups -> $backup"

# 1. ~/.claude/setup -> repo
Set-Junction (Join-Path $claude 'setup') $repo

# 2. ~/.claude/skills: a folder of the person's with one junction per skill of global\skills beside their own
#    skills (SU-Q98). The one junction an older install made is replaced; Anthropic's skills that a Claude program
#    wrote through it into global\skills\synced move out of the repo (SU-Q111).
$skills = Join-Path $claude 'skills'
$repoSkills = Join-Path $repo 'global\skills'
$did = Convert-SkillsJunction $skills $repoSkills
if ($did) { Say $did }
New-Item -ItemType Directory -Force -Path $skills | Out-Null
$did = Move-SyncedSkills $repoSkills $skills
if ($did) { Say $did }
$links = Sync-SkillLinks $repoSkills $skills
Format-SkillLinkLines $links $skills | ForEach-Object { Say $_ }
$linkFailed = @($links | Where-Object { $_.Action -eq 'failed' }).Count -gt 0

# 3. the person's own files in local\, which git ignores (SU-Q90): made from the examples when missing
foreach ($name in @('personal.md', 'settings.personal.json')) {
    $made = Initialize-LocalFile $repo $name
    if ($made) { Say $made }
}

# 4. ~/.claude/CLAUDE.md = two import lines: the shared rules and the lines about the person
$md = Join-Path $claude 'CLAUDE.md'
if (Test-Path -LiteralPath $md) {
    # a file holding only this repo's import lines (one before SU-Q56, two since, the second moved by SU-Q90) is
    # ours; anything else is backed up
    $ours = @($importLine, $personalLine, $oldPersonalLine)
    $other = @([IO.File]::ReadAllLines($md) | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' -and $ours -notcontains $_ })
    if ($other.Count -gt 0) {
        Copy-Item -LiteralPath $md -Destination (Join-Path $backup 'CLAUDE.md')
        Say "old ~/.claude/CLAUDE.md saved to the backup: merge anything worth keeping into global/CLAUDE.md"
    }
}
[IO.File]::WriteAllText($md, "$importLine`n$personalLine`n", $utf8)
Say "~/.claude/CLAUDE.md imports global/CLAUDE.md and local/personal.md"

# 5. merge global/settings.json, then local/settings.personal.json, into ~/.claude/settings.json
$settings = Join-Path $claude 'settings.json'
$fragment = [IO.File]::ReadAllText((Join-Path $repo 'global\settings.json')) | ConvertFrom-Json
if (Test-Path -LiteralPath $settings) {
    Copy-Item -LiteralPath $settings -Destination (Join-Path $backup 'settings.json')
    $current = [IO.File]::ReadAllText($settings) | ConvertFrom-Json
} else {
    $current = [pscustomobject]@{}
}
Merge-Json $current $fragment ''
# the personal fragment (the auto mode block): {{PROJECTS}} becomes this machine's projects folder. An untouched
# example is left out, so its placeholders never replace a description this machine already has (SU-Q102).
$personalPath = Join-Path $repo 'local\settings.personal.json'
if (Test-LocalFileIsExample $repo 'settings.personal.json') {
    Say "local\settings.personal.json is still the example: not merged"
} else {
    $projectsJson = $projects.Replace('\', '\\').Replace('"', '\"')
    $personal = [IO.File]::ReadAllText($personalPath).Replace('{{PROJECTS}}', $projectsJson) | ConvertFrom-Json
    Merge-Json $current $personal ''
    Say "projects folder in the auto mode block: $projects"
}
$json = $current | ConvertTo-Json -Depth 32
[IO.File]::WriteAllText($settings, $json, $utf8)
Say "~/.claude/settings.json merged"

Write-Host "done."
if ($linkFailed) {
    Write-Host "  Some skills could not be linked (the FAILED lines above): fix the cause and run this again."
}
if (Test-LocalFileIsExample $repo 'personal.md') {
    Write-Host "  Next: fill in $local\personal.md, the lines about you. It applies from the next chat."
}
if (Test-LocalFileIsExample $repo 'settings.personal.json') {
    Write-Host "  Next: fill in $local\settings.personal.json, what Claude's auto mode should know about your machines,"
    Write-Host "  then run this again."
}
