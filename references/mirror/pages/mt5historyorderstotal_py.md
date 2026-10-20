---
title: "history_orders_total"
url: https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py
parent: https://www.mql5.com/en/docs/python_metatrader5
depth: 1
fetched_at: 2026-10-20T11:21:59+00:00
source: www.mql5.com
---

# history_orders_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py>

## Description

Get the number of orders in trading history within the specified interval.

## Signatures

```python
history_orders_total(
   date_from,    // date the orders are requested from
   date_to       // date, up to which the orders are requested
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `date_from` | — | [in] Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `date_to` | — | [in] Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Integer value.

## Note

The function is similar to [HistoryOrdersTotal](https://www.mql5.com/en/docs/trading/historyorderstotal).

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of orders in history
from_date=datetime(2020,1,1)
to_date=datetime.now()
history_orders=mt5.history_orders_total(from_date, datetime.now())
if history_orders>0:
    print("Total history orders=",history_orders)
else:
    print("Orders not found in history")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py)
- [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)
