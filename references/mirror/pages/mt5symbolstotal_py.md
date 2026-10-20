---
title: "symbols_total"
url: https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py
parent: https://www.mql5.com/en/docs/python_metatrader5
depth: 1
fetched_at: 2026-10-20T11:21:59+00:00
source: www.mql5.com
---

# symbols_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py>

## Description

Get the number of all financial instruments in the MetaTrader 5 terminal.

## Signatures

```python
symbols_total()
```

## Return Value

Integer value.

## Note

The function is similar to [SymbolsTotal()](https://www.mql5.com/en/docs/marketinformation/symbolstotal). However, it returns the number of all symbols including [custom](https://www.mql5.com/en/docs/customsymbols) ones and the ones disabled in [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch).

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

# get the number of financial instruments
symbols=mt5.symbols_total()
if symbols>0:
    print("Total symbols =",symbols)
else:
    print("symbols not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [symbols_get](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py)
- [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py)
- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)
