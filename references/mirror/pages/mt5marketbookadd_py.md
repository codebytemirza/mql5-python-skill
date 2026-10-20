---
title: "market_book_add"
url: https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py
parent: https://www.mql5.com/en/docs/python_metatrader5
depth: 1
fetched_at: 2026-10-20T11:21:59+00:00
source: www.mql5.com
---

# market_book_add

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py>

## Description

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

## Signatures

```python
market_book_add(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

True if successful, otherwise – False.

## Note

The function is similar to [MarketBookAdd](https://www.mql5.com/en/docs/marketinformation/marketbookadd).

## See also

- [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py)
- [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py)
- [Market Depth structure](https://www.mql5.com/en/docs/constants/structures/mqlbookinfo)
