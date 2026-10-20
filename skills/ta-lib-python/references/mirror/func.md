---
title: "Function API Examples"
url: https://ta-lib.github.io/ta-lib-python/func.html
parent: https://ta-lib.github.io/ta-lib-python/doc_index.html
depth: 0
fetched_at: 2026-10-20T12:30:54+00:00
source: ta-lib.github.io
---

# Function API Examples

Similar to TA-Lib, the function interface provides a lightweight wrapper of
the exposed TA-Lib indicators.

Each function returns an output array and have default values for their
parameters, unless specified as keyword arguments. Typically, these functions
will have an initial "lookback" period (a required number of observations
before an output is generated) set to NaN.

The lookback is function-specific and may be larger than the timeperiod
parameter. For example, RSI(timeperiod=14) needs 15 price observations,
because the first RSI value is derived from 14 consecutive price changes.

All of the following examples use the function API:

```python
import numpy
import talib

close = numpy.random.random(100)
```

Calculate a simple moving average of the close prices:

```python
output = talib.SMA(close)
```

Calculating bollinger bands, with triple exponential moving average:

```python
from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
```

Calculating momentum of the close prices, with a time period of 5:

```python
output = talib.MOM(close, timeperiod=5)
```

Functions documented as having an unstable period start with that extra
unstable-period setting at 0. get_unstable_period() only returns a
non-zero value after you set one explicitly with set_unstable_period().

Documentation for all functions:

1. [Overlap Studies](func_groups/overlap_studies.html)
2. [Momentum Indicators](func_groups/momentum_indicators.html)
3. [Volume Indicators](func_groups/volume_indicators.html)
4. [Volatility Indicators](func_groups/volatility_indicators.html)
5. [Pattern Recognition](func_groups/pattern_recognition.html)
6. [Cycle Indicators](func_groups/cycle_indicators.html)
7. [Statistic Functions](func_groups/statistic_functions.html)
8. [Price Transform](func_groups/price_transform.html)
9. [Math Transform](func_groups/math_transform.html)
10. [Math Operators](func_groups/math_operators.html)

[Documentation Index](doc_index.html)
[Next: Using the Abstract API](abstract.html)
