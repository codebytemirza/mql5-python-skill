# Notice

This skill contains two kinds of material.

## 1. The skill itself - MIT licensed

`SKILL.md`, `README.md`, `references/*.md` (except `references/mirror/`),
`data/api.json`, `scripts/*` and `skill.json` were written for this skill and
are covered by the MIT licence in `LICENSE`.

## 2. The mirrored documentation - owned by MetaQuotes Ltd.

`references/mirror/` is a **verbatim copy** of the public MQL5 documentation
section *Python Integration for MetaTrader 5*
(https://www.mql5.com/en/docs/python_metatrader5), which is the property of
MetaQuotes Ltd. It is included so the skill works offline and so every claim
can be traced back to its source page.

**If you redistribute this skill publicly, consider removing
`references/mirror/`** and letting the agent fetch the pages from mql5.com
instead. The skill's own reference material (the API summary, the cookbook,
the measured behaviour) stands on its own, and the links in it point at the
original pages.

The mirror also records its own provenance:

- `references/mirror/report.md` - how the crawl was performed and verified
- `references/mirror/verification.md` - the checks that were run
- `references/mirror/tree.md` - the page tree
- `references/mirror/pages/*.md` - one file per page, each with a source URL

## 3. Measured behaviour

`references/live.md` and `references/trading.md` describe behaviour that was
observed by running the `MetaTrader5` package against a live MetaTrader 5
terminal on a demo account. Those are observations, not MetaQuotes text, and
are covered by the MIT licence above.
