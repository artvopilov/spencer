# AlgorithmicTrading

## APIs

#### Intrinio
- over 300 feeds
- pay for only the data you want and choose a pricing tier to fit your specific needs
- they also cater exceptionally to developers and students
- 30-day trial - 100 calls/second

#### Alpha Vantage - My Choice
- free
- 5 requests per minute
- $19.99/month for 15 requests per minute, $249.99/month for 600 requests per minute.
- up to 20 years of historical data
- [API](https://www.alphavantage.co/documentation/)
- [Python library for API](https://github.com/RomelTorres/alpha_vantage/blob/develop/alpha_vantage/techindicators.py)

#### Quandl
- subscribe to the feeds you want
- 300 calls per 10 seconds, 2,000 calls per 10 minutes, and 50,000 calls per day (a free tier)
- $29.00/month for a single developer (720,000 calls per day and more accurate, reliable data)
- does not offer a free trial for their US Stock Prices feed
- a bit harder to read than the key/value structure Intrinio and Alpha Vantage return

#### Xignite
- free trial only lasts 7 days (small number of calls)
- they don’t offer a month-to-month payment option, so you have to commit to a full year of API access

#### IEX
- based out of NYC
- free and doesn’t require users to make an account
- 100 calls per second
- a few years of data 
- only covers IEX :(

## Trading stategies

#### My strategy - Day trading 

* [The complete guide to trading strategies and styles](https://www.ig.com/en/trading-strategies/the-complete-guide-to-trading-strategies-and-styles-190709)
* [Momentum trading strategies: a beginner's guide](https://www.ig.com/en/trading-strategies/momentum-trading-strategies--a-beginners-guide-190905#RSI)

## Technical indicators

1) SMA/EMA/DEMA - Moving avarage
2) MOM - Momentum - https://www.investopedia.com/investing/momentum-and-relative-strength-index/
3) RSI (oversold/overbougth upavg/downavg) - https://www.investopedia.com/articles/active-trading/042114/overbought-or-oversold-use-relative-strength-index-find-out.asp
4) Stochastic oscillator (close,lowestLow,highestHigh) - https://www.fmlabs.com/reference/default.htm?url=StochasticOscillator.htm, https://commodity.com/technical-analysis/stochastics/
5) DEMA - Double Exponential Moving Average (with less lag than a straight exponential moving average) - https://www.fmlabs.com/reference/default.htm?url=DEMA.htm
6) MACD - moving average convergence / divergence (not used) - https://www.fmlabs.com/reference/default.htm?url=MACD.htm
7) ADX - average directional movement index (trend strength) - https://www.fmlabs.com/reference/default.htm?url=ADX.htm
8) CCI - Commodity Channel Index (relation between price and a moving average (MA), or more specifically, normal deviations from that average) - http://www.fmlabs.com/reference/default.htm?url=CCI.htm
9) AROON - periods since highest high/lowest low, AroonUp/AroonDown - https://www.fmlabs.com/reference/default.htm?url=Aroon.htm
10) MFI - money flow index - https://www.fmlabs.com/reference/default.htm?url=MoneyFlowIndex.htm
11) AD -  Chaikin A/D line (AD) - (volume and close/low/high) - https://www.fmlabs.com/reference/default.htm?url=AccumDist.htm
12) OBV - On Balance Volume - a cumulative total of the up and down volume - https://www.fmlabs.com/reference/default.htm?url=OBV.htm

## Articles on stock market forecasting

* [Stock market forecasting using Time Series analysis](https://towardsdatascience.com/stock-market-forecasting-using-time-series-c3d21f2dd37f)
* [Predicting stock prices using deep learning](https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe)
* [Stock Prices Prediction using Deep LearningModels](https://arxiv.org/pdf/1909.12227.pdf)
* [An overview of time series forecasting models](https://towardsdatascience.com/an-overview-of-time-series-forecasting-models-a2fa7a358fcb)
* [Huge Stock Market Dataset - Kaggle](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/kernels)

## Online courses

- https://www.ig.com/en/learn-to-trade/ig-academy/the-basics-of-technical-analysis
- https://www.quantopian.com/lectures/statistical-moments#notebook


