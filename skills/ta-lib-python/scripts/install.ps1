# Create a virtual environment and install TA-Lib.
param(
    [string]$TargetProjectDir = "."
)

$ErrorActionPreference = "Stop"
Set-Location $TargetProjectDir

if (-not (Test-Path ".venv")) {
    Write-Host "creating .venv in $TargetProjectDir"
    python -m venv .venv
}

$py = Join-Path (Get-Location) ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    throw "no interpreter found in .venv"
}

& $py -m pip install --upgrade pip
& $py -m pip install numpy TA-Lib
& $py -c "import talib; print('TA-Lib', talib.__version__, 'installed')"
Write-Host ""
Write-Host "On Linux the TA-Lib C library must be installed first -"
Write-Host "see references/mirror/install.md"
