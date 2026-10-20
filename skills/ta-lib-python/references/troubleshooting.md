# Troubleshooting

| symptom | cause | fix |
| --- | --- | --- |
| `TypeError: ... takes exactly N positional argument(s)` | wrong number of price arrays | check `input_names` for that function - the order differs per function |
| `ValueError: all input arrays must have the same length` | mismatched series | slice them to a common length first |
| the first values are `NaN` | normal - that is the lookback | drop them with `arr[lookback:]` or keep them |
| `TypeError: 'float' object is not subscriptable` | you passed a scalar instead of an array | pass a numpy array of prices |
| `Exception: Cannot mix polars and pandas` | two different series libraries in one call | convert to numpy first |
| `ImportError: talib could not load its extension module` | the TA-Lib C library is missing or too old | install the C library, or use a prebuilt wheel |
| `talib.InsufficientHistory` | the streaming handle was opened on too little history | feed more bars, then retry - see `references/quickstart.md` |
| results look wrong for the first bars | the function has an **unstable period** | ignore the first values, or see `talib.set_unstable_period` |
| `matype` has no effect | wrong number | the values are in `references/constants.md` |
| pattern always returns 0 | no pattern in the data, or the array is too short | check with `np.unique(result)` |

## Checking a function's contract

```python
import talib.abstract

f = talib.abstract.Function("ADX")
print(f.info["input_names"])     # {'prices': ['high', 'low', 'close']}
print(f.info["parameters"])      # {'timeperiod': 14}
print(f.info["output_names"])     # ['real']
print(f.lookback)                 # 27
print(f.info["function_flags"])   # ['Function has an unstable period']
```

## Cleaning the input

`NaN` and `inf` in the history are undefined behaviour in the C library.

```python
import numpy as np

def clean(series):
    s = np.asarray(series, dtype="float64")
    s[~np.isfinite(s)] = np.nan      # inf -> NaN
    return s
```

## The unstable period

Some indicators have a warm-up during which their values are unreliable.
The official documentation marks each one with a `NOTE:` line, and the
package exposes them at runtime:

```python
import talib.abstract

unstable = [n for n in talib.get_functions()
            if any("unstable" in f
               for f in talib.abstract.Function(n).info["function_flags"])]
```

