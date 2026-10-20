"""Environment smoke test for the MetaTrader5 package.

Run:  .\.venv\Scripts\python.exe scripts\smoke_test.py

Exits 0 when the environment is ready, 1 otherwise. Safe to run without a
terminal: it reports the exact failure instead of raising a traceback.
"""
import sys

import MetaTrader5 as mt5


def main():
    print("MetaTrader5 package version:", mt5.__version__)
    print("author:", mt5.__author__)
    print()

    if not mt5.initialize():
        code, message = mt5.last_error()
        print("FAILED to connect to the MetaTrader 5 terminal")
        print("  last_error():", (code, message))
        if code == -6:
            print("  -> start MetaTrader 5 and log in, then run this again")
        elif code == -2:
            print("  -> bad terminal path; pass the full path to terminal64.exe")
        return 1

    print("connected")
    try:
        term = mt5.terminal_info()
        print("terminal:", term)
        acct = mt5.account_info()
        print("account:", acct)
        print("symbols:", mt5.symbols_total())

        tick = mt5.symbol_info_tick("EURUSD")
        print("EURUSD tick:", tick)

        bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 10)
        if bars is None:
            print("no bars for EURUSD M1 (symbol may not be selected)")
        else:
            print("EURUSD M1 bars:", len(bars), "columns:", bars.dtype.names)
        return 0
    finally:
        mt5.shutdown()
        print("shutdown ok")


if __name__ == "__main__":
    sys.exit(main())
