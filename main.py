# adapted from : http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
# adapted from : https://github.com/Erlemar/digits_little
# adapted from : https://github.com/sugyan/tensorflow-mnist/blob/master/main.py

# imports
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from mnist import model

# placeholder images x will consist of a 2d tensor of floating point numbers
x = tf.placeholder("float", [None, 784])
#  TensorFlow session that holds the exporting trained model
sess = tf.Session()

# restore trained data
with tf.variable_scope("regression"):
    y1, variables = model.regression(x)

# #Load the stored model   
saver = tf.train.Saver(variables)
# from file in data folder
saver.restore(sess, "mnist/data/regression.ckpt")

# restore trained data
with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.convolutional(x, keep_prob)
# #Load the stored model   
saver = tf.train.Saver(variables)
# from file in data folder
saver.restore(sess, "mnist/data/convolutional.ckpt")

# execute regression model
def regression(input):
    return sess.run(y1, feed_dict={x: input}).flatten().tolist()

# execute convolutional model
def convolutional(input):
    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()


# webapp
app = Flask(__name__)

# Flask  request handler for calling the Tensorflow model
@app.route('/api/mnist', methods=['POST'])
def mnist():
    # prepare the model
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(input)
    output2 = convolutional(input)
    # respond the result as JSON
    return jsonify(results=[output1, output2])

#Flask main reqest to home html page
@app.route('/')
def main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
