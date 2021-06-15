import os
from collections import defaultdict

import pandas as pd
import numpy as np
from catboost import CatBoostClassifier


SP_500_PATH = '../../sp_500_symbols.txt'

MODELS_PATH = 'models'
MODEL_NAME = 'model_v5'

MODEL = CatBoostClassifier()
MODEL.load_model(os.path.join(MODELS_PATH, MODEL_NAME))


def predict_sp_500():
    with open('../sp_500_symbols.txt', 'r') as f:
        sp_500_stocks = f.read().split('\n')[:-1]

    stock_to_prediction = defaultdict(float)
    for stock in sp_500_stocks:
        prediction = predict(stock)
        stock_to_prediction[stock] = prediction

    return stock_to_prediction


def predict(stock: str) -> float:
    data = get_fake_data(stock)
    print(data)
    pred = MODEL.predict_proba(data)[0][1]
    return pred


def get_data(stock: str) -> pd.DataFrame:
    pass


def get_fake_data(stock: str) -> pd.DataFrame:
    features = ['sma_9', 'sma_13', 'sma_26', 'mom_1', 'mom_8', 'mom_15', 'rsi_7',
                'rsi_14', 'slowd', 'slowk', 'dema_13', 'dema_26', 'adx_7', 'adx_14',
                'cci_7', 'cci_14', 'aroon_up', 'aroon_down', 'mfi_7', 'mfi_14',
                'chaikin_a/d', 'obv', 'bbands_14_up', 'bbands_14_mid', 'bbands_14_low',
                'bbands_7_mid', 'bbands_7_up', 'bbands_7_low', 'open', 'high', 'low',
                'close', 'volume']
    values = np.random.random(len(features)).tolist()
    df = pd.DataFrame([values], columns=features)

    return df
