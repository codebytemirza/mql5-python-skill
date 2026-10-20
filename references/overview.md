# MetaTrader5 Python - agent handbook

Everything a coding agent needs to **learn the API and start working** with the
`MetaTrader5` PyPI package. Read this file first, then jump to the reference
file that matches the task in front of you.

| File | Read it when |
| --- | --- |
| `QUICKSTART.md` | You need a working script: install, connect, first data pull, disconnect. |
| `API.md` | You need the exact signature, parameters and return value of a function. |
| `COOKBOOK.md` | You need to accomplish a task (get bars, place an order, ...). |
| `CONSTANTS.md` | You need an enum value (`TIMEFRAME_M5`, `TRADE_ACTION_DEAL`, ...). |
| `TROUBLESHOOTING.md` | `initialize()` returned False, or a call returned `None`. |
| `TRADING.md` | You are placing orders: the verified sequence, the real retcodes, the real results. |
| `LIVE.md` | You need the **real** field names of the result structs and the real dtypes. |
| `api.json` | You are writing a tool that needs the API surface as data. |
| `SKILL.md` | You want to load this as an agent skill. |
| `examples/` | You want runnable starting points. |

## The 60-second version

```python
import MetaTrader5 as mt5

if not mt5.initialize():                 # finds the terminal automatically
    raise RuntimeError(mt5.last_error())  # -> (code, 'message')

bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 100)
mt5.shutdown()
```

Three rules that prevent almost every failure:

1. **`initialize()` must succeed before any other call.** Every other function
   returns `None`/empty while there is no connection.
2. **Data calls need a *running* MetaTrader 5 terminal**, not just the package.
   The package is a thin IPC client to the terminal.
3. **Always `mt5.shutdown()`** at the end, or the next run can fail to attach.

## Hard environment requirements

| Requirement | Detail |
| --- | --- |
| OS | Windows only. The package ships a native IPC client; it will not import on Linux/macOS. |
| MetaTrader 5 terminal | Must be **installed and running** on the same machine. |
| Terminal login | The terminal must be signed in to an account (or the demo account) for trading calls. |
| Package | `pip install MetaTrader5` (installed here: **5.0.6231**). |
| Python | Any supported CPython on Windows; `numpy` is pulled in automatically. |

Without a running terminal you get:

```
mt5.initialize()  ->  False
mt5.last_error()  ->  (-6, 'Terminal: Authorization failed')
```

`-6` is `RES_E_AUTH_FAILED`: the client could not attach to the terminal.
See `TROUBLESHOOTING.md`.

With a running, logged-in terminal it works:

```
mt5.initialize()  ->  True
mt5.last_error()  ->  (1, 'Success')
```

This bundle was verified against a live session on this machine
(terminal build [500, 5836, '28 Apr 2026'], 12278 symbols, demo account).
See `LIVE.md` for the measured values.

## What is in this bundle

- **33 function pages** mirrored from the official MQL5 documentation section
  *Python Integration for MetaTrader 5* (`https://www.mql5.com/en/docs/python_metatrader5`).
- Every fact here is traceable: each API entry links to the source page, and
  the complete page-by-page mirror lives in `references/mirror/pages/`, with the crawl
  provenance in `references/mirror/report.md` and `references/mirror/verification.md`.
- The **installed package** was introspected directly, so the constant list and
  the helper functions below are verified against the real build, not copied
  from the website.

