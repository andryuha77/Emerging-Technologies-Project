# adpted from: hhttps://www.tensorflow.org/get_started/mnist/pros
# adpted from: https://github.com/sugyan/tensorflow-mnist/blob/master/mnist/convolutional.py

import os
import model
import tensorflow as tf

# download and read MNIST data
from tensorflow.examples.tutorials.mnist import input_data
# read from data folder
data = input_data.read_data_sets("/tmp/data/", one_hot=True)

# model
with tf.variable_scope("convolutional"):
    #placeholder to input any number of MNIST images, 
    #each flattened into a 784-dimensional vector
    x = tf.placeholder(tf.float32, [None, 784])
    keep_prob = tf.placeholder(tf.float32)
    y, variables = model.convolutional(x, keep_prob)

# Training
# add a new placeholder to input the correct answers
y_ = tf.placeholder(tf.float32, [None, 10])

# implementing the cross-entropy function −∑y′log⁡(y)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# minimize cross_entropy using the gradient descent algorithm with a learning rate of 0.1
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver(variables)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(20000):
        batch = data.train.next_batch(50)
        if i % 100 == 0:
            train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %g" % (i, train_accuracy))
        sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

    print(sess.run(accuracy, feed_dict={x: data.test.images, y_: data.test.labels, keep_prob: 1.0}))

    path = saver.save(
        sess, os.path.join(os.path.dirname(__file__), 'data', 'convolutional.ckpt'),
        write_meta_graph=False, write_state=False)
    print("Saved:", path)
