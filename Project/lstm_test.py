import tensorflow as tf


def test_model(x, y, config):
    """Test the saved model against the test dataset"""

    save_model_path = config.save_model_path

    n_samples = 4
    #test_features, test_labels = pickle.load(open(save_model_path, mode='rb'))
    loaded_graph = tf.Graph()

    with tf.Session(graph=loaded_graph) as sess:
        # Load model
        loader = tf.train.import_meta_graph(save_model_path + '.meta')
        loader.restore(sess, save_model_path)
        # Get Tensors from loaded model
        with tf.name_scope('inputs'):
            loaded_x = loaded_graph.get_tensor_by_name('inputs/x:0')
        loaded_y = loaded_graph.get_tensor_by_name('targets/y:0')
        loaded_keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')
        loaded_acc = loaded_graph.get_tensor_by_name('cost/loss:0')

        # TODO: implement accuracy in batches for memory limitations
        # test_batch_acc_total = 0
        test_batch_count = n_samples

        test_batch_acc = sess.run(
            loaded_acc,
            feed_dict={loaded_x: x, loaded_y: y, loaded_keep_prob: 1.0})
        test_batch_count += 1
        print('Testing Accuracy: {} %\n'.format(
            (1 - test_batch_acc/test_batch_count)*100))


if __name__ == '__main__':

    from deepstocks.common_configs import RNNConfig, Stock_names, Features

    stock_name = 'apple'
    config = RNNConfig(stock_name)

    x = []
    y = []

    test_model(x, y, config)
