# mql5-python skill

An agent skill for the `MetaTrader5` Python package: the official MQL5
documentation section mirrored and verified, plus the API surface and the
traps that only show up when you run it against a live terminal.

## Install with the skills CLI

This repository is already structured as a compatible skill package because it
contains a root-level `SKILL.md` and `skill.json` manifest.

```bash
# interactive install
npx skills add codebytemirza/mql5-python-skill

# install one specific skill from this repo
npx skills add codebytemirza/mql5-python-skill --skill mql5-python

# direct shorthand
npx skills add codebytemirza/mql5-python-skill@mql5-python

# global install for all projects
npx skills add codebytemirza/mql5-python-skill -g

# target a specific agent
npx skills add codebytemirza/mql5-python-skill -a claude-code

# non-interactive / CI
npx skills add codebytemirza/mql5-python-skill -y
```

The skill name exposed by this repo is `mql5-python`, so the shorthand form is:

```bash
npx skills add codebytemirza/mql5-python-skill@mql5-python
```

## Local/manual install

Copy the folder into your agent's skills directory and restart the agent.

```powershell
# opencode / claude-style agents
Copy-Item -Recurse mql5-python "$HOME\.config\opencode\skills\mql5-python"

# or, for agents that read ~/.agents/skills
Copy-Item -Recurse mql5-python "$HOME\.agents\skills\mql5-python"
```

Then ask the agent for something like *"write a script that pulls EURUSD M1 bars with the MetaTrader5 Python package"*.

Verify the install:

```powershell
.\.venv\Scripts\python.exe .\scripts\verify_install.py
```

## Publish it for others

```bash
./publish.sh yourname/mql5-python-skill public
```

The script initialises the git repo, creates the GitHub repository and
pushes. It needs the GitHub CLI (`gh auth login`).

**Before publishing publicly:** `references/mirror/` is a verbatim copy of
MetaQuotes' documentation. See [NOTICE.md](NOTICE.md) - removing that
folder makes the skill redistributable without the third-party text; the
agent's own reference material stands on its own and links back to the
original pages.

## Set up the package in your project

```powershell
.\scripts\install.ps1                 # creates .venv and installs MetaTrader5
.\.venv\Scripts\python.exe .\scripts\smoke_test.py
```

Requirements: **Windows**, and a **running MetaTrader 5 terminal** signed
in to an account. The package is only an IPC client to that terminal.

## Layout

```
mql5-python/
  SKILL.md            entry point
  README.md           this file
  skill.json          version and provenance
  references/         quickstart, api, cookbook, trading, constants,
                      troubleshooting, live, overview
  references/mirror/  the 33-page official documentation mirror
  data/api.json       machine-readable API surface
  scripts/            install, verify and runnable examples
```

## What it contains

| | |
| --- | --- |
| Official docs mirrored | 33 pages, crawled and verified |
| Functions documented | 32 |
| Constants listed | 223, with real values from the installed build |
| Live-verified | result field names, numpy dtypes, order round trip |

