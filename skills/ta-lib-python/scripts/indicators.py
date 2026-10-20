"""A small indicator panel over one OHLCV set: trend, momentum, volatility, volume.

    python scripts/indicators.py
"""
import numpy as np

import talib


def panel(high, low, close, volume=None):
    """Return a dict of the most common indicators, with the lookback NaNs kept."""
    out = {
        "sma20": talib.SMA(close, timeperiod=20),
        "ema50": talib.EMA(close, timeperiod=50),
        "rsi14": talib.RSI(close, timeperiod=14),
        "atr14": talib.ATR(high, low, close, timeperiod=14),
        "adx14": talib.ADX(high, low, close, timeperiod=14),
        "mfi14": None,
        "macd": None,
        "bbands": None,
    }
    if volume is not None:
        out["mfi14"] = talib.MFI(high, low, close, volume, timeperiod=14)
    macd, signal, hist = talib.MACD(close)
    out["macd"] = (macd, signal, hist)
    upper, middle, lower = talib.BBANDS(close, timeperiod=20)
    out["bbands"] = (upper, middle, lower)
    return out


def main():
    n = 300
    rng = np.random.default_rng(7)
    close = 100 + np.cumsum(rng.normal(0, 0.5, n))
    high = close + np.abs(rng.normal(0, 0.3, n))
    low = close - np.abs(rng.normal(0, 0.3, n))
    volume = rng.integers(100, 1000, n).astype(float)

    p = panel(high, low, close, volume)
    for key in ("sma20", "ema50", "rsi14", "atr14", "adx14", "mfi14"):
        print("%-8s last = %s" % (key, round(float(p[key][-1]), 4)))
    macd, signal, hist = p["macd"]
    print("macd    last = %.4f  signal = %.4f  hist = %.4f"
          % (macd[-1], signal[-1], hist[-1]))
    upper, middle, lower = p["bbands"]
    print("bands   upper = %.4f  mid = %.4f  lower = %.4f"
          % (upper[-1], middle[-1], lower[-1]))


if __name__ == "__main__":
    main()
