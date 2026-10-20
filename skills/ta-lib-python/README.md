# ta-lib-python skill

An agent skill for the `TA-Lib` Python package: the official documentation
mirrored, plus the API surface read from the installed build and the
behaviour measured by running it.

## Install

```bash
npx skills add codebytemirza/mql5-python-skill --full-depth --skill ta-lib-python

# or, from a clone of this repo
cd skills/ta-lib-python
./scripts/install.ps1
```

`--full-depth` is required: without it the CLI only finds the skill at the
repository root and never looks into `skills/`.

## Contents

| | |
| --- | --- |
| Functions documented | 201, in 10 groups |
| Official docs mirrored | 16 pages |
| API surface as data | `data/api.json` |

## Requirements

Python 3.8+, `numpy`, and `TA-Lib`. On Linux the TA-Lib C library must be
installed first; Windows and macOS resolve to a prebuilt wheel.

