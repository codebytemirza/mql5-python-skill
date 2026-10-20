---
title: "symbol_info_tick"
url: https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py
parent: https://www.mql5.com/en/docs/python_metatrader5
depth: 1
fetched_at: 2026-10-20T11:21:59+00:00
source: www.mql5.com
---

# symbol_info_tick

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py>

## Description

Get the last tick for the specified financial instrument.

## Signatures

```python
symbol_info_tick(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a tuple. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function is similar to [SymbolInfoTick](https://www.mql5.com/en/docs/marketinformation/symbolinfotick).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# attempt to enable the display of the GBPUSD in MarketWatch
selected=mt5.symbol_select("GBPUSD",True)
if not selected:
    print("Failed to select GBPUSD")
    mt5.shutdown()
    quit()

# display the last GBPUSD tick
lasttick=mt5.symbol_info_tick("GBPUSD")
print(lasttick)
# display tick field values in the form of a list
print("Show symbol_info_tick(\"GBPUSD\")._asdict():")
symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
for prop in symbol_info_tick_dict:
    print("  {}={}".format(prop, symbol_info_tick_dict[prop]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)
Show symbol_info_tick._asdict():
  time=1585070338
  bid=1.17264
  ask=1.17279
  last=0.0
  volume=0
  time_msc=1585070338728
  flags=2
  volume_real=0.0
```

## See also

- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)
- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)
