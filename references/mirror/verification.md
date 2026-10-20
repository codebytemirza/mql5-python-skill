# Verification report

Generated: 2026-10-20T11:34:43+00:00

## 1. Root re-scan (live)

- Root re-fetched live: HTTP 200, 33 in-scope links in content, 32 in the sidebar.
- Union of live in-scope links: **33**.
- All of them present in `visited` or `failed`: **yes**.

| # | live in-scope link | in urls.txt | page file |
| --- | --- | --- | --- |
| 1 | `https://www.mql5.com/en/docs/python_metatrader5` | yes | python_metatrader5.md |
| 2 | `https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py` | yes | mt5accountinfo_py.md |
| 3 | `https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py` | yes | mt5copyratesfrom_py.md |
| 4 | `https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py` | yes | mt5copyratesfrompos_py.md |
| 5 | `https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py` | yes | mt5copyratesrange_py.md |
| 6 | `https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py` | yes | mt5copyticksfrom_py.md |
| 7 | `https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py` | yes | mt5copyticksrange_py.md |
| 8 | `https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py` | yes | mt5historydealsget_py.md |
| 9 | `https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py` | yes | mt5historydealstotal_py.md |
| 10 | `https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py` | yes | mt5historyordersget_py.md |
| 11 | `https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py` | yes | mt5historyorderstotal_py.md |
| 12 | `https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py` | yes | mt5initialize_py.md |
| 13 | `https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py` | yes | mt5lasterror_py.md |
| 14 | `https://www.mql5.com/en/docs/python_metatrader5/mt5login_py` | yes | mt5login_py.md |
| 15 | `https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py` | yes | mt5marketbookadd_py.md |
| 16 | `https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py` | yes | mt5marketbookget_py.md |
| 17 | `https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py` | yes | mt5marketbookrelease_py.md |
| 18 | `https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py` | yes | mt5ordercalcmargin_py.md |
| 19 | `https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py` | yes | mt5ordercalcprofit_py.md |
| 20 | `https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py` | yes | mt5ordercheck_py.md |
| 21 | `https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py` | yes | mt5ordersend_py.md |
| 22 | `https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py` | yes | mt5ordersget_py.md |
| 23 | `https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py` | yes | mt5orderstotal_py.md |
| 24 | `https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py` | yes | mt5positionsget_py.md |
| 25 | `https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py` | yes | mt5positionstotal_py.md |
| 26 | `https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py` | yes | mt5shutdown_py.md |
| 27 | `https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py` | yes | mt5symbolinfo_py.md |
| 28 | `https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py` | yes | mt5symbolinfotick_py.md |
| 29 | `https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py` | yes | mt5symbolselect_py.md |
| 30 | `https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py` | yes | mt5symbolsget_py.md |
| 31 | `https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py` | yes | mt5symbolstotal_py.md |
| 32 | `https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py` | yes | mt5terminalinfo_py.md |
| 33 | `https://www.mql5.com/en/docs/python_metatrader5/mt5version_py` | yes | mt5version_py.md |

## 2. urls.txt -> pages/ coverage

- URLs in `urls.txt`: **33**
- Markdown files in `pages/`: **33**
- URLs without a page file (and not in failed.txt): **0**
- Orphan page files / unmatched: **0**

## 3. Spot checks

Spot-checked pages (random seed 20261020): `mt5historydealstotal_py`, `mt5copyratesrange_py`, `mt5ordersend_py`, `mt5ordersget_py`, `mt5marketbookrelease_py`, `mt5ordercalcprofit_py`, `python_metatrader5`

| page | signatures (src/md) | params (src/md) | enum tables (src/md) | enum rows (src/md) | code blocks (src/md) | code text identical | nav/ad leak |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mt5historydealstotal_py` | 1/1 | 2/2 | 0/0 | 0/0 | 2/2 | yes | none |
| `mt5copyratesrange_py` | 1/1 | 4/4 | 0/0 | 0/0 | 2/2 | yes | none |
| `mt5ordersend_py` | 1/1 | 1/1 | 1/1 | 17/17 | 2/2 | yes | none |
| `mt5ordersget_py` | 4/4 | 3/3 | 0/0 | 0/0 | 5/5 | yes | none |
| `mt5marketbookrelease_py` | 1/1 | 1/1 | 0/0 | 0/0 | 1/1 | yes | none |
| `mt5ordercalcprofit_py` | 1/1 | 5/5 | 0/0 | 0/0 | 2/2 | yes | none |
| `python_metatrader5` | 0/0 | 0/0 | 1/1 | 32/32 | 6/6 | yes | none |

Notes:

- *signatures* counts the code blocks that are function signatures,
  source-side vs. markdown-side.
- *code text identical* checks that every code block found in the
  source HTML appears verbatim in the generated markdown.
- *nav/ad leak* scans the generated markdown for site chrome
  (footer, cookie, login, docs-nav, ads).

## 3b. Full-coverage check (all 33 pages)

Every fetched page is compared against its source HTML: all code blocks
must appear verbatim, all parameters must be present in the parameter
table, and all enum/constant table rows must be present.

| page | code blocks ok | params ok | enum rows ok | text ok |
| --- | --- | --- | --- | --- |
| `mt5positionsget_py` | yes | yes | yes | yes |
| `mt5ordersget_py` | yes | yes | yes | yes |
| `mt5login_py` | yes | yes | yes | yes |
| `mt5positionstotal_py` | yes | yes | yes | yes |
| `mt5historydealsget_py` | yes | yes | yes | yes |
| `mt5version_py` | yes | yes | yes | yes |
| `mt5copyratesrange_py` | yes | yes | yes | yes |
| `mt5copyratesfrompos_py` | yes | yes | yes | yes |
| `mt5symbolstotal_py` | yes | yes | yes | yes |
| `mt5marketbookadd_py` | yes | yes | yes | yes |
| `mt5initialize_py` | yes | yes | yes | yes |
| `mt5symbolinfo_py` | yes | yes | yes | yes |
| `mt5ordercalcmargin_py` | yes | yes | yes | yes |
| `mt5lasterror_py` | yes | yes | yes | yes |
| `mt5symbolsget_py` | yes | yes | yes | yes |
| `mt5ordersend_py` | yes | yes | yes | yes |
| `mt5symbolinfotick_py` | yes | yes | yes | yes |
| `mt5orderstotal_py` | yes | yes | yes | yes |
| `python_metatrader5` | yes | yes | yes | yes |
| `mt5shutdown_py` | yes | yes | yes | yes |
| `mt5copyticksrange_py` | yes | yes | yes | yes |
| `mt5historydealstotal_py` | yes | yes | yes | yes |
| `mt5copyratesfrom_py` | yes | yes | yes | yes |
| `mt5symbolselect_py` | yes | yes | yes | yes |
| `mt5historyordersget_py` | yes | yes | yes | yes |
| `mt5marketbookget_py` | yes | yes | yes | yes |
| `mt5ordercalcprofit_py` | yes | yes | yes | yes |
| `mt5accountinfo_py` | yes | yes | yes | yes |
| `mt5historyorderstotal_py` | yes | yes | yes | yes |
| `mt5terminalinfo_py` | yes | yes | yes | yes |
| `mt5copyticksfrom_py` | yes | yes | yes | yes |
| `mt5ordercheck_py` | yes | yes | yes | yes |
| `mt5marketbookrelease_py` | yes | yes | yes | yes |

All 33 pages passed.

## 4. Retry of failed URLs

- No URL failed during the crawl, so there was nothing to retry.
- The crawl log (`crawl_state.json`) shows 0 entries in `failed`.

## Result

**All checks passed.**

