# local-files.ps1: each person's own files (SU-Q90, SU-Q102). Dot-sourced by install.ps1 and build-agents-md.ps1.
# They live in <repo>\local\, which git ignores, so they never enter the shared history. Each has a tracked
# example beside the shared files: local\personal.md <- global\personal.example.md, and so on.
# Windows PowerShell 5.1 compatible.

function Get-ExamplePath([string]$repo, [string]$name) {
    $stem = [IO.Path]::GetFileNameWithoutExtension($name)
    $ext  = [IO.Path]::GetExtension($name)
    return (Join-Path $repo "global\$stem.example$ext")
}

function Initialize-LocalFile([string]$repo, [string]$name) {
    # makes local\<name> from its example when it is missing; returns what it did, or '' when the file was there
    $path = Join-Path $repo "local\$name"
    if (Test-Path -LiteralPath $path) { return '' }
    $example = Get-ExamplePath $repo $name
    if (-not (Test-Path -LiteralPath $example)) { throw "missing global\$(Split-Path -Leaf $example) in $repo" }
    New-Item -ItemType Directory -Force -Path (Join-Path $repo 'local') | Out-Null
    Copy-Item -LiteralPath $example -Destination $path
    return "created local\$name from global\$(Split-Path -Leaf $example): fill in your own lines"
}

function Test-LocalFileIsExample([string]$repo, [string]$name) {
    # true while local\<name> is still the untouched example (line endings and outer blank lines aside)
    $utf8 = New-Object System.Text.UTF8Encoding $false
    $mine = [IO.File]::ReadAllText((Join-Path $repo "local\$name"), $utf8).Replace("`r`n", "`n").Trim()
    $example = [IO.File]::ReadAllText((Get-ExamplePath $repo $name), $utf8).Replace("`r`n", "`n").Trim()
    return ($mine -eq $example)
}
