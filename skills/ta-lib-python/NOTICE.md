# Notice

## The skill itself

`SKILL.md`, `README.md`, `references/*.md` (except `references/mirror/`),
`data/api.json` and `scripts/*` were written for this skill and are covered by
the MIT licence of the parent repository.

## The mirrored documentation

`references/mirror/` is a copy of the official TA-Lib **Python wrapper**
documentation published at <https://ta-lib.github.io/ta-lib-python/>.

The TA-Lib project (both the C library and the Python wrapper) is distributed
under the **BSD 2-Clause Licence**, which permits redistribution of the
documentation as well as the code, provided the copyright notice and licence
text travel with it:

    Copyright (c) 2003-2025, TA-Lib Project Contributors
    All rights reserved.
    https://github.com/TA-Lib/ta-lib-python/blob/main/LICENSE

## The measured behaviour

`references/live.md` describes behaviour observed by running the installed
`TA-Lib` package. Those are observations, not upstream text.

## The TA-Lib C library is separate

This skill covers the **Python** package only. The C library it wraps is a
separate project with its own BSD 2-Clause licence; the Python package ships
prebuilt wheels for Windows and macOS, while on Linux the C library has to be
installed first.
