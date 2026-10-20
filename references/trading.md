# Trading, verified end to end

This is the part of the API that cannot be read from a website: what the
server actually returns. Every value below was produced by running the
round trip on the live demo account (0.01 lot, opened and closed again).

> **This path places real orders** on whatever account the terminal is
> logged into. The account used here is the MetaQuotes-Demo account; the
> round trip finished with the balance back at its starting value and no
> open positions.

## The sequence that works

| # | step | call | how to judge success |
| --- | --- | --- | --- |
| 1 | dry run | `order_check(request)` | `retcode == 0` and `comment == 'Done'` |
| 2 | open | `order_send(request)` | `retcode == mt5.TRADE_RETCODE_DONE` (10009) |
| 3 | confirm | `positions_get(symbol=...)` | the position ticket is in the list |
| 4 | close | `order_send(close_request)` | `retcode == mt5.TRADE_RETCODE_DONE` |
| 5 | confirm flat | `positions_total()` | `0` |
| 6 | audit | `history_deals_get(ticket=...)` | one deal per side |

## What `order_check` returned (measured)

```
OrderCheckResult(retcode=0, balance=5000.0, equity=5000.0, profit=0.0,
                 margin=11.21, margin_free=4988.79,
                 margin_level=44603.03300624442, comment='Done',
                 request=TradeRequest(action=1, magic=234000, order=0,
                 symbol='EURUSD', volume=0.01, price=1.12094, stoplimit=0.0,
                 sl=0.0, tp=0.0, deviation=30, type=0, type_filling=0,
                 type_time=0, expiration=0, comment='py-roundtrip open',
                 position=0, position_by=0))
```

`order_check` has its **own** retcode: `0` with comment `Done` means the
request is acceptable, and only then are `balance`, `equity`, `margin`,
`margin_free` and `margin_level` populated. When the request is rejected
those fields stay `0.0` - do not read a margin from a failed check.

## What `order_send` returned (measured)

Open:

```
OrderSendResult(retcode=10009, deal=58574738308, order=58970981795,
                 volume=0.01, price=1.1209, bid=0.0, ask=0.0,
                 comment='Request executed', request_id=4053463544,
                 retcode_external=0, request=TradeRequest(...))
```

Close:

```
OrderSendResult(retcode=10009, deal=58574738813, order=58970982315,
                 volume=0.01, price=1.12089, bid=0.0, ask=0.0,
                 comment='Request executed', request_id=4053463545,
                 retcode_external=0, request=TradeRequest(...))
```

`order_send` uses the `TRADE_RETCODE_*` family, where success is
`TRADE_RETCODE_DONE` = 10009 and `comment` is `'Request executed'`.
`bid` and `ask` stay `0.0` in the answer - the fill price is in `price`.

## The audit trail (measured)

| record | key values |
| --- | --- |
| open deal | `type=0` (BUY), `entry=0` (IN), `reason=3` (CLIENT), `volume=0.01`, `price=1.1209`, `profit=0.0` |
| close deal | `type=1` (SELL), `entry=1` (OUT), `reason=3`, `volume=0.01`, `price=1.12089`, `profit=-0.01` |
| open order | `type=0`, `state=4` (FILLED), `type_filling=0` (FOK), `volume_initial=0.01`, `volume_current=0.0` |
| close order | `type=1`, `state=4` (FILLED), `type_filling=0`, `volume_current=0.0` |

Notes that will save you time:

- **Comments are truncated to 16 characters** by the server:
  `'py-roundtrip open'` is stored as `'py-roundtrip ope'`. Do not use the
  comment to identify a position beyond 16 characters.
- `price_open` is `0.0` on a market order; the fill price is in
  `price_current` on the order and `price` on the deal.
- `volume_current` becomes `0.0` once the order is fully closed.
- `type_filling` on the stored order is the value you sent, so it is a
  cheap way to confirm the broker honoured your filling mode.

## Reading history back - the calling convention

`history_*_get` and `history_*_total` are the most surprising calls in
the API. Measured behaviour:

| call | result |
| --- | --- |
| `history_deals_get()` | `None`, `last_error() = (-2, 'Invalid arguments')` |
| `history_deals_get(since)` | `None`, `(-2, 'Invalid arguments')` |
| `history_deals_get(since, now)` | works - tuple of `TradeDeal` |
| `history_deals_get(since, now, "")` | `None`, `(-2, 'Invalid arguments')` |
| `history_deals_get(date_from=..., date_to=...)` | `None`, `(-2, ...)` - **keywords are rejected** |
| `history_deals_get(ticket=...)` | works - tuple with that one deal |
| `history_deals_total()` | `None`, `(-2, 'Invalid arguments')` |
| `history_deals_total(since, now)` | works - `int` |
| `history_deals_total(date_from=...)` | `TypeError: takes no keyword arguments` |

So: **both dates, positional only** for the range form; **keyword only** for
the `ticket=` / `position=` filter form.

```python
from datetime import datetime, timedelta

now = datetime.now()
since = now - timedelta(days=30)

# range form: two positional dates
deals = mt5.history_deals_get(since, now)      # -> tuple, may be empty
count = mt5.history_deals_total(since, now)     # -> int

# single-record form: keyword filter
one = mt5.history_deals_get(ticket=58574738308)  # -> tuple with 1 deal
```

On the demo account used here, the range form returned **0 rows** even
though the deals existed, while `history_deals_get(ticket=...)` returned
them. If a range query looks empty, look the records up by ticket before
concluding that nothing happened.

## The script

`examples/order_round_trip.py` in this bundle is the exact script that
produced the numbers above.

```powershell
.\.venv\Scripts\python.exe scripts\order_round_trip.py EURUSD 0.01
```

It exits `0` when the account is flat again and `2` if a position is
left open.

## Request fields, as the server sees them

The `request` field of every result is the structure the terminal
received, echoed back:

```
action, magic, order, symbol, volume, price, stoplimit, sl, tp,
deviation, type, type_filling, type_time, expiration, comment,
position, position_by
```

Use it to debug: if the server filled at a different price than you
asked for, the echo tells you exactly what was sent.

