from flask_restful import Resource, reqparse
import pandas as pd
import os


data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

class StockData(Resource):

    def get(self, name):
        data = pd.read_csv(os.path.join(data_path, 'AAPL.csv'), usecols=['Date', 'Adj Close', 'Close'], index_col="Date")
        data.rename(columns={'Adj Close': 'AAPL'}, inplace=True)
        return data.to_dict()