# Quickstart

Goal: a script that connects to a running MetaTrader 5 terminal and pulls data.

## 1. Install

```powershell
.\.venv\Scripts\pip.exe install MetaTrader5
```

Installed in this workspace: **5.0.6231** (author: MetaQuotes Ltd.).

## 2. Check the environment

```python
import MetaTrader5 as mt5
print(mt5.__version__, mt5.__author__)
print("initialize ->", mt5.initialize())
print("last_error ->", mt5.last_error())
```

If `initialize()` is `False`, the terminal is not running or not reachable -
stop here and read `TROUBLESHOOTING.md`.

## 3. Connect

Three call variants, in order of preference:

```python
mt5.initialize()                                    # terminal found automatically
mt5.initialize(r"C:\Program Files\MetaTrader 5\terminal64.exe")   # explicit path
mt5.initialize(path, login=LOGIN, password="PASSWORD",
                 server="SERVER", timeout=60000, portable=False)
```

`path` is the only **unnamed** parameter; everything else is a **named**
parameter. The terminal is launched for you if it is not already running.

## 4. First data pull

```python
import MetaTrader5 as mt5
from datetime import datetime

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    raise SystemExit(1)

# how many symbols does the terminal know?
print("symbols:", mt5.symbols_total())

# metadata for one symbol
info = mt5.symbol_info("EURUSD")
if info is not None:
    print("point=%s digits=%s trade_mode=%s" %
          (info.point, info.digits, info.trade_mode))

# the latest tick
tick = mt5.symbol_info_tick("EURUSD")
print("bid=%s ask=%s time=%s" % (tick.bid, tick.ask, tick.time))

# the last 100 M1 bars as a numpy structured array
bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 100)
print(bars.dtype.names)   # ('time','open','high','low','close','tick_volume','spread','real_volume')

mt5.shutdown()
```

## 5. Shape of the data

| Call | Returns |
| --- | --- |
| `copy_rates_from` / `_pos` / `_range` | numpy structured array with columns `time, open, high, low, close, tick_volume, spread, real_volume` |
| `copy_ticks_from` / `_range` | numpy structured array with columns `time, bid, ask, last, volume, flags, volume_real` |
| `symbol_info`, `account_info`, `terminal_info`, `symbol_info_tick` | a named tuple; `None` on failure |
| `orders_get`, `positions_get`, `history_*_get` | tuple of named tuples; `None` on failure |
| `orders_total`, `positions_total`, `history_*_total` | `int` |
| `order_send`, `order_check` | named tuple with a `retcode` field |

The exact bar dtype, measured on a live terminal:

```
[('time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'), ('tick_volume', '<u8'), ('spread', '<i4'), ('real_volume', '<u8')]
```

The exact field names of every result struct are in `LIVE.md`.

## 6. Always shut down

```python
try:
    ...            # work
finally:
    mt5.shutdown()
```

## 7. Run it

```powershell
.\.venv\Scripts\python.exe scripts\smoke_test.py
```

`smoke_test.py` connects, prints the account/terminal state, pulls bars and
ticks, and exits with a non-zero status if the environment is not ready.

