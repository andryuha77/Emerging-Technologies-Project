# -*- coding: utf-8 -*-
"""
adapted from: https://github.com/visraman26/DigitRecognition/blob/master/digitRecognition.py
"""

from keras.datasets import mnist

from keras.models import Sequential
from keras.layers import Dense 
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import np_utils
from PIL import Image
    
seed=7
np.random.seed(seed)

(x_train,y_train),(x_test,y_test)=mnist.load_data()
#plt.imshow(x_train[0],cmap=plt.get_cmap('gray'))
#print x_train[0]

numPixels=x_train.shape[1]*x_train.shape[2]
#print x_train.shape[0]
x_train=x_train.reshape(x_train.shape[0],numPixels).astype('float32')

x_test=x_test.reshape(x_test.shape[0],numPixels).astype('float32')
#print x_train.shape[0]

x_train=x_train/255
x_test=x_test/255

y_train=np_utils.to_categorical(y_train)

y_test=np_utils.to_categorical(y_test)
num_classes=y_test.shape[1]

def create_model():
    model=Sequential()
    model.add(Dense(numPixels,input_dim=numPixels,init='normal',activation='relu'))
    model.add(Dense(num_classes,init='normal',activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics =['accuracy'] )
    return model
    
model=create_model()
model.fit(x_train,y_train,nb_epoch=10,batch_size=200 , verbose=2)
scores = model.evaluate(x_test, y_test, verbose=0)

model.save('digitRecognitionModel.h5')  # creates a HDF5 file 'my_model.h5'



    
    