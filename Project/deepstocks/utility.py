import tensorflow as tf

def lstm_cell(_size, keep_prob):
    cell = tf.contrib.rnn.LSTMCell(_size, 
                                        activation=tf.nn.leaky_relu, 
                                        use_peepholes = True
                                       )
    if keep_prob is not None:
        cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)
    return cell

def basic_rnn_cell(_size, keep_prob=1):
    cell = tf.contrib.rnn.BasicLSTMCell(_size, activation=tf.nn.elu)
    if keep_prob is not None:
        cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)
    return cell

def gru_cell(_size, keep_prob=1):
    cell = tf.contrib.rnn.GRUCell(_size, activation=tf.nn.leaky_relu)
    if keep_prob is not None:
        cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)
    return cell
    
def get_init_cell(rnn_size, n_layers, keep_prob):
    """
    Create an RNN Cell and initialize it.
    :param rnn_size: Size of RNNs
    :return: Tuple (cell, initialize state)
    """
    # TODO: Implement Function
    
    #cell = [basic_rnn_cell(rnn_size, keep_prob) for layer in range(n_layers)]

    cell = [lstm_cell(rnn_size, keep_prob) for layer in range(n_layers)]
    
    cell = tf.contrib.rnn.MultiRNNCell(cell)
    
    return cell

def build_rnn(cell, inputs):
    """
    Create a RNN using a RNN Cell
    :param cell: RNN Cell
    :param inputs: Input text data
    :return: Tuple (Outputs, Final State)
    """
    # TODO: Implement Function
    
    output, final_state = tf.nn.dynamic_rnn(cell=cell, dtype= tf.float32, inputs= inputs)
    
    final_state = tf.identity(input= final_state)
    
    return output, final_state

def build_nn(cell, rnn_size, inputs, num_output, n_steps):
    """
    Build part of the neural network
    """
    rnn_outputs, states = build_rnn(cell, inputs)
    
    stacked_rnn_outputs = tf.reshape(rnn_outputs, [-1, rnn_size]) 
    
    stacked_outputs = tf.layers.dense(stacked_rnn_outputs, num_output)
    
    logits = tf.reshape(stacked_outputs, [-1, n_steps, num_output] , name= 'logits')
    
    # keep only last output of sequence
    logits = logits[:,n_steps-1,:] 

    return logits

def train_neural_network(session, optimizer, feed_dict):
    """
    Optimize the session on a batch of data
    : session: Current TensorFlow session
    : optimizer: TensorFlow optimizer function
    : keep_probability: keep probability
    """
    session.run(optimizer, feed_dict=feed_dict)
    

def neural_net_feature_input(feature_shape):
    """
    Return a Tensor for a batch of feature input
    : feature_shape: Shape of the featurs
    : return: Tensor for feature input.
    """
    return tf.placeholder(dtype=tf.float32, shape=[None, feature_shape[0], feature_shape[1]], name='x')


# PLACEHOLDERS

def neural_net_label_input(n_classes):
    """
    Return a Tensor for a batch of label input
    : n_classes: Number of classes
    : return: Tensor for label input.
    """
    # TODO: Implement Function
    return tf.placeholder(dtype=tf.float32, shape=[None, n_classes], name='y')


def neural_net_keep_prob_input():
    """
    Return a Tensor for keep probability
    : return: Tensor for keep probability.
    """
    # TODO: Implement Function
    return tf.placeholder(dtype=tf.float32, name='keep_prob')
