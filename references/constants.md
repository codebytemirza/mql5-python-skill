# Constants

All 223 constants exported by the installed `MetaTrader5` package
(version 5.0.6231). Values are the real values from the installed build.

Where the official documentation describes a constant, the description is
shown as well; otherwise only the value is listed.

## Discrepancies between the docs and the package

These were found by comparing the mirrored documentation tables with
the installed package. Trust **the package** for values.

| constant | as documented | finding |
| --- | --- | --- |
| `TIMEFRAME_M12` | 15 minutes | docs describe it as "15 minutes" but the package value is 12 |
| `ORDER_FILLING_BOC` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_CLIENT` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_EXPERT` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_MOBILE` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_SL` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_SO` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_TP` | - | exported by the package but **missing** from the docs |
| `ORDER_REASON_WEB` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_CANCELED` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_EXPIRED` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_FILLED` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_PARTIAL` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_PLACED` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_REJECTED` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_REQUEST_ADD` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_REQUEST_CANCEL` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_REQUEST_MODIFY` | - | exported by the package but **missing** from the docs |
| `ORDER_STATE_STARTED` | - | exported by the package but **missing** from the docs |
| `TIMEFRAME_M15` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_CANCEL` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_CLIENT_DISABLES_AT` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_CLOSE_ONLY` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_CLOSE_ORDER_EXIST` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_CONNECTION` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_DONE` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_DONE_PARTIAL` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_ERROR` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_FIFO_CLOSE` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_FROZEN` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_CLOSE_VOLUME` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_EXPIRATION` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_FILL` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_ORDER` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_PRICE` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_STOPS` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_INVALID_VOLUME` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_LIMIT_ORDERS` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_LIMIT_POSITIONS` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_LIMIT_VOLUME` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_LOCKED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_LONG_ONLY` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_MARKET_CLOSED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_NO_CHANGES` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_NO_MONEY` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_ONLY_REAL` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_ORDER_CHANGED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_PLACED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_POSITION_CLOSED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_PRICE_CHANGED` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_PRICE_OFF` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_REJECT` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_REJECT_CANCEL` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_REQUOTE` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_SERVER_DISABLES_AT` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_SHORT_ONLY` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_TIMEOUT` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_TOO_MANY_REQUESTS` | - | exported by the package but **missing** from the docs |
| `TRADE_RETCODE_TRADE_DISABLED` | - | exported by the package but **missing** from the docs |

The `TIMEFRAME` table on the MQL5 website lists `TIMEFRAME_M12` twice,
the second time as "15 minutes". That second row should be
`TIMEFRAME_M15`, which the package exports with the value 15.

| group | count |
| --- | --- |
| `ACCOUNT_*` | 8 |
| `BOOK_*` | 4 |
| `COPY_*` | 3 |
| `DAY_*` | 7 |
| `DEAL_*` | 32 |
| `ORDER_*` | 34 |
| `POSITION_*` | 6 |
| `RES_*` | 15 |
| `SYMBOL_*` | 41 |
| `TICK_*` | 6 |
| `TIMEFRAME_*` | 21 |
| `TRADE_*` | 46 |

## `ACCOUNT_*`

| constant | value | description |
| --- | --- | --- |
| `ACCOUNT_MARGIN_MODE_EXCHANGE` | 1 |  |
| `ACCOUNT_MARGIN_MODE_RETAIL_HEDGING` | 2 |  |
| `ACCOUNT_MARGIN_MODE_RETAIL_NETTING` | 0 |  |
| `ACCOUNT_STOPOUT_MODE_MONEY` | 1 |  |
| `ACCOUNT_STOPOUT_MODE_PERCENT` | 0 |  |
| `ACCOUNT_TRADE_MODE_CONTEST` | 1 |  |
| `ACCOUNT_TRADE_MODE_DEMO` | 0 |  |
| `ACCOUNT_TRADE_MODE_REAL` | 2 |  |

## `BOOK_*`

| constant | value | description |
| --- | --- | --- |
| `BOOK_TYPE_BUY` | 2 |  |
| `BOOK_TYPE_BUY_MARKET` | 4 |  |
| `BOOK_TYPE_SELL` | 1 |  |
| `BOOK_TYPE_SELL_MARKET` | 3 |  |

## `COPY_*`

| constant | value | description |
| --- | --- | --- |
| `COPY_TICKS_ALL` | -1 | all ticks |
| `COPY_TICKS_INFO` | 1 | ticks containing Bid and/or Ask price changes |
| `COPY_TICKS_TRADE` | 2 | ticks containing Last and/or Volume price changes |

## `DAY_*`

| constant | value | description |
| --- | --- | --- |
| `DAY_OF_WEEK_FRIDAY` | 5 |  |
| `DAY_OF_WEEK_MONDAY` | 1 |  |
| `DAY_OF_WEEK_SATURDAY` | 6 |  |
| `DAY_OF_WEEK_SUNDAY` | 0 |  |
| `DAY_OF_WEEK_THURSDAY` | 4 |  |
| `DAY_OF_WEEK_TUESDAY` | 2 |  |
| `DAY_OF_WEEK_WEDNESDAY` | 3 |  |

## `DEAL_*`

| constant | value | description |
| --- | --- | --- |
| `DEAL_DIVIDEND` | 15 |  |
| `DEAL_DIVIDEND_FRANKED` | 16 |  |
| `DEAL_ENTRY_IN` | 0 |  |
| `DEAL_ENTRY_INOUT` | 2 |  |
| `DEAL_ENTRY_OUT` | 1 |  |
| `DEAL_ENTRY_OUT_BY` | 3 |  |
| `DEAL_REASON_CLIENT` | 0 |  |
| `DEAL_REASON_EXPERT` | 3 |  |
| `DEAL_REASON_MOBILE` | 1 |  |
| `DEAL_REASON_ROLLOVER` | 7 |  |
| `DEAL_REASON_SL` | 4 |  |
| `DEAL_REASON_SO` | 6 |  |
| `DEAL_REASON_SPLIT` | 9 |  |
| `DEAL_REASON_TP` | 5 |  |
| `DEAL_REASON_VMARGIN` | 8 |  |
| `DEAL_REASON_WEB` | 2 |  |
| `DEAL_TAX` | 17 |  |
| `DEAL_TYPE_BALANCE` | 2 |  |
| `DEAL_TYPE_BONUS` | 6 |  |
| `DEAL_TYPE_BUY` | 0 |  |
| `DEAL_TYPE_BUY_CANCELED` | 13 |  |
| `DEAL_TYPE_CHARGE` | 4 |  |
| `DEAL_TYPE_COMMISSION` | 7 |  |
| `DEAL_TYPE_COMMISSION_AGENT_DAILY` | 10 |  |
| `DEAL_TYPE_COMMISSION_AGENT_MONTHLY` | 11 |  |
| `DEAL_TYPE_COMMISSION_DAILY` | 8 |  |
| `DEAL_TYPE_COMMISSION_MONTHLY` | 9 |  |
| `DEAL_TYPE_CORRECTION` | 5 |  |
| `DEAL_TYPE_CREDIT` | 3 |  |
| `DEAL_TYPE_INTEREST` | 12 |  |
| `DEAL_TYPE_SELL` | 1 |  |
| `DEAL_TYPE_SELL_CANCELED` | 14 |  |

## `ORDER_*`

| constant | value | description |
| --- | --- | --- |
| `ORDER_FILLING_BOC` | 3 |  |
| `ORDER_FILLING_FOK` | 0 | This execution policy means that an order can be executed only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The desired volume can be made up of several available offers. |
| `ORDER_FILLING_IOC` | 1 | An agreement to execute a deal at the maximum volume available in the market within the volume specified in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled. |
| `ORDER_FILLING_RETURN` | 2 | This policy is used only for market (ORDER_TYPE_BUY and ORDER_TYPE_SELL), limit and stop limit orders (ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT, ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT) and only for the symbols with Market or Exchange execution [modes](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution). If filled partially, a market or limit order with the remaining volume is not canceled, and is processed further.
During activation of the ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT orders, an appropriate limit order ORDER_TYPE_BUY_LIMIT/ORDER_TYPE_SELL_LIMIT with the ORDER_FILLING_RETURN type is created. |
| `ORDER_REASON_CLIENT` | 0 |  |
| `ORDER_REASON_EXPERT` | 3 |  |
| `ORDER_REASON_MOBILE` | 1 |  |
| `ORDER_REASON_SL` | 4 |  |
| `ORDER_REASON_SO` | 6 |  |
| `ORDER_REASON_TP` | 5 |  |
| `ORDER_REASON_WEB` | 2 |  |
| `ORDER_STATE_CANCELED` | 2 |  |
| `ORDER_STATE_EXPIRED` | 6 |  |
| `ORDER_STATE_FILLED` | 4 |  |
| `ORDER_STATE_PARTIAL` | 3 |  |
| `ORDER_STATE_PLACED` | 1 |  |
| `ORDER_STATE_REJECTED` | 5 |  |
| `ORDER_STATE_REQUEST_ADD` | 7 |  |
| `ORDER_STATE_REQUEST_CANCEL` | 9 |  |
| `ORDER_STATE_REQUEST_MODIFY` | 8 |  |
| `ORDER_STATE_STARTED` | 0 |  |
| `ORDER_TIME_DAY` | 1 | The order is active only during the current trading day |
| `ORDER_TIME_GTC` | 0 | The order stays in the queue until it is manually canceled |
| `ORDER_TIME_SPECIFIED` | 2 | The order is active until the specified date |
| `ORDER_TIME_SPECIFIED_DAY` | 3 | The order is active until 23:59:59 of the specified day. If this time appears to be out of a trading session, the expiration is processed at the nearest trading time. |
| `ORDER_TYPE_BUY` | 0 | Market buy order |
| `ORDER_TYPE_BUY_LIMIT` | 2 | Buy Limit pending order |
| `ORDER_TYPE_BUY_STOP` | 4 | Buy Stop pending order |
| `ORDER_TYPE_BUY_STOP_LIMIT` | 6 | Upon reaching the order price, Buy Limit pending order is placed at StopLimit price |
| `ORDER_TYPE_CLOSE_BY` | 8 | Order for closing a position by an opposite one |
| `ORDER_TYPE_SELL` | 1 | Market sell order |
| `ORDER_TYPE_SELL_LIMIT` | 3 | Sell Limit pending order |
| `ORDER_TYPE_SELL_STOP` | 5 | Sell Stop pending order |
| `ORDER_TYPE_SELL_STOP_LIMIT` | 7 | Upon reaching the order price, Sell Limit pending order is placed at StopLimit price |

## `POSITION_*`

| constant | value | description |
| --- | --- | --- |
| `POSITION_REASON_CLIENT` | 0 |  |
| `POSITION_REASON_EXPERT` | 3 |  |
| `POSITION_REASON_MOBILE` | 1 |  |
| `POSITION_REASON_WEB` | 2 |  |
| `POSITION_TYPE_BUY` | 0 |  |
| `POSITION_TYPE_SELL` | 1 |  |

## `RES_*`

| constant | value | description |
| --- | --- | --- |
| `RES_E_AUTH_FAILED` | -6 | authorization failed |
| `RES_E_AUTO_TRADING_DISABLED` | -8 | auto-trading disabled |
| `RES_E_FAIL` | -1 | generic fail |
| `RES_E_INTERNAL_FAIL` | -10000 | internal IPC general error |
| `RES_E_INTERNAL_FAIL_CONNECT` | -10004 | internal IPC no ipc |
| `RES_E_INTERNAL_FAIL_INIT` | -10003 | internal IPC initialization fail |
| `RES_E_INTERNAL_FAIL_RECEIVE` | -10002 | internal IPC recv failed |
| `RES_E_INTERNAL_FAIL_SEND` | -10001 | internal IPC send failed |
| `RES_E_INTERNAL_FAIL_TIMEOUT` | -10005 | internal timeout |
| `RES_E_INVALID_PARAMS` | -2 | invalid arguments/parameters |
| `RES_E_INVALID_VERSION` | -5 | invalid version |
| `RES_E_NOT_FOUND` | -4 | no history |
| `RES_E_NO_MEMORY` | -3 | no memory condition |
| `RES_E_UNSUPPORTED` | -7 | unsupported method |
| `RES_S_OK` | 1 | generic success |

## `SYMBOL_*`

| constant | value | description |
| --- | --- | --- |
| `SYMBOL_CALC_MODE_CFD` | 2 |  |
| `SYMBOL_CALC_MODE_CFDINDEX` | 3 |  |
| `SYMBOL_CALC_MODE_CFDLEVERAGE` | 4 |  |
| `SYMBOL_CALC_MODE_EXCH_BONDS` | 37 |  |
| `SYMBOL_CALC_MODE_EXCH_BONDS_MOEX` | 39 |  |
| `SYMBOL_CALC_MODE_EXCH_FUTURES` | 33 |  |
| `SYMBOL_CALC_MODE_EXCH_OPTIONS` | 34 |  |
| `SYMBOL_CALC_MODE_EXCH_OPTIONS_MARGIN` | 36 |  |
| `SYMBOL_CALC_MODE_EXCH_STOCKS` | 32 |  |
| `SYMBOL_CALC_MODE_EXCH_STOCKS_MOEX` | 38 |  |
| `SYMBOL_CALC_MODE_FOREX` | 0 |  |
| `SYMBOL_CALC_MODE_FOREX_NO_LEVERAGE` | 5 |  |
| `SYMBOL_CALC_MODE_FUTURES` | 1 |  |
| `SYMBOL_CALC_MODE_SERV_COLLATERAL` | 64 |  |
| `SYMBOL_CHART_MODE_BID` | 0 |  |
| `SYMBOL_CHART_MODE_LAST` | 1 |  |
| `SYMBOL_OPTION_MODE_AMERICAN` | 1 |  |
| `SYMBOL_OPTION_MODE_EUROPEAN` | 0 |  |
| `SYMBOL_OPTION_RIGHT_CALL` | 0 |  |
| `SYMBOL_OPTION_RIGHT_PUT` | 1 |  |
| `SYMBOL_ORDERS_DAILY` | 1 |  |
| `SYMBOL_ORDERS_DAILY_NO_STOPS` | 2 |  |
| `SYMBOL_ORDERS_GTC` | 0 |  |
| `SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT` | 4 |  |
| `SYMBOL_SWAP_MODE_CURRENCY_MARGIN` | 3 |  |
| `SYMBOL_SWAP_MODE_CURRENCY_SYMBOL` | 2 |  |
| `SYMBOL_SWAP_MODE_DISABLED` | 0 |  |
| `SYMBOL_SWAP_MODE_INTEREST_CURRENT` | 5 |  |
| `SYMBOL_SWAP_MODE_INTEREST_OPEN` | 6 |  |
| `SYMBOL_SWAP_MODE_POINTS` | 1 |  |
| `SYMBOL_SWAP_MODE_REOPEN_BID` | 8 |  |
| `SYMBOL_SWAP_MODE_REOPEN_CURRENT` | 7 |  |
| `SYMBOL_TRADE_EXECUTION_EXCHANGE` | 3 |  |
| `SYMBOL_TRADE_EXECUTION_INSTANT` | 1 |  |
| `SYMBOL_TRADE_EXECUTION_MARKET` | 2 |  |
| `SYMBOL_TRADE_EXECUTION_REQUEST` | 0 |  |
| `SYMBOL_TRADE_MODE_CLOSEONLY` | 3 |  |
| `SYMBOL_TRADE_MODE_DISABLED` | 0 |  |
| `SYMBOL_TRADE_MODE_FULL` | 4 |  |
| `SYMBOL_TRADE_MODE_LONGONLY` | 1 |  |
| `SYMBOL_TRADE_MODE_SHORTONLY` | 2 |  |

## `TICK_*`

| constant | value | description |
| --- | --- | --- |
| `TICK_FLAG_ASK` | 4 | Ask price changed |
| `TICK_FLAG_BID` | 2 | Bid price changed |
| `TICK_FLAG_BUY` | 32 | last Buy price changed |
| `TICK_FLAG_LAST` | 8 | Last price changed |
| `TICK_FLAG_SELL` | 64 | last Sell price changed |
| `TICK_FLAG_VOLUME` | 16 | Volume changed |

## `TIMEFRAME_*`

| constant | value | description |
| --- | --- | --- |
| `TIMEFRAME_D1` | 16408 | 1 day |
| `TIMEFRAME_H1` | 16385 | 1 hour |
| `TIMEFRAME_H12` | 16396 | 12 hours |
| `TIMEFRAME_H2` | 16386 | 2 hours |
| `TIMEFRAME_H3` | 16387 | 3 hours |
| `TIMEFRAME_H4` | 16388 | 4 hours |
| `TIMEFRAME_H6` | 16390 | 6 hours |
| `TIMEFRAME_H8` | 16392 | 8 hours |
| `TIMEFRAME_M1` | 1 | 1 minute |
| `TIMEFRAME_M10` | 10 | 10 minutes |
| `TIMEFRAME_M12` | 12 | 15 minutes |
| `TIMEFRAME_M15` | 15 |  |
| `TIMEFRAME_M2` | 2 | 2 minutes |
| `TIMEFRAME_M20` | 20 | 20 minutes |
| `TIMEFRAME_M3` | 3 | 3 minutes |
| `TIMEFRAME_M30` | 30 | 30 minutes |
| `TIMEFRAME_M4` | 4 | 4 minutes |
| `TIMEFRAME_M5` | 5 | 5 minutes |
| `TIMEFRAME_M6` | 6 | 6 minutes |
| `TIMEFRAME_MN1` | 49153 | 1 month |
| `TIMEFRAME_W1` | 32769 | 1 week |

## `TRADE_*`

| constant | value | description |
| --- | --- | --- |
| `TRADE_ACTION_CLOSE_BY` | 10 | Close a position by an opposite one |
| `TRADE_ACTION_DEAL` | 1 | Place an order for an instant deal with the specified parameters (set a market order) |
| `TRADE_ACTION_MODIFY` | 7 | Change parameters of the previously placed trading order |
| `TRADE_ACTION_PENDING` | 5 | Place an order for performing a deal at specified conditions (pending order) |
| `TRADE_ACTION_REMOVE` | 8 | Remove previously placed pending order |
| `TRADE_ACTION_SLTP` | 6 | Change open position Stop Loss and Take Profit |
| `TRADE_RETCODE_CANCEL` | 10007 |  |
| `TRADE_RETCODE_CLIENT_DISABLES_AT` | 10027 |  |
| `TRADE_RETCODE_CLOSE_ONLY` | 10044 |  |
| `TRADE_RETCODE_CLOSE_ORDER_EXIST` | 10039 |  |
| `TRADE_RETCODE_CONNECTION` | 10031 |  |
| `TRADE_RETCODE_DONE` | 10009 |  |
| `TRADE_RETCODE_DONE_PARTIAL` | 10010 |  |
| `TRADE_RETCODE_ERROR` | 10011 |  |
| `TRADE_RETCODE_FIFO_CLOSE` | 10045 |  |
| `TRADE_RETCODE_FROZEN` | 10029 |  |
| `TRADE_RETCODE_INVALID` | 10013 |  |
| `TRADE_RETCODE_INVALID_CLOSE_VOLUME` | 10038 |  |
| `TRADE_RETCODE_INVALID_EXPIRATION` | 10022 |  |
| `TRADE_RETCODE_INVALID_FILL` | 10030 |  |
| `TRADE_RETCODE_INVALID_ORDER` | 10035 |  |
| `TRADE_RETCODE_INVALID_PRICE` | 10015 |  |
| `TRADE_RETCODE_INVALID_STOPS` | 10016 |  |
| `TRADE_RETCODE_INVALID_VOLUME` | 10014 |  |
| `TRADE_RETCODE_LIMIT_ORDERS` | 10033 |  |
| `TRADE_RETCODE_LIMIT_POSITIONS` | 10040 |  |
| `TRADE_RETCODE_LIMIT_VOLUME` | 10034 |  |
| `TRADE_RETCODE_LOCKED` | 10028 |  |
| `TRADE_RETCODE_LONG_ONLY` | 10042 |  |
| `TRADE_RETCODE_MARKET_CLOSED` | 10018 |  |
| `TRADE_RETCODE_NO_CHANGES` | 10025 |  |
| `TRADE_RETCODE_NO_MONEY` | 10019 |  |
| `TRADE_RETCODE_ONLY_REAL` | 10032 |  |
| `TRADE_RETCODE_ORDER_CHANGED` | 10023 |  |
| `TRADE_RETCODE_PLACED` | 10008 |  |
| `TRADE_RETCODE_POSITION_CLOSED` | 10036 |  |
| `TRADE_RETCODE_PRICE_CHANGED` | 10020 |  |
| `TRADE_RETCODE_PRICE_OFF` | 10021 |  |
| `TRADE_RETCODE_REJECT` | 10006 |  |
| `TRADE_RETCODE_REJECT_CANCEL` | 10041 |  |
| `TRADE_RETCODE_REQUOTE` | 10004 |  |
| `TRADE_RETCODE_SERVER_DISABLES_AT` | 10026 |  |
| `TRADE_RETCODE_SHORT_ONLY` | 10043 |  |
| `TRADE_RETCODE_TIMEOUT` | 10012 |  |
| `TRADE_RETCODE_TOO_MANY_REQUESTS` | 10024 |  |
| `TRADE_RETCODE_TRADE_DISABLED` | 10017 |  |

