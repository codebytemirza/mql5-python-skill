"""Read-only snapshot of the account, terminal, orders, positions and history.

Run:  .\.venv\Scripts\python.exe scripts\inspect_state.py
"""
import MetaTrader5 as mt5


def show(title, value):
    print("\n== %s ==" % title)
    if value is None:
        print("  None (no connection, or no data for this account)")
        return
    if hasattr(value, "_asdict"):
        # a single named tuple: terminal_info(), account_info(), ...
        print("  ", value)
        return
    if isinstance(value, tuple):
        # a collection of named tuples: orders_get(), positions_get(), ...
        print("  %d entries" % len(value))
        for item in value[:5]:
            print("   ", item)
        if len(value) > 5:
            print("    ... %d more" % (len(value) - 5))
        return
    print("  ", value)


def main():
    if not mt5.initialize():
        raise RuntimeError("MetaTrader5 connection failed: %s" % (mt5.last_error(),))
    try:
        show("terminal_info", mt5.terminal_info())
        show("account_info", mt5.account_info())
        show("symbols_total", mt5.symbols_total())
        show("orders_total", mt5.orders_total())
        show("orders_get", mt5.orders_get())
        show("positions_total", mt5.positions_total())
        show("positions_get", mt5.positions_get())
        show("history_orders_total", mt5.history_orders_total())
        show("history_orders_get", mt5.history_orders_get())
        show("history_deals_total", mt5.history_deals_total())
        show("history_deals_get", mt5.history_deals_get())
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    main()
