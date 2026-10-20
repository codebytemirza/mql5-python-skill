---
name: ta-lib-python
description: >-
  Technical analysis with the TA-Lib Python package (import talib) - moving averages,
  momentum oscillators, volatility bands, volume indicators, candlestick pattern
  recognition and statistics over OHLCV price data. Use when the task mentions TA-Lib,
  talib, SMA, EMA, WMA, RSI, MACD, Bollinger Bands, BBANDS, ATR, ADX, Stochastic,
  CCI, OBV, candlestick patterns like CDLDOJI or CDLHAMMER, technical indicators,
  or computing indicators over a pandas DataFrame. Covers the Function API, the
  Abstract API and the streaming API, with the official documentation mirrored.
metadata:
  author: TA-Lib documentation mirror
  version: "1.0.0"
---

# TA-Lib for Python

`TA-Lib` is a C library of 201 technical-analysis functions with a Cython
wrapper. Installed here: **0.8.2**.

## The 60-second version

```python
import numpy as np
import talib

sma20 = talib.SMA(close, timeperiod=20)     # one array in, one array out
macd, signal, hist = talib.MACD(close)      # several outputs -> a tuple
rsi14 = talib.RSI(close, timeperiod=14)
```

## The calling convention - the one thing to get right

Every function takes **its price arrays positionally, in a fixed order**, then
its parameters as keyword arguments:

| input style | what you pass | example |
| --- | --- | --- |
| one price series | 1 array (usually `close`) | `talib.SMA(close, 20)` |
| several price series | N arrays, in the documented order | `talib.ADX(high, low, close)` |
| price + volume | 4 arrays | `talib.MFI(high, low, close, volume)` |

The order is **not** always `open, high, low, close` - it is whatever the
function needs, and it differs per function (`AROON` wants `high, low`;
`MFI` wants `high, low, close, volume`). `references/api.md` lists the exact
inputs for every function, and `talib.abstract.Function(name).info['input_names']`
gives them at runtime.

## Lookback: the leading NaNs are normal

An indicator needs history before it can produce a value. The first
`lookback` elements of the output are `NaN`, and the output has the **same
length** as the input.

```python
sma = talib.SMA(close, timeperiod=30)
sma[:29]      # 29 NaN values
sma[29]       # first real value
talib.abstract.Function("SMA").lookback   # -> 29
```

The lookback is often **larger** than `timeperiod`: `RSI(14)` needs 15
observations, `ADX(14)` needs 28. Always check `.lookback`, do not assume.

## Multiple outputs

A function that produces more than one series returns a **tuple**:

```python
macd, macd_signal, macd_hist = talib.MACD(close)
upper, middle, lower = talib.BBANDS(close, timeperiod=20)
aroon_down, aroon_up = talib.AROON(high, low)
```

The order is fixed; `talib.abstract.Function(name).output_names` names them.

## The three APIs

| API | use it for |
| --- | --- |
| **Function** (`talib.SMA(...)`) | the normal case - fastest, simplest |
| **Abstract** (`talib.abstract.Function("SMA")`) | named inputs, dataframe in, discovery of a function's metadata |
| **Stream** (`talib.stream.RSI(history)`) | one handle per indicator, O(1) per new bar |

## pandas and polars work natively

Pass a `pandas.Series` or `polars.Series` and you get the same type back,
with the index preserved. Do not convert to numpy yourself unless you want to.

```python
sma = talib.SMA(df["close"], timeperiod=20)   # -> pandas Series
```

Mixing pandas and polars in one call raises `Exception: Cannot mix polars
and pandas`.

## Pattern recognition returns 0 / +100 / -100

Candlestick functions return `0` (no pattern), `+100` (bullish) or `-100`
(bearish) - **not** True/False. The stronger variants (`CDLKICKINGBYLENGTH`,
`CDLSTALLEDPATTERN`, ...) return a graded value in `[-200, 200]`.

## Non-negotiables

1. All input arrays must be **the same length** and the same dtype (float64).
2. `NaN` and `inf` anywhere in the history are undefined behaviour in the C
   library - clean the data first.
3. Some functions have an **unstable period** (ADX, ATR, CMO, DX, MAMA, SAR,
   T3, TEMA, TRIMA, ...). Their first values are unreliable; the official docs
   flag each one with a `NOTE:` line, and `Function.info['function_flags']`
   marks it at runtime.
4. `matype` is a **number**, not a name - see `references/constants.md`.

## Where to look

| Need | File |
| --- | --- |
| Install and first calls | [references/quickstart.md](references/quickstart.md) |
| One function: inputs, defaults, outputs, lookback | [references/api.md](references/api.md) |
| A recipe for a task | [references/cookbook.md](references/cookbook.md) |
| All 201 functions with one-line descriptions | [references/functions.md](references/functions.md) |
| `matype` values, flags, pattern values | [references/constants.md](references/constants.md) |
| Something failed | [references/troubleshooting.md](references/troubleshooting.md) |
| Measured behaviour | [references/live.md](references/live.md) |
| The official documentation, page by page | [references/mirror/](references/mirror/) |
| The API surface as data | [data/api.json](data/api.json) |

## Scripts

```powershell
.\scripts\install.ps1                       # venv + TA-Lib
.\.venv\Scripts\python.exe .\scripts\smoke_test.py
.\.venv\Scripts\python.exe .\scripts\indicators.py
.\.venv\Scripts\python.exe .\scripts\pandas_pipeline.py
.\.venv\Scripts\python.exe .\scripts\stream_demo.py
```

## Provenance

- The reference material is a verified mirror of the official TA-Lib Python
  documentation site (https://ta-lib.github.io/ta-lib-python/), 16 pages.
- Every signature, default, input order and lookback in this skill was
  taken from the **installed** package, not from the website, and checked
  against the official pages.

