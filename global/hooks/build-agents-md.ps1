# build-agents-md.ps1: build ChatGPT's global rules file from this repo (SU-Q60). Safe to re-run.
# ChatGPT (the desktop app, Codex) reads %USERPROFILE%\.codex\AGENTS.md and cannot import another file, so the
# shared rules, the ChatGPT part, both profiles and the lines about the person are written into it as one block
# between two marker lines. Text outside the block is the user's own and is kept.
# The lines about the person are local\personal.md, which git ignores (SU-Q90); when it is missing it is made from
# global\personal.example.md and one line says so, also with -Quiet (SU-Q101).
# Called by install-chatgpt.ps1 and by the session-start hook (session-start.ps1); writes only when the block
# changed. Prints one line when it wrote, nothing otherwise. Windows PowerShell 5.1 compatible.

param(
    [string]$CodexDir = (Join-Path $env:USERPROFILE '.codex'),
    [switch]$Quiet      # print nothing when the file was written
)

$ErrorActionPreference = 'Stop'
$repo  = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)   # <repo>\global\hooks -> <repo>
$utf8  = New-Object System.Text.UTF8Encoding $false
$begin = '<!-- agent-setup:begin (built from the agent-setup repo; change global/rules.md, global/rules-chatgpt.md, local/personal.md or profiles/ there, not this block) -->'
$end   = '<!-- agent-setup:end -->'
$limit = 32768     # ChatGPT's default limit for all its rules files together (project_doc_max_bytes)

function Read-Part($relative) {
    $path = Join-Path $repo $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "missing $relative in $repo" }
    return [IO.File]::ReadAllText($path, $utf8).Replace("`r`n", "`n").Trim()
}

. (Join-Path $PSScriptRoot 'local-files.ps1')     # Initialize-LocalFile
$made = Initialize-LocalFile $repo 'personal.md'
if ($made) {
    # also on a PC that has pulled SU-Q90 and not yet rerun an install: the chat hears that the file waits
    Write-Output "agent-setup: $made ($(Join-Path $repo 'local\personal.md')). Until then the rules file holds no lines about the user; tell the user."
}

# the order ChatGPT reads them in: shared rules, the ChatGPT part (it ends by introducing the profiles),
# the two profiles, the lines about the person
$parts = @(
    (Read-Part 'global\rules.md'),
    (Read-Part 'global\rules-chatgpt.md'),
    (Read-Part 'profiles\code.md'),
    (Read-Part 'profiles\docs.md'),
    (Read-Part 'local\personal.md')
)
$block = $begin + "`n`n" + ($parts -join "`n`n") + "`n`n" + $end

$target = Join-Path $CodexDir 'AGENTS.md'
$old = ''
if (Test-Path -LiteralPath $target) { $old = [IO.File]::ReadAllText($target, $utf8).Replace("`r`n", "`n") }

$i = $old.IndexOf('<!-- agent-setup:begin')
$j = $old.IndexOf($end)
if ($i -ge 0 -and $j -gt $i) {
    $new = $old.Substring(0, $i) + $block + $old.Substring($j + $end.Length)
} elseif ($old.Trim() -eq '') {
    $new = $block + "`n"
} else {
    $new = $old.TrimEnd() + "`n`n" + $block + "`n"      # the user's own text stays on top
}

if ($new -ne $old) {
    New-Item -ItemType Directory -Force -Path $CodexDir | Out-Null
    [IO.File]::WriteAllText($target, $new, $utf8)
    $bytes = $utf8.GetByteCount($new)
    if (-not $Quiet) {
        Write-Output "agent-setup: rules file rebuilt ($bytes bytes): $target. It applies from the next chat."
        if ($bytes -gt ($limit - 8192)) {
            Write-Output "agent-setup: the rules file is within 8 KB of ChatGPT's $limit byte limit; a project's AGENTS.md may be cut short."
        }
    }
}
