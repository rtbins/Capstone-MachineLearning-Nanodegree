
class RNNConfig():
    n_inputs = 2
    n_neurons = 200
    n_outputs = 2
    n_layers = 3
    learning_rate = 0.002
    batch_size = 50
    # epoch count represent a full training paa within the loop
    n_epochs = 100
    window = 10
    valid_ratio = 15
    test_ratio = 15
    seq_len = 20
    n_steps = seq_len - 1
    save_model_path = './checkpoints/forecast_model'


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
