# Constants and enumerations

## `matype` - the moving average type

Several functions take a `matype` parameter. It is a **number**; the
package does not export friendly names for it, so keep this table handy.

| value | name | meaning |
| --- | --- | --- |
| 0 | `SMA` | Simple Moving Average |
| 1 | `EMA` | Exponential Moving Average |
| 2 | `WMA` | Weighted Moving Average |
| 3 | `DEMA` | Double Exponential Moving Average |
| 4 | `TEMA` | Triple Exponential Moving Average |
| 5 | `TRIMA` | Triangular Moving Average |
| 6 | `KAMA` | Kaufman Adaptive Moving Average |
| 7 | `MAMA` | MESA Adaptive Moving Average |
| 8 | `T3` | Triple Generalized Double Exponential Moving Average |
| 9 | `HMA` | Hull Moving Average |
| 10 | `DISABLED` | No Moving Average (identity) |
| 11 | `DEFAULT` | The Function's Own Default Moving Average |
| 12 | `ZLEMA` | Zero-Lag Exponential Moving Average |
| 13 | `RMA` | Wilder's Smoothed Moving Average |

These values were **verified** against the installed build: `talib.MA(close,
matype=N)` reproduces `talib.<NAME>(close)` exactly for N = 0, 1, 2, 3, 4,
5, 6, 9, 12 and 13.

```python
talib.MA(close, timeperiod=20, matype=1)   # == talib.EMA(close, 20)
```

## Pattern recognition values

| value | meaning |
| --- | --- |
| `0` | no pattern |
| `+100` | bullish pattern |
| `-100` | bearish pattern |

The stronger variants return a graded value:

| range | meaning |
| --- | --- |
| `[-200, -100]` | bearish |
| `[-100, 0]` | getting bearish |
| `0` | neutral |
| `[0, 100]` | getting bullish |
| `[100, 200]` | bullish |

## `TA_FUNC_FLAGS`

Flags attached to a function. Read them at runtime with
`talib.abstract.Function(name).info['function_flags']`.

| flag | meaning |
| --- | --- |
| `1` | A period of 1 performs no smoothing |
| `16777216` | Output scale same as input |
| `33554432` | Function has a streaming API |
| `67108864` | Output is over volume |
| `134217728` | Function has an unstable period |
| `268435456` | Output is a candlestick |
| `536870912` | Output is path-dependent |
| `1073741824` | Output can be NaN or infinite |

## `TA_INPUT_FLAGS`

| flag | price series |
| --- | --- |
| `1` | open |
| `2` | high |
| `4` | low |
| `8` | close |
| `16` | volume |
| `32` | openInterest |
| `64` | timeStamp |

## `TA_OUTPUT_FLAGS`

| flag | meaning |
| --- | --- |
| `1` | Line |
| `2` | Dotted Line |
| `4` | Dashed Line |
| `8` | Dot |
| `16` | Histogram |
| `32` | Pattern (Bool) |
| `64` | Bull/Bear Pattern (Bearish < 0, Neutral = 0, Bullish > 0) |
| `128` | Strength Pattern ([-200..-100] = Bearish, [-100..0] = Getting Bearish, 0 = Neutral, [0..100] = Getting Bullish, [100-200] = Bullish) |
| `256` | Output can be positive |
| `512` | Output can be negative |
| `1024` | Output can be zero |
| `2048` | Values represent an upper limit |
| `4096` | Values represent a lower limit |
| `8192` | Output is optional (nullable) |

## `InsufficientHistory`

`talib.InsufficientHistory` is raised when a streaming handle is opened on
too little history. The batch Function API does **not** raise it - it
returns an all-`NaN` array instead.

