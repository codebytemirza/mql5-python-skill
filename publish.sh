#!/usr/bin/env bash
# Create a GitHub repo for this skill and push it.
#
#   ./publish.sh <owner>/<repo> [public|private]
#
# Needs the GitHub CLI:  https://cli.github.com  (gh auth login)
set -euo pipefail

SLUG="${1:-}"
VISIBILITY="${2:-public}"

if [ -z "$SLUG" ]; then
  echo "usage: ./publish.sh <owner>/<repo> [public|private]" >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "the GitHub CLI is required:  https://cli.github.com  then  gh auth login" >&2
  exit 1
fi

cd "$(dirname "$0")"

if [ ! -d .git ]; then
  git init -b main
  git add -A
  git commit -m "mql5-python skill: MetaTrader5 Python agent handbook"
fi

if gh repo view "$SLUG" >/dev/null 2>&1; then
  echo "repo $SLUG already exists - pushing to it"
else
  gh repo create "$SLUG" --"$VISIBILITY" --description \
    "Agent skill for the MetaTrader5 Python package: verified MQL5 docs mirror, API reference, cookbook and live-measured behaviour" \
    --source . --remote origin --push
  echo "created and pushed $SLUG"
  exit 0
fi

git push -u origin main
echo "pushed to $SLUG"
