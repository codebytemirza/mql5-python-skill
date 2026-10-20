---
title: "Math Operator Functions"
url: https://ta-lib.github.io/ta-lib-python/func_groups/math_operators.html
parent: https://ta-lib.github.io/ta-lib-python/
depth: 0
fetched_at: 2026-10-20T12:30:53+00:00
source: ta-lib.github.io
---

# Math Operator Functions

#### ADD - Vector Arithmetic Add

```python
real = ADD(high, low)
```

#### CUMSUM - Cumulative Sum

```python
real = CUMSUM(close)
```

#### DIV - Vector Arithmetic Div

```python
real = DIV(high, low)
```

#### MAX - Highest value over a specified period

```python
real = MAX(close, timeperiod=30)
```

#### MAXINDEX - Index of highest value over a specified period

```python
integer = MAXINDEX(close, timeperiod=30)
```

#### MIN - Lowest value over a specified period

```python
real = MIN(close, timeperiod=30)
```

#### MININDEX - Index of lowest value over a specified period

```python
integer = MININDEX(close, timeperiod=30)
```

#### MINMAX - Lowest and highest values over a specified period

```python
min, max = MINMAX(close, timeperiod=30)
```

#### MINMAXINDEX - Indexes of lowest and highest values over a specified period

```python
minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
```

#### MULT - Vector Arithmetic Mult

```python
real = MULT(high, low)
```

#### SUB - Vector Arithmetic Subtraction

```python
real = SUB(high, low)
```

#### SUM - Summation

```python
real = SUM(close, timeperiod=30)
```

[Documentation Index](../doc_index.html)
[All Function Groups](../funcs.html)
