"""The streaming API: one handle per indicator, one bar at a time.

    python scripts/stream_demo.py
"""
import numpy as np

import talib
from talib import stream


def main():
    n = 200
    rng = np.random.default_rng(7)
    close = 100 + np.cumsum(rng.normal(0, 0.5, n))

    history = []
    handle = None
    # a handle needs enough history; until then it raises InsufficientHistory.
    # the history must be a numpy array (or a pandas/polars Series), not a list.
    for value in close:
        history.append(float(value))
        if handle is None:
            try:
                handle = stream.RSI(np.asarray(history, dtype="float64"),
                                    timeperiod=14)
            except talib.InsufficientHistory:
                continue
        else:
            handle.update(float(value))
        if handle is not None and len(history) > n - 3:
            print("bar %3d  rsi = %s"
                  % (len(history), None if handle.value is None
                     else round(float(handle.value), 4)))

    print()
    print("handle methods:", [m for m in dir(handle) if not m.startswith("_")])


if __name__ == "__main__":
    main()
