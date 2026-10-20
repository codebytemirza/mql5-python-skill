"""Check that this skill is installed correctly and the environment is ready.

    python scripts/verify_install.py

Exits 0 when the package imports and the docs are present, 1 otherwise.
It never places an order.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ok = True


def check(label, cond, extra=""):
    global ok
    print("%-46s %s %s" % (label, "OK" if cond else "FAIL", extra))
    if not cond:
        ok = False


def main():
    print("skill root:", ROOT)
    print()

    for rel in ["SKILL.md", "README.md", "skill.json", "data/api.json",
                "references/quickstart.md", "references/api.md",
                "references/cookbook.md", "references/trading.md",
                "references/constants.md", "references/troubleshooting.md",
                "references/live.md", "references/mirror/all_docs.md",
                "references/mirror/tree.md"]:
        check(rel, os.path.exists(os.path.join(ROOT, rel)))

    pages = os.path.join(ROOT, "references", "mirror", "pages")
    n = len([f for f in os.listdir(pages) if f.endswith(".md")]) if os.path.isdir(pages) else 0
    check("references/mirror/pages", n == 33, "%d pages" % n)

    print()
    try:
        import MetaTrader5 as mt5
        check("MetaTrader5 package importable", True, mt5.__version__)
        if mt5.initialize():
            check("terminal connection", True, "last_error=%s" % (mt5.last_error(),))
            check("symbols_total()", bool(mt5.symbols_total() > 0),
                  "%s symbols" % mt5.symbols_total())
            mt5.shutdown()
        else:
            print("%-46s %s" % ("terminal connection", "SKIP"))
            print("    last_error:", mt5.last_error())
            print("    the terminal is not running or not signed in -")
            print("    the docs are still usable, only the live calls are not.")
    except ImportError as e:
        check("MetaTrader5 package importable", False, str(e))
        print("    install it with:  python -m pip install MetaTrader5")

    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
