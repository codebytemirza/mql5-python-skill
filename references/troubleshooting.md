# Troubleshooting

## `last_error()` - function level errors

`mt5.last_error()` returns a tuple `(code, message)`. The codes are the
`RES_E_*` family below.

| code | value | meaning |
| --- | --- | --- |
| `RES_E_AUTH_FAILED` | -6 | authorization failed |
| `RES_E_AUTO_TRADING_DISABLED` | -8 | auto-trading disabled |
| `RES_E_FAIL` | -1 | generic fail |
| `RES_E_INTERNAL_FAIL` | -10000 | internal IPC general error |
| `RES_E_INTERNAL_FAIL_CONNECT` | -10004 | internal IPC no ipc |
| `RES_E_INTERNAL_FAIL_INIT` | -10003 | internal IPC initialization fail |
| `RES_E_INTERNAL_FAIL_RECEIVE` | -10002 | internal IPC recv failed |
| `RES_E_INTERNAL_FAIL_SEND` | -10001 | internal IPC send failed |
| `RES_E_INTERNAL_FAIL_TIMEOUT` | -10005 | internal timeout |
| `RES_E_INVALID_PARAMS` | -2 | invalid arguments/parameters |
| `RES_E_INVALID_VERSION` | -5 | invalid version |
| `RES_E_NOT_FOUND` | -4 | no history |
| `RES_E_NO_MEMORY` | -3 | no memory condition |
| `RES_E_UNSUPPORTED` | -7 | unsupported method |
| `RES_S_OK` | 1 | generic success |

### What to do

| symptom | cause | fix |
| --- | --- | --- |
| `initialize()` -> `False`, `(-6, 'Terminal: Authorization failed')` | no terminal attached | start MetaTrader 5, log in, then retry; see `QUICKSTART.md` |
| `initialize()` -> `False`, `(-2, invalid arguments/parameters)` | bad `path` | use the full path to `terminal64.exe` |
| `initialize()` -> `False`, `(-7, unsupported method)` | terminal too old for this package build | update the terminal |
| `initialize()` -> `False`, `(-8, auto-trading disabled)` | AutoTrading is off in the terminal | enable AutoTrading (Ctrl+E) for trading calls |
| any call returns `None` | no connection, or the terminal has no data for that symbol | call `initialize()` first; check `last_error()` |
| `symbol_info(sym)` -> `None` | symbol unknown to the terminal | use `mt5.symbols_get()` to list real names |
| `symbol_info(sym).visible` is `False` | not in MarketWatch | `mt5.symbol_select(sym, True)` |
| `copy_rates_*` -> `None` | no history for that symbol/timeframe | widen the range, check the symbol is selected |
| `history_*_get()` / `history_*_total()` -> `None` with `(-2, 'Invalid arguments')` | missing arguments | the range form needs **both** dates, positionally: `history_deals_get(since, now)` |
| `history_*_get(date_from=...)` -> `None` | keyword arguments are rejected | use the positional range form, or the keyword `ticket=` filter |
| `history_deals_get(since, now, "")` -> `None` | a third positional argument breaks it | pass exactly two dates |
| `history_*_get(from, to)` -> empty but the trade happened | the account history list is not populated | look the record up by ticket: `history_deals_get(ticket=...)` |
| `order_send` -> retcode != `TRADE_RETCODE_DONE` | server rejected the request | read the retcode table below |
| `order_check` -> retcode `10030` ('Unsupported filling mode') | `type_filling` does not match the symbol | derive it from `symbol_info.filling_mode` - see below |
| `order_check` -> retcode `10014` / `10016` | volume or SL/TP outside the symbol limits | respect `volume_min/max/step`, `trade_stops_level` |

### The filling-mode trap (measured, not guessed)

`order_check` and `order_send` reject a `type_filling` the symbol does not
support with retcode `10030` (`TRADE_RETCODE_INVALID_FILL`).

`symbol_info.filling_mode` is a **bitmask**: 1 = FOK, 2 = IOC, 4 = RETURN.
The package does not export `SYMBOL_FILLING_*`, so map it yourself:

```python
def pick_filling(symbol_info):
    mode = symbol_info.filling_mode
    if mode & 1:
        return mt5.ORDER_FILLING_FOK
    if mode & 2:
        return mt5.ORDER_FILLING_IOC
    if mode & 4:
        return mt5.ORDER_FILLING_RETURN
    return mt5.ORDER_FILLING_FOK
```

Measured on `EURUSD` (filling_mode = 1):

| type_filling | value | order_check retcode | comment |
| --- | --- | --- | --- |
| `FOK` | 0 | 0 | Done |
| `IOC` | 1 | 10030 | Unsupported filling mode |
| `RETURN` | 2 | 10030 | Unsupported filling mode |

`order_check` uses its own retcode: `0` with comment `Done` means the
request is acceptable. `order_send` uses `TRADE_RETCODE_DONE` (10009).

## `order_send` / `order_check` retcodes

The result named tuple has a `retcode` field. A successful action is
`mt5.TRADE_RETCODE_DONE`. The package exports the retcode constants:

| retcode | value |  |
| --- | --- | --- |
| `TRADE_RETCODE_CANCEL` | 10007 |  |
| `TRADE_RETCODE_CLIENT_DISABLES_AT` | 10027 |  |
| `TRADE_RETCODE_CLOSE_ONLY` | 10044 |  |
| `TRADE_RETCODE_CLOSE_ORDER_EXIST` | 10039 |  |
| `TRADE_RETCODE_CONNECTION` | 10031 |  |
| `TRADE_RETCODE_DONE` | 10009 |  |
| `TRADE_RETCODE_DONE_PARTIAL` | 10010 |  |
| `TRADE_RETCODE_ERROR` | 10011 |  |
| `TRADE_RETCODE_FIFO_CLOSE` | 10045 |  |
| `TRADE_RETCODE_FROZEN` | 10029 |  |
| `TRADE_RETCODE_INVALID` | 10013 |  |
| `TRADE_RETCODE_INVALID_CLOSE_VOLUME` | 10038 |  |
| `TRADE_RETCODE_INVALID_EXPIRATION` | 10022 |  |
| `TRADE_RETCODE_INVALID_FILL` | 10030 |  |
| `TRADE_RETCODE_INVALID_ORDER` | 10035 |  |
| `TRADE_RETCODE_INVALID_PRICE` | 10015 |  |
| `TRADE_RETCODE_INVALID_STOPS` | 10016 |  |
| `TRADE_RETCODE_INVALID_VOLUME` | 10014 |  |
| `TRADE_RETCODE_LIMIT_ORDERS` | 10033 |  |
| `TRADE_RETCODE_LIMIT_POSITIONS` | 10040 |  |
| `TRADE_RETCODE_LIMIT_VOLUME` | 10034 |  |
| `TRADE_RETCODE_LOCKED` | 10028 |  |
| `TRADE_RETCODE_LONG_ONLY` | 10042 |  |
| `TRADE_RETCODE_MARKET_CLOSED` | 10018 |  |
| `TRADE_RETCODE_NO_CHANGES` | 10025 |  |
| `TRADE_RETCODE_NO_MONEY` | 10019 |  |
| `TRADE_RETCODE_ONLY_REAL` | 10032 |  |
| `TRADE_RETCODE_ORDER_CHANGED` | 10023 |  |
| `TRADE_RETCODE_PLACED` | 10008 |  |
| `TRADE_RETCODE_POSITION_CLOSED` | 10036 |  |
| `TRADE_RETCODE_PRICE_CHANGED` | 10020 |  |
| `TRADE_RETCODE_PRICE_OFF` | 10021 |  |
| `TRADE_RETCODE_REJECT` | 10006 |  |
| `TRADE_RETCODE_REJECT_CANCEL` | 10041 |  |
| `TRADE_RETCODE_REQUOTE` | 10004 |  |
| `TRADE_RETCODE_SERVER_DISABLES_AT` | 10026 |  |
| `TRADE_RETCODE_SHORT_ONLY` | 10043 |  |
| `TRADE_RETCODE_TIMEOUT` | 10012 |  |
| `TRADE_RETCODE_TOO_MANY_REQUESTS` | 10024 |  |
| `TRADE_RETCODE_TRADE_DISABLED` | 10017 |  |

Always compare the retcode, never assume success:

```python
result = mt5.order_send(request)
if result is None:
    print("no answer from the terminal:", mt5.last_error())
elif result.retcode != mt5.TRADE_RETCODE_DONE:
    print("rejected, retcode =", result.retcode)
    print("comment:", result.comment)
    print("request:", result.request)
else:
    print("done, order =", result.order, "deal =", result.deal)
```

## Tracing a failed request

`result._asdict()` gives every field of the answer, including the
`request` echo. This is the fastest way to see what the terminal actually
received:

```python
d = result._asdict()
for k, v in d.items():
    print(k, "=", v)
    if k == "request":
        for rk, rv in v._asdict().items():
            print("   ", rk, "=", rv)
```

## A safe skeleton

```python
import MetaTrader5 as mt5

def connect():
    if mt5.initialize():
        return True
    code, msg = mt5.last_error()
    raise RuntimeError("MetaTrader5 connection failed: %s (%s)" % (msg, code))

try:
    connect()
    # ... work ...
finally:
    mt5.shutdown()
```

## Two error-code families, do not mix them up

| family | used by | success value |
| --- | --- | --- |
| `RES_E_*` / `RES_S_OK` | `last_error()` | `RES_S_OK` = 1, `'Success'` |
| `TRADE_RETCODE_*` | `order_send`, `order_check` | `order_send`: `TRADE_RETCODE_DONE` = 10009 |
| `order_check` retcode | `order_check` only | `0` with comment `'Done'` |

`order_check` does **not** use `TRADE_RETCODE_*`; it returns `0` for an
acceptable request. Comparing `order_check` against
`TRADE_RETCODE_DONE` will make a perfectly good request look broken.

