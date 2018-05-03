import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_rolling_mean(values, window):
    return pd.Series.rolling(values, window=window).mean()

def get_data(symbol, dates):
    df = pd.DataFrame(index=dates)

    df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date', 'Adj Close', 'Volume'],
                              na_values=['nan'])
   
    df = df.join(df_temp)
    df = df.dropna(subset=["Adj Close"])

    df['Adj Close'] = df['Adj Close']/df.iloc[0]['Adj Close']
    df['Volume'] = df['Volume']/df.iloc[0]['Volume']

    rm = get_rolling_mean(df['Adj Close'], window=20)
    df.loc[0:20, 'Rolling mean'] = None
    df.loc[20:, 'Rolling mean'] = rm
    return df

