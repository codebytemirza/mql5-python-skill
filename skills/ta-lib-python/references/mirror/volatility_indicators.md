---
title: "Volatility Indicator Functions"
url: https://ta-lib.github.io/ta-lib-python/func_groups/volatility_indicators.html
parent: https://ta-lib.github.io/ta-lib-python/
depth: 0
fetched_at: 2026-10-20T12:30:44+00:00
source: ta-lib.github.io
---

# Volatility Indicator Functions

#### ADR - Average Day Range

```python
real = ADR(high, low, timeperiod=14)
```

#### ATR - Average True Range

NOTE: The ATR function has an unstable period.

```python
real = ATR(high, low, close, timeperiod=14)
```

#### CVI - Chaikin's Volatility

```python
real = CVI(high, low, timeperiod=10, rocperiod=10)
```

#### MASSI - Mass Index

```python
real = MASSI(high, low, fastperiod=9, slowperiod=25)
```

#### NATR - Normalized Average True Range

NOTE: The NATR function has an unstable period.

```python
real = NATR(high, low, close, timeperiod=14)
```

#### RVI - Relative Volatility Index

NOTE: The RVI function has an unstable period.

```python
real = RVI(close, timeperiod=14, stddevperiod=10)
```

#### TRANGE - True Range

```python
real = TRANGE(high, low, close)
```

[Documentation Index](../doc_index.html)
[All Function Groups](../funcs.html)
