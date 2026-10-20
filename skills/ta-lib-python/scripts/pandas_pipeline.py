"""Indicators as columns of a pandas DataFrame.

    python scripts/pandas_pipeline.py
"""
import numpy as np
import pandas as pd

import talib


def build_frame(n=300, seed=7):
    rng = np.random.default_rng(seed)
    close = 100 + np.cumsum(rng.normal(0, 0.5, n))
    high = close + np.abs(rng.normal(0, 0.3, n))
    low = close - np.abs(rng.normal(0, 0.3, n))
    open_ = close + rng.normal(0, 0.1, n)
    volume = rng.integers(100, 1000, n).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=pd.date_range("2024-01-01", periods=n, freq="D"))


def add_indicators(df):
    df = df.copy()
    df["sma20"] = talib.SMA(df["close"], timeperiod=20)
    df["ema50"] = talib.EMA(df["close"], timeperiod=50)
    df["rsi14"] = talib.RSI(df["close"], timeperiod=14)
    df["atr14"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=14)

    macd, signal, hist = talib.MACD(df["close"])
    df["macd"], df["macd_signal"], df["macd_hist"] = macd, signal, hist

    upper, middle, lower = talib.BBANDS(df["close"], timeperiod=20)
    df["bb_upper"], df["bb_mid"], df["bb_lower"] = upper, middle, lower

    df["obv"] = talib.OBV(df["close"], df["volume"])
    df["mfi14"] = talib.MFI(df["high"], df["low"], df["close"], df["volume"],
                            timeperiod=14)
    return df


def main():
    df = build_frame()
    df = add_indicators(df)
    print(df.tail(3).to_string())
    print()
    print("columns:", ", ".join(df.columns))
    print("the indicator columns keep the original date index")


if __name__ == "__main__":
    main()
