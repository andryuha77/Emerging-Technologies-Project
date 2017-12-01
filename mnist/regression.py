# adapted from: https://www.tensorflow.org/get_started/mnist/pros
# adapted from: https://github.com/sugyan/tensorflow-mnist/blob/master/mnist/regression.py

import os
import model
import tensorflow as tf

# download and read MNIST data
from tensorflow.examples.tutorials.mnist import input_data
# read from datafolder
data = input_data.read_data_sets("/tmp/data/", one_hot=True)

# adapted from: https://www.tensorflow.org/get_started/mnist/beginners
# model
with tf.variable_scope("regression"):
    #placeholder to input any number of MNIST images, 
    #each flattened into a 784-dimensional vector
    x = tf.placeholder(tf.float32, [None, 784])
    y, variables = model.regression(x)

# Training
# add a new placeholder to input the correct answers
y_ = tf.placeholder("float", [None, 10])

# implementing the cross-entropy function −∑y′log⁡(y)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# minimize cross_entropy using the gradient descent algorithm with a learning rate of 0.1
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#Evaluating Our Model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver(variables)
with tf.Session() as sess:
    # initial values and assigns them to each Variable
    sess.run(tf.global_variables_initializer())

    #Training the model by running train_step 1000 times
    for _ in range(1000):
        batch_xs, batch_ys = data.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # evaluate our accuracy on the test data
    print(sess.run(accuracy, feed_dict={x: data.test.images, y_: data.test.labels}))

    # save regression to file
    path = saver.save(
        sess, os.path.join(os.path.dirname(__file__), 'data', 'regression.ckpt'),
        write_meta_graph=False, write_state=False)
    print("Saved:", path)
