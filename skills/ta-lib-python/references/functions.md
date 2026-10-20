# All functions

The complete list of the 201 functions, grouped, with a one-line
description. Output names are shown for the functions that return more
than one array.

## Cycle Indicators

| function | description | outputs |
| --- | --- | --- |
| `HT_DCPERIOD` | Hilbert Transform - Dominant Cycle Period |  |
| `HT_DCPHASE` | Hilbert Transform - Dominant Cycle Phase |  |
| `HT_PHASOR` | Hilbert Transform - Phasor Components | inphase, quadrature |
| `HT_SINE` | Hilbert Transform - SineWave | sine, leadsine |
| `HT_TRENDMODE` | Hilbert Transform - Trend vs Cycle Mode |  |

## Math Operators

| function | description | outputs |
| --- | --- | --- |
| `ADD` | Vector Arithmetic Add |  |
| `CUMSUM` | Cumulative Sum |  |
| `DIV` | Vector Arithmetic Div |  |
| `MAX` | Highest value over a specified period |  |
| `MAXINDEX` | Index of highest value over a specified period |  |
| `MIN` | Lowest value over a specified period |  |
| `MININDEX` | Index of lowest value over a specified period |  |
| `MINMAX` | Lowest and highest values over a specified period | min, max |
| `MINMAXINDEX` | Indexes of lowest and highest values over a specified period | minidx, maxidx |
| `MULT` | Vector Arithmetic Mult |  |
| `SUB` | Vector Arithmetic Subtraction |  |
| `SUM` | Summation |  |

## Math Transform

| function | description | outputs |
| --- | --- | --- |
| `ACOS` | Vector Trigonometric ACos |  |
| `ASIN` | Vector Trigonometric ASin |  |
| `ATAN` | Vector Trigonometric ATan |  |
| `CEIL` | Vector Ceil |  |
| `COS` | Vector Trigonometric Cos |  |
| `COSH` | Vector Trigonometric Cosh |  |
| `EXP` | Vector Arithmetic Exp |  |
| `FLOOR` | Vector Floor |  |
| `LN` | Vector Log Natural |  |
| `LOG10` | Vector Log10 |  |
| `SIN` | Vector Trigonometric Sin |  |
| `SINH` | Vector Trigonometric Sinh |  |
| `SQRT` | Vector Square Root |  |
| `TAN` | Vector Trigonometric Tan |  |
| `TANH` | Vector Trigonometric Tanh |  |

## Momentum Indicators

| function | description | outputs |
| --- | --- | --- |
| `AC` | Accelerator/Decelerator Oscillator |  |
| `ADX` | Average Directional Movement Index |  |
| `ADXR` | Average Directional Movement Index Rating |  |
| `AO` | Awesome Oscillator |  |
| `APO` | Absolute Price Oscillator |  |
| `AROON` | Aroon | aroondown, aroonup |
| `AROONOSC` | Aroon Oscillator |  |
| `BOP` | Balance Of Power |  |
| `CCI` | Commodity Channel Index |  |
| `CMO` | Chande Momentum Oscillator |  |
| `CMOU` | Chande Momentum Oscillator (Unsmoothed) |  |
| `COPPOCK` | Coppock Curve |  |
| `DPO` | Detrended Price Oscillator |  |
| `DX` | Directional Movement Index |  |
| `ER` | Kaufman Efficiency Ratio |  |
| `ERI` | Elder Ray Index (Bull Power / Bear Power) | bullpower, bearpower |
| `FOSC` | Forecast Oscillator |  |
| `FRACTAL` | Williams Fractal | swinghigh, swinglow |
| `IMI` | Intraday Momentum Index |  |
| `KDJ` | KDJ Stochastic | k, d, j |
| `MACD` | Moving Average Convergence/Divergence | macd, macdsignal, macdhist |
| `MACDEXT` | MACD with controllable MA type | macd, macdsignal, macdhist |
| `MACDFIX` | Moving Average Convergence/Divergence Fix 12/26 | macd, macdsignal, macdhist |
| `MFI` | Money Flow Index |  |
| `MINUS_DI` | Minus Directional Indicator |  |
| `MINUS_DM` | Minus Directional Movement |  |
| `MOM` | Momentum |  |
| `PLUS_DI` | Plus Directional Indicator |  |
| `PLUS_DM` | Plus Directional Movement |  |
| `PPO` | Percentage Price Oscillator |  |
| `QSTICK` | Qstick |  |
| `ROC` | Rate of change : ((price/prevPrice)-1)*100 |  |
| `ROCP` | Rate of change Percentage: (price-prevPrice)/prevPrice |  |
| `ROCR` | Rate of change ratio: (price/prevPrice) |  |
| `ROCR100` | Rate of change ratio 100 scale: (price/prevPrice)*100 |  |
| `RSI` | Relative Strength Index |  |
| `SMI` | Stochastic Momentum Index | smi, smisignal |
| `STOCH` | Stochastic | slowk, slowd |
| `STOCHF` | Stochastic Fast | fastk, fastd |
| `STOCHRSI` | Stochastic Relative Strength Index | fastk, fastd |
| `TRIX` | 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA |  |
| `TSI` | True Strength Index |  |
| `ULTOSC` | Ultimate Oscillator |  |
| `VHF` | Vertical Horizontal Filter |  |
| `VORTEX` | Vortex Indicator | plusvi, minusvi |
| `WAD` | Williams' Accumulation/Distribution |  |
| `WILLR` | Williams' %R |  |

## Overlap Studies

| function | description | outputs |
| --- | --- | --- |
| `ACCBANDS` | Acceleration Bands | upperband, middleband, lowerband |
| `BBANDS` | Bollinger Bands | upperband, middleband, lowerband |
| `DEMA` | Double Exponential Moving Average |  |
| `DONCHIAN` | Donchian Channels | upperband, middleband, lowerband |
| `EMA` | Exponential Moving Average |  |
| `HMA` | Hull Moving Average |  |
| `HT_TRENDLINE` | Hilbert Transform - Instantaneous Trendline |  |
| `KAMA` | Kaufman Adaptive Moving Average |  |
| `KC` | Keltner Channels | upperband, middleband, lowerband |
| `MA` | Moving average |  |
| `MAMA` | MESA Adaptive Moving Average | mama, fama |
| `MAVP` | Moving average with variable period |  |
| `MIDPOINT` | MidPoint over period |  |
| `MIDPRICE` | Midpoint Price over period |  |
| `RMA` | Wilder's Smoothed Moving Average |  |
| `SAR` | Parabolic SAR |  |
| `SAREXT` | Parabolic SAR - Extended |  |
| `SMA` | Simple Moving Average |  |
| `SUPERTREND` | SuperTrend | supertrend, trend |
| `T3` | Triple Exponential Moving Average (T3) |  |
| `TEMA` | Triple Exponential Moving Average |  |
| `TRIMA` | Triangular Moving Average |  |
| `VWMA` | Volume Weighted Moving Average |  |
| `WMA` | Weighted Moving Average |  |
| `ZLEMA` | Zero-Lag Exponential Moving Average |  |

## Pattern Recognition

| function | description | outputs |
| --- | --- | --- |
| `CDL2CROWS` | Two Crows |  |
| `CDL3BLACKCROWS` | Three Black Crows |  |
| `CDL3INSIDE` | Three Inside Up/Down |  |
| `CDL3LINESTRIKE` | Three-Line Strike |  |
| `CDL3OUTSIDE` | Three Outside Up/Down |  |
| `CDL3STARSINSOUTH` | Three Stars In The South |  |
| `CDL3WHITESOLDIERS` | Three Advancing White Soldiers |  |
| `CDLABANDONEDBABY` | Abandoned Baby |  |
| `CDLADVANCEBLOCK` | Advance Block |  |
| `CDLBELTHOLD` | Belt-hold |  |
| `CDLBREAKAWAY` | Breakaway |  |
| `CDLCLOSINGMARUBOZU` | Closing Marubozu |  |
| `CDLCONCEALBABYSWALL` | Concealing Baby Swallow |  |
| `CDLCOUNTERATTACK` | Counterattack |  |
| `CDLDARKCLOUDCOVER` | Dark Cloud Cover |  |
| `CDLDOJI` | Doji |  |
| `CDLDOJISTAR` | Doji Star |  |
| `CDLDRAGONFLYDOJI` | Dragonfly Doji |  |
| `CDLENGULFING` | Engulfing Pattern |  |
| `CDLEVENINGDOJISTAR` | Evening Doji Star |  |
| `CDLEVENINGSTAR` | Evening Star |  |
| `CDLGAPSIDESIDEWHITE` | Up/Down-gap side-by-side white lines |  |
| `CDLGRAVESTONEDOJI` | Gravestone Doji |  |
| `CDLHAMMER` | Hammer |  |
| `CDLHANGINGMAN` | Hanging Man |  |
| `CDLHARAMI` | Harami Pattern |  |
| `CDLHARAMICROSS` | Harami Cross Pattern |  |
| `CDLHIGHWAVE` | High-Wave Candle |  |
| `CDLHIKKAKE` | Hikkake Pattern |  |
| `CDLHIKKAKEMOD` | Modified Hikkake Pattern |  |
| `CDLHOMINGPIGEON` | Homing Pigeon |  |
| `CDLIDENTICAL3CROWS` | Identical Three Crows |  |
| `CDLINNECK` | In-Neck Pattern |  |
| `CDLINVERTEDHAMMER` | Inverted Hammer |  |
| `CDLKICKING` | Kicking |  |
| `CDLKICKINGBYLENGTH` | Kicking - bull/bear determined by the longer marubozu |  |
| `CDLLADDERBOTTOM` | Ladder Bottom |  |
| `CDLLONGLEGGEDDOJI` | Long Legged Doji |  |
| `CDLLONGLINE` | Long Line Candle |  |
| `CDLMARUBOZU` | Marubozu |  |
| `CDLMATCHINGLOW` | Matching Low |  |
| `CDLMATHOLD` | Mat Hold |  |
| `CDLMORNINGDOJISTAR` | Morning Doji Star |  |
| `CDLMORNINGSTAR` | Morning Star |  |
| `CDLONNECK` | On-Neck Pattern |  |
| `CDLPIERCING` | Piercing Pattern |  |
| `CDLRICKSHAWMAN` | Rickshaw Man |  |
| `CDLRISEFALL3METHODS` | Rising/Falling Three Methods |  |
| `CDLSEPARATINGLINES` | Separating Lines |  |
| `CDLSHOOTINGSTAR` | Shooting Star |  |
| `CDLSHORTLINE` | Short Line Candle |  |
| `CDLSPINNINGTOP` | Spinning Top |  |
| `CDLSTALLEDPATTERN` | Stalled Pattern |  |
| `CDLSTICKSANDWICH` | Stick Sandwich |  |
| `CDLTAKURI` | Takuri (Dragonfly Doji with very long lower shadow) |  |
| `CDLTASUKIGAP` | Tasuki Gap |  |
| `CDLTHRUSTING` | Thrusting Pattern |  |
| `CDLTRISTAR` | Tristar Pattern |  |
| `CDLUNIQUE3RIVER` | Unique 3 River |  |
| `CDLUPSIDEGAP2CROWS` | Upside Gap Two Crows |  |
| `CDLXSIDEGAP3METHODS` | Upside/Downside Gap Three Methods |  |

## Price Transform

| function | description | outputs |
| --- | --- | --- |
| `AVGDEV` | Average Deviation |  |
| `AVGPRICE` | Average Price |  |
| `HA` | Heikin-Ashi Candles | haopen, hahigh, halow, haclose |
| `MEDPRICE` | Median Price |  |
| `TYPPRICE` | Typical Price |  |
| `WCLPRICE` | Weighted Close Price |  |

## Statistic Functions

| function | description | outputs |
| --- | --- | --- |
| `BETA` | Beta |  |
| `CORREL` | Pearson's Correlation Coefficient (r) |  |
| `LINEARREG` | Linear Regression |  |
| `LINEARREG_ANGLE` | Linear Regression Angle |  |
| `LINEARREG_INTERCEPT` | Linear Regression Intercept |  |
| `LINEARREG_SLOPE` | Linear Regression Slope |  |
| `PERCENTILE` | Percentile (nearest rank) |  |
| `PERCENTRANK` | Percent Rank |  |
| `STDDEV` | Standard Deviation |  |
| `TSF` | Time Series Forecast |  |
| `VAR` | Variance |  |

## Volatility Indicators

| function | description | outputs |
| --- | --- | --- |
| `ADR` | Average Day Range |  |
| `ATR` | Average True Range |  |
| `CVI` | Chaikin's Volatility |  |
| `MASSI` | Mass Index |  |
| `NATR` | Normalized Average True Range |  |
| `RVI` | Relative Volatility Index |  |
| `TRANGE` | True Range |  |

## Volume Indicators

| function | description | outputs |
| --- | --- | --- |
| `AD` | Chaikin A/D Line |  |
| `ADOSC` | Chaikin A/D Oscillator |  |
| `CMF` | Chaikin Money Flow |  |
| `EFI` | Elder's Force Index |  |
| `MARKETFI` | Market Facilitation Index |  |
| `NVI` | Negative Volume Index |  |
| `OBV` | On Balance Volume |  |
| `PVI` | Positive Volume Index |  |
| `PVO` | Percentage Volume Oscillator |  |
| `PVT` | Price Volume Trend |  |
| `RVOL` | Relative Volume |  |
| `VWAP` | Volume Weighted Average Price |  |

