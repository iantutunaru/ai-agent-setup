# skill-links.ps1: one link per skill (SU-Q54, SU-Q98, SU-Q110, SU-Q111). Dot-sourced by install.ps1,
# install-chatgpt.ps1 and session-start.ps1; session-start.sh calls it through PowerShell when the links differ.
# Each skill folder of the repo's global\skills gets a junction of its own in an assistant's skills folder:
# %USERPROFILE%\.claude\skills for Claude Code, %USERPROFILE%\.agents\skills for ChatGPT. The person's own skill
# folders there are never touched, also when one has the name of a repo skill. A junction is removed with
# cmd /c rmdir, which removes the link only, never the target's contents.
# Windows PowerShell 5.1 compatible. Junctions need no admin rights.

# Not linked: Anthropic's own skills that a Claude program writes into ~/.claude/skills/synced (SU-Q37).
$script:SkillLinkSkip = @('synced')

function Get-LinkTarget([string]$path) {
    # the link's target; '' when the path exists and is not a link; $null when nothing is there
    $item = Get-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
    if ($null -eq $item) { return $null }
    if ($item.LinkType -eq 'Junction' -or $item.LinkType -eq 'SymbolicLink') { return [string]$item.Target }
    return ''
}

function Test-SamePath([string]$a, [string]$b) { return $a.TrimEnd('\') -ieq $b.TrimEnd('\') }

function Resolve-RealPath([string]$path) {
    # the path with every link along it replaced by its target, so that a repo reached through
    # %USERPROFILE%\.codex\setup or ~/.claude/setup compares equal to the clone's own folder
    $full = [IO.Path]::GetFullPath($path).TrimEnd('\')
    if ($full.StartsWith('\\')) { return $full }
    for ($round = 0; $round -lt 32; $round++) {
        $parts = $full.Split('\')
        $prefix = $parts[0] + '\'
        $changed = $false
        for ($i = 1; $i -lt $parts.Count; $i++) {
            $prefix = Join-Path $prefix $parts[$i]
            $item = Get-Item -LiteralPath $prefix -Force -ErrorAction SilentlyContinue
            if ($null -eq $item) { break }
            if ($item.LinkType -eq 'Junction' -or $item.LinkType -eq 'SymbolicLink') {
                $to = [string]$item.Target
                if (-not [IO.Path]::IsPathRooted($to)) { $to = Join-Path (Split-Path -Parent $prefix) $to }
                if ($i -lt $parts.Count - 1) { $to = Join-Path $to ($parts[($i + 1)..($parts.Count - 1)] -join '\') }
                $full = [IO.Path]::GetFullPath($to).TrimEnd('\')
                $changed = $true
                break
            }
        }
        if (-not $changed) { break }
    }
    return $full
}

function Get-SetupSkills([string]$RepoSkills) {
    # the repo's skill folders: each folder of global\skills that holds a SKILL.md, without synced
    return @(Get-ChildItem -LiteralPath $RepoSkills -Directory -Force |
        Where-Object { ($script:SkillLinkSkip -notcontains $_.Name) -and (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md')) })
}

function New-SkillLinkResult([string]$name, [string]$action, [string]$detail, [bool]$wanted = $true) {
    # Wanted: one of the repo's skills, as opposed to an old link that was removed (or could not be)
    return [pscustomobject]@{ Name = $name; Action = $action; Detail = $detail; Wanted = $wanted }
}

function Sync-SkillLinks([string]$RepoSkills, [string]$Target) {
    # links each skill of $RepoSkills into $Target and removes links that point into a setup repo's skills folder
    # but are no longer wanted. Returns one result per skill or link: Action is linked, relinked, ok, kept,
    # removed or failed. It never throws for one link; it throws only when $Target cannot be used at all.
    $real = Resolve-RealPath $RepoSkills
    if (-not (Test-Path -LiteralPath $real)) { throw "$RepoSkills not found" }
    $state = Get-LinkTarget $Target
    if ($null -ne $state -and $state -ne '') {
        throw "$Target is one link (to $state), not a folder: run install.ps1 again"
    }
    New-Item -ItemType Directory -Force -Path $Target -ErrorAction SilentlyContinue | Out-Null
    if (-not (Test-Path -LiteralPath $Target -PathType Container)) { throw "$Target is not a folder and cannot be made one" }

    $results = New-Object System.Collections.ArrayList
    $wanted = Get-SetupSkills $real
    foreach ($skill in $wanted) {
        $link = Join-Path $Target $skill.Name
        $current = Get-LinkTarget $link
        try {
            if ($null -eq $current) {
                New-Item -ItemType Junction -Path $link -Target $skill.FullName -ErrorAction Stop | Out-Null
                [void]$results.Add((New-SkillLinkResult $skill.Name 'linked' ''))
            } elseif ($current -eq '') {
                [void]$results.Add((New-SkillLinkResult $skill.Name 'kept' ''))
            } elseif ((Test-Path -LiteralPath $current) -and (Test-SamePath (Resolve-RealPath $current) $skill.FullName)) {
                [void]$results.Add((New-SkillLinkResult $skill.Name 'ok' ''))
            } else {
                cmd /c rmdir "$link" 2>&1 | Out-Null
                if (Test-Path -LiteralPath $link) { throw "could not remove the old link to $current" }
                New-Item -ItemType Junction -Path $link -Target $skill.FullName -ErrorAction Stop | Out-Null
                [void]$results.Add((New-SkillLinkResult $skill.Name 'relinked' $current))
            }
        } catch {
            [void]$results.Add((New-SkillLinkResult $skill.Name 'failed' $_.Exception.Message))
        }
    }

    # links into a setup repo's skills folder that are no longer wanted: a skill removed, renamed or now skipped,
    # or a link left behind by the repo's old folder
    $names = @($wanted | ForEach-Object { $_.Name })
    $prefix = $real.ToLower() + '\'
    foreach ($child in @(Get-ChildItem -LiteralPath $Target -Force)) {
        if ($names -contains $child.Name) { continue }
        $current = Get-LinkTarget $child.FullName
        if (-not $current) { continue }
        $alive = Test-Path -LiteralPath $current
        $inRepo = $alive -and (Resolve-RealPath $current).ToLower().StartsWith($prefix)
        $dead = (-not $alive) -and ($current -match '\\global\\skills\\[^\\]+\\?$')
        if ($inRepo -or $dead) {
            cmd /c rmdir "$($child.FullName)" 2>&1 | Out-Null
            if (Test-Path -LiteralPath $child.FullName) {
                [void]$results.Add((New-SkillLinkResult $child.Name 'failed' "could not remove the link to $current" $false))
            } else {
                [void]$results.Add((New-SkillLinkResult $child.Name 'removed' $current $false))
            }
        }
    }
    return ,$results
}

function Format-SkillLinkLines($results, [string]$Target) {
    # what the installs print: one line per skill, then a count
    $lines = @()
    foreach ($r in $results) {
        switch ($r.Action) {
            'linked'   { $lines += "linked  $($r.Name)" }
            'relinked' { $lines += "linked  $($r.Name) (was a link to $($r.Detail))" }
            'ok'       { $lines += "ok      $($r.Name)" }
            'kept'     { $lines += "kept    $($r.Name): a folder of that name is already there and is not a link; not touched" }
            'removed'  { $lines += "removed $($r.Name): no longer among the setup's skills" }
            'failed'   { $lines += "FAILED  $($r.Name): $($r.Detail)" }
        }
    }
    $done = @($results | Where-Object { @('linked', 'relinked', 'ok') -contains $_.Action }).Count
    $all = @($results | Where-Object { $_.Wanted }).Count
    $lines += "$done of $all skills linked in $Target"
    return $lines
}

function Get-SkillLinkHookLine($results, [string]$Target) {
    # what the session-start hooks print: nothing when no link changed, else one line. It becomes model context.
    $added   = @($results | Where-Object { @('linked', 'relinked') -contains $_.Action } | ForEach-Object { $_.Name })
    $removed = @($results | Where-Object { $_.Action -eq 'removed' } | ForEach-Object { $_.Name })
    $failed  = @($results | Where-Object { $_.Action -eq 'failed' })
    $parts = @()
    if ($added.Count)   { $parts += "linked $($added -join ', ')" }
    if ($removed.Count) { $parts += "removed $($removed -join ', ')" }
    if ($failed.Count)  {
        # the names, and the first error only: one cause usually stops them all
        $parts += "could not link $(($failed | ForEach-Object { $_.Name }) -join ', ') ($($failed[0].Detail))"
    }
    if (-not $parts.Count) { return '' }
    return "agent-setup: skill links in ${Target}: $($parts -join '; ')."
}

function Convert-SkillsJunction([string]$Skills, [string]$RepoSkills) {
    # the old install made ~/.claude/skills one junction to global\skills (SU-Q10); now it is a plain folder
    # (SU-Q98). Removes such a junction (the link only) and returns what it did, or '' when there was none.
    $current = Get-LinkTarget $Skills
    if ($null -eq $current -or $current -eq '') { return '' }
    $alive = Test-Path -LiteralPath $current
    $ours = $alive -and (Test-SamePath (Resolve-RealPath $current) (Resolve-RealPath $RepoSkills))
    $setupLike = $current -match '\\global\\skills\\?$'
    if (-not ($ours -or (-not $alive) -or $setupLike)) {
        throw "$Skills is a link to $current, not to a setup repo's skills folder; move it away first."
    }
    cmd /c rmdir "$Skills" 2>&1 | Out-Null
    if (Test-Path -LiteralPath $Skills) { throw "could not remove the link $Skills" }
    New-Item -ItemType Directory -Path $Skills -ErrorAction Stop | Out-Null
    return "skills was one link to $current; now a folder of its own with one link per skill"
}

function Move-SyncedSkills([string]$RepoSkills, [string]$Skills) {
    # Anthropic's own skills, which a Claude program wrote into global\skills\synced through the old junction,
    # move to ~/.claude/skills/synced, where the program writes them once that folder is plain (SU-Q111).
    # Returns what it did, or '' when there is nothing to move.
    $from = Join-Path $RepoSkills 'synced'
    $to = Join-Path $Skills 'synced'
    $kind = Get-LinkTarget $from
    if ($null -eq $kind) { return '' }
    if ($kind -ne '') { return "global\skills\synced is a link, not a folder: left as it is" }
    if ($null -ne (Get-LinkTarget $to)) {
        return "global\skills\synced is still in the repo and $to exists too: left both; the repo's copy can go by hand"
    }
    $links = @(Get-ChildItem -LiteralPath $from -Recurse -Force -Attributes ReparsePoint -ErrorAction SilentlyContinue)
    if ($links.Count) { return "global\skills\synced holds links: not moved; move it to $to by hand" }
    # copy, check, then delete: a move across drives (repo on one, profile on another) is not a rename
    Copy-Item -LiteralPath $from -Destination $to -Recurse -Force -ErrorAction Stop
    $had = @(Get-ChildItem -LiteralPath $from -Recurse -Force -File).Count
    $has = @(Get-ChildItem -LiteralPath $to -Recurse -Force -File).Count
    if ($had -ne $has) {
        throw "copying global\skills\synced to $to gave $has of $had files; the repo's copy is kept"
    }
    Remove-Item -LiteralPath $from -Recurse -Force -ErrorAction Stop
    return "moved global\skills\synced (Anthropic's own skills, $had files) to $to"
}
