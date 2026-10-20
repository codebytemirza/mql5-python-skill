---
title: "Price Transform Functions"
url: https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html
parent: https://ta-lib.github.io/ta-lib-python/
depth: 0
fetched_at: 2026-10-20T12:30:46+00:00
source: ta-lib.github.io
---

# Price Transform Functions

#### AVGDEV - Average Deviation

```python
real = AVGDEV(close, timeperiod=14)
```

#### AVGPRICE - Average Price

```python
real = AVGPRICE(open, high, low, close)
```

#### HA - Heikin-Ashi Candles

NOTE: The HA function has an unstable period.

```python
haopen, hahigh, halow, haclose = HA(open, high, low, close)
```

#### MEDPRICE - Median Price

```python
real = MEDPRICE(high, low)
```

#### TYPPRICE - Typical Price

```python
real = TYPPRICE(high, low, close)
```

#### WCLPRICE - Weighted Close Price

```python
real = WCLPRICE(high, low, close)
```

[Documentation Index](../doc_index.html)
[All Function Groups](../funcs.html)
