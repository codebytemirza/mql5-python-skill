"""Is TA-Lib installed and working?

    python scripts/smoke_test.py
"""
import sys

import numpy as np

import talib

print("TA-Lib", talib.__version__)
print("functions:", len(talib.get_functions()))
print("groups   :", len(talib.get_function_groups()))

n = 200
rng = np.random.default_rng(7)
close = 100 + np.cumsum(rng.normal(0, 0.5, n))
high = close + np.abs(rng.normal(0, 0.3, n))
low = close - np.abs(rng.normal(0, 0.3, n))
open_ = close + rng.normal(0, 0.1, n)
volume = rng.integers(100, 1000, n).astype(float)

sma = talib.SMA(close, timeperiod=20)
rsi = talib.RSI(close, timeperiod=14)
macd, signal, hist = talib.MACD(close)
atr = talib.ATR(high, low, close, timeperiod=14)
adx = talib.ADX(high, low, close, timeperiod=14)
doji = talib.CDLDOJI(open_, high, low, close)

print()
print("SMA     ->", sma.shape, "first valid at", int(np.argmax(~np.isnan(sma))))
print("RSI     ->", rsi.shape, "last", round(float(rsi[-1]), 4))
print("MACD    ->", macd.shape, signal.shape, hist.shape)
print("ATR     ->", round(float(atr[-1]), 6))
print("ADX     ->", round(float(adx[-1]), 4))
print("CDLDOJI -> unique values", sorted(set(np.unique(doji[np.isfinite(doji)]).tolist())))
print()
print("OK")
