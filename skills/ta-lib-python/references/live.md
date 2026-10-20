# Measured behaviour

Values below were produced by running the installed package, not copied
from the documentation.

| item | value |
| --- | --- |
| package | TA-Lib 0.8.2 |
| functions | 201 |
| groups | 10 |
| Cycle Indicators | 5 |
| Math Operators | 12 |
| Math Transform | 15 |
| Momentum Indicators | 47 |
| Overlap Studies | 25 |
| Pattern Recognition | 61 |
| Price Transform | 6 |
| Statistic Functions | 11 |
| Volatility Indicators | 7 |
| Volume Indicators | 12 |

## Output shape

```
SMA(close, timeperiod=30) -> ndarray shape (300,) dtype float64
   the first 29 values are NaN, index 29 is the first real value
MACD(close)               -> 3 arrays, each shape (300,)
BBANDS(close, 20)         -> 3 arrays, each shape (300,)
STOCH(high, low, close)   -> 2 arrays, each shape (300,)
```

The output length always equals the input length.

## Lookback vs timeperiod

| function | timeperiod | lookback | first valid index |
| --- | --- | --- | --- |
| `SMA` | 30 | 29 | 29 |
| `EMA` | 30 | 29 | 29 |
| `RSI` | 14 | 14 | 14 |
| `ATR` | 14 | 14 | 14 |
| `ADX` | 14 | 27 | 27 |
| `MACD` | 12/26/9 | 33 | 33 |

`RSI(14)` needs 15 observations and `ADX(14)` needs 28 - the lookback is
not the timeperiod. `talib.abstract.Function(name).lookback` gives it
exactly.

## Pattern values

```
CDLDOJI -> unique values [0, 100]; 0 = no pattern, +100 = bullish, -100 = bearish
```

## pandas

```
talib.SMA(df['close'], timeperiod=30)  -> pandas.Series, index preserved
talib.MACD(df['close'])                 -> tuple of 3 pandas.Series
```

Mixing pandas and polars in one call raises
`Exception: Cannot mix polars and pandas`.

## The streaming API

```
stream.RSI(history, timeperiod=14)   # same arguments as talib.RSI
handle.value                            # value at the last history bar
handle.update(bar)                      # one closed bar in, its value out
handle.peek(forming_bar)                # preview; commits nothing
handle.copy()                           # an independent handle at the same bar
handle.advance()                        # count a bar you did not feed
handle.out_range                        # (begidx, nbelement)
stream.RSI.open_and_fill(history, 14)   # the handle and the whole series
```

Opening a handle on too little history raises `talib.InsufficientHistory`;
the batch Function API returns an all-`NaN` array instead.

