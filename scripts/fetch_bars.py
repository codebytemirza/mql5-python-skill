"""Download bars with the three copy_rates_* variants and print a summary.

Run:  .\.venv\Scripts\python.exe scripts\fetch_bars.py
"""
from datetime import datetime, timedelta

import MetaTrader5 as mt5

SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M1


def main():
    if not mt5.initialize():
        raise RuntimeError("MetaTrader5 connection failed: %s" % (mt5.last_error(),))
    try:
        if not mt5.symbol_info(SYMBOL).visible:
            mt5.symbol_select(SYMBOL, True)

        # 1. the last N bars
        last = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, 0, 100)
        print("copy_rates_from_pos  ->", None if last is None else len(last))

        # 2. bars from a point in time
        since = datetime.now() - timedelta(hours=5)
        from_dt = mt5.copy_rates_from(SYMBOL, TIMEFRAME, since, 100)
        print("copy_rates_from      ->", None if from_dt is None else len(from_dt))

        # 3. bars in a date range
        rng = mt5.copy_rates_range(SYMBOL, TIMEFRAME,
                                   datetime.now() - timedelta(hours=2),
                                   datetime.now())
        print("copy_rates_range     ->", None if rng is None else len(rng))

        if last is not None:
            print("columns:", last.dtype.names)
            print("newest bar:", last[-1])
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    main()
