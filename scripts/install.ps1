# Create a virtual environment and install the MetaTrader5 package.
#
#   .\install.ps1 [-TargetProjectDir .]
#
# Windows only: the MetaTrader5 package ships a native IPC client.
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
& $py -m pip install MetaTrader5
& $py -c "import MetaTrader5 as mt5; print('MetaTrader5', mt5.__version__, 'installed')"
