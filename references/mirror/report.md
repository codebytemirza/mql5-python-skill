# Crawl report - MQL5 "Python Integration for MetaTrader 5"

Generated: 2026-10-20T11:21:59+00:00

## Scope

| Item | Value |
| --- | --- |
| Root URL | <https://www.mql5.com/en/docs/python_metatrader5> |
| Host | www.mql5.com |
| Allowed path prefix | `/en/docs/python_metatrader5` |
| Discovered in-scope URLs | 33 |

## Totals

| Metric | Count |
| --- | --- |
| Pages discovered (in-scope, unique) | 33 |
| Pages fetched successfully | 33 |
| Pages failed | 0 |
| Pages skipped (robots.txt) | 0 |
| Pages written to `pages/` | 33 |
| Markdown files in `pages/` on disk | 33 |

## Tree

- Maximum tree depth: **1** (root = 0, function pages = 1)
- Top-level sections under the root: **32**

The left sidebar (`ul.docsMenu`) lists all 32 function pages as a flat set of
siblings directly under the section root, so the sidebar hierarchy and the
discovery-parent map agree on every page.

### Top-level sections

- initialize
- login
- shutdown
- version
- last_error
- account_info
- terminal_info
- symbols_total
- symbols_get
- symbol_info
- symbol_info_tick
- symbol_select
- market_book_add
- market_book_get
- market_book_release
- copy_rates_from
- copy_rates_from_pos
- copy_rates_range
- copy_ticks_from
- copy_ticks_range
- orders_total
- orders_get
- order_calc_margin
- order_calc_profit
- order_check
- order_send
- positions_total
- positions_get
- history_orders_total
- history_orders_get
- history_deals_total
- history_deals_get

## Content extraction

| Metric | Count |
| --- | --- |
| Pages with at least one function signature | 32 |
| Code blocks rendered (in `## Description`/other sections) | 36 |
| Pages containing a parameter table | 24 |
| Parameters extracted | 69 |
| Pages containing an enumeration/constant table | 8 |
| Table rows extracted | 119 |

## Verification performed

1. **Root re-scan (live).** The root page was re-fetched from the server and
   re-parsed; every in-scope link in its content and in its sidebar was checked
   against `visited` + `failed`. Itemised table in `verification.md`.
2. **URL/file coverage.** Every URL in `urls.txt` was matched to a file in
   `pages/`, and every file in `pages/` back to a URL. 33/33 matched, 0 orphans.
3. **Spot checks.** 6 randomly chosen pages (seed 20261020) plus the root were
   re-read against the source HTML: signatures, parameter rows, enum tables and
   every code block compared, plus a scan for site-chrome/advert text.
4. **Full-coverage check.** The same comparison was then run over **all 33**
   pages: every code block appears verbatim, every parameter is present, every
   enum/constant table row is present, and every source paragraph is present.
5. **Failed-URL retry.** No URL failed during the crawl, so there was nothing to
   retry (0 entries in `crawl_state.json.failed`).

**Verification verdict: All checks passed.**  (full detail in `verification.md`)

## Pages with empty or suspicious extraction

- None: every fetched page produced at least one content block.

## Decisions taken during the crawl (no questions asked)

- **URL normalisation.** Fragments are dropped, tracking/noise query parameters
  (from the `Clean-Param` list in robots.txt plus common ad parameters) are
  stripped, `http`/`https` and trailing slashes are unified, and
  `mql5.com` is treated as `www.mql5.com`.
- **robots.txt** was fetched and honoured with the crawler user agent;
  `User-agent: *` disallows `/*/search*`, `/data*` and similar paths only, so
  every `/en/docs/python_metatrader5` URL is allowed. Nothing was skipped.
- **Sitemap cross-check.** `sitemap_docs_en.xml` lists exactly the same 33 URLs
  under `/en/docs/python_metatrader5` that link-following discovered, which
  independently confirms the section has no orphaned pages.
- **Parameter type column.** The source pages never state a type separately;
  the `Type` column therefore shows the value placeholder exactly as written
  in the signature (`login=LOGIN` -> `LOGIN`), and `-` when the parameter is
  positional. This is stated in a footnote under every parameter table.
- **Code block language tags.** All blocks in this section are Python; the two
  `pip install ...` lines on the root page are tagged `bash`. No other
  language is used by the source.
- **`&nbsp;` in code.** Non-breaking spaces used for indentation are rendered as
  ordinary spaces so the code stays copy-pasteable; nothing else is altered.
- **Signature detection.** A code block is treated as a function signature when
  it starts with one of this section's function names and contains no
  `import`/`print`. Example blocks are never treated as signatures.

## Anything that could not be verified

- The site serves identical HTML to every client, so the pages were read
  from the server's HTML rather than a JS-rendered DOM. Any content that the
  site only injects for logged-in users was not captured (no such content
  was observed in the fetched HTML).
- `robots.txt` answered `200`; a `403` is returned for the default urllib
  user agent, so the crawler identifies itself with a browser user agent.
