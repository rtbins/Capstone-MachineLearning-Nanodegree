import datetime
import tensorflow as tf

import deepstocks.utility as utils
from deepstocks.data_loader import get_next_batch

def train_rnn(config, features, data):

    # create train, test, valid data
    x_train, y_train, x_valid, y_valid = data[0], data[1], data[2], data[3]


    n_steps = config.seq_len-1 
    n_inputs = config.n_inputs
    n_neurons = config.n_neurons
    n_outputs = config.n_outputs
    n_layers = config.n_layers
    learning_rate = config.learning_rate
    batch_size = config.batch_size
    n_epochs = config.n_epochs
    save_model_path = config.save_model_path + '__' + config.stock_name

    train_set_size = x_train.shape[0]

    tf.reset_default_graph()

    X = utils.neural_net_feature_input([n_steps, n_inputs])

    y = utils.neural_net_label_input(n_outputs)

    keep_prob = utils.neural_net_keep_prob_input()

    # define cells

    multi_layer_cell = utils.get_init_cell(n_neurons, n_layers, keep_prob)

    outputs = utils.build_nn(multi_layer_cell, n_neurons, X, n_outputs, n_steps)
                                                
    loss = tf.reduce_mean(tf.square(outputs - y), name='accuracy') # loss function = mean squared error 

    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
                                                
    # run graph
    with tf.Session() as sess: 
        # initialize the value of the graph with default values
        sess.run(tf.global_variables_initializer())
        
        iterations = int(n_epochs*train_set_size/batch_size)
        
        iteration = 0
        
        for _x, _y in get_next_batch(batch_size, x_train, y_train, iterations):
            
            x_batch, y_batch =  _x, _y# fetch the next training batch
            # create a dict to feed into graph
            feed_dict = {X: x_batch, y:y_batch, keep_prob: 1}
            # training the data using AdamOptimizer function
            utils.train_neural_network(sess, optimizer, feed_dict)
            
            
            if iteration % int(5*train_set_size/batch_size) == 0:
                
                mse_train = loss.eval(feed_dict={X: x_train, y: y_train, keep_prob: 0.8}) 
                
                mse_valid = loss.eval(feed_dict={X: x_valid, y: y_valid, keep_prob: 0.8}) 
                
                print('Epochs : %d,  Mean square error train/valid = %.6f/%.6f'%(
                    iteration*batch_size/train_set_size + 5, mse_train, mse_valid))
                
            iteration += 1
        
        saver = tf.train.Saver()
        
        save_path = saver.save(sess, save_model_path)


