import pandas as pd
import numpy as np
import os


def symbol_to_path(symbol, base_dir="data"):
    '''
        declares the base directory inside which data resides
    '''
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_rolling_mean(values, window):
    '''
        outputs rolling mean for a given series and window size
    '''
    return pd.Series.rolling(values, window=window).mean()


def get_csv_data(symbol, start_date, end_date, window=10):
    '''
    input: symbol of a stock, 
           and date range for which we need data
    output: a dataframe having 'Adj Close', 'Volume' and 'Rolling Mean'
            attributes of a stock
    '''

    dates = pd.date_range( start_date, end_date)

    df = pd.DataFrame(index=dates)

    df_temp = pd.read_csv(symbol_to_path(symbol),
                          index_col='Date',
                          parse_dates=True,
                          usecols=['Date', 'Adj Close', 'Volume'],
                          na_values=['nan'])

    df = df.join(df_temp, how='inner')

    df = df.dropna(subset=["Adj Close"])

    #df['Adj Close'] = df['Adj Close']/df.iloc[0]['Adj Close']
    df['Volume'] = df['Volume']/df.iloc[0]['Volume']

    rm = get_rolling_mean(df['Adj Close'], window)
    df.loc[0:window, 'Rolling mean'] = None
    df.loc[window:, 'Rolling mean'] = rm
    return df



def get_next_batch(batch_size, x, y, counts):
    index_in_epoch = 0
    perm_array = np.arange(x.shape[0])
    np.random.shuffle(perm_array)
   
    for i in range(counts):
        start = index_in_epoch
        index_in_epoch += batch_size

        if index_in_epoch > x.shape[0]:
            np.random.shuffle(perm_array) # shuffle permutation array
            start = 0 # start next epoch
            index_in_epoch = batch_size

        end = index_in_epoch
        yield x[perm_array[start:end]], y[perm_array[start:end]]
