import os


file_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


class RNNConfig:
    def __init__(self, stock_name, cell='lstm'):
        self.stock_name = stock_name
        # represents number of features being passed to model
        self.n_inputs = 2
        self.n_neurons = 156
        self.n_outputs = 2
        self.n_layers = 2
        self.learning_rate = 0.0008
        self.batch_size = 64
        # epoch count represent a full training pass within the loop
        self.n_epochs = 64
        # window to preprocess the data
        self.window = 10
        self.valid_ratio = 15
        self.test_ratio = 15
        # is the size of the batch
        self.seq_len = 20
        self.n_steps = self.seq_len - 1
        # gru, basic, lstm
        self.rnn_type = cell
        # path locations
        self.log_path = os.path.join(file_dir, ('logs/' + cell))
        self.log_path_test = os.path.join(self.log_path, 'train')
        self.log_path_train = os.path.join(self.log_path, 'test')
        self.save_model_path = os.path.join(
            file_dir, ('checkpoints/' + cell + '/forecast_model' + '__' + self.stock_name))


class Stock_names:
    to_symbol = {
        'apple': 'AAPL',
        'amazon': 'AMZN',
        'google': 'GOOG',
        'spy': 'SPY'
    }


class Features:
    adj = 'Adj Close'
    vol = 'Volume'
    rol = 'Rolling mean'
    to_use = [adj, rol]
