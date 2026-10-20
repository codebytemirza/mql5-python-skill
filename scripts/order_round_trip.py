# -*- coding: utf-8 -*-
"""
Live order round trip on the connected demo account.

  order_check  -> order_send (open) -> verify -> order_send (close) -> verify flat

Places REAL orders on the account the terminal is logged into. Volume is
symbol volume_min so the exposure is the smallest the broker accepts.

Run:  .\\.venv\\Scripts\\python.exe order_round_trip.py [SYMBOL] [VOLUME]
"""
import io
import json
import sys
import time
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import MetaTrader5 as mt5

SYMBOL = sys.argv[1] if len(sys.argv) > 1 else "EURUSD"
MAGIC = 234000
DEVIATION = 30
TAG = "py-roundtrip"


def pick_filling(info):
    """The package does not export SYMBOL_FILLING_*; derive it from the bitmask."""
    mode = info.filling_mode
    if mode & 1:
        return mt5.ORDER_FILLING_FOK, "ORDER_FILLING_FOK"
    if mode & 2:
        return mt5.ORDER_FILLING_IOC, "ORDER_FILLING_IOC"
    if mode & 4:
        return mt5.ORDER_FILLING_RETURN, "ORDER_FILLING_RETURN"
    return mt5.ORDER_FILLING_FOK, "ORDER_FILLING_FOK (fallback)"


def dump(label, result):
    print("\n--- %s ---" % label)
    print(result)
    d = result._asdict()
    for k, v in d.items():
        print("   %-14s = %r" % (k, v))
        if k == "request" and hasattr(v, "_asdict"):
            print("   request echo:")
            for rk, rv in v._asdict().items():
                print("      %-12s = %r" % (rk, rv))
    return d


def main():
    if not mt5.initialize():
        print("initialize failed:", mt5.last_error())
        return 1

    report = {"at": datetime.now().isoformat(timespec="seconds"),
              "symbol": SYMBOL, "magic": MAGIC}
    io.open("_cache/round_trip.json", "w", encoding="utf-8").write("{}")

    try:
        acct = mt5.account_info()
        term = mt5.terminal_info()
        print("account: login=%s server=%s balance=%s %s"
              % (acct.login, acct.server, acct.balance, acct.currency))
        print("terminal: build=%s connected=%s trade_allowed=%s"
              % (term.build, term.connected, term.trade_allowed))
        if not acct.trade_allowed:
            print("ACCOUNT DOES NOT ALLOW TRADING")
            return 1
        if acct.balance <= 0:
            print("ACCOUNT HAS NO BALANCE")
            return 1

        info = mt5.symbol_info(SYMBOL)
        if info is None:
            print("unknown symbol:", SYMBOL)
            return 1
        if not info.visible:
            print("symbol not visible, selecting ...")
            mt5.symbol_select(SYMBOL, True)
            info = mt5.symbol_info(SYMBOL)

        volume = float(sys.argv[2]) if len(sys.argv) > 2 else info.volume_min
        # round to the broker's volume step
        volume = round(round(volume / info.volume_step) * info.volume_step, 8)
        fill, fill_name = pick_filling(info)
        tick = mt5.symbol_info_tick(SYMBOL)
        if tick is None:
            print("no tick for", SYMBOL)
            return 1

        print("\nsymbol   : %s  digits=%d point=%s" % (SYMBOL, info.digits, info.point))
        print("volume   : %s (min=%s step=%s)" % (volume, info.volume_min, info.volume_step))
        print("filling  : %s (filling_mode=%s)" % (fill_name, info.filling_mode))
        print("deviation: %s points" % DEVIATION)
        print("positions before: %d" % mt5.positions_total())

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": SYMBOL,
            "volume": volume,
            "type": mt5.ORDER_TYPE_BUY,
            "price": tick.ask,
            "deviation": DEVIATION,
            "magic": MAGIC,
            "comment": TAG + " open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": fill,
        }
        report["open_request"] = dict(request)
        report["filling"] = fill_name

        # ---- 1. dry run -------------------------------------------------
        print("\n=== STEP 1: order_check (no server side effect) ===")
        check = mt5.order_check(request)
        if check is None:
            print("order_check returned None:", mt5.last_error())
            return 1
        dump("order_check result", check)
        print("   margin needed: %s   free margin: %s" % (check.margin, check.margin_free))
        if check.retcode != 0:
            print("REQUEST REJECTED BY order_check (retcode %s): %s"
                  % (check.retcode, check.comment))
            return 1
        print("   order_check accepted the request (retcode 0, comment %r)" % check.comment)

        # ---- 2. open ----------------------------------------------------
        print("\n=== STEP 2: order_send (OPEN) ===")
        result = mt5.order_send(request)
        if result is None:
            print("order_send returned None:", mt5.last_error())
            return 1
        d = dump("order_send (open) result", result)
        report["open_result"] = {k: str(v) for k, v in d.items()}
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("OPEN FAILED, retcode=%s comment=%r" % (result.retcode, result.comment))
            return 1
        position_id = result.order
        print("   OPENED. position/order ticket = %s  deal = %s  price = %s"
              % (position_id, result.deal, result.price))

        # ---- 3. confirm it is really there -----------------------------
        print("\n=== STEP 3: verify the position exists ===")
        time.sleep(2)
        positions = mt5.positions_get(symbol=SYMBOL)
        print("positions_total() = %s" % mt5.positions_total())
        for p in (positions or []):
            print("   position ticket=%s type=%s volume=%s price_open=%s sl=%s tp=%s"
                  % (p.ticket, p.type, p.volume, p.price_open, p.sl, p.tp))
        found = [p for p in (positions or []) if p.ticket == position_id]
        if not found:
            print("position %s not visible yet - aborting before closing" % position_id)
            report["error"] = "position not found after open"
            return 1
        pos = found[0]
        report["position"] = {k: str(v) for k, v in pos._asdict().items()}

        # ---- 4. close ---------------------------------------------------
        print("\n=== STEP 4: order_send (CLOSE) ===")
        tick2 = mt5.symbol_info_tick(SYMBOL)
        close_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": SYMBOL,
            "volume": pos.volume,
            "type": mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY
                    else mt5.ORDER_TYPE_BUY,
            "position": position_id,
            "price": tick2.bid if pos.type == mt5.ORDER_TYPE_BUY else tick2.ask,
            "deviation": DEVIATION,
            "magic": MAGIC,
            "comment": TAG + " close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": fill,
        }
        report["close_request"] = dict(close_request)
        close_result = None
        for attempt in range(5):
            close_result = mt5.order_send(close_request)
            if close_result is None:
                print("   close attempt %d: None, last_error=%s"
                      % (attempt + 1, mt5.last_error()))
            else:
                print("   close attempt %d: retcode=%s" % (attempt + 1, close_result.retcode))
                if close_result.retcode == mt5.TRADE_RETCODE_DONE:
                    break
                if close_result.retcode in (mt5.TRADE_RETCODE_REQUOTE,
                                            mt5.TRADE_RETCODE_PRICE_OFF):
                    time.sleep(1)
                    t = mt5.symbol_info_tick(SYMBOL)
                    close_request["price"] = t.bid if pos.type == mt5.ORDER_TYPE_BUY else t.ask
                    continue
            time.sleep(1)
        dump("order_send (close) result", close_result)
        report["close_result"] = {k: str(v) for k, v in close_result._asdict().items()}

        if close_result.retcode != mt5.TRADE_RETCODE_DONE:
            print("CLOSE FAILED, retcode=%s" % close_result.retcode)
            return 1
        print("   CLOSED. order=%s deal=%s" % (close_result.order, close_result.deal))

        # ---- 5. confirm flat --------------------------------------------
        print("\n=== STEP 5: verify the account is flat again ===")
        time.sleep(2)
        left = mt5.positions_get(symbol=SYMBOL)
        print("positions_total() = %s" % mt5.positions_total())
        for p in (left or []):
            print("   STILL OPEN: ticket=%s type=%s volume=%s" % (p.ticket, p.type, p.volume))
        report["positions_after"] = len(left or [])

        # ---- 6. history -------------------------------------------------
        # NOTE: history_*_get needs BOTH date_from and date_to, and only as
        # positional arguments. A single date, or keyword arguments, are
        # rejected with (-2, 'Invalid arguments').
        print("\n=== STEP 6: read the history back ===")
        since = datetime.now() - timedelta(days=30)
        now = datetime.now()
        deals = mt5.history_deals_get(since, now)
        orders = mt5.history_orders_get(since, now)
        print("history_deals_get(from, to)  -> %s rows, err=%s"
              % (0 if deals is None else len(deals), mt5.last_error()))
        print("history_orders_get(from, to) -> %s rows, err=%s"
              % (0 if orders is None else len(orders), mt5.last_error()))
        print("history_deals_total(from, to)  -> %s" % mt5.history_deals_total(since, now))
        print("history_orders_total(from, to) -> %s" % mt5.history_orders_total(since, now))

        for label, ticket in (("open deal", result.deal),
                              ("close deal", close_result.deal)):
            got = mt5.history_deals_get(ticket=ticket)
            if got:
                dd = got[0]
                print("   %-10s ticket=%s type=%s entry=%s volume=%s price=%s "
                      "profit=%s comment=%r"
                      % (label, dd.ticket, dd.type, dd.entry, dd.volume, dd.price,
                         dd.profit, dd.comment))
                report.setdefault("deals_by_ticket", {})[label] = {
                    k: str(v) for k, v in dd._asdict().items()}
        for label, ticket in (("open order", position_id),
                              ("close order", close_result.order)):
            got = mt5.history_orders_get(ticket=ticket)
            if got:
                oo = got[0]
                print("   %-11s ticket=%s type=%s state=%s type_filling=%s "
                      "volume_initial=%s volume_current=%s"
                      % (label, oo.ticket, oo.type, oo.state, oo.type_filling,
                         oo.volume_initial, oo.volume_current))
                report.setdefault("orders_by_ticket", {})[label] = {
                    k: str(v) for k, v in oo._asdict().items()}

        print("\nfinal account: balance=%s equity=%s margin=%s"
              % (acct.balance, acct.equity, acct.margin))
        print("RESULT: round trip completed, %d position(s) left open"
              % len(left or []))
        return 0 if not left else 2
    finally:
        mt5.shutdown()
        print("shutdown ok")
        io.open("_cache/round_trip.json", "w", encoding="utf-8").write(
            json.dumps(report, indent=2, ensure_ascii=False, default=str))
        print("wrote _cache/round_trip.json")


if __name__ == "__main__":
    code = main()
    sys.exit(code)
