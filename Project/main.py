import matplotlib.pyplot as plt
import numpy as np
import sys
import datetime

from deepstocks.common_configs import RNNConfig, Stock_names, Features
from lstm_train import train_rnn
from lstm_test import test_model
from lstm_predict import predict
from deepstocks.visualize import plot_predictions
from deepstocks.data_loader import get_csv_data
from deepstocks.preprocess import normalize, prepare_data


def train_test_predict(config, stock_names, features, isTrain):
    # load data based on symbol
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime(2015, 1, 1)

    df = get_csv_data(stock_names.to_symbol[config.stock_name], start_date, end_date, config.window)

    # normalize and prepare data
    df_stock = df.copy()
    df_stock_norm = df_stock.copy()
    df_stock_norm = normalize(df_stock_norm, features.to_use, features.rol, config.window)
    # x_train, y_train, x_valid, y_valid, x_test, y_test = prepare_data(df_stock_norm, config.seq_len, config.valid_ratio, config.test_ratio)
    data = prepare_data(df_stock_norm, config.seq_len, config.valid_ratio, config.test_ratio)

    if isTrain:
        train_rnn(config, features, data)
        test_model(data[4], data[5], config)

    data.append(predict(config, data[0]))
    data.append(predict(config, data[4]))
    data.append(predict(config, data[2]))

    _, axes = plt.subplots(nrows=1, ncols=2)
    plot_predictions(axes, data, config.stock_name)
    plt.show()
    plt.tight_layout()

if __name__ == '__main__':
    import os
    import shutil
    # Turn off TensorFlow warning messages in program output
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    stock_name = sys.argv[1]
    isTrain = 'True' == sys.argv[2]
    print(isTrain)

    # set the configs for model
    # gru, basic, lstm
    config = RNNConfig(stock_name, 'gru')
    # remove old tensorboard logs
    if os.path.isdir(config.log_path):
        shutil.rmtree(config.log_path)
    stock_names = Stock_names()
    features = Features()

    train_test_predict(config, stock_names, features, isTrain)