from sklearn.preprocessing import MinMaxScaler
import numpy as np


def normalize(df, usecols, rol, window):
    '''Normalize the values ina given dataframe removes nan window from the df'''
    scalar = MinMaxScaler()
    for col in df.columns.values:
        if col not in usecols:
            df = df.drop([col], 1)

    for col in df.columns.values:
        if col == rol:
            df.iloc[window:][rol] = scalar.fit_transform(
                df.iloc[window:][col].values.reshape(-1, 1))
        else:
            df[col] = scalar.fit_transform(df[col].values.reshape(-1, 1))
    return df.iloc[window:]


def prepare_data(df, seq_len, valid_ratio, test_ratio):
    # convert to numpy array
    data_raw = df.as_matrix()
    data = []

    for index in range(len(data_raw) - seq_len):
        data.append(data_raw[index: index + seq_len])

    data = np.array(data)
    valid_set_size = int(np.round(valid_ratio/100*data.shape[0]))
    test_set_size = int(np.round(test_ratio/100*data.shape[0]))
    train_set_size = data.shape[0] - (valid_set_size + test_set_size)

    x_train = data[:train_set_size, :-1, :]
    y_train = data[:train_set_size, -1, :]

    x_valid = data[train_set_size:train_set_size+valid_set_size, :-1, :]
    y_valid = data[train_set_size:train_set_size+valid_set_size, -1, :]

    x_test = data[train_set_size+valid_set_size:, :-1, :]
    y_test = data[train_set_size+valid_set_size:, -1, :]

    return [x_train, y_train, x_valid, y_valid, x_test, y_test]
