import os
import time
import importlib

from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
import tqdm

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

import common
importlib.reload(common)
from common import get_daily_time_series_df, get_technical_indicators_df


def load_training_data(ts, ti, symbols):
    for stock in symbols:
        print('Loading ts for {}'.format(stock))
        stock_ts_df = get_daily_time_series_df(ts, stock)
        stock_ts_df.to_csv('{}/{}_time_series.csv'.format(time_series_dir, stock))
        time.sleep(61)  # API calls frequency restrictions
        print('Loading ti for {}'.format(stock))
        stock_ti_df = get_technical_indicators_df(ti, stock)
        stock_ti_df.to_csv('{}/{}_tech_ind.csv'.format(tech_ind_dir, stock))
        time.sleep(61)  # API calls frequency restrictions


key = '4Q11GLKMBNKWBAXQ'

ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key, output_format='pandas')

if __name__ == '__main__':
    with open('../sp_500_symbols.txt', 'r') as f:
        sp_500_symbols = f.read().split('\n')[:-1]
    
    time_series_dir = '../time_series_data'
    tech_ind_dir = '../tech_ind_data'

    if not os.path.exists(time_series_dir):
        os.mkdir(time_series_dir)
    if not os.path.exists(tech_ind_dir):
        os.mkdir(tech_ind_dir)
        
    load_training_data(ts, ti, sp_500_symbols[84:])
        
        
