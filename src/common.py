import time

import catboost
from catboost import CatBoostClassifier, Pool
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


def join_dataframes(df1, df2, on, how='inner'):
    return df1.join(df2, on=on, how=how)


def get_daily_time_series_df(ts, stock):
    data, meta_data = ts.get_daily(symbol=stock)
    data.rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', 
                         '4. close': 'close', '5. volume': 'volume'}, inplace=True)
    return data


def get_technical_indicators_df(ti, stock, time_sleep=61):
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
    # Bollinger bands (BBANDS) values - 14 days
    bbands_14, meta_bbands_14 = ti.get_bbands(stock, interval='daily', time_period=14)
    bbands_14.rename(columns={'Real Upper Band': 'bbands_14_up'}, inplace=True)
    bbands_14.rename(columns={'Real Lower Band': 'bbands_14_low'}, inplace=True)
    bbands_14.rename(columns={'Real Middle Band': 'bbands_14_mid'}, inplace=True)
    # Bollinger bands (BBANDS) values - 7 days
    bbands_7, meta_bbands_7 = ti.get_bbands(stock, interval='daily', time_period=7)
    bbands_7.rename(columns={'Real Upper Band': 'bbands_7_up'}, inplace=True)
    bbands_7.rename(columns={'Real Lower Band': 'bbands_7_low'}, inplace=True)
    bbands_7.rename(columns={'Real Middle Band': 'bbands_7_mid'}, inplace=True)
    
    ti_dfs = [sma_9, sma_13, sma_26, mom_1, mom_8, mom_15, rsi_7, rsi_14, stoch_14_3_3, dema_13, dema_26, 
              adx_7, adx_14, cci_7, cci_14, aroon_14, mfi_7, mfi_14, ad, obv, bbands_14, bbands_7]
    
    stock_ti_df = join_dataframes(ti_dfs[0], ti_dfs[1], 'date')
    for ti_df_ind in range(2, len(ti_dfs)):
        stock_ti_df = join_dataframes(stock_ti_df, ti_dfs[ti_df_ind], 'date')

    stock_ti_df.columns = map(lambda c: '_'.join(str.lower(c).split()), stock_ti_df.columns)
    return stock_ti_df


def chech_if_should_buy(ti, stock):
    try:
        # Moving Average Convergence Divergence - 9 days
        macd_9, macd_sma_9 = ti.get_macd(stock, interval='daily')
        # RSI - 14 day
        rsi_14, meta_rsi_14 = ti.get_rsi(stock, interval='daily', time_period=14)
        # Accumulation/Distribution Line / Chaikin A/D (AD)
        ad, meta_ad = ti.get_ad(stock, interval='daily')

        stock_ti_df = join_dataframes(macd_9[-2:], rsi_14[-2:], 'date')
        stock_ti_df = join_dataframes(stock_ti_df, ad[-2:], 'date')   
        stock_ti_df.columns = map(lambda c: '_'.join(str.lower(c).split()), stock_ti_df.columns)
        
        print('Stock: {}'.format(stock))
        print(stock_ti_df)
        macd_is_good = stock_ti_df['macd_hist'][-1] > 0 and stock_ti_df['macd_hist'][-2] < 0
        rsi_is_good = stock_ti_df['rsi'][-1] > 30 and stock_ti_df['rsi'][-2] < 30
        ad_is_good = stock_ti_df['chaikin_a/d'][-1] > 0 and stock_ti_df['chaikin_a/d'][-2] < 0

        return stock_ti_df, sum([macd_is_good, rsi_is_good, ad_is_good]) > 0
    except:
        print('Stock: {} - error'.format(stock))  
        return None, False
    

def plot_features_target_correlation(df, df_tag, target_column):
    features_target_corr = df.drop(target_column, axis=1).apply(lambda x: abs(x.corr(df[target_column]))).nlargest(25)
    features_target_corr.sort_values().plot.bar(figsize=(15, 7), grid=True, fontsize=14,
                                                title='Target with features correlation in {}'.format(df_tag))


def plot_learning_curve(model, loss_func='RMSE'):
    evals_learn = model.evals_result_['learn'][loss_func]
    evals_validation = model.evals_result_['validation'][loss_func]
    iterations = list(range(len(evals_learn)))

    df_evals_learn = pd.DataFrame({'iteration': iterations, 'error': evals_learn, 'eval_type': 'learn'})
    df_evals_validation = pd.DataFrame({'iteration': iterations, 'error': evals_validation, 'eval_type': 'validation'})

    df_evals = df_evals_learn.append(df_evals_validation, ignore_index=True)

    sns.relplot(data=df_evals, x='iteration', y='error', hue='eval_type', kind='line')
    
    
def calculate_eval_metrics(trained_model, X, y, eval_metrics):
    pool = Pool(data=X, label=y)
    tree_count = trained_model.tree_count_
    return trained_model.eval_metrics(data=pool, 
                                      metrics=eval_metrics, 
                                      ntree_start=tree_count - 1, 
                                      ntree_end=tree_count)


def get_sorted_factors(trained_model):
    feature_importance_df = pd.DataFrame({'feature_importances': trained_model.feature_importances_, 
                                          'feature_names': trained_model.feature_names_})
    feature_importance_df.sort_values('feature_importances', ascending=False, inplace=True)
    return feature_importance_df['feature_names'].values.tolist()
    
    
def plot_feature_importance(trained_model, model_loss, top=20):
    feature_importance_df = pd.DataFrame()
    feature_importance_df['feature_importances'] = trained_model.feature_importances_
    feature_importance_df['feature_names'] = trained_model.feature_names_
    feature_importance_df = feature_importance_df.nlargest(top, 'feature_importances')
    feature_importance_df.sort_values(by='feature_importances', axis=0, inplace=True)
    feature_importance_df.plot.bar(x='feature_names', y='feature_importances', figsize=(15, 7),
                                   title='Feature importances in {} model'.format(model_loss), 
                                   grid=True, fontsize=14)
    