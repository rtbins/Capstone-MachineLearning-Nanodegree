"""author: rtbins"""
"""common functions used to construct graphs"""
import tensorflow as tf
import os


# helper functions for utils
def _cell(_size, keep_prob, type='lstm'):
    """
    Below functions represents different kind of cells which can be used in nn: Lstm, basic RNN, GRU
    We are going to train over them, and find the best suited     architecture for the problem statement
    """
    if type == 'basic':
        cell = tf.contrib.rnn.BasicLSTMCell(
            _size, activation=tf.nn.leaky_relu)
    elif type == 'gru':
        cell = tf.contrib.rnn.GRUCell(
            _size, activation=tf.nn.leaky_relu)
    else:
        cell = tf.contrib.rnn.LSTMCell(
            _size, activation=tf.nn.leaky_relu, use_peepholes=True)

    if keep_prob is not None:
        cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)
    return cell


def _build_rnn(cell, inputs):
    """Creates a recurrent neural network specified by RNNCell cell
    :param cell: RNN Cell
    :param inputs: Input
    :return: Tuple (Outputs, Final State)
    """
    with tf.name_scope("RNN_forward"):
        output, final_state = tf.nn.dynamic_rnn(
            cell=cell, dtype=tf.float32, inputs=inputs)
    # final_state = tf.identity(input= final_state)
    return output, final_state


# util functions
def get_init_cell(rnn_size, n_layers, keep_prob, type='lstm'):
    """Create an RNN Cell and initialize it.
    :param rnn_size: Size of RNNs
    :return: Tuple (cell, initialize state)
    """
    with tf.variable_scope('RNN_cells'):
        cell = [_cell(rnn_size, keep_prob, type)
                for layer in range(n_layers)]
        cell = tf.contrib.rnn.MultiRNNCell(cell)
    return cell


def build_nn(cell, rnn_size, inputs, num_output, n_steps):
    """Build part of the neural network"""
    rnn_outputs, _ = _build_rnn(cell, inputs)

    with tf.name_scope('sequence_reshape'):
        stacked_rnn_outputs = tf.reshape(rnn_outputs, [-1, rnn_size])

    with tf.name_scope('logits'):
        stacked_outputs = tf.layers.dense(stacked_rnn_outputs, num_output)
        logits = tf.reshape(
            stacked_outputs, [-1, n_steps, num_output], name='logits')
        # keep only last output of sequence

    with tf.name_scope('predictions'):
        logits = logits[:, n_steps-1, :]
    return logits


def train_neural_network(session, optimizer, feed_dict):
    """
    Optimize the session on a batch of data
    : session: Current TensorFlow session
    : optimizer: TensorFlow optimizer function
    : keep_probability: keep probability
    """
    session.run(optimizer, feed_dict=feed_dict)


# model placeholders

def neural_net_feature_input(feature_shape, name='x'):
    """Return a Tensor for a batch of feature input"""
    return tf.placeholder(dtype=tf.float32, shape=[None, feature_shape[0], feature_shape[1]], name=name)


def neural_net_label_input(n_classes, name='y'):
    """Return a Tensor for a batch of label input"""
    return tf.placeholder(dtype=tf.float32, shape=[None, n_classes], name=name)


def neural_net_keep_prob_input(name='keep_prob'):
    """Return a Tensor for keep probability"""
    return tf.placeholder(dtype=tf.float32, name=name)

