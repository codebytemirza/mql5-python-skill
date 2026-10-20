---
name: mql5-python
description: >-
  Work with the MetaTrader5 Python package (import MetaTrader5 as mt5) - connect to a
  running MetaTrader 5 terminal, pull bars, ticks and market depth, inspect the
  account, orders, positions and trade history, and place or close orders.
  Use when the task mentions MetaTrader5, MT5, mt5.initialize, copy_rates_from,
  copy_rates_from_pos, copy_rates_range, copy_ticks_from, order_send, order_check,
  symbol_info, symbol_info_tick, positions_get, history_deals_get, or trading via
  Python. Includes the full official MQL5 "Python Integration for MetaTrader 5"
  documentation mirror, a machine-readable api.json, and behaviour measured
  against a live terminal.
metadata:
  author: MetaQuotes-documentation mirror
  version: "1.0.0"
---

# MetaTrader5 Python (`mt5`)

The `MetaTrader5` package is a **thin IPC client to a running MetaTrader 5
terminal**. Installing the package is not enough - the terminal must be
running and signed in, or every call returns `None`.

## Start here

```python
import MetaTrader5 as mt5

if not mt5.initialize():                 # finds the terminal automatically
    raise RuntimeError(mt5.last_error())  # -> (code, 'message')

bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 100)
mt5.shutdown()
```

## Non-negotiables

1. `mt5.initialize()` must return `True` before any other call.
2. `mt5.shutdown()` in a `finally` block when the script ends.
3. Check `result.retcode != mt5.TRADE_RETCODE_DONE` after every
   `order_send`. `order_check` uses a **different** retcode: `0` +
   `comment == 'Done'` means the request is acceptable.
4. `type_filling` must match `symbol_info.filling_mode` (bitmask:
   1=FOK, 2=IOC, 4=RETURN) or the request is rejected with retcode `10030`.
5. `history_*_get` / `history_*_total` need **both** dates, positionally:
   `history_deals_get(since, now)`. Keywords are rejected.
6. Windows only. The package will not import on Linux or macOS.

## Where to look

| Need | File |
| --- | --- |
| Install, connect, first data pull | [references/quickstart.md](references/quickstart.md) |
| Exact signature / parameters / returns of a function | [references/api.md](references/api.md) |
| A runnable recipe for a task | [references/cookbook.md](references/cookbook.md) |
| Placing orders (verified end to end) | [references/trading.md](references/trading.md) |
| An enum value | [references/constants.md](references/constants.md) |
| `initialize()` failed, or a call returned `None` | [references/troubleshooting.md](references/troubleshooting.md) |
| Real field names of the result structs, real dtypes | [references/live.md](references/live.md) |
| The full official documentation, page by page | [references/mirror/](references/mirror/) |
| The API surface as data | [data/api.json](data/api.json) |

## Scripts

```powershell
.\scripts\install.ps1                       # venv + MetaTrader5 in the current project
.\.venv\Scripts\python.exe .\scripts\smoke_test.py     # is the environment ready?
.\.venv\Scripts\python.exe .\scripts\fetch_bars.py     # download bars
.\.venv\Scripts\python.exe .\scripts\inspect_state.py # account, orders, positions, history
.\.venv\Scripts\python.exe .\scripts\order_round_trip.py EURUSD 0.01   # PLACES REAL ORDERS
```

`order_round_trip.py` opens a position and closes it again on whatever
account the terminal is signed into. Run it only when the user asks for a
real order; `order_check` and `order_calc_*` are the read-only ones.

## Provenance

- The reference material is a verified mirror of the official MQL5
  section *Python Integration for MetaTrader 5* - 33 pages, crawled and
  checked, see [references/mirror/report.md](references/mirror/report.md) and
  [references/mirror/verification.md](references/mirror/verification.md).
- The constant list, the helper functions and the measured behaviour come
  from introspecting the installed `MetaTrader5` package (5.0.6231) and from
  running it against a live terminal - not from the website alone.

