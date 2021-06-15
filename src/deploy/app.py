import numpy as np
from .utils import predict, predict_sp_500

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/predict-all')
def predict_all():
    stock_to_prediction = predict_sp_500()
    return ' --- '.join(map(
        lambda item: f'Stock: {item[0]} | Prediction: {item[1]}',
        stock_to_prediction.items()
    ))


@app.route('/predict/<string:stock>')
def predict_stock(stock):
    return f'Stock: {stock} | Prediction: {predict(stock)}'
