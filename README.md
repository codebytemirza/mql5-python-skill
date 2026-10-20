# Agent skills for trading with Python

Two agent skills, each with the official documentation mirrored and
verified, plus the API surface read from the **installed** package and the
behaviour measured by running it.

| Skill | Package | What it covers |
| --- | --- | --- |
| `mql5-python` | `MetaTrader5` | connect to a running MetaTrader 5 terminal, pull bars/ticks/depth, place and close orders |
| `ta-lib-python` | `TA-Lib` | 201 technical-analysis functions: moving averages, momentum, volatility, volume, candlestick patterns, statistics |

## Install

```bash
# both skills, into the current project
npx skills add codebytemirza/mql5-python-skill --full-depth

# just one of them
npx skills add codebytemirza/mql5-python-skill --full-depth --skill ta-lib-python

# pick the agent, install globally, no prompts
npx skills add codebytemirza/mql5-python-skill --full-depth -a opencode -g -y

# see what is in the repo before installing
npx skills add codebytemirza/mql5-python-skill --full-depth --list

# copy instead of symlinking (Windows, or a shared install)
npx skills add codebytemirza/mql5-python-skill --full-depth -a opencode -g -y --copy
```

> **Use `--full-depth`.** Without it the CLI only finds the skill at the
> repository root (`mql5-python`) and stops there. With `--full-depth` it
> also finds the nested `skills/ta-lib-python/`.

`skills` needs **Node.js 22.20 or later** and supports OpenCode, Claude Code,
Codex, Cursor and 70+ other agents. It installs a canonical copy to
`~/.agents/skills/<skill>` and then links (or copies, with `--copy`) it into
each selected agent's skills directory.

Without the CLI, copy the folder yourself:

```powershell
Copy-Item -Recurse mql5-python "$HOME\.agents\skills\mql5-python"
Copy-Item -Recurse mql5-python "$HOME\.config\opencode\skills\mql5-python"
Copy-Item -Recurse skills\ta-lib-python "$HOME\.agents\skills\ta-lib-python"
```

Then ask the agent for something like *"write a script that pulls EURUSD
M1 bars with the MetaTrader5 Python package"*.

Verify the install:

```powershell
.\.venv\Scripts\python.exe .\scripts\verify_install.py
```

## Publish it for others

```bash
./publish.sh <owner>/<repo> public
```

The script initialises the git repo, creates the GitHub repository and
pushes. It needs the GitHub CLI (`gh auth login`).

**Before publishing publicly:** `references/mirror/` holds third-party
documentation. The MetaTrader5 mirror is MetaQuotes' text; the TA-Lib mirror
is BSD-2-Clause and fine to redistribute. See [NOTICE.md](NOTICE.md) and
[skills/ta-lib-python/NOTICE.md](skills/ta-lib-python/NOTICE.md).

## Layout

```
mql5-python-skill/          <- the mql5-python skill (root)
  SKILL.md
  README.md
  NOTICE.md  LICENSE  skill.json
  references/    quickstart, api, cookbook, trading, constants,
                 troubleshooting, live, overview
  references/mirror/  the 33-page official documentation mirror
  data/api.json       machine-readable API surface
  scripts/            install, verify and runnable examples

skills/
  ta-lib-python/      <- the ta-lib-python skill
    SKILL.md  README.md  NOTICE.md
    references/       quickstart, api, functions, constants,
                     troubleshooting, cookbook, live
    references/mirror/ the 16-page official documentation mirror
    data/api.json
    scripts/           install and runnable examples
```

## What is in each

| | mql5-python | ta-lib-python |
| --- | --- | --- |
| Functions documented | 32 | 201 |
| Constants listed | 223, real values from the installed build | MA types, flags, pattern values |
| Official docs mirrored | 33 pages | 16 pages |
| Live-verified | terminal session, order round trip | output shapes, lookbacks, streaming API |

