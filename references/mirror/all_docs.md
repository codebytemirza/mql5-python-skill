# MQL5 - Python Integration for MetaTrader 5

Complete mirror of <https://www.mql5.com/en/docs/python_metatrader5> (33 pages).

## Table of contents

- [MetaTrader module for integration with Python](https://www.mql5.com/en/docs/python_metatrader5)
  - [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
  - [login](https://www.mql5.com/en/docs/python_metatrader5/mt5login_py)
  - [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)
  - [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)
  - [last_error](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py)
  - [account_info](https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py)
  - [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)
  - [symbols_total](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py)
  - [symbols_get](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py)
  - [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)
  - [symbol_info_tick](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py)
  - [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py)
  - [market_book_add](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py)
  - [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py)
  - [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py)
  - [copy_rates_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py)
  - [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py)
  - [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
  - [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
  - [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)
  - [orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py)
  - [orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py)
  - [order_calc_margin](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py)
  - [order_calc_profit](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py)
  - [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py)
  - [order_send](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py)
  - [positions_total](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py)
  - [positions_get](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py)
  - [history_orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py)
  - [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py)
  - [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)
  - [history_deals_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py)

---


# MetaTrader module for integration with Python

**Source:** MQL5 Reference  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5>

## Description

MQL5 is designed for the development of high-performance trading applications in the financial markets and is unparalleled among other specialized languages used in the algorithmic trading. The syntax and speed of MQL5 programs are very close to C++, there is support for [OpenCL](https://www.mql5.com/en/docs/opencl) and [integration with MS Visual Studio](https://www.metatrader5.com/en/metaeditor/help/development/c_dll). [Statistics](https://www.mql5.com/en/docs/standardlibrary/mathematics/stat), [fuzzy logic](https://www.mql5.com/en/docs/standardlibrary/mathematics/fuzzy_logic) and [ALGLIB](https://www.mql5.com/en/code/1146) libraries are available as well. MetaEditor development environment features native [support for .NET libraries](https://www.metatrader5.com/en/releasenotes/terminal/1898) with "smart" functions import eliminating the need to develop special wrappers. Third-party C++ DLLs can also be used. C++ source code files (CPP and H) can be edited and compiled into DLL directly from the editor. Microsoft Visual Studio installed on user's PC can be used for that.

Python is a modern high-level programming language for developing scripts and applications. It contains multiple libraries for machine learning, process automation, as well as data analysis and visualization.

MetaTrader package for Python is designed for convenient and fast obtaining of exchange data via interprocessor communication directly from the MetaTrader 5 terminal. The data received this way can be further used for statistical calculations and machine learning.

Installing the package from the command line:

```bash
  pip install MetaTrader5
```

Updating the package from the command line:

```bash
  pip install --upgrade MetaTrader5
```

Functions for integrating MetaTrader 5 and Python

| Function | Action |
| --- | --- |
| [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py) | Establish a connection with the MetaTrader 5 terminal |
| [login](https://www.mql5.com/en/docs/python_metatrader5/mt5login_py) | Connect to a trading account using specified parameters |
| [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py) | Close the previously established connection to the MetaTrader 5 terminal |
| [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py) | Return the MetaTrader 5 terminal version |
| [last_error](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py) | Return data on the last error |
| [account_info](https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py) | Get info on the current trading account |
| [terminal_Info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py) | Get status and parameters of the connected MetaTrader 5 terminal |
| [symbols_total](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py) | Get the number of all financial instruments in the MetaTrader 5 terminal |
| [symbols_get](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py) | Get all financial instruments from the MetaTrader 5 terminal |
| [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py) | Get data on the specified financial instrument |
| [symbol_info_tick](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py) | Get the last tick for the specified financial instrument |
| [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py) | Select a symbol in the [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch) window or remove a symbol from the window |
| [market_book_add](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py) | Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol |
| [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py) | Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol |
| [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py) | Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol |
| [copy_rates_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py) | Get bars from the MetaTrader 5 terminal starting from the specified date |
| [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py) | Get bars from the MetaTrader 5 terminal starting from the specified index |
| [copyrates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py) | Get bars in the specified date range from the MetaTrader 5 terminal |
| [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py) | Get ticks from the MetaTrader 5 terminal starting from the specified date |
| [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py) | Get ticks for the specified date range from the MetaTrader 5 terminal |
| [orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py) | Get the number of active orders. |
| [orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py) | Get active orders with the ability to filter by symbol or ticket |
| [order_calc_margin](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py) | Return margin in the account currency to perform a specified trading operation |
| [order_calc_profit](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py) | Return profit in the account currency for a specified trading operation |
| [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py) | Check funds sufficiency for performing a required [trading operation](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions) |
| [order_send](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py) | Send a [request](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) to perform a trading operation. |
| [positions_total](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py) | Get the number of open positions |
| [positions_get](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py) | Get open positions with the ability to filter by symbol or ticket |
| [history_orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py) | Get the number of orders in trading history within the specified interval |
| [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py) | Get orders from trading history with the ability to filter by ticket or position |
| [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py) | Get the number of deals in trading history within the specified interval |
| [history_deals_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py) | Get deals from trading history with the ability to filter by ticket or position |

## Example of connecting Python to MetaTrader 5

1. Download the latest version of Python 3.8 from [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)
2. When installing Python, check "Add Python 3.8 to PATH%" to be able to run Python scripts from the command line.
3. Install the MetaTrader 5 module from the command line

```bash
  pip install MetaTrader5
```

1. Add matplotlib and pandas packages

```bash
  pip install matplotlib
  pip install pandas
```

1. Launch the test script

```python
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

# request 1000 ticks from EURAUD
euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime(2020,1,28,13), 1000, mt5.COPY_TICKS_ALL)
# request ticks from AUDUSD within 2019.04.01 13:00 - 2019.04.02 13:00
audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2020,1,27,13), datetime(2020,1,28,13), mt5.COPY_TICKS_ALL)

# get bars from different symbols in a number of ways
eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2020,1,28,13), 1000)
eurgbp_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
eurcad_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M1, datetime(2020,1,27,13), datetime(2020,1,28,13))

# shut down connection to MetaTrader 5
mt5.shutdown()

#DATA
print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)

print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)

print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)

print('eurgbp_rates(', len(eurgbp_rates), ')')
for val in eurgbp_rates[:10]: print(val)

print('eurcad_rates(', len(eurcad_rates), ')')
for val in eurcad_rates[:10]: print(val)

#PLOT
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(euraud_ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
# display ticks on the chart
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')

# display the legends
plt.legend(loc='upper left')

# add the header
plt.title('EURAUD ticks')

# display the chart
plt.show()
```

1. Get data and chart

```python
[2, 'MetaQuotes-Demo', '16167573']
[500, 2325, '19 Feb 2020']

euraud_ticks( 1000 )
(1580209200, 1.63412, 1.63437, 0., 0, 1580209200067, 130, 0.)
(1580209200, 1.63416, 1.63437, 0., 0, 1580209200785, 130, 0.)
(1580209201, 1.63415, 1.63437, 0., 0, 1580209201980, 130, 0.)
(1580209202, 1.63419, 1.63445, 0., 0, 1580209202192, 134, 0.)
(1580209203, 1.6342, 1.63445, 0., 0, 1580209203004, 130, 0.)
(1580209203, 1.63419, 1.63445, 0., 0, 1580209203487, 130, 0.)
(1580209203, 1.6342, 1.63445, 0., 0, 1580209203694, 130, 0.)
(1580209203, 1.63419, 1.63445, 0., 0, 1580209203990, 130, 0.)
(1580209204, 1.63421, 1.63445, 0., 0, 1580209204194, 130, 0.)
(1580209204, 1.63425, 1.63445, 0., 0, 1580209204392, 130, 0.)
audusd_ticks( 40449 )
(1580122800, 0.67858, 0.67868, 0., 0, 1580122800244, 130, 0.)
(1580122800, 0.67858, 0.67867, 0., 0, 1580122800429, 4, 0.)
(1580122800, 0.67858, 0.67865, 0., 0, 1580122800817, 4, 0.)
(1580122801, 0.67858, 0.67866, 0., 0, 1580122801618, 4, 0.)
(1580122802, 0.67858, 0.67865, 0., 0, 1580122802928, 4, 0.)
(1580122809, 0.67855, 0.67865, 0., 0, 1580122809526, 130, 0.)
(1580122809, 0.67855, 0.67864, 0., 0, 1580122809699, 4, 0.)
(1580122813, 0.67855, 0.67863, 0., 0, 1580122813576, 4, 0.)
(1580122815, 0.67856, 0.67863, 0., 0, 1580122815190, 130, 0.)
(1580122815, 0.67855, 0.67863, 0., 0, 1580122815479, 130, 0.)
eurusd_rates( 1000 )
(1580149260, 1.10132, 1.10151, 1.10131, 1.10149, 44, 1, 0)
(1580149320, 1.10149, 1.10161, 1.10143, 1.10154, 42, 1, 0)
(1580149380, 1.10154, 1.10176, 1.10154, 1.10174, 40, 2, 0)
(1580149440, 1.10174, 1.10189, 1.10168, 1.10187, 47, 1, 0)
(1580149500, 1.10185, 1.10191, 1.1018, 1.10182, 53, 1, 0)
(1580149560, 1.10182, 1.10184, 1.10176, 1.10183, 25, 3, 0)
(1580149620, 1.10183, 1.10187, 1.10177, 1.10187, 49, 2, 0)
(1580149680, 1.10187, 1.1019, 1.1018, 1.10187, 53, 1, 0)
(1580149740, 1.10187, 1.10202, 1.10187, 1.10198, 28, 2, 0)
(1580149800, 1.10198, 1.10198, 1.10183, 1.10188, 39, 2, 0)
eurgbp_rates( 1000 )
(1582236360, 0.83767, 0.83767, 0.83764, 0.83765, 23, 9, 0)
(1582236420, 0.83765, 0.83765, 0.83764, 0.83765, 15, 8, 0)
(1582236480, 0.83765, 0.83766, 0.83762, 0.83765, 19, 7, 0)
(1582236540, 0.83765, 0.83768, 0.83758, 0.83763, 39, 6, 0)
(1582236600, 0.83763, 0.83768, 0.83763, 0.83767, 21, 6, 0)
(1582236660, 0.83767, 0.83775, 0.83765, 0.83769, 63, 5, 0)
(1582236720, 0.83769, 0.8377, 0.83758, 0.83764, 40, 7, 0)
(1582236780, 0.83766, 0.83769, 0.8376, 0.83766, 37, 6, 0)
(1582236840, 0.83766, 0.83772, 0.83763, 0.83772, 22, 6, 0)
(1582236900, 0.83772, 0.83773, 0.83768, 0.8377, 36, 5, 0)
eurcad_rates( 1441 )
(1580122800, 1.45321, 1.45329, 1.4526, 1.4528, 146, 15, 0)
(1580122860, 1.4528, 1.45315, 1.45274, 1.45301, 93, 15, 0)
(1580122920, 1.453, 1.45304, 1.45264, 1.45264, 82, 15, 0)
(1580122980, 1.45263, 1.45279, 1.45231, 1.45277, 109, 15, 0)
(1580123040, 1.45275, 1.4528, 1.45259, 1.45271, 53, 14, 0)
(1580123100, 1.45273, 1.45285, 1.45269, 1.4528, 62, 16, 0)
(1580123160, 1.4528, 1.45284, 1.45267, 1.45282, 64, 14, 0)
(1580123220, 1.45282, 1.45299, 1.45261, 1.45272, 48, 14, 0)
(1580123280, 1.45272, 1.45275, 1.45255, 1.45275, 74, 14, 0)
(1580123340, 1.45275, 1.4528, 1.4526, 1.4528, 94, 13, 0)
```

---


# initialize

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py>

## Description

Establish a connection with the MetaTrader 5 terminal. There are three call options.

Call without parameters. The terminal for connection is found automatically.

Call specifying the path to the MetaTrader 5 terminal we want to connect to.

Call specifying the trading account path and parameters.

## Signatures

```python
initialize()
```

```python
initialize(
   path                      // path to the MetaTrader 5 terminal EXE file
   )
```

```python
initialize(
   path,                     // path to the MetaTrader 5 terminal EXE file
   login=LOGIN,              // account number
   password="PASSWORD",      // password
   server="SERVER",          // server name as it is specified in the terminal
   timeout=TIMEOUT,          // timeout
   portable=False            // portable mode
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | — | [in] Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. It is indicated first without a parameter name. If the path is not specified, the module attempts to find the executable file on its own. |
| `login=LOGIN` | `LOGIN` | [in] Trading account number. Optional named parameter. If not specified, the last trading account is used. |
| `password="PASSWORD"` | `"PASSWORD"` | [in] Trading account password. Optional named parameter. If the password is not set, the password for a specified trading account saved in the terminal database is applied automatically. |
| `server="SERVER"` | `"SERVER"` | [in] Trade server name. Optional named parameter. If the server is not set, the server for a specified trading account saved in the terminal database is applied automatically. |
| `timeout=TIMEOUT` | `TIMEOUT` | [in] Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied. |
| `portable=False` | `False` | [in] Flag of the terminal launch in [portable](https://www.metatrader5.com/en/terminal/help/start_advanced/start#portable) mode. Optional named parameter. If not specified, the value of False is used. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns True in case of successful connection to the MetaTrader 5 terminal, otherwise - False.

## Note

If required, the MetaTrader 5 terminal is launched to establish connection when executing the initialize() call.

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# display data on connection status, server name and trading account
print(mt5.terminal_info())
# display data on MetaTrader 5 version
print(mt5.version())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)
- [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)
- [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)

---


# login

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5login_py>

## Description

Connect to a trading account using specified parameters.

## Signatures

```python
login(
   login,                    // account number
   password="PASSWORD",      // password
   server="SERVER",          // server name as it is specified in the terminal
   timeout=TIMEOUT           // timeout
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `login` | — | [in] Trading account number. Required unnamed parameter. |
| `password` | — | [in] Trading account password. Optional named parameter. If the password is not set, the password saved in the terminal database is applied automatically. |
| `server` | — | [in] Trade server name. Optional named parameter. If no server is set, the last used server is applied automatically. |
| `timeout=TIMEOUT` | `TIMEOUT` | [in] Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied. If the connection is not established within the specified time, the call is forcibly terminated and the exception is generated. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

True in case of a successful connection to the trade account, otherwise – False.

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# display data on MetaTrader 5 version
print(mt5.version())
# connect to the trade account without specifying a password and a server
account=17221085
authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account #{}".format(account))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# now connect to another trading account specifying the password
account=25115284
authorized=mt5.login(account, password="gqrtz0lbdm")
if authorized:
    # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
[500, 2367, '23 Mar 2020']

connected to account #17221085

connected to account #25115284
AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ...
account properties:
   login=25115284
   trade_mode=0
   leverage=100
   limit_orders=200
   margin_so_mode=0
   trade_allowed=True
   trade_expert=True
   margin_mode=2
   currency_digits=2
   fifo_close=False
   balance=99588.33
   credit=0.0
   profit=-45.23
   equity=99543.1
   margin=54.37
   margin_free=99488.73
   margin_level=183084.6054809638
   margin_so_call=50.0
   margin_so_so=30.0
   margin_initial=0.0
   margin_maintenance=0.0
   assets=0.0
   liabilities=0.0
   commission_blocked=0.0
   name=James Smith
   server=MetaQuotes-Demo
   currency=USD
   company=MetaQuotes Software Corp.
```

## See also

- [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
- [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)

---


# shutdown

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py>

## Description

Close the previously established connection to the MetaTrader 5 terminal.

## Signatures

```python
shutdown()
```

## Return Value

None.

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed")
    quit()

# display data on connection status, server name and trading account
print(mt5.terminal_info())
# display data on MetaTrader 5 version
print(mt5.version())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
- [login_py](https://www.mql5.com/en/docs/python_metatrader5/mt5login_py)
- [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)
- [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)

---


# version

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5version_py>

## Description

Return the MetaTrader 5 terminal version.

## Signatures

```python
version()
```

## Return Value

Return the MetaTrader 5 terminal version, build and release date. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The version() function returns the terminal version, build and release date as a tuple of three values:

| Type | Description | Sample value |
| --- | --- | --- |
| integer | MetaTrader 5 terminal version | 500 |
| integer | Build | 2007 |
| string | Build release date | '25 Feb 2019' |

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# display data on MetaTrader 5 version
print(mt5.version())

# display data on connection status, server name and trading account 'as is'
print(mt5.terminal_info())
print()

# get properties in the form of a dictionary
terminal_info_dict=mt5.terminal_info()._asdict()
# convert the dictionary into DataFrame and print
df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
print("terminal_info() as dataframe:")
print(df[:-1])

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
[500, 2367, '23 Mar 2020']
TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...

terminal_info() as dataframe:
                 property                         value
0       community_account                          True
1    community_connection                          True
2               connected                          True
3            dlls_allowed                         False
4           trade_allowed                         False
5       tradeapi_disabled                         False
6           email_enabled                         False
7             ftp_enabled                         False
8   notifications_enabled                         False
9                    mqid                         False
10                  build                          2367
11                maxbars                          5000
12               codepage                          1251
13              ping_last                         77881
14      community_balance                       707.107
15         retransmission                             0
16                company     MetaQuotes Software Corp.
17                   name                  MetaTrader 5
18               language                       Russian
19                   path  E:\ProgramFiles\MetaTrader 5
20              data_path  E:\ProgramFiles\MetaTrader 5
```

## See also

- [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
- [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)
- [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)

---


# last_error

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py>

## Description

Return data on the last error.

## Signatures

```python
last_error()
```

## Return Value

Return the last error code and description as a tuple.

## Note

last_error() allows obtaining an error code in case of a failed execution of a MetaTrader 5 library function. It is similar to [GetLastError()](https://www.mql5.com/en/docs/check/getlasterror). However, it applies its own error codes. Possible values:

| Constant | Value | Description |
| --- | --- | --- |
| RES_S_OK | 1 | generic success |
| RES_E_FAIL | -1 | generic fail |
| RES_E_INVALID_PARAMS | -2 | invalid arguments/parameters |
| RES_E_NO_MEMORY | -3 | no memory condition |
| RES_E_NOT_FOUND | -4 | no history |
| RES_E_INVALID_VERSION | -5 | invalid version |
| RES_E_AUTH_FAILED | -6 | authorization failed |
| RES_E_UNSUPPORTED | -7 | unsupported method |
| RES_E_AUTO_TRADING_DISABLED | -8 | auto-trading disabled |
| RES_E_INTERNAL_FAIL | -10000 | internal IPC general error |
| RES_E_INTERNAL_FAIL_SEND | -10001 | internal IPC send failed |
| RES_E_INTERNAL_FAIL_RECEIVE | -10002 | internal IPC recv failed |
| RES_E_INTERNAL_FAIL_INIT | -10003 | internal IPC initialization fail |
| RES_E_INTERNAL_FAIL_CONNECT | -10003 | internal IPC no ipc |
| RES_E_INTERNAL_FAIL_TIMEOUT | -10005 | internal timeout |

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)
- [GetLastError](https://www.mql5.com/en/docs/check/getlasterror)

---


# account_info

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py>

## Description

Get info on the current trading account.

## Signatures

```python
account_info()
```

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function returns all data that can be obtained using [AccountInfoInteger](https://www.mql5.com/en/docs/account/accountinfointeger), [AccountInfoDouble](https://www.mql5.com/en/docs/account/accountinfodouble) and [AccountInfoString](https://www.mql5.com/en/docs/account/accountinfostring) in one call.

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# connect to the trade account specifying a password and a server
authorized=mt5.login(25115284, password="gqz0343lbdm")
if authorized:
    account_info=mt5.account_info()
    if account_info!=None:
        # display trading account data 'as is'
        print(account_info)
        # display trading account data in the form of a dictionary
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        print()

        # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
        print("account_info() as dataframe:")
        print(df)
else:
    print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....
Show account_info()._asdict():
  login=25115284
  trade_mode=0
  leverage=100
  limit_orders=200
  margin_so_mode=0
  trade_allowed=True
  trade_expert=True
  margin_mode=2
  currency_digits=2
  fifo_close=False
  balance=99511.4
  credit=0.0
  profit=41.82
  equity=99553.22
  margin=98.18
  margin_free=99455.04
  margin_level=101398.67590140559
  margin_so_call=50.0
  margin_so_so=30.0
  margin_initial=0.0
  margin_maintenance=0.0
  assets=0.0
  liabilities=0.0
  commission_blocked=0.0
  server=MetaQuotes-Demo
  currency=USD
  company=MetaQuotes Software Corp.

account_info() as dataframe
              property                      value
0                login                   25115284
1           trade_mode                          0
2             leverage                        100
3         limit_orders                        200
4       margin_so_mode                          0
5        trade_allowed                       True
6         trade_expert                       True
7          margin_mode                          2
8      currency_digits                          2
9           fifo_close                      False
10             balance                    99588.3
11              credit                          0
12              profit                     -45.13
13              equity                    99543.2
14              margin                      54.37
15         margin_free                    99488.8
16        margin_level                     183085
17      margin_so_call                         50
18        margin_so_so                         30
19      margin_initial                          0
20  margin_maintenance                          0
21              assets                          0
22         liabilities                          0
23  commission_blocked                          0
24                name                James Smith
25              server            MetaQuotes-Demo
26            currency                        USD
27             company  MetaQuotes Software Corp.
```

## See also

- [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
- [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)
- [login](https://www.mql5.com/en/docs/python_metatrader5/mt5login_py)

---


# terminal_info

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py>

## Description

Get the connected MetaTrader 5 client terminal status and settings.

## Signatures

```python
terminal_info()
```

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function returns all data that can be obtained using [TerminalInfoInteger](https://www.mql5.com/en/docs/check/terminalinfointeger), [TerminalInfoDouble](https://www.mql5.com/en/docs/check/terminalinfodouble) and [TerminalInfoDouble](https://www.mql5.com/en/docs/check/terminalinfodouble) in one call.

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# display data on MetaTrader 5 version
print(mt5.version())
# display info on the terminal settings and status
terminal_info=mt5.terminal_info()
if terminal_info!=None:
    # display the terminal data 'as is'
    print(terminal_info)
    # display data in the form of a list
    print("Show terminal_info()._asdict():")
    terminal_info_dict = mt5.terminal_info()._asdict()
    for prop in terminal_info_dict:
        print("  {}={}".format(prop, terminal_info_dict[prop]))
    print()
   # convert the dictionary into DataFrame and print
    df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
    print("terminal_info() as dataframe:")
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
[500, 2366, '20 Mar 2020']
TerminalInfo(community_account=True, community_connection=True, connected=True,....
Show terminal_info()._asdict():
  community_account=True
  community_connection=True
  connected=True
  dlls_allowed=False
  trade_allowed=False
  tradeapi_disabled=False
  email_enabled=False
  ftp_enabled=False
  notifications_enabled=False
  mqid=False
  build=2366
  maxbars=5000
  codepage=1251
  ping_last=77850
  community_balance=707.10668201585
  retransmission=0.0
  company=MetaQuotes Software Corp.
  name=MetaTrader 5
  language=Russian
  path=E:\ProgramFiles\MetaTrader 5
  data_path=E:\ProgramFiles\MetaTrader 5
  commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Common

terminal_info() as dataframe:
                 property                      value
0       community_account                       True
1    community_connection                       True
2               connected                       True
3            dlls_allowed                      False
4           trade_allowed                      False
5       tradeapi_disabled                      False
6           email_enabled                      False
7             ftp_enabled                      False
8   notifications_enabled                      False
9                    mqid                      False
10                  build                       2367
11                maxbars                       5000
12               codepage                       1251
13              ping_last                      80953
14      community_balance                    707.107
15         retransmission                   0.063593
16                company  MetaQuotes Software Corp.
17                   name               MetaTrader 5
18               language                    Russian
```

## See also

- [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
- [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)
- [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)

---


# symbols_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py>

## Description

Get the number of all financial instruments in the MetaTrader 5 terminal.

## Signatures

```python
symbols_total()
```

## Return Value

Integer value.

## Note

The function is similar to [SymbolsTotal()](https://www.mql5.com/en/docs/marketinformation/symbolstotal). However, it returns the number of all symbols including [custom](https://www.mql5.com/en/docs/customsymbols) ones and the ones disabled in [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of financial instruments
symbols=mt5.symbols_total()
if symbols>0:
    print("Total symbols =",symbols)
else:
    print("symbols not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [symbols_get](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py)
- [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py)
- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)

---


# symbols_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py>

## Description

Get all financial instruments from the MetaTrader 5 terminal.

## Signatures

```python
symbols_get(
   group="GROUP"      // symbol selection filter
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `group="GROUP"` | `"GROUP"` | [in] The filter for arranging a group of necessary symbols. Optional parameter. If the group is specified, the function returns only symbols meeting a specified criteria. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return symbols in the form of a tuple. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The group parameter allows sorting out symbols by name. '*' can be used at the beginning and the end of a string.

The group parameter can be used as a named or an unnamed one. Both options work the same way. The named option (group="GROUP") makes the code easier to read.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that all symbols should be selected first and the ones containing "EUR" in their names should be excluded afterwards.

Unlike [symbol_info()](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py), the symbols_get() function returns data on all requested symbols within a single call.

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get all symbols
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# display the first five ones
for s in symbols:
    count+=1
    print("{}. {}".format(count,s.name))
    if count==5: break
print()

# get symbols containing RU in their names
ru_symbols=mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()

# get symbols whose names do not contain USD, EUR, JPY and GBP
group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name,":",s)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Symbols:  84
1. EURUSD
2. GBPUSD
3. USDCHF
4. USDJPY
5. USDCNH

len(*RU*):  8
EURUSD
USDRUB
USDRUR
EURRUR
EURRUB
FORTS.RUB.M5
EURUSD_T20
EURUSD4

len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13
AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...
AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
```

## See also

- [symbols_total](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py)
- [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py)
- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)

---


# symbol_info

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py>

## Description

Get data on the specified financial instrument.

## Signatures

```python
symbol_info(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function returns all data that can be obtained using [SymbolInfoInteger](https://www.mql5.com/en/docs/marketinformation/symbolinfointeger), [SymbolInfoDouble](https://www.mql5.com/en/docs/marketinformation/symbolinfodouble) and [SymbolInfoString](https://www.mql5.com/en/docs/marketinformation/symbolinfostring) in one call.

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# attempt to enable the display of the EURJPY symbol in MarketWatch
selected=mt5.symbol_select("EURJPY",True)
if not selected:
    print("Failed to select EURJPY")
    mt5.shutdown()
    quit()

# display EURJPY symbol properties
symbol_info=mt5.symbol_info("EURJPY")
if symbol_info!=None:
    # display the terminal data 'as is'
    print(symbol_info)
    print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
    # display symbol properties as a list
    print("Show symbol_info(\"EURJPY\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURJPY")._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...
EURJPY: spread = 17   digits = 3
Show symbol_info()._asdict():
  custom=False
  chart_mode=0
  select=True
  visible=True
  session_deals=0
  session_buy_orders=0
  session_sell_orders=0
  volume=0
  volumehigh=0
  volumelow=0
  time=1585069682
  digits=3
  spread=17
  spread_float=True
  ticks_bookdepth=10
  trade_calc_mode=0
  trade_mode=4
  start_time=0
  expiration_time=0
  trade_stops_level=0
  trade_freeze_level=0
  trade_exemode=1
  swap_mode=1
  swap_rollover3days=3
  margin_hedged_use_leg=False
  expiration_mode=7
  filling_mode=1
  order_mode=127
  order_gtc_mode=0
  option_mode=0
  option_right=0
  bid=120.024
  bidhigh=120.506
  bidlow=118.798
  ask=120.041
  askhigh=120.526
  asklow=118.828
  last=0.0
  lasthigh=0.0
  lastlow=0.0
  volume_real=0.0
  volumehigh_real=0.0
  volumelow_real=0.0
  option_strike=0.0
  point=0.001
  trade_tick_value=0.8977708350166538
  trade_tick_value_profit=0.8977708350166538
  trade_tick_value_loss=0.8978272580355541
  trade_tick_size=0.001
  trade_contract_size=100000.0
  trade_accrued_interest=0.0
  trade_face_value=0.0
  trade_liquidity_rate=0.0
  volume_min=0.01
  volume_max=500.0
  volume_step=0.01
  volume_limit=0.0
  swap_long=-0.2
  swap_short=-1.2
  margin_initial=0.0
  margin_maintenance=0.0
  session_volume=0.0
  session_turnover=0.0
  session_interest=0.0
  session_buy_orders_volume=0.0
  session_sell_orders_volume=0.0
  session_open=0.0
  session_close=0.0
  session_aw=0.0
  session_price_settlement=0.0
  session_price_limit_min=0.0
  session_price_limit_max=0.0
  margin_hedged=100000.0
  price_change=0.0
  price_volatility=0.0
  price_theoretical=0.0
  price_greeks_delta=0.0
  price_greeks_theta=0.0
  price_greeks_gamma=0.0
  price_greeks_vega=0.0
  price_greeks_rho=0.0
  price_greeks_omega=0.0
  price_sensitivity=0.0
  basis=
  category=
  currency_base=EUR
  currency_profit=JPY
  currency_margin=EUR
  bank=
  description=Euro vs Japanese Yen
  exchange=
  formula=
  isin=
  name=EURJPY
  page=http://www.google.com/finance?q=EURJPY
  path=Forex\EURJPY
```

## See also

- [account_info](https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py)
- [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)

---


# symbol_info_tick

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py>

## Description

Get the last tick for the specified financial instrument.

## Signatures

```python
symbol_info_tick(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a tuple. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function is similar to [SymbolInfoTick](https://www.mql5.com/en/docs/marketinformation/symbolinfotick).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# attempt to enable the display of the GBPUSD in MarketWatch
selected=mt5.symbol_select("GBPUSD",True)
if not selected:
    print("Failed to select GBPUSD")
    mt5.shutdown()
    quit()

# display the last GBPUSD tick
lasttick=mt5.symbol_info_tick("GBPUSD")
print(lasttick)
# display tick field values in the form of a list
print("Show symbol_info_tick(\"GBPUSD\")._asdict():")
symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
for prop in symbol_info_tick_dict:
    print("  {}={}".format(prop, symbol_info_tick_dict[prop]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)
Show symbol_info_tick._asdict():
  time=1585070338
  bid=1.17264
  ask=1.17279
  last=0.0
  volume=0
  time_msc=1585070338728
  flags=2
  volume_real=0.0
```

## See also

- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)
- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)

---


# symbol_select

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py>

## Description

Select a symbol in the [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch) window or remove a symbol from the window.

## Signatures

```python
symbol_select(
   symbol,      // financial instrument name
   enable=None  // enable or disable
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |
| `enable` | — | [in] Switch. Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window. Otherwise, it should be selected in the MarketWatch window. A symbol cannot be removed if open charts with this symbol are currently present or positions are opened on it. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

True if successful, otherwise – False.

## Note

The function is similar to [SymbolSelect](https://www.mql5.com/en/docs/marketinformation/symbolselect).

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# attempt to enable the display of the EURCAD in MarketWatch
selected=mt5.symbol_select("EURCAD",True)
if not selected:
    print("Failed to select EURCAD, error code =",mt5.last_error())
else:
    symbol_info=mt5.symbol_info("EURCAD")
    print(symbol_info)
    print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)
    print()

    # get symbol properties in the form of a dictionary
    print("Show symbol_info()._asdict():")
    symbol_info_dict = symbol_info._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))
    print()

    # convert the dictionary into DataFrame and print
    df=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])
    print("symbol_info_dict() as dataframe:")
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....
EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EUR

Show symbol_info()._asdict():
  custom=False
  chart_mode=0
  select=True
  visible=True
  session_deals=0
  session_buy_orders=0
  session_sell_orders=0
  volume=0
  volumehigh=0
  volumelow=0
  time=1585217595
  digits=5
  spread=39
  spread_float=True
  ticks_bookdepth=10
  trade_calc_mode=0
  trade_mode=4
  start_time=0
  expiration_time=0
  trade_stops_level=0
  trade_freeze_level=0
  trade_exemode=1
  swap_mode=1
  swap_rollover3days=3
  margin_hedged_use_leg=False
  expiration_mode=7
  filling_mode=1
  order_mode=127
  order_gtc_mode=0
  option_mode=0
  option_right=0
  bid=1.55192
  bidhigh=1.55842
  bidlow=1.5419800000000001
  ask=1.5523099999999999
  askhigh=1.55915
  asklow=1.5436299999999998
  last=0.0
  lasthigh=0.0
  lastlow=0.0
  volume_real=0.0
  volumehigh_real=0.0
  volumelow_real=0.0
  option_strike=0.0
  point=1e-05
  trade_tick_value=0.7043642408362214
  trade_tick_value_profit=0.7043642408362214
  trade_tick_value_loss=0.7044535553770941
  trade_tick_size=1e-05
  trade_contract_size=100000.0
  trade_accrued_interest=0.0
  trade_face_value=0.0
  trade_liquidity_rate=0.0
  volume_min=0.01
  volume_max=500.0
  volume_step=0.01
  volume_limit=0.0
  swap_long=-1.1
  swap_short=-0.9
  margin_initial=0.0
  margin_maintenance=0.0
  session_volume=0.0
  session_turnover=0.0
  session_interest=0.0
  session_buy_orders_volume=0.0
  session_sell_orders_volume=0.0
  session_open=0.0
  session_close=0.0
  session_aw=0.0
  session_price_settlement=0.0
  session_price_limit_min=0.0
  session_price_limit_max=0.0
  margin_hedged=100000.0
  price_change=0.0
  price_volatility=0.0
  price_theoretical=0.0
  price_greeks_delta=0.0
  price_greeks_theta=0.0
  price_greeks_gamma=0.0
  price_greeks_vega=0.0
  price_greeks_rho=0.0
  price_greeks_omega=0.0
  price_sensitivity=0.0
  basis=
  category=
  currency_base=EUR
  currency_profit=CAD
  currency_margin=EUR
  bank=
  description=Euro vs Canadian Dollar
  exchange=
  formula=
  isin=
  name=EURCAD
  page=http://www.google.com/finance?q=EURCAD
  path=Forex\EURCAD

symbol_info_dict() as dataframe:
         property                                   value
0          custom                                   False
1      chart_mode                                       0
2          select                                    True
3         visible                                    True
4   session_deals                                       0
..            ...                                     ...
91        formula
92           isin
93           name                                  EURCAD
94           page  http://www.google.com/finance?q=EURCAD
95           path                            Forex\EURCAD

[96 rows x 2 columns]
```

## See also

- [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)

---


# market_book_add

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py>

## Description

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

## Signatures

```python
market_book_add(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

True if successful, otherwise – False.

## Note

The function is similar to [MarketBookAdd](https://www.mql5.com/en/docs/marketinformation/marketbookadd).

## See also

- [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py)
- [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py)
- [Market Depth structure](https://www.mql5.com/en/docs/constants/structures/mqlbookinfo)

---


# market_book_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py>

## Description

Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

## Signatures

```python
market_book_get(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots. BookInfo is similar to the [MqlBookInfo](https://www.mql5.com/en/docs/constants/structures/mqlbookinfo) structure.

Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The subscription to the Market Depth change events should be preliminarily performed using the [market_book_add()](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py) function.

The function is similar to [MarketBookGet](https://www.mql5.com/en/docs/marketinformation/marketbookget).

## Example:

```python
import MetaTrader5 as mt5
import time
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print("")

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
   # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()
    quit()

# subscribe to market depth updates for EURUSD (Depth of Market)
if mt5.market_book_add('EURUSD'):
  # get the market depth data 10 times in a loop
   for i in range(10):
        # get the market depth content (Depth of Market)
        items = mt5.market_book_get('EURUSD')
        # display the entire market depth 'as is' in a single string
        print(items)
        # now display each order separately for more clarity
        if items:
            for it in items:
                # order content
                print(it._asdict())
        # pause for 5 seconds before the next request of the market depth data
        time.sleep(5)
  # cancel the subscription to the market depth updates (Depth of Market)
   mt5.market_book_release('EURUSD')
else:
    print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.34

(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...
{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...
{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...
{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...
{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...
{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...
{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}
```

## See also

- [market_book_add](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py)
- [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py)
- [Market Depth structure](https://www.mql5.com/en/docs/constants/structures/mqlbookinfo)

---


# market_book_release

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py>

## Description

Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

## Signatures

```python
market_book_release(
   symbol      // financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

True if successful, otherwise – False.

## Note

The function is similar to [MarketBookRelease](https://www.mql5.com/en/docs/marketinformation/marketbookrelease).

## See also

- [market_book_add](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py)
- [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py)
- [Market Depth structure](https://www.mql5.com/en/docs/constants/structures/mqlbookinfo)

---


# copy_rates_from

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py>

## Description

Get bars from the MetaTrader 5 terminal starting from the specified date.

## Signatures

```python
copy_rates_from(
   symbol,       // symbol name
   timeframe,    // timeframe
   date_from,    // initial bar open date
   count         // number of bars
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| `timeframe` | — | [in] Timeframe the bars are requested for. Set by a value from the [TIMEFRAME](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py#timeframe) enumeration. Required unnamed parameter. |
| `date_from` | — | [in] Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `count` | — | [in] Number of bars to receive. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

See the [CopyRates()](https://www.mql5.com/en/docs/series/copyrates) function for more information.

Only data whose date is less than (earlier) or equal to the date specified will be returned. It means, the open time of any bar is always less or equal to the specified one.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "[Max. bars in chart](https://www.metatrader5.com/en/terminal/help/startworking/settings#max_bars)" parameter.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.

TIMEFRAME is an enumeration with possible chart period values

| ID | Description |
| --- | --- |
| TIMEFRAME_M1 | 1 minute |
| TIMEFRAME_M2 | 2 minutes |
| TIMEFRAME_M3 | 3 minutes |
| TIMEFRAME_M4 | 4 minutes |
| TIMEFRAME_M5 | 5 minutes |
| TIMEFRAME_M6 | 6 minutes |
| TIMEFRAME_M10 | 10 minutes |
| TIMEFRAME_M12 | 12 minutes |
| TIMEFRAME_M12 | 15 minutes |
| TIMEFRAME_M20 | 20 minutes |
| TIMEFRAME_M30 | 30 minutes |
| TIMEFRAME_H1 | 1 hour |
| TIMEFRAME_H2 | 2 hours |
| TIMEFRAME_H3 | 3 hours |
| TIMEFRAME_H4 | 4 hours |
| TIMEFRAME_H6 | 6 hours |
| TIMEFRAME_H8 | 8 hours |
| TIMEFRAME_H12 | 12 hours |
| TIMEFRAME_D1 | 1 day |
| TIMEFRAME_W1 | 1 week |
| TIMEFRAME_MN1 | 1 month |

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame)


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Display obtained data 'as is'
(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)
(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)
(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)
(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)
(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)
(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)
(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)
(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)
(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)
(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)

Display dataframe with data
                 time     open     high      low    close  tick_volume  spread  real_volume
0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            0
1 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            0
2 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            0
3 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            0
4 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            0
5 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            0
6 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            0
7 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            0
8 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            0
9 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0
```

## See also

- [CopyRates](https://www.mql5.com/en/docs/series/copyrates)
- [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py)
- [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
- [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
- [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

---


# copy_rates_from_pos

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py>

## Description

Get bars from the MetaTrader 5 terminal starting from the specified index.

## Signatures

```python
copy_rates_from_pos(
   symbol,       // symbol name
   timeframe,    // timeframe
   start_pos,    // initial bar index
   count         // number of bars
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| `timeframe` | — | [in] Timeframe the bars are requested for. Set by a value from the [TIMEFRAME](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py#timeframe) enumeration. Required unnamed parameter. |
| `start_pos` | — | [in] Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter. |
| `count` | — | [in] Number of bars to receive. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

See the [CopyRates()](https://www.mql5.com/en/docs/series/copyrates) function for more information.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "[Max. bars in chart](https://www.metatrader5.com/en/terminal/help/startworking/settings#max_bars)" parameter.

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get 10 GBPUSD D1 bars from the current day
rates = mt5.copy_rates_from_pos("GBPUSD", mt5.TIMEFRAME_D1, 0, 10)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame)

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Display obtained data 'as is'
(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)
(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)
(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)
(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)
(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)
(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)
(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)
(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)
(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)
(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)

Display dataframe with data
        time     open     high      low    close  tick_volume  spread  real_volume
0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            0
1 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            0
2 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            0
3 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            0
4 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            0
5 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            0
6 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            0
7 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            0
8 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            0
9 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0
```

## See also

- [CopyRates](https://www.mql5.com/en/docs/series/copyrates)
- [copy_rates_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py)
- [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
- [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
- [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

---


# copy_rates_range

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py>

## Description

Get bars in the specified date range from the MetaTrader 5 terminal.

## Signatures

```python
copy_rates_range(
   symbol,       // symbol name
   timeframe,    // timeframe
   date_from,    // date the bars are requested from
   date_to       // date, up to which the bars are requested
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| `timeframe` | — | [in] Timeframe the bars are requested for. Set by a value from the [TIMEFRAME](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py#timeframe) enumeration. Required unnamed parameter. |
| `date_from` | — | [in] Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter. |
| `date_to` | — | [in] Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

See the [CopyRates()](https://www.mql5.com/en/docs/series/copyrates) function for more information.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "[Max. bars in chart](https://www.metatrader5.com/en/terminal/help/startworking/settings#max_bars)" parameter.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, hour = 13, tzinfo=timezone)
# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
counter=0
for rate in rates:
    counter+=1
    if counter<=10:
        print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the 'datetime' format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Display obtained data 'as is'
(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)
(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)
(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)
(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)
(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)
(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)
(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)
(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)
(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)
(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)

Display dataframe with data
                 time     open     high      low    close  tick_volume  spread  real_volume
0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            0
1 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            0
2 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            0
3 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            0
4 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            0
5 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            0
6 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            0
7 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            0
8 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            0
9 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0
```

## See also

- [CopyRates](https://www.mql5.com/en/docs/series/copyrates)
- [copy_rates_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py)
- [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
- [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
- [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

---


# copy_ticks_from

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py>

## Description

Get ticks from the MetaTrader 5 terminal starting from the specified date.

## Signatures

```python
copy_ticks_from(
   symbol,       // symbol name
   date_from,    // date the ticks are requested from
   count,        // number of requested ticks
   flags         // combination of flags defining the type of requested ticks
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| `from` | — | [in] Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `count` | — | [in] Number of ticks to receive. Required unnamed parameter. |
| `flags` | — | [in] A flag to define the type of the requested ticks. COPY_TICKS_INFO – ticks with Bid and/or Ask changes, COPY_TICKS_TRADE – ticks with changes in Last and Volume, COPY_TICKS_ALL – all ticks. Flag values are described in the [COPY_TICKS](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py#copy_ticks) enumeration. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from the [TICK_FLAG](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py#tick_flag) enumeration. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

See the [CopyTicks](https://www.mql5.com/en/docs/series/copyticks) function for more information.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.

COPY_TICKS defines the types of ticks that can be requested using the [copy_ticks_from()](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py) and [copy_ticks_range()](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py) functions.

| ID | Description |
| --- | --- |
| COPY_TICKS_ALL | all ticks |
| COPY_TICKS_INFO | ticks containing Bid and/or Ask price changes |
| COPY_TICKS_TRADE | ticks containing Last and/or Volume price changes |

TICK_FLAG defines possible flags for ticks. These flags are used to describe ticks obtained by the [copy_ticks_from()](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py) and [copy_ticks_range()](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py) functions.

| ID | Description |
| --- | --- |
| TICK_FLAG_BID | Bid price changed |
| TICK_FLAG_ASK | Ask price changed |
| TICK_FLAG_LAST | Last price changed |
| TICK_FLAG_VOLUME | Volume changed |
| TICK_FLAG_BUY | last Buy price changed |
| TICK_FLAG_SELL | last Sell price changed |

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
ticks = mt5.copy_ticks_from("EURUSD", utc_from, 100000, mt5.COPY_TICKS_ALL)
print("Ticks received:",len(ticks))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break

# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Ticks received: 100000
Display obtained ticks 'as is'
(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)
(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)
(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)
(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)
(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)
(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)
(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)
(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)
(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)
(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)

Display dataframe with ticks
                 time      bid      ask  last  volume       time_msc  flags  volume_real
0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.0
1 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.0
2 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.0
3 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.0
4 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.0
5 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.0
6 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.0
7 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.0
8 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.0
9 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0
```

## See also

- [CopyRates](https://www.mql5.com/en/docs/series/copyrates)
- [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py)
- [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
- [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
- [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

---


# copy_ticks_range

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py>

## Description

Get ticks for the specified date range from the MetaTrader 5 terminal.

## Signatures

```python
copy_ticks_range(
   symbol,       // symbol name
   date_from,    // date the ticks are requested from
   date_to,      // date, up to which the ticks are requested
   flags         // combination of flags defining the type of requested ticks
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol` | — | [in] Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| `date_from` | — | [in] Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `date_to` | — | [in] Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `flags` | — | [in] A flag to define the type of the requested ticks. COPY_TICKS_INFO – ticks with Bid and/or Ask changes, COPY_TICKS_TRADE – ticks with changes in Last and Volume, COPY_TICKS_ALL – all ticks. Flag values are described in the [COPY_TICKS](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py#copy_ticks) enumeration. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from the [TICK_FLAG](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py#tick_flag) enumeration. Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

See the [CopyTicks](https://www.mql5.com/en/docs/series/copyticks) function for more information.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. The data obtained from MetaTrader 5 have UTC time, but Python applies the local time shift again when trying to print them. Thus, the obtained data should also be corrected for visual presentation.

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, tzinfo=timezone)
# request AUDUSD ticks within 11.01.2020 - 11.01.2020
ticks = mt5.copy_ticks_range("AUDUSD", utc_from, utc_to, mt5.COPY_TICKS_ALL)
print("Ticks received:",len(ticks))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break

# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Ticks received: 37008
Display obtained ticks 'as is'
(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)
(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)
(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)
(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)
(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)
(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)
(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)
(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)
(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)
(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)

Display dataframe with ticks
                 time      bid      ask  last  volume       time_msc  flags  volume_real
0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.0
1 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.0
2 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.0
3 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.0
4 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.0
5 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.0
6 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.0
7 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.0
8 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.0
9 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0
```

## See also

- [CopyRates](https://www.mql5.com/en/docs/series/copyrates)
- [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py)
- [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)
- [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)
- [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

---


# orders_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py>

## Description

Get the number of active orders.

## Signatures

```python
orders_total()
```

## Return Value

Integer value.

## Note

The function is similar to [OrdersTotal](https://www.mql5.com/en/docs/trading/orderstotal).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# check the presence of active orders
orders=mt5.orders_total()
if orders>0:
    print("Total orders=",orders)
else:
    print("Orders not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py)
- [positions_total](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py)

---


# orders_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py>

## Description

Get active orders with the ability to filter by symbol or ticket. There are three call options.

Call without parameters. Return active orders on all symbols.

Call specifying a symbol active orders should be received for.

Call specifying a group of symbols active orders should be received for.

Call specifying the order ticket.

## Signatures

```python
orders_get()
```

```python
orders_get(
   symbol="SYMBOL"      // symbol name
)
```

```python
orders_get(
   group="GROUP"        // filter for selecting orders for symbols
)
```

```python
orders_get(
   ticket=TICKET        // ticket
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol="SYMBOL"` | `"SYMBOL"` | [in] Symbol name. Optional named parameter. If a symbol is specified, the ticket parameter is ignored. |
| `group="GROUP"` | `"GROUP"` | [in] The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only active orders meeting a specified criteria for a symbol name. |
| `ticket=TICKET` | `TICKET` | [in] Order ticket ([ORDER_TICKET](https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_property_integer)). Optional named parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows receiving all active orders within one call similar to the [OrdersTotal](https://www.mql5.com/en/docs/trading/orderstotal) and [OrderSelect](https://www.mql5.com/en/docs/trading/orderselect) tandem.

The group parameter allows sorting out orders by symbols. '*' can be used at the beginning and the end of a string.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that orders for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# display data on active orders on GBPUSD
orders=mt5.orders_get(symbol="GBPUSD")
if orders is None:
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on GBPUSD:",len(orders))
    # display all active orders
    for order in orders:
        print(order)
print()

# get the list of orders on symbols whose names contain "*GBP*"
gbp_orders=mt5.orders_get(group="*GBP*")
if gbp_orders is None:
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
else:
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
    # display these orders as a table using pandas.DataFrame
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Total orders on GBPUSD: 2
TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...
TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...

orders_get(group="*GBP*")=4
      ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id
0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD
1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD
2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP
3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP
```

## See also

- [orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py)
- [positions_get](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py)

---


# order_calc_margin

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py>

## Description

Return margin in the account currency to perform a specified trading operation.

## Signatures

```python
order_calc_margin(
   action,      // order type (ORDER_TYPE_BUY or ORDER_TYPE_SELL)
   symbol,      // symbol name
   volume,      // volume
   price        // open price
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `action` | — | [in] Order type taking values from the [ORDER_TYPE](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py#order_type) enumeration. Required unnamed parameter. |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |
| `volume` | — | [in] Trading operation volume. Required unnamed parameter. |
| `price` | — | [in] Open price. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Real value if successful, otherwise None. The error info can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows estimating the margin necessary for a specified order type on the current account and in the current market environment without considering the current pending orders and open positions. The function is similar to [OrderCalcMargin](https://www.mql5.com/en/docs/trading/ordercalcmargin).

ORDER_TYPE

| ID | Description |
| --- | --- |
| ORDER_TYPE_BUY | Market buy order |
| ORDER_TYPE_SELL | Market sell order |
| ORDER_TYPE_BUY_LIMIT | Buy Limit pending order |
| ORDER_TYPE_SELL_LIMIT | Sell Limit pending order |
| ORDER_TYPE_BUY_STOP | Buy Stop pending order |
| ORDER_TYPE_SELL_STOP | Sell Stop pending order |
| ORDER_TYPE_BUY_STOP_LIMIT | Upon reaching the order price, Buy Limit pending order is placed at StopLimit price |
| ORDER_TYPE_SELL_STOP_LIMIT | Upon reaching the order price, Sell Limit pending order is placed at StopLimit price |
| ORDER_TYPE_CLOSE_BY | Order for closing a position by an opposite one |

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get account currency
account_currency=mt5.account_info().currency
print("Account currency:",account_currency)

# arrange the symbol list
symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")
print("Symbols to check margin:", symbols)
action=mt5.ORDER_TYPE_BUY
lot=0.1
for symbol in symbols:
    symbol_info=mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol,"not found, skipped")
        continue
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, skipped",symbol)
            continue
    ask=mt5.symbol_info_tick(symbol).ask
    margin=mt5.order_calc_margin(action,symbol,lot,ask)
    if margin != None:
        print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));
    else:
        print("order_calc_margin failed: , error code =", mt5.last_error())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Account currency: USD

Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')
   EURUSD buy 0.1 lot margin: 109.91 USD
   GBPUSD buy 0.1 lot margin: 122.73 USD
   USDJPY buy 0.1 lot margin: 100.0 USD
   USDCHF buy 0.1 lot margin: 100.0 USD
   EURJPY buy 0.1 lot margin: 109.91 USD
   GBPJPY buy 0.1 lot margin: 122.73 USD
```

## See also

- [order_calc_profit](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py)
- [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py)

---


# order_calc_profit

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py>

## Description

Return profit in the account currency for a specified trading operation.

## Signatures

```python
order_calc_profit(
   action,          // order type (ORDER_TYPE_BUY or ORDER_TYPE_SELL)
   symbol,          // symbol name
   volume,          // volume
   price_open,      // open price
   price_close      // close price
   );
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `action` | — | [in] Order type may take one of the two [ORDER_TYPE](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py#order_type) enumeration values: ORDER_TYPE_BUY or ORDER_TYPE_SELL. Required unnamed parameter. |
| `symbol` | — | [in] Financial instrument name. Required unnamed parameter. |
| `volume` | — | [in] Trading operation volume. Required unnamed parameter. |
| `price_open` | — | [in] Open price. Required unnamed parameter. |
| `price_close` | — | [in] Close price. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Real value if successful, otherwise None. The error info can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows estimating a trading operation result on the current account and in the current trading environment. The function is similar to [OrderCalcProfit](https://www.mql5.com/en/docs/trading/ordercalcprofit).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get account currency
account_currency=mt5.account_info().currency
print("Account currency:",account_currency)

# arrange the symbol list
symbols = ("EURUSD","GBPUSD","USDJPY")
print("Symbols to check margin:", symbols)
# estimate profit for buying and selling
lot=1.0
distance=300
for symbol in symbols:
    symbol_info=mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol,"not found, skipped")
        continue
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, skipped",symbol)
            continue
    point=mt5.symbol_info(symbol).point
    symbol_tick=mt5.symbol_info_tick(symbol)
    ask=symbol_tick.ask
    bid=symbol_tick.bid
    buy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)
    if buy_profit!=None:
        print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));
    else:
        print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())
    sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)
    if sell_profit!=None:
        print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));
    else:
        print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())
    print()

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Account currency: USD
Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')
   buy EURUSD 1.0 lot: profit on 300 points => 300.0 USD
   sell EURUSD 1.0 lot: profit on 300 points => 300.0 USD

   buy GBPUSD 1.0 lot: profit on 300 points => 300.0 USD
   sell GBPUSD 1.0 lot: profit on 300 points => 300.0 USD

   buy USDJPY 1.0 lot: profit on 300 points => 276.54 USD
   sell USDJPY 1.0 lot: profit on 300 points => 278.09 USD
```

## See also

- [order_calc_margin](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py)
- [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py)

---


# order_check

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py>

## Description

Check funds sufficiency for performing a required [trading operation](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions). Check result are returned as the [MqlTradeCheckResult](https://www.mql5.com/en/docs/constants/structures/mqltradecheckresult) structure.

## Signatures

```python
order_check(
   request      // request structure
   );
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `request` | — | [in] [MqlTradeRequest](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py#traderequest) type structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Check result as the [MqlTradeCheckResult](https://www.mql5.com/en/docs/constants/structures/mqltradecheckresult) structure. The request field in the answer contains the structure of a trading request passed to order_check().

## Note

Successful sending of a request does not entail that the requested trading operation will be executed successfully. The order_check function is similar to [OrderCheck](https://www.mql5.com/en/docs/trading/ordercheck).

TRADE_REQUEST_ACTIONS

| ID | Description |
| --- | --- |
| TRADE_ACTION_DEAL | Place an order for an instant deal with the specified parameters (set a market order) |
| TRADE_ACTION_PENDING | Place an order for performing a deal at specified conditions (pending order) |
| TRADE_ACTION_SLTP | Change open position Stop Loss and Take Profit |
| TRADE_ACTION_MODIFY | Change parameters of the previously placed trading order |
| TRADE_ACTION_REMOVE | Remove previously placed pending order |
| TRADE_ACTION_CLOSE_BY | Close a position by an opposite one |

ORDER_TYPE_FILLING

| ID | Description |
| --- | --- |
| ORDER_FILLING_FOK | This execution policy means that an order can be executed only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The desired volume can be made up of several available offers. |
| ORDER_FILLING_IOC | An agreement to execute a deal at the maximum volume available in the market within the volume specified in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled. |
| ORDER_FILLING_RETURN | This policy is used only for market (ORDER_TYPE_BUY and ORDER_TYPE_SELL), limit and stop limit orders (ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT, ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT) and only for the symbols with Market or Exchange execution [modes](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution). If filled partially, a market or limit order with the remaining volume is not canceled, and is processed further. During activation of the ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT orders, an appropriate limit order ORDER_TYPE_BUY_LIMIT/ORDER_TYPE_SELL_LIMIT with the ORDER_FILLING_RETURN type is created. |

ORDER_TYPE_TIME

| ID | Description |
| --- | --- |
| ORDER_TIME_GTC | The order stays in the queue until it is manually canceled |
| ORDER_TIME_DAY | The order is active only during the current trading day |
| ORDER_TIME_SPECIFIED | The order is active until the specified date |
| ORDER_TIME_SPECIFIED_DAY | The order is active until 23:59:59 of the specified day. If this time appears to be out of a trading session, the expiration is processed at the nearest trading time. |

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get account currency
account_currency=mt5.account_info().currency
print("Account currency:",account_currency)

# prepare the request structure
symbol="USDJPY"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

# if the symbol is unavailable in MarketWatch, add it
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol,True):
        print("symbol_select({}}) failed, exit",symbol)
        mt5.shutdown()
        quit()

# prepare the request
point=mt5.symbol_info(symbol).point
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 1.0,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "sl": mt5.symbol_info_tick(symbol).ask-100*point,
    "tp": mt5.symbol_info_tick(symbol).ask+100*point,
    "deviation": 10,
    "magic": 234000,
    "comment": "python script",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# perform the check and display the result 'as is'
result = mt5.order_check(request)
print(result);
# request the result as a dictionary and display it element by element
result_dict=result._asdict()
for field in result_dict.keys():
    print("   {}={}".format(field,result_dict[field]))
    # if this is a trading request structure, display it element by element as well
    if field=="request":
        traderequest_dict=result_dict[field]._asdict()
        for tradereq_filed in traderequest_dict:
            print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

Account currecy: USD
   retcode=0
   balance=101300.53
   equity=68319.53
   profit=-32981.0
   margin=51193.67
   margin_free=17125.86
   margin_level=133.45308121101692
   comment=Done
   request=TradeRequest(action=1, magic=234000, order=0, symbol='USDJPY', volume=1.0, ...
       traderequest: action=1
       traderequest: magic=234000
       traderequest: order=0
       traderequest: symbol=USDJPY
       traderequest: volume=1.0
       traderequest: price=108.081
       traderequest: stoplimit=0.0
       traderequest: sl=107.98100000000001
       traderequest: tp=108.181
       traderequest: deviation=10
       traderequest: type=0
       traderequest: type_filling=2
       traderequest: type_time=0
       traderequest: expiration=0
       traderequest: comment=python script
       traderequest: position=0
       traderequest: position_by=0
```

## See also

- [order_send](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py)
- [OrderCheck](https://www.mql5.com/en/docs/trading/ordercheck)
- [Trading operation types](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions)
- [Trading request structure](https://www.mql5.com/en/docs/constants/structures/mqltraderequest)
- [Structure of the trading request check results](https://www.mql5.com/en/docs/constants/structures/mqltradecheckresult)
- [Structure of the trading request result](https://www.mql5.com/en/docs/constants/structures/mqltraderesult)

---


# order_send

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py>

## Description

Send a [request](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) to perform a [trading operation](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions) from the terminal to the trade server. The function is similar to [OrderSend](https://www.mql5.com/en/docs/trading/ordersend).

## Signatures

```python
order_send(
   request      // request structure
   );
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `request` | — | [in] [MqlTradeRequest](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) type structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Execution result as the [MqlTradeResult](https://www.mql5.com/en/docs/constants/structures/mqltraderesult) structure. The request field in the answer contains the structure of a trading request passed to order_send(). The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

The [MqlTradeRequest](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) trading request structure

| Field | Description |
| --- | --- |
| action | Trading operation type. The value can be one of the values of the [TRADE_REQUEST_ACTIONS](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#trade_request_actions) enumeration |
| magic | EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request |
| order | Order ticket. Required for modifying pending orders |
| symbol | The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions |
| volume | Requested volume of a deal in lots. A real volume when making a deal depends on an [order execution type](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#order_type_filling). |
| price | Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" ([SYMBOL_TRADE_EXECUTION_MARKET](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution)) type having the [TRADE_ACTION_DEAL](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#trade_request_actions) type |
| stoplimit | A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment |
| sl | A price a Stop Loss order is activated at when the price moves in an unfavorable direction |
| tp | A price a Take Profit order is activated at when the price moves in a favorable direction |
| deviation | Maximum acceptable deviation from the requested price, specified in [points](https://www.mql5.com/en/docs/predefined/_point) |
| type | Order type. The value can be one of the values of the [ORDER_TYPE](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py#order_type) enumeration |
| type_filling | Order filling type. The value can be one of the [ORDER_TYPE_FILLING](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#order_type_filling) values |
| type_time | Order type by expiration. The value can be one of the [ORDER_TYPE_TIME](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#order_type_time) values |
| expiration | Pending order expiration time (for [TIME_SPECIFIED](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py#order_type_time) type orders) |
| comment | Comment to an order |
| position | Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position. |
| position_by | Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction). |

## Note

A trading request passes several verification stages on the trade server. First, the validity of all the necessary request fields is checked. If there are no errors, the server accepts the order for further handling. See the [OrderSend](https://www.mql5.com/en/docs/trading/ordersend) function description for the details about executing trading operations.

## Example:

```python
import time
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# prepare the buy request structure
symbol = "USDJPY"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

# if the symbol is unavailable in MarketWatch, add it
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol,True):
        print("symbol_select({}}) failed, exit",symbol)
        mt5.shutdown()
        quit()

lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 100 * point,
    "tp": price + 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# send a trading request
result = mt5.order_send(request)
# check the execution result
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    mt5.shutdown()
    quit()

print("2. order_send done, ", result)
print("   opened position with POSITION_TICKET={}".format(result.order))
print("   sleep 2 seconds before closing position #{}".format(result.order))
time.sleep(2)
# create a close request
position_id=result.order
price=mt5.symbol_info_tick(symbol).bid
deviation=20
request={
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
# send a trading request
result=mt5.order_send(request)
# check the execution result
print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send failed, retcode={}".format(result.retcode))
    print("   result",result)
else:
    print("4. position #{} closed, {}".format(position_id,result))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

Result
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
1. order_send(): by USDJPY 0.1 lots at 108.023 with deviation=20 points
2. order_send done,  OrderSendResult(retcode=10009, deal=535084512, order=557416535, volume=0.1, price=108.023, ...
   opened position with POSITION_TICKET=557416535
   sleep 2 seconds before closing position #557416535
3. close position #557416535: sell USDJPY 0.1 lots at 108.018 with deviation=20 points
4. position #557416535 closed, OrderSendResult(retcode=10009, deal=535084631, order=557416654, volume=0.1, price=...
   retcode=10009
   deal=535084631
   order=557416654
   volume=0.1
   price=108.015
   bid=108.015
   ask=108.02
   comment=Request executed
   request_id=55
   retcode_external=0
   request=TradeRequest(action=1, magic=234000, order=0, symbol='USDJPY', volume=0.1, price=108.018, stoplimit=0.0, ...
       traderequest: action=1
       traderequest: magic=234000
       traderequest: order=0
       traderequest: symbol=USDJPY
       traderequest: volume=0.1
       traderequest: price=108.018
       traderequest: stoplimit=0.0
       traderequest: sl=0.0
       traderequest: tp=0.0
       traderequest: deviation=20
       traderequest: type=1
       traderequest: type_filling=2
       traderequest: type_time=0
       traderequest: expiration=0
       traderequest: comment=python script close
       traderequest: position=557416535
       traderequest: position_by=0
```

## See also

- [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py)
- [OrderSend](https://www.mql5.com/en/docs/trading/ordersend)
- [Trading operation types](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions)
- [Trading request structure](https://www.mql5.com/en/docs/constants/structures/mqltraderequest)
- [Structure of the trading request check results](https://www.mql5.com/en/docs/constants/structures/mqltradecheckresult)
- [Structure of the trading request result](https://www.mql5.com/en/docs/constants/structures/mqltraderesult)

---


# positions_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py>

## Description

Get the number of open positions.

## Signatures

```python
positions_total()
```

## Return Value

Integer value.

## Note

The function is similar to [PositionsTotal](https://www.mql5.com/en/docs/trading/positionstotal).

## Example:

```python
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# check the presence of open positions
positions_total=mt5.positions_total()
if positions_total>0:
    print("Total positions=",positions_total)
else:
    print("Positions not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [positions_get](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py)
- [orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py)

---


# positions_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py>

## Description

Get open positions with the ability to filter by symbol or ticket. There are three call options.

Call without parameters. Return open positions for all symbols.

Call specifying a symbol open positions should be received for.

Call specifying a group of symbols open positions should be received for.

Call specifying a position ticket.

## Signatures

```python
positions_get()
```

```python
positions_get(
   symbol="SYMBOL"      // symbol name
)
```

```python
positions_get(
   group="GROUP"        // filter for selecting positions by symbols
)
```

```python
positions_get(
   ticket=TICKET        // ticket
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `symbol="SYMBOL"` | `"SYMBOL"` | [in] Symbol name. Optional named parameter. If a symbol is specified, the ticket parameter is ignored. |
| `group="GROUP"` | `"GROUP"` | [in] The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only positions meeting a specified criteria for a symbol name. |
| `ticket=TICKET` | `TICKET` | [in] Position ticket ([POSITION_TICKET](https://www.mql5.com/en/docs/constants/tradingconstants/positionproperties#enum_position_property_integer)). Optional named parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows receiving all open positions within one call similar to the [PositionsTotal](https://www.mql5.com/en/docs/trading/positionstotal) and [PositionSelect](https://www.mql5.com/en/docs/trading/positionselect) tandem.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that positions for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

## Example:

```python
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get open positions on USDCHF
positions=mt5.positions_get(symbol="USDCHF")
if positions==None:
    print("No positions on USDCHF, error code={}".format(mt5.last_error()))
elif len(positions)>0:
    print("Total positions on USDCHF =",len(positions))
    # display all open positions
    for position in positions:
        print(position)

# get the list of positions on symbols whose names contain "*USD*"
usd_positions=mt5.positions_get(group="*USD*")
if usd_positions==None:
    print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(usd_positions)>0:
    print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    # display these positions as a table using pandas.DataFrame
    df=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

positions_get(group="*USD*")=5
      ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment
0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD
1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD
2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD
3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD
4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD
```

## See also

- [positions_total](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py)
- [orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py)

---


# history_orders_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py>

## Description

Get the number of orders in trading history within the specified interval.

## Signatures

```python
history_orders_total(
   date_from,    // date the orders are requested from
   date_to       // date, up to which the orders are requested
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `date_from` | — | [in] Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `date_to` | — | [in] Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Integer value.

## Note

The function is similar to [HistoryOrdersTotal](https://www.mql5.com/en/docs/trading/historyorderstotal).

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of orders in history
from_date=datetime(2020,1,1)
to_date=datetime.now()
history_orders=mt5.history_orders_total(from_date, datetime.now())
if history_orders>0:
    print("Total history orders=",history_orders)
else:
    print("Orders not found in history")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py)
- [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)

---


# history_orders_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py>

## Description

Get orders from trading history with the ability to filter by ticket or position. There are three call options.

Call specifying a time interval. Return all orders falling within the specified interval.

Call specifying the order ticket. Return an order with the specified ticket.

Call specifying the position ticket. Return all orders with a position ticket specified in the [ORDER_POSITION_ID](https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_property_integer) property.

## Signatures

```python
history_orders_get(
   date_from,                // date the orders are requested from
   date_to,                  // date, up to which the orders are requested
   group="GROUP"        // filter for selecting orders by symbols
   )
```

```python
history_orders_get(
   ticket=TICKET        // order ticket
)
```

```python
history_orders_get(
   position=POSITION    // position ticket
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `date_from` | — | [in] Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first. |
| `date_to` | — | [in] Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second. |
| `group="GROUP"` | `"GROUP"` | [in] The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name. |
| `ticket=TICKET` | `TICKET` | [in] Order ticket that should be received. Optional parameter. If not specified, the filter is not applied. |
| `position=POSITION` | `POSITION` | [in] Ticket of a position (stored in [ORDER_POSITION_ID](https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_property_integer)) all orders should be received for. Optional parameter. If not specified, the filter is not applied. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows receiving all history orders within a specified period in a single call similar to the [HistoryOrdersTotal](https://www.mql5.com/en/docs/trading/historyorderstotal) and [HistoryOrderSelect](https://www.mql5.com/en/docs/trading/historyorderselect) tandem.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that deals for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of orders in history
from_date=datetime(2020,1,1)
to_date=datetime.now()
history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")
if history_orders==None:
    print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(history_orders)>0:
    print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))
print()

# display all historical orders by a position ticket
position_id=530218319
position_history_orders=mt5.history_orders_get(position=position_id)
if position_history_orders==None:
    print("No orders with position #{}".format(position_id))
    print("error code =",mt5.last_error())
elif len(position_history_orders)>0:
    print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))
    # display all historical orders having a specified position ticket
    for position_order in position_history_orders:
        print(position_order)
    print()
    # display these orders as a table using pandas.DataFrame
    df=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())
    df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14

Total history orders on position #530218319: 2
TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...
TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...

      ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id
0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF
1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF
```

## See also

- [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)
- [history_deals_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py)

---


# history_deals_total

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py>

## Description

Get the number of deals in trading history within the specified interval.

## Signatures

```python
history_deals_total(
   date_from,    // date the deals are requested from
   date_to       // date, up to which the deals are requested
   )
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `date_from` | — | [in] Date the deals are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| `date_to` | — | [in] Date, up to which the deals are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Integer value.

## Note

The function is similar to [HistoryDealsTotal](https://www.mql5.com/en/docs/trading/historydealstotal).

## Example:

```python
from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of deals in history
from_date=datetime(2020,1,1)
to_date=datetime.now()
deals=mt5.history_deals_total(from_date, to_date)
if deals>0:
    print("Total deals=",deals)
else:
    print("Deals not found in history")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

- [history_deals_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py)
- [history_orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py)

---


# history_deals_get

**Source:** MQL5 Reference > Python Integration  
**URL:** <https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py>

## Description

Get deals from trading history within the specified interval with the ability to filter by ticket or position.

Call specifying a time interval. Return all deals falling within the specified interval.

Call specifying the order ticket. Return all deals having the specified order ticket in the [DEAL_ORDER](https://www.mql5.com/en/docs/constants/tradingconstants/dealproperties#enum_deal_property_integer) property.

Call specifying the position ticket. Return all deals having the specified position ticket in the [DEAL_POSITION_ID](https://www.mql5.com/en/docs/constants/tradingconstants/dealproperties#enum_deal_property_integer) property.

## Signatures

```python
history_deals_get(
   date_from,                // date the deals are requested from
   date_to,                  // date, up to which the deals are requested
   group="GROUP"        // filter for selecting deals for symbols
   )
```

```python
history_deals_get(
   ticket=TICKET        // order ticket
)
```

```python
history_deals_get(
   position=POSITION    // position ticket
)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `date_from` | — | [in] Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first. |
| `date_to` | — | [in] Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second. |
| `group="GROUP"` | `"GROUP"` | [in] The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name. |
| `ticket=TICKET` | `TICKET` | [in] Ticket of an order (stored in [DEAL_ORDER](https://www.mql5.com/en/docs/constants/tradingconstants/dealproperties#enum_deal_property_integer)) all deals should be received for. Optional parameter. If not specified, the filter is not applied. |
| `position=POSITION` | `POSITION` | [in] Ticket of a position (stored in [DEAL_POSITION_ID](https://www.mql5.com/en/docs/constants/tradingconstants/dealproperties#enum_deal_property_integer)) all deals should be received for. Optional parameter. If not specified, the filter is not applied. |

*The Type column shows the value placeholder as written in the function signature; the source page does not declare types separately.*

## Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last_error()](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py).

## Note

The function allows receiving all history deals within a specified period in a single call similar to the [HistoryDealsTotal](https://www.mql5.com/en/docs/trading/historydealstotal) and [HistoryDealSelect](https://www.mql5.com/en/docs/trading/historydealselect) tandem.

The group parameter allows sorting out deals by symbols. '*' can be used at the beginning and the end of a string.

The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that deals for all symbols should be selected first and the ones containing "EUR" in symbol names should be excluded afterwards.

## Example:

```python
import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
print()
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# get the number of deals in history
from_date=datetime(2020,1,1)
to_date=datetime.now()
# get deals for symbols whose names contain "GBP" within a specified interval
deals=mt5.history_deals_get(from_date, to_date, group="*GBP*")
if deals==None:
    print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(deals)> 0:
    print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))

# get deals for symbols whose names contain neither "EUR" nor "GBP"
deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")
if deals == None:
    print("No deals, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
    # display all obtained deals 'as is'
    for deal in deals:
        print("  ",deal)
    print()
    # display these deals as a table using pandas.DataFrame
    df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
print("")

# get all deals related to the position #530218319
position_id=530218319
position_deals = mt5.history_deals_get(position=position_id)
if position_deals == None:
    print("No deals with position #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_deals) > 0:
    print("Deals with position id #{}: {}".format(position_id, len(position_deals)))
    # display these deals as a table using pandas.DataFrame
    df=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29

history_deals_get(from_date, to_date, group="*GBP*") = 14

history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7
   TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...
   TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...
   TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...
   TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...
   TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...
   TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...
   TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...

      ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id
0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.0
1  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF
2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF
3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF
4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD
5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF
6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSD

Deals with position id #530218319: 2
      ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id
0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF
1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF
```

## See also

- [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)
- [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py)

---
