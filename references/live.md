# Live session reference (verified)

Captured by running a **read-only** probe against a live MetaTrader 5
terminal on this machine. This file answers the questions the website
cannot: the actual field names of the result structures, the actual numpy
dtypes, and the values the server really returns.

| item | value |
| --- | --- |
| probed at | 2026-10-20T16:30:24 |
| package | 5.0.6231 |
| terminal build | [500, 5836, '28 Apr 2026'] |
| `initialize()` | True |
| `last_error()` after connect | [1, 'Success'] |
| `symbols_total()` | 12278 |

## Result structures - the real field lists

The named tuples expose no `_fields`, so these lists come from a live
`_asdict()` call. Use them to write correct attribute access.

### `TerminalInfo` - returned by `terminal_info()`

```
community_account, community_connection, connected, dlls_allowed, trade_allowed, tradeapi_disabled, email_enabled, ftp_enabled, notifications_enabled, mqid, build, maxbars, codepage, ping_last, community_balance, retransmission, company, name, language, path, data_path, commondata_path
```

### `AccountInfo` - returned by `account_info()`

```
login, trade_mode, leverage, limit_orders, margin_so_mode, trade_allowed, trade_expert, margin_mode, currency_digits, fifo_close, balance, credit, profit, equity, margin, margin_free, margin_level, margin_so_call, margin_so_so, margin_initial, margin_maintenance, assets, liabilities, commission_blocked, name, server, currency, company
```

### `SymbolInfo` - returned by `symbol_info()`, `symbols_get()`

```
custom, chart_mode, select, visible, session_deals, session_buy_orders, session_sell_orders, volume, volumehigh, volumelow, time, digits, spread, spread_float, ticks_bookdepth, trade_calc_mode, trade_mode, start_time, expiration_time, trade_stops_level, trade_freeze_level, trade_exemode, swap_mode, swap_rollover3days, margin_hedged_use_leg, expiration_mode, filling_mode, order_mode, order_gtc_mode, option_mode, option_right, bid, bidhigh, bidlow, ask, askhigh, asklow, last, lasthigh, lastlow, volume_real, volumehigh_real, volumelow_real, option_strike, point, trade_tick_value, trade_tick_value_profit, trade_tick_value_loss, trade_tick_size, trade_contract_size, trade_accrued_interest, trade_face_value, trade_liquidity_rate, volume_min, volume_max, volume_step, volume_limit, swap_long, swap_short, margin_initial, margin_maintenance, session_volume, session_turnover, session_interest, session_buy_orders_volume, session_sell_orders_volume, session_open, session_close, session_aw, session_price_settlement, session_price_limit_min, session_price_limit_max, margin_hedged, price_change, price_volatility, price_theoretical, price_greeks_delta, price_greeks_theta, price_greeks_gamma, price_greeks_vega, price_greeks_rho, price_greeks_omega, price_sensitivity, basis, category, currency_base, currency_profit, currency_margin, bank, description, exchange, formula, isin, name, page, path
```

### `Tick` - returned by `symbol_info_tick()`

```
time, bid, ask, last, volume, time_msc, flags, volume_real
```

### `OrderCheckResult` - returned by `order_check()`

```
retcode, balance, equity, profit, margin, margin_free, margin_level, comment, request
```

### `TradeRequest` - returned by the `request` field of an order result

```
action, magic, order, symbol, volume, price, stoplimit, sl, tp, deviation, type, type_filling, type_time, expiration, comment, position, position_by
```

## Structures that were empty in this session

The demo account had no orders, positions, deals or depth rows at the time
of the first probe, so these field lists could not be observed then. They
were observed later, after a real round trip - see `TRADING.md`.

- `orders_get()` -> `TradeOrder` - 0 rows in this session
- `positions_get()` -> `TradePosition` - 0 rows in this session
- `history_orders_get()` -> `TradeOrder` - 0 rows in this session
- `history_deals_get()` -> `TradeDeal` - 0 rows in this session
- `market_book_get()` -> `BookInfo` - 0 rows in this session

### `TradeDeal` - returned by `history_deals_get()`

Observed live on the demo account:

```
ticket, order, time, time_msc, type, entry, magic, position_id, reason,
volume, price, commission, swap, profit, fee, symbol, comment, external_id
```

### `TradeOrder` - returned by `orders_get()` / `history_orders_get()`

Observed live on the demo account:

```
ticket, time_setup, time_setup_msc, time_done, time_done_msc,
time_expiration, type, type_time, type_filling, state, magic,
position_id, position_by_id, reason, volume_initial, volume_current,
price_open, sl, tp, price_current, price_stoplimit, symbol, comment,
external_id
```

### `TradePosition` - returned by `positions_get()`

Observed live:

```
ticket, time, time_msc, time_update, time_update_msc, type, magic, identifier, reason, volume, price_open, sl, tp, price_current, swap, profit, symbol, comment, external_id
```

## numpy dtypes

**Bars** (`copy_rates_from` / `_pos` / `_range`):

```
[('time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'), ('tick_volume', '<u8'), ('spread', '<i4'), ('real_volume', '<u8')]
```

**Ticks** (`copy_ticks_from` / `_range`):

```
(no tick rows returned in this session - the demo feed had none)
```

## Trading maths, measured

| call | result |
| --- | --- |
| `order_calc_margin(ORDER_TYPE_BUY, EURUSD, 1.0, ask)` | 1120.83 |
| `order_calc_profit(ORDER_TYPE_BUY, EURUSD, 1.0, ask, ask+10*point)` | 10.0 |

## The filling-mode rule (a real trap)

`order_check` does **not** accept any filling mode: it must match what
the symbol allows. The symbol exposes this as a bitmask in
`symbol_info.filling_mode`:

| bit | meaning | `type_filling` constant | value |
| --- | --- | --- | --- |
| 1 | Fill or Kill | `mt5.ORDER_FILLING_FOK` | 0 |
| 2 | Immediate or Cancel | `mt5.ORDER_FILLING_IOC` | 1 |
| 4 | Return | `mt5.ORDER_FILLING_RETURN` | 2 |

Measured on `EURUSD` (filling_mode = 1):

| type_filling | value | order_check retcode | comment |
| --- | --- | --- | --- |
| `FOK` | 0 | 0 | Done |
| `IOC` | 1 | 10030 | Unsupported filling mode |
| `RETURN` | 2 | 10030 | Unsupported filling mode |

Note that `order_check` uses its **own** retcode: `0` + comment `Done`
means the request is acceptable. `order_send` uses the `TRADE_RETCODE_*`
family, where success is `TRADE_RETCODE_DONE` (10009).

```python
import MetaTrader5 as mt5

def pick_filling(symbol_info):
    """Return a type_filling the symbol actually accepts."""
    mode = symbol_info.filling_mode
    if mode & 1:
        return mt5.ORDER_FILLING_FOK
    if mode & 2:
        return mt5.ORDER_FILLING_IOC
    if mode & 4:
        return mt5.ORDER_FILLING_RETURN
    return mt5.ORDER_FILLING_FOK
```

