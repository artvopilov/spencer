import time

from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


def join_dataframes(df1, df2, on, how='inner'):
    return df1.join(df2, on=on, how=how)


def get_technical_indicators_df(ti, stock):
    # Simple Moving Average - 9 days
    sma_9, meta_sma_9 = ti.get_sma(stock, interval='daily', time_period=9)
    sma_9.rename(columns={'SMA': 'sma_9'}, inplace=True)
    # Simple Moving Average - 13 days
    sma_13, meta_sma_13 = ti.get_sma(stock, interval='daily', time_period=13)
    sma_13.rename(columns={'SMA': 'sma_13'}, inplace=True)
    # Simple Moving Average - 26 days
    sma_26, meta_sma_26 = ti.get_sma(stock, interval='daily', time_period=26)
    sma_26.rename(columns={'SMA': 'sma_26'}, inplace=True)
    # Momentum - 1 day
    mom_1, meta_mom_1 = ti.get_mom(stock, interval='daily', time_period=1)
    mom_1.rename(columns={'MOM': 'mom_1'}, inplace=True)
    # Momentum - 8 day
    mom_8, meta_mom_8 = ti.get_mom(stock, interval='daily', time_period=8)
    mom_8.rename(columns={'MOM': 'mom_8'}, inplace=True)
    time.sleep(61)
    # Momentum - 15 day
    mom_15, meta_mom_15 = ti.get_mom(stock, interval='daily', time_period=15)
    mom_15.rename(columns={'MOM': 'mom_15'}, inplace=True)
    # RSI - 14 day
    rsi_14, meta_rsi_14 = ti.get_rsi(stock, interval='daily', time_period=14)
    rsi_14.rename(columns={'RSI': 'rsi_14'}, inplace=True)
    # RSI - 7 day
    rsi_7, meta_rsi_7 = ti.get_rsi(stock, interval='daily', time_period=7)
    rsi_7.rename(columns={'RSI': 'rsi_7'}, inplace=True)
    # Stochastic oscillator - 14 days faskK, 3 days fastD/slowK, 3 days slowD
    # https://commodity.com/technical-analysis/stochastics/
    # https://www.fmlabs.com/reference/default.htm?url=StochasticOscillator.htm
    stoch_14_3_3, meta_stoch_14_3_3 = ti.get_stoch(stock, interval='daily', fastkperiod=14, slowkperiod=3, 
                                                   slowdperiod=3, slowkmatype=0, slowdmatype=0)
    # Double Exponential Moving Average - 13 days
    dema_13, meta_dema_13 = ti.get_dema(stock, interval='daily', time_period=13)
    dema_13.rename(columns={'DEMA': 'dema_13'}, inplace=True)
    time.sleep(61)
    # Double Exponential Moving Average - 26 days
    dema_26, meta_dema_26 = ti.get_dema(stock, interval='daily', time_period=26)
    dema_26.rename(columns={'DEMA': 'dema_26'}, inplace=True)
    # Average Directional Movement Index (ADX) - 7 days
    adx_7, meta_adx_7 = ti.get_adx(stock, interval='daily', time_period=7)
    adx_7.rename(columns={'ADX': 'adx_7'}, inplace=True)
    # Average Directional Movement Index (ADX) - 14 days
    adx_14, meta_adx_14 = ti.get_adx(stock, interval='daily', time_period=14)
    adx_14.rename(columns={'ADX': 'adx_14'}, inplace=True)
    # Commodity Channel Index (CCI) - 7 days
    cci_7, meta_cci_7 = ti.get_cci(stock, interval='daily', time_period=7)
    cci_7.rename(columns={'CCI': 'cci_7'}, inplace=True)
    # Commodity Channel Index (CCI) - 14 days
    cci_14, meta_cci_14 = ti.get_cci(stock, interval='daily', time_period=14)
    cci_14.rename(columns={'CCI': 'cci_14'}, inplace=True)
    time.sleep(61)
    # Aroon (AROON) values (AroonUp/AroonDown) - 14 days
    aroon_14, meta_aroon_14 = ti.get_aroon(stock, interval='daily', time_period=14)
    # Money Flow Index (MFI) - 7 days
    mfi_7, meta_mfi_7 = ti.get_mfi(stock, interval='daily', time_period=7)
    mfi_7.rename(columns={'MFI': 'mfi_7'}, inplace=True)
    # Money Flow Index (MFI) - 14 days
    mfi_14, meta_mfi_14 = ti.get_mfi(stock, interval='daily', time_period=14)
    mfi_14.rename(columns={'MFI': 'mfi_14'}, inplace=True)
    # Accumulation/Distribution Line / Chaikin A/D (AD)
    ad, meta_ad = ti.get_ad(stock, interval='daily')
    # On Balance Volume (OBV)
    obv, meta_obv = ti.get_obv(stock, interval='daily')
    
    ti_dfs = [sma_9,sma_13, sma_26, mom_1, mom_8, mom_15, rsi_7, rsi_14, stoch_14_3_3, 
              dema_13, dema_26, adx_7, adx_14, cci_7, cci_14, aroon_14, mfi_7, mfi_14, ad, obv]
    
    stock_ti_df = join_dataframes(ti_dfs[0], ti_dfs[1], 'date')
    for ti_df_ind in range(2, len(ti_dfs)):
        stock_ti_df = join_dataframes(stock_ti_df, ti_dfs[ti_df_ind], 'date')

    stock_ti_df.columns = map(lambda c: '_'.join(str.lower(c).split()), stock_ti_df.columns)
    return stock_ti_df


