#!/usr/bin/env bash
# Create a virtual environment and install the MetaTrader5 package.
#
#   ./install.sh [target-project-dir]
#
# Windows only in practice: the MetaTrader5 package ships a native IPC client
# and will not import on Linux or macOS. Use install.ps1 there.
set -euo pipefail

TARGET="${1:-.}"
cd "$TARGET"

if [ ! -d ".venv" ]; then
  echo "creating .venv in $TARGET"
  python -m venv .venv
fi

if [ -x ".venv/Scripts/python.exe" ]; then
  PY=".venv/Scripts/python.exe"
elif [ -x ".venv/bin/python" ]; then
  PY=".venv/bin/python"
else
  echo "no interpreter found in .venv" >&2
  exit 1
fi

"$PY" -m pip install --upgrade pip
"$PY" -m pip install MetaTrader5
"$PY" -c "import MetaTrader5 as mt5; print('MetaTrader5', mt5.__version__, 'installed')"
