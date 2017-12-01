#adapted from: https://www.tensorflow.org/get_started/mnist/pros
#adapted from: https://github.com/sugyan/tensorflow-mnist/blob/master/m

#To use TensorFlow, first we need to import it.
import tensorflow as tf


# Softmax Regression Model
def regression(x):
    # pass the initial value for each parameter in the call to tf.Variable
    W = tf.Variable(tf.zeros([784, 10]), name="W")
    b = tf.Variable(tf.zeros([10]), name="b")
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    return y, [W, b]


# Multilayer Convolutional Network
def convolutional(x, keep_prob):
    # stride of one and are zero padded so that the output is the same size as the input
    def conv2d(x, W):
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
    # max pooling over 2x2 blocks
    def max_pool_2x2(x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # Weight Initialization
    # initialize weights with a small amount of noise for symmetry breaking
    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(shape):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    # First Convolutional Layer
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    # convolution will compute 32 features for each 5x5 patch
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    # convolve x_image with the weight tensor, add the bias, apply the ReLU function
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    # The max_pool_2x2 method will reduce the image size to 14x14
    h_pool1 = max_pool_2x2(h_conv1)

    # Second layer will have 64 features for each 5x5 patch
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    # The max_pool_2x2 method will reduce the image size to 14x14
    h_pool2 = max_pool_2x2(h_conv2)

    # Densely Connected Layer
    # image size has been reduced to 7x7,
    # add a fully-connected layer with 1024 neurons to allow processing on the entire image
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    # reshape the tensor from the pooling layer into a batch of vectors,
    # multiply by a weight matrix,
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    # add a bias, and apply a ReLU
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # Dropout 
    # tf.nn.dropout automatically handles scaling neuron outputs in addition to masking them
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    # Readout Layer
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    y = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
    return y, [W_conv1, b_conv1, W_conv2, b_conv2, W_fc1, b_fc1, W_fc2, b_fc2]
