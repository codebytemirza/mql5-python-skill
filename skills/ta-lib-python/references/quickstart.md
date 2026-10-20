# Quickstart

## Install

```powershell
.\scripts\install.ps1
```

On Windows and macOS `pip install TA-Lib` resolves to a prebuilt wheel.
On Linux the wheel is built against the TA-Lib C library, which must be
present first - see the official install page, mirrored at
[mirror/install.md](mirror/install.md).

Installed here: **TA-Lib 0.8.2** (with numpy).

## Your first call

```python
import numpy as np
import talib

close = np.array([...], dtype="float64")   # your price series

sma = talib.SMA(close, timeperiod=20)
print(sma[-5:])       # the last 5 values; the first 19 are NaN
print(len(sma) == len(close))   # True - same length as the input
```

## The four shapes of a call

```python
# 1. one price series
talib.SMA(close, timeperiod=20)

# 2. several price series, positional, in the function's own order
talib.ADX(high, low, close, timeperiod=14)

# 3. several outputs -> a tuple
macd, signal, hist = talib.MACD(close)

# 4. a moving-average family chosen by number
talib.MA(close, timeperiod=20, matype=1)   # 1 = EMA
```

## Discover a function instead of guessing

```python
import talib.abstract

f = talib.abstract.Function("MACD")
print(f.info["input_names"])      # {{'price': 'close'}}
print(f.info["parameters"])       # fastperiod, slowperiod, signalperiod
print(f.info["output_names"])      # macd, macdsignal, macdhist
print(f.lookback)                  # bars needed before the first value
print(f.info["function_flags"])    # e.g. 'Function has an unstable period'
```

## With pandas

```python
import pandas as pd
import talib

df = pd.read_csv("ohlcv.csv", index_col="date", parse_dates=True)

df["sma20"] = talib.SMA(df["close"], timeperiod=20)
df["rsi14"] = talib.RSI(df["close"], timeperiod=14)
macd, signal, hist = talib.MACD(df["close"])
df["macd"], df["macd_signal"], df["macd_hist"] = macd, signal, hist
```

A `pandas.Series` in gives a `pandas.Series` out, with the index kept.

## The abstract API, when you want names

```python
import talib.abstract as ta

inputs = {"open": o, "high": h, "low": l, "close": c, "volume": v}
rsi = ta.Function("RSI", inputs).run()

# or let it pick the inputs itself
f = ta.Function("RSI")
f.set_input_arrays(inputs)
rsi = f.outputs["real"]
```

## Check the environment

```powershell
.\.venv\Scripts\python.exe .\scripts\smoke_test.py
```

