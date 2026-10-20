# Cookbook

Task-oriented recipes. All of them run against numpy arrays unless noted.

## Moving average

```python
import numpy as np
import talib

def sma(close, period=20):
    """Simple moving average, NaNs trimmed."""
    out = talib.SMA(close, timeperiod=period)
    return out[talib.abstract.Function("SMA").lookback:]
```

## Exponential moving average and the family

```python
sma20 = talib.SMA(close, timeperiod=20)
ema20 = talib.EMA(close, timeperiod=20)
wma20 = talib.WMA(close, timeperiod=20)
rma14 = talib.RMA(close, timeperiod=14)      # Wilder's smoothing
hull  = talib.HMA(close, timeperiod=20)      # Hull
kama  = talib.KAMA(close, timeperiod=20)     # Kaufman adaptive

# the same thing, chosen by number
generic = talib.MA(close, timeperiod=20, matype=1)   # 1 = EMA
```

## A moving-average crossover

```python
fast = talib.EMA(close, timeperiod=12)
slow = talib.EMA(close, timeperiod=26)

# True where the fast average crosses above the slow one
cross_up = (fast > slow) & (fast.shift(1) <= slow.shift(1))
cross_down = (fast < slow) & (fast.shift(1) >= slow.shift(1))
```

## RSI and overbought / oversold

```python
rsi = talib.RSI(close, timeperiod=14)
overbought = rsi > 70
oversold = rsi < 30
```

## MACD

```python
macd, macd_signal, macd_hist = talib.MACD(
    close, fastperiod=12, slowperiod=26, signalperiod=9)

histogram_turns_positive = (macd_hist > 0) & (macd_hist.shift(1) <= 0)
```

## Bollinger Bands and %B

```python
upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2)

percent_b = (close - lower) / (upper - lower)
bandwidth = (upper - lower) / middle
```

## ATR, true range and volatility-based stops

```python
atr = talib.ATR(high, low, close, timeperiod=14)
true_range = talib.TRANGE(high, low, close)

stop = close - 2 * atr
target = close + 3 * atr
```

## ADX and directional movement

```python
adx = talib.ADX(high, low, close, timeperiod=14)     # 28-bar lookback, unstable period
plus_di = talib.PLUS_DI(high, low, close, timeperiod=14)
minus_di = talib.MINUS_DI(high, low, close, timeperiod=14)

strong_trend = adx > 25
uptrend = (plus_di > minus_di) & strong_trend
```

## Stochastic oscillator

```python
slowk, slowd = talib.STOCH(high, low, close,
                           fastk_period=14, slowk_period=3,
                           slowk_matype=0, slowd_period=3, slowd_matype=0)
fastk, fastd = talib.STOCHF(high, low, close, fastk_period=5, fastd_period=3)
```

## Candlestick patterns

```python
# 0 = none, +100 = bullish, -100 = bearish
hammer = talib.CDHAMMER(open_, high, low, close)
doji = talib.CDLDOJI(open_, high, low, close)
engulfing = talib.CDLENGULFING(open_, high, low, close)

bullish_hammer = hammer == 100
```

## Volume indicators

```python
obv = talib.OBV(close, volume)
mfv = talib.MFI(high, low, close, volume, timeperiod=14)
ad = talib.AD(high, low, close, volume)
vwap = talib.VWAP(high, low, close, volume)
```

## Statistics over two series

```python
beta = talib.BETA(high, low, timeperiod=5)
corr = talib.CORREL(high, low, timeperiod=5)
slope, intercept = talib.LINEARREG(high, low, timeperiod=14)
```

## A pandas pipeline

```python
import pandas as pd
import talib

df = pd.read_csv("ohlcv.csv", index_col="date", parse_dates=True)

df["sma20"] = talib.SMA(df["close"], timeperiod=20)
df["ema50"] = talib.EMA(df["close"], timeperiod=50)
df["rsi14"] = talib.RSI(df["close"], timeperiod=14)

macd, signal, hist = talib.MACD(df["close"])
df["macd"], df["macd_signal"], df["macd_hist"] = macd, signal, hist

upper, middle, lower = talib.BBANDS(df["close"], timeperiod=20)
df["bb_upper"], df["bb_mid"], df["bb_lower"] = upper, middle, lower

df["atr14"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=14)

# the columns keep the dataframe's index
```

## The abstract API

```python
import talib.abstract as ta

inputs = {"open": o, "high": h, "low": l, "close": c, "volume": v}

f = ta.Function("RSI", inputs)
rsi = f.run()                    # -> the 'real' output

# or set things yourself
f2 = ta.Function("RSI")
f2.set_input_arrays(inputs)
f2.set_parameters({"timeperiod": 21})
rsi21 = f2.outputs["real"]
```

## The streaming API - one bar at a time

```python
from talib import stream

history = list(close[:200])

handle = None
while handle is None:
    history.append(next(feed))
    try:
        handle = stream.RSI(np.asarray(history, dtype="float64"), timeperiod=14)
    except talib.InsufficientHistory:
        pass          # not enough history yet - keep feeding

value = handle.value             # value at the last history bar

for bar in feed:
    rsi_now = handle.update(bar)     # one closed bar in, its value out
    print(rsi_now)

# peek at a forming bar without committing it
forming_value = handle.peek(forming_bar)
```

## Discovery

```python
import talib
import talib.abstract

talib.get_functions()          # every function name
talib.get_function_groups()    # group -> [names]

talib.abstract.Function("MACD").info
talib.abstract.Function("MACD").lookback
```

---

## Which API should I use?

| situation | use |
| --- | --- |
| a handful of indicators over a whole history | **Function API** - `talib.SMA(close, 20)` |
| you need named inputs, or want to look a function up | **Abstract API** - `ta.Function("SMA")` |
| bars arrive one at a time | **Stream API** - `stream.RSI(history)` |
| a pandas DataFrame | **Function API** - it accepts and returns Series |

