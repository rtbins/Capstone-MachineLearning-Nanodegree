import tensorflow as tf

def predict(config, x):
    """Test the saved model against the test dataset"""

    n_steps = config.n_steps
    save_model_path = config.save_model_path
    loaded_graph = tf.Graph()

    with tf.Session(graph=loaded_graph) as sess:
        # Load model
        loader = tf.train.import_meta_graph(save_model_path + '.meta')
        loader.restore(sess, save_model_path)

        # Get Tensors from loaded model
        loaded_x = loaded_graph.get_tensor_by_name('inputs/x:0')
        loaded_keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')
        loaded_logits = loaded_graph.get_tensor_by_name('logits/logits:0')
        
        
        _logits = loaded_logits[:,n_steps-1,:]

        predictions = sess.run(
            _logits,
            feed_dict={loaded_x: x, loaded_keep_prob: 1.0})
        return predictions