---
title: "Statistic Functions"
url: https://ta-lib.github.io/ta-lib-python/func_groups/statistic_functions.html
parent: https://ta-lib.github.io/ta-lib-python/
depth: 0
fetched_at: 2026-10-20T12:30:51+00:00
source: ta-lib.github.io
---

# Statistic Functions

#### BETA - Beta

```python
real = BETA(high, low, timeperiod=5)
```

#### CORREL - Pearson's Correlation Coefficient (r)

```python
real = CORREL(high, low, timeperiod=30)
```

#### LINEARREG - Linear Regression

```python
real = LINEARREG(close, timeperiod=14)
```

#### LINEARREG_ANGLE - Linear Regression Angle

```python
real = LINEARREG_ANGLE(close, timeperiod=14)
```

#### LINEARREG_INTERCEPT - Linear Regression Intercept

```python
real = LINEARREG_INTERCEPT(close, timeperiod=14)
```

#### LINEARREG_SLOPE - Linear Regression Slope

```python
real = LINEARREG_SLOPE(close, timeperiod=14)
```

#### PERCENTILE - Percentile (nearest rank)

```python
real = PERCENTILE(close, timeperiod=30, percentile=50)
```

#### PERCENTRANK - Percent Rank

```python
real = PERCENTRANK(close, timeperiod=100)
```

#### STDDEV - Standard Deviation

```python
real = STDDEV(close, timeperiod=5, nbdev=1)
```

#### TSF - Time Series Forecast

```python
real = TSF(close, timeperiod=14)
```

#### VAR - Variance

```python
real = VAR(close, timeperiod=5, nbdev=1)
```

[Documentation Index](../doc_index.html)
[All Function Groups](../funcs.html)
