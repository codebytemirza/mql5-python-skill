# API reference

All 201 functions of the TA-Lib Python package.

Everything below was read from the **installed** package
(TA-Lib 0.8.2) and checked against the official documentation pages.

- **Inputs** - the positional price arrays, in the exact order to pass them.
- **Parameters** - keyword arguments and their defaults.
- **Outputs** - the tuple order when a function returns more than one array.
- **Lookback** - how many leading values are `NaN`.

## Cycle Indicators

5 functions.

### `HT_DCPERIOD`

**Hilbert Transform - Dominant Cycle Period**

```python
real = HT_DCPERIOD(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 32 |

**Note:** NOTE: The HT_DCPERIOD function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/cycle_indicators.html>

### `HT_DCPHASE`

**Hilbert Transform - Dominant Cycle Phase**

```python
real = HT_DCPHASE(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 63 |

**Note:** NOTE: The HT_DCPHASE function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/cycle_indicators.html>

### `HT_PHASOR`

**Hilbert Transform - Phasor Components**

```python
inphase, quadrature = HT_PHASOR(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | inphase, quadrature |
| lookback | 32 |

**Note:** NOTE: The HT_PHASOR function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/cycle_indicators.html>

### `HT_SINE`

**Hilbert Transform - SineWave**

```python
sine, leadsine = HT_SINE(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | sine, leadsine |
| lookback | 63 |

**Note:** NOTE: The HT_SINE function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/cycle_indicators.html>

### `HT_TRENDMODE`

**Hilbert Transform - Trend vs Cycle Mode**

```python
integer = HT_TRENDMODE(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | integer |
| lookback | 63 |

**Note:** NOTE: The HT_TRENDMODE function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/cycle_indicators.html>

## Math Operators

12 functions.

### `ADD`

**Vector Arithmetic Add**

```python
real = ADD(high, low)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `CUMSUM`

**Cumulative Sum**

```python
real = CUMSUM(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `DIV`

**Vector Arithmetic Div**

```python
real = DIV(high, low)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MAX`

**Highest value over a specified period**

```python
real = MAX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MAXINDEX`

**Index of highest value over a specified period**

```python
integer = MAXINDEX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | integer |
| lookback | 29 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MIN`

**Lowest value over a specified period**

```python
real = MIN(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MININDEX`

**Index of lowest value over a specified period**

```python
integer = MININDEX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | integer |
| lookback | 29 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MINMAX`

**Lowest and highest values over a specified period**

```python
min, max = MINMAX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | min, max |
| lookback | 29 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MINMAXINDEX`

**Indexes of lowest and highest values over a specified period**

```python
minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | minidx, maxidx |
| lookback | 29 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `MULT`

**Vector Arithmetic Mult**

```python
real = MULT(high, low)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `SUB`

**Vector Arithmetic Subtraction**

```python
real = SUB(high, low)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

### `SUM`

**Summation**

```python
real = SUM(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html>

## Math Transform

15 functions.

### `ACOS`

**Vector Trigonometric ACos**

```python
real = ACOS(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `ASIN`

**Vector Trigonometric ASin**

```python
real = ASIN(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `ATAN`

**Vector Trigonometric ATan**

```python
real = ATAN(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `CEIL`

**Vector Ceil**

```python
real = CEIL(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `COS`

**Vector Trigonometric Cos**

```python
real = COS(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `COSH`

**Vector Trigonometric Cosh**

```python
real = COSH(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `EXP`

**Vector Arithmetic Exp**

```python
real = EXP(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `FLOOR`

**Vector Floor**

```python
real = FLOOR(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `LN`

**Vector Log Natural**

```python
real = LN(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `LOG10`

**Vector Log10**

```python
real = LOG10(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `SIN`

**Vector Trigonometric Sin**

```python
real = SIN(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `SINH`

**Vector Trigonometric Sinh**

```python
real = SINH(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `SQRT`

**Vector Square Root**

```python
real = SQRT(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `TAN`

**Vector Trigonometric Tan**

```python
real = TAN(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

### `TANH`

**Vector Trigonometric Tanh**

```python
real = TANH(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/math_transform.html>

## Momentum Indicators

47 functions.

### `AC`

**Accelerator/Decelerator Oscillator**

```python
real = AC(high, low, fastperiod=5, slowperiod=34, signalperiod=5)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | fastperiod=5, slowperiod=34, signalperiod=5 |
| outputs | real |
| lookback | 37 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ADX`

**Average Directional Movement Index**

```python
real = ADX(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 27 |

**Note:** NOTE: The ADX function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ADXR`

**Average Directional Movement Index Rating**

```python
real = ADXR(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 40 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `AO`

**Awesome Oscillator**

```python
real = AO(high, low, fastperiod=5, slowperiod=34)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | fastperiod=5, slowperiod=34 |
| outputs | real |
| lookback | 33 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `APO`

**Absolute Price Oscillator**

```python
real = APO(close, fastperiod=12, slowperiod=26, matype=1)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | fastperiod=12, slowperiod=26, matype=1 |
| outputs | real |
| lookback | 25 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `AROON`

**Aroon**

```python
aroondown, aroonup = AROON(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | aroondown, aroonup |
| lookback | 14 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `AROONOSC`

**Aroon Oscillator**

```python
real = AROONOSC(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `BOP`

**Balance Of Power**

```python
real = BOP(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `CCI`

**Commodity Channel Index**

```python
real = CCI(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `CMO`

**Chande Momentum Oscillator**

```python
real = CMO(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The CMO function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `CMOU`

**Chande Momentum Oscillator (Unsmoothed)**

```python
real = CMOU(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `COPPOCK`

**Coppock Curve**

```python
real = COPPOCK(close, wmaperiod=10, roc1period=11, roc2period=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | wmaperiod=10, roc1period=11, roc2period=14 |
| outputs | real |
| lookback | 23 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `DPO`

**Detrended Price Oscillator**

```python
real = DPO(close, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=20 |
| outputs | real |
| lookback | 19 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `DX`

**Directional Movement Index**

```python
real = DX(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The DX function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ER`

**Kaufman Efficiency Ratio**

```python
real = ER(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ERI`

**Elder Ray Index (Bull Power / Bear Power)**

```python
bullpower, bearpower = ERI(high, low, close, timeperiod=13)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=13 |
| outputs | bullpower, bearpower |
| lookback | 12 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `FOSC`

**Forecast Oscillator**

```python
real = FOSC(close, timeperiod=5)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=5 |
| outputs | real |
| lookback | 5 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `FRACTAL`

**Williams Fractal**

```python
swinghigh, swinglow = FRACTAL(high, low, leftbars=2, rightbars=2)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | leftbars=2, rightbars=2 |
| outputs | swinghigh, swinglow |
| lookback | 4 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `IMI`

**Intraday Momentum Index**

```python
real = IMI(open, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | open, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `KDJ`

**KDJ Stochastic**

```python
k, d, j = KDJ(high, low, close, fastk_period=9, slowk_period=3, slowk_matype=13, slowd_period=3, slowd_matype=13)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | fastk_period=9, slowk_period=3, slowk_matype=13, slowd_period=3, slowd_matype=13 |
| outputs | k, d, j |
| lookback | 12 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MACD`

**Moving Average Convergence/Divergence**

```python
macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | fastperiod=12, slowperiod=26, signalperiod=9 |
| outputs | macd, macdsignal, macdhist |
| lookback | 33 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MACDEXT`

**MACD with controllable MA type**

```python
macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0 |
| outputs | macd, macdsignal, macdhist |
| lookback | 33 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MACDFIX`

**Moving Average Convergence/Divergence Fix 12/26**

```python
macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | signalperiod=9 |
| outputs | macd, macdsignal, macdhist |
| lookback | 33 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MFI`

**Money Flow Index**

```python
real = MFI(high, low, close, volume, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close, volume |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MINUS_DI`

**Minus Directional Indicator**

```python
real = MINUS_DI(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The MINUS_DI function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MINUS_DM`

**Minus Directional Movement**

```python
real = MINUS_DM(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Note:** NOTE: The MINUS_DM function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `MOM`

**Momentum**

```python
real = MOM(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `PLUS_DI`

**Plus Directional Indicator**

```python
real = PLUS_DI(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The PLUS_DI function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `PLUS_DM`

**Plus Directional Movement**

```python
real = PLUS_DM(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Note:** NOTE: The PLUS_DM function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `PPO`

**Percentage Price Oscillator**

```python
real = PPO(close, fastperiod=12, slowperiod=26, matype=1)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | fastperiod=12, slowperiod=26, matype=1 |
| outputs | real |
| lookback | 25 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `QSTICK`

**Qstick**

```python
real = QSTICK(open, close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | open, close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 9 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ROC`

**Rate of change : ((price/prevPrice)-1)*100**

```python
real = ROC(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ROCP`

**Rate of change Percentage: (price-prevPrice)/prevPrice**

```python
real = ROCP(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ROCR`

**Rate of change ratio: (price/prevPrice)**

```python
real = ROCR(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ROCR100`

**Rate of change ratio 100 scale: (price/prevPrice)*100**

```python
real = ROCR100(close, timeperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=10 |
| outputs | real |
| lookback | 10 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `RSI`

**Relative Strength Index**

```python
real = RSI(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The RSI function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `SMI`

**Stochastic Momentum Index**

```python
smi, smisignal = SMI(high, low, close, timeperiod=13, fastperiod=2, slowperiod=25, signalperiod=9)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=13, fastperiod=2, slowperiod=25, signalperiod=9 |
| outputs | smi, smisignal |
| lookback | 45 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `STOCH`

**Stochastic**

```python
slowk, slowd = STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0 |
| outputs | slowk, slowd |
| lookback | 8 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `STOCHF`

**Stochastic Fast**

```python
fastk, fastd = STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | fastk_period=5, fastd_period=3, fastd_matype=0 |
| outputs | fastk, fastd |
| lookback | 6 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `STOCHRSI`

**Stochastic Relative Strength Index**

```python
fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0 |
| outputs | fastk, fastd |
| lookback | 20 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `TRIX`

**1-day Rate-Of-Change (ROC) of a Triple Smooth EMA**

```python
real = TRIX(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 88 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `TSI`

**True Strength Index**

```python
real = TSI(close, firstperiod=25, secondperiod=13)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | firstperiod=25, secondperiod=13 |
| outputs | real |
| lookback | 37 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `ULTOSC`

**Ultimate Oscillator**

```python
real = ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod1=7, timeperiod2=14, timeperiod3=28 |
| outputs | real |
| lookback | 28 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `VHF`

**Vertical Horizontal Filter**

```python
real = VHF(close, timeperiod=28)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=28 |
| outputs | real |
| lookback | 28 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `VORTEX`

**Vortex Indicator**

```python
plusvi, minusvi = VORTEX(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | plusvi, minusvi |
| lookback | 14 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `WAD`

**Williams' Accumulation/Distribution**

```python
real = WAD(high, low, close)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

### `WILLR`

**Williams' %R**

```python
real = WILLR(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html>

## Overlap Studies

25 functions.

### `ACCBANDS`

**Acceleration Bands**

```python
upperband, middleband, lowerband = ACCBANDS(high, low, close, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=20 |
| outputs | upperband, middleband, lowerband |
| lookback | 19 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `BBANDS`

**Bollinger Bands**

```python
upperband, middleband, lowerband = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=20, nbdevup=2.0, nbdevdn=2.0, matype=0 |
| outputs | upperband, middleband, lowerband |
| lookback | 19 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `DEMA`

**Double Exponential Moving Average**

```python
real = DEMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 58 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `DONCHIAN`

**Donchian Channels**

```python
upperband, middleband, lowerband = DONCHIAN(high, low, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=20 |
| outputs | upperband, middleband, lowerband |
| lookback | 19 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `EMA`

**Exponential Moving Average**

```python
real = EMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Note:** NOTE: The EMA function has an unstable period.

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `HMA`

**Hull Moving Average**

```python
real = HMA(close, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=20 |
| outputs | real |
| lookback | 22 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `HT_TRENDLINE`

**Hilbert Transform - Instantaneous Trendline**

```python
real = HT_TRENDLINE(close)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | none |
| outputs | real |
| lookback | 63 |

**Note:** NOTE: The HT_TRENDLINE function has an unstable period.

**Flags:** Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `KAMA`

**Kaufman Adaptive Moving Average**

```python
real = KAMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 30 |

**Note:** NOTE: The KAMA function has an unstable period.

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `KC`

**Keltner Channels**

```python
upperband, middleband, lowerband = KC(high, low, close, timeperiod=20, atrperiod=10, nbdev=2)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=20, atrperiod=10, nbdev=2.0 |
| outputs | upperband, middleband, lowerband |
| lookback | 19 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `MA`

**Moving average**

```python
real = MA(close, timeperiod=30, matype=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30, matype=0 |
| outputs | real |
| lookback | 29 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `MAMA`

**MESA Adaptive Moving Average**

```python
mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | fastlimit=0.5, slowlimit=0.05 |
| outputs | mama, fama |
| lookback | 32 |

**Note:** NOTE: The MAMA function has an unstable period.

**Flags:** Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `MAVP`

**Moving average with variable period**

```python
real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | minperiod=2, maxperiod=30, matype=0 |
| outputs | real |
| lookback | 29 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `MIDPOINT`

**MidPoint over period**

```python
real = MIDPOINT(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `MIDPRICE`

**Midpoint Price over period**

```python
real = MIDPRICE(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `RMA`

**Wilder's Smoothed Moving Average**

```python
real = RMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Note:** NOTE: The RMA function has an unstable period.

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `SAR`

**Parabolic SAR**

```python
real = SAR(high, low, acceleration=0, maximum=0)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | acceleration=0.02, maximum=0.2 |
| outputs | real |
| lookback | 1 |

**Flags:** Output scale same as input; Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `SAREXT`

**Parabolic SAR - Extended**

```python
real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | startvalue=0.0, offsetonreverse=0.0, accelerationinitlong=0.02, accelerationlong=0.02, accelerationmaxlong=0.2, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.2 |
| outputs | real |
| lookback | 1 |

**Flags:** Output scale same as input; Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `SMA`

**Simple Moving Average**

```python
real = SMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `SUPERTREND`

**SuperTrend**

```python
supertrend, trend = SUPERTREND(high, low, close, timeperiod=10, multiplier=3)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=10, multiplier=3.0 |
| outputs | supertrend, trend |
| lookback | 10 |

**Flags:** Output scale same as input; Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `T3`

**Triple Exponential Moving Average (T3)**

```python
real = T3(close, timeperiod=5, vfactor=0)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=5, vfactor=0.7 |
| outputs | real |
| lookback | 24 |

**Note:** NOTE: The T3 function has an unstable period.

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `TEMA`

**Triple Exponential Moving Average**

```python
real = TEMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 87 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `TRIMA`

**Triangular Moving Average**

```python
real = TRIMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `VWMA`

**Volume Weighted Moving Average**

```python
real = VWMA(close, volume, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | volume |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `WMA`

**Weighted Moving Average**

```python
real = WMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

### `ZLEMA`

**Zero-Lag Exponential Moving Average**

```python
real = ZLEMA(close, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 43 |

**Flags:** A period of 1 performs no smoothing; Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/overlap_studies.html>

## Pattern Recognition

61 functions.

### `CDL2CROWS`

**Two Crows**

```python
integer = CDL2CROWS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3BLACKCROWS`

**Three Black Crows**

```python
integer = CDL3BLACKCROWS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 13 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3INSIDE`

**Three Inside Up/Down**

```python
integer = CDL3INSIDE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3LINESTRIKE`

**Three-Line Strike**

```python
integer = CDL3LINESTRIKE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 8 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3OUTSIDE`

**Three Outside Up/Down**

```python
integer = CDL3OUTSIDE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 3 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3STARSINSOUTH`

**Three Stars In The South**

```python
integer = CDL3STARSINSOUTH(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDL3WHITESOLDIERS`

**Three Advancing White Soldiers**

```python
integer = CDL3WHITESOLDIERS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLABANDONEDBABY`

**Abandoned Baby**

```python
integer = CDLABANDONEDBABY(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.3 |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLADVANCEBLOCK`

**Advance Block**

```python
integer = CDLADVANCEBLOCK(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLBELTHOLD`

**Belt-hold**

```python
integer = CDLBELTHOLD(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLBREAKAWAY`

**Breakaway**

```python
integer = CDLBREAKAWAY(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 14 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLCLOSINGMARUBOZU`

**Closing Marubozu**

```python
integer = CDLCLOSINGMARUBOZU(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLCONCEALBABYSWALL`

**Concealing Baby Swallow**

```python
integer = CDLCONCEALBABYSWALL(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 13 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLCOUNTERATTACK`

**Counterattack**

```python
integer = CDLCOUNTERATTACK(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLDARKCLOUDCOVER`

**Dark Cloud Cover**

```python
integer = CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.5 |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLDOJI`

**Doji**

```python
integer = CDLDOJI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLDOJISTAR`

**Doji Star**

```python
integer = CDLDOJISTAR(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLDRAGONFLYDOJI`

**Dragonfly Doji**

```python
integer = CDLDRAGONFLYDOJI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLENGULFING`

**Engulfing Pattern**

```python
integer = CDLENGULFING(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 2 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLEVENINGDOJISTAR`

**Evening Doji Star**

```python
integer = CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.3 |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLEVENINGSTAR`

**Evening Star**

```python
integer = CDLEVENINGSTAR(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.3 |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLGAPSIDESIDEWHITE`

**Up/Down-gap side-by-side white lines**

```python
integer = CDLGAPSIDESIDEWHITE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 7 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLGRAVESTONEDOJI`

**Gravestone Doji**

```python
integer = CDLGRAVESTONEDOJI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHAMMER`

**Hammer**

```python
integer = CDLHAMMER(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHANGINGMAN`

**Hanging Man**

```python
integer = CDLHANGINGMAN(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHARAMI`

**Harami Pattern**

```python
integer = CDLHARAMI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHARAMICROSS`

**Harami Cross Pattern**

```python
integer = CDLHARAMICROSS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHIGHWAVE`

**High-Wave Candle**

```python
integer = CDLHIGHWAVE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHIKKAKE`

**Hikkake Pattern**

```python
integer = CDLHIKKAKE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 5 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHIKKAKEMOD`

**Modified Hikkake Pattern**

```python
integer = CDLHIKKAKEMOD(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLHOMINGPIGEON`

**Homing Pigeon**

```python
integer = CDLHOMINGPIGEON(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLIDENTICAL3CROWS`

**Identical Three Crows**

```python
integer = CDLIDENTICAL3CROWS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLINNECK`

**In-Neck Pattern**

```python
integer = CDLINNECK(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLINVERTEDHAMMER`

**Inverted Hammer**

```python
integer = CDLINVERTEDHAMMER(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLKICKING`

**Kicking**

```python
integer = CDLKICKING(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLKICKINGBYLENGTH`

**Kicking - bull/bear determined by the longer marubozu**

```python
integer = CDLKICKINGBYLENGTH(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLLADDERBOTTOM`

**Ladder Bottom**

```python
integer = CDLLADDERBOTTOM(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 14 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLLONGLEGGEDDOJI`

**Long Legged Doji**

```python
integer = CDLLONGLEGGEDDOJI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLLONGLINE`

**Long Line Candle**

```python
integer = CDLLONGLINE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLMARUBOZU`

**Marubozu**

```python
integer = CDLMARUBOZU(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLMATCHINGLOW`

**Matching Low**

```python
integer = CDLMATCHINGLOW(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 6 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLMATHOLD`

**Mat Hold**

```python
integer = CDLMATHOLD(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.5 |
| outputs | integer |
| lookback | 14 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLMORNINGDOJISTAR`

**Morning Doji Star**

```python
integer = CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.3 |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLMORNINGSTAR`

**Morning Star**

```python
integer = CDLMORNINGSTAR(open, high, low, close, penetration=0)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | penetration=0.3 |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLONNECK`

**On-Neck Pattern**

```python
integer = CDLONNECK(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLPIERCING`

**Piercing Pattern**

```python
integer = CDLPIERCING(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLRICKSHAWMAN`

**Rickshaw Man**

```python
integer = CDLRICKSHAWMAN(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLRISEFALL3METHODS`

**Rising/Falling Three Methods**

```python
integer = CDLRISEFALL3METHODS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 14 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSEPARATINGLINES`

**Separating Lines**

```python
integer = CDLSEPARATINGLINES(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSHOOTINGSTAR`

**Shooting Star**

```python
integer = CDLSHOOTINGSTAR(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSHORTLINE`

**Short Line Candle**

```python
integer = CDLSHORTLINE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSPINNINGTOP`

**Spinning Top**

```python
integer = CDLSPINNINGTOP(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSTALLEDPATTERN`

**Stalled Pattern**

```python
integer = CDLSTALLEDPATTERN(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLSTICKSANDWICH`

**Stick Sandwich**

```python
integer = CDLSTICKSANDWICH(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 7 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLTAKURI`

**Takuri (Dragonfly Doji with very long lower shadow)**

```python
integer = CDLTAKURI(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 10 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLTASUKIGAP`

**Tasuki Gap**

```python
integer = CDLTASUKIGAP(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 7 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLTHRUSTING`

**Thrusting Pattern**

```python
integer = CDLTHRUSTING(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 11 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLTRISTAR`

**Tristar Pattern**

```python
integer = CDLTRISTAR(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLUNIQUE3RIVER`

**Unique 3 River**

```python
integer = CDLUNIQUE3RIVER(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLUPSIDEGAP2CROWS`

**Upside Gap Two Crows**

```python
integer = CDLUPSIDEGAP2CROWS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 12 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

### `CDLXSIDEGAP3METHODS`

**Upside/Downside Gap Three Methods**

```python
integer = CDLXSIDEGAP3METHODS(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | integer |
| lookback | 2 |

**Flags:** Function has a streaming API; Output is a candlestick

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/pattern_recognition.html>

## Price Transform

6 functions.

### `AVGDEV`

**Average Deviation**

```python
real = AVGDEV(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

### `AVGPRICE`

**Average Price**

```python
real = AVGPRICE(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

### `HA`

**Heikin-Ashi Candles**

```python
haopen, hahigh, halow, haclose = HA(open, high, low, close)
```

|  |  |
| --- | --- |
| inputs | open, high, low, close |
| parameters | none |
| outputs | haopen, hahigh, halow, haclose |
| lookback | 0 |

**Note:** NOTE: The HA function has an unstable period.

**Flags:** Output scale same as input; Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

### `MEDPRICE`

**Median Price**

```python
real = MEDPRICE(high, low)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

### `TYPPRICE`

**Typical Price**

```python
real = TYPPRICE(high, low, close)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

### `WCLPRICE`

**Weighted Close Price**

```python
real = WCLPRICE(high, low, close)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/price_transform.html>

## Statistic Functions

11 functions.

### `BETA`

**Beta**

```python
real = BETA(high, low, timeperiod=5)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=5 |
| outputs | real |
| lookback | 5 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `CORREL`

**Pearson's Correlation Coefficient (r)**

```python
real = CORREL(high, low, timeperiod=30)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30 |
| outputs | real |
| lookback | 29 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `LINEARREG`

**Linear Regression**

```python
real = LINEARREG(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `LINEARREG_ANGLE`

**Linear Regression Angle**

```python
real = LINEARREG_ANGLE(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `LINEARREG_INTERCEPT`

**Linear Regression Intercept**

```python
real = LINEARREG_INTERCEPT(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `LINEARREG_SLOPE`

**Linear Regression Slope**

```python
real = LINEARREG_SLOPE(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `PERCENTILE`

**Percentile (nearest rank)**

```python
real = PERCENTILE(close, timeperiod=30, percentile=50)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=30, percentile=50.0 |
| outputs | real |
| lookback | 29 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `PERCENTRANK`

**Percent Rank**

```python
real = PERCENTRANK(close, timeperiod=100)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=100 |
| outputs | real |
| lookback | 100 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `STDDEV`

**Standard Deviation**

```python
real = STDDEV(close, timeperiod=5, nbdev=1)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=5, nbdev=1.0 |
| outputs | real |
| lookback | 4 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `TSF`

**Time Series Forecast**

```python
real = TSF(close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Output scale same as input; Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

### `VAR`

**Variance**

```python
real = VAR(close, timeperiod=5, nbdev=1)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=5, nbdev=1.0 |
| outputs | real |
| lookback | 4 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html>

## Volatility Indicators

7 functions.

### `ADR`

**Average Day Range**

```python
real = ADR(high, low, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `ATR`

**Average True Range**

```python
real = ATR(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The ATR function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `CVI`

**Chaikin's Volatility**

```python
real = CVI(high, low, timeperiod=10, rocperiod=10)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | timeperiod=10, rocperiod=10 |
| outputs | real |
| lookback | 19 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `MASSI`

**Mass Index**

```python
real = MASSI(high, low, fastperiod=9, slowperiod=25)
```

|  |  |
| --- | --- |
| inputs | high, low |
| parameters | fastperiod=9, slowperiod=25 |
| outputs | real |
| lookback | 40 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `NATR`

**Normalized Average True Range**

```python
real = NATR(high, low, close, timeperiod=14)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | timeperiod=14 |
| outputs | real |
| lookback | 14 |

**Note:** NOTE: The NATR function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `RVI`

**Relative Volatility Index**

```python
real = RVI(close, timeperiod=14, stddevperiod=10)
```

|  |  |
| --- | --- |
| inputs | close |
| parameters | timeperiod=14, stddevperiod=10 |
| outputs | real |
| lookback | 22 |

**Note:** NOTE: The RVI function has an unstable period.

**Flags:** Function has a streaming API; Function has an unstable period

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

### `TRANGE`

**True Range**

```python
real = TRANGE(high, low, close)
```

|  |  |
| --- | --- |
| inputs | high, low, close |
| parameters | none |
| outputs | real |
| lookback | 1 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html>

## Volume Indicators

12 functions.

### `AD`

**Chaikin A/D Line**

```python
real = AD(high, low, close, volume)
```

|  |  |
| --- | --- |
| inputs | high, low, close, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `ADOSC`

**Chaikin A/D Oscillator**

```python
real = ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
```

|  |  |
| --- | --- |
| inputs | high, low, close, volume |
| parameters | fastperiod=3, slowperiod=10 |
| outputs | real |
| lookback | 9 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `CMF`

**Chaikin Money Flow**

```python
real = CMF(high, low, close, volume, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | high, low, close, volume |
| parameters | timeperiod=20 |
| outputs | real |
| lookback | 19 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `EFI`

**Elder's Force Index**

```python
real = EFI(close, volume, timeperiod=13)
```

|  |  |
| --- | --- |
| inputs | close, volume |
| parameters | timeperiod=13 |
| outputs | real |
| lookback | 13 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `MARKETFI`

**Market Facilitation Index**

```python
real = MARKETFI(high, low, volume)
```

|  |  |
| --- | --- |
| inputs | high, low, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `NVI`

**Negative Volume Index**

```python
real = NVI(close, volume)
```

|  |  |
| --- | --- |
| inputs | close, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `OBV`

**On Balance Volume**

```python
real = OBV(close, volume)
```

|  |  |
| --- | --- |
| inputs | volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `PVI`

**Positive Volume Index**

```python
real = PVI(close, volume)
```

|  |  |
| --- | --- |
| inputs | close, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `PVO`

**Percentage Volume Oscillator**

```python
real = PVO(volume, fastperiod=12, slowperiod=26, matype=1)
```

|  |  |
| --- | --- |
| inputs | volume |
| parameters | fastperiod=12, slowperiod=26, matype=1 |
| outputs | real |
| lookback | 25 |

**Flags:** Function has a streaming API

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `PVT`

**Price Volume Trend**

```python
real = PVT(close, volume)
```

|  |  |
| --- | --- |
| inputs | close, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `RVOL`

**Relative Volume**

```python
real = RVOL(volume, timeperiod=20)
```

|  |  |
| --- | --- |
| inputs | volume |
| parameters | timeperiod=20 |
| outputs | real |
| lookback | 20 |

**Flags:** Function has a streaming API; Output can be NaN or infinite

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

### `VWAP`

**Volume Weighted Average Price**

```python
real = VWAP(high, low, close, volume)
```

|  |  |
| --- | --- |
| inputs | high, low, close, volume |
| parameters | none |
| outputs | real |
| lookback | 0 |

**Flags:** Output scale same as input; Function has a streaming API; Output is path-dependent

**Source:** <https://ta-lib.github.io/ta-lib-python/func_groups/volume_indicators.html>

