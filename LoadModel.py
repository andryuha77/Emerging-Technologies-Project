# -*- coding: utf-8 -*-
"""
adapted from: https://github.com/visraman26/DigitRecognition/blob/master/digitRecognitionLoadModel.py
"""

from keras.models import load_model
import numpy as np
from PIL import Image

from keras.models import Sequential
from keras.layers import Dense 

model = load_model('digitRecognitionModel.h5')

originalImage = Image.open('tmp/digit1__b7d8b518-c8bc-11e7-889e-001cc07f8fce.bmp')
reducedImage = originalImage.resize((28,28))
#plt.imshow(reducedImage ,cmap=plt.get_cmap('gray'))
imageArray= np.array(reducedImage)
numPixels=imageArray.shape[0]*imageArray.shape[1]
#data.reshape((50,1104,-1))
imageArray=imageArray.reshape(-1,numPixels).astype('float32')
#####imageArray=imageArray/255 #######not compulsory
predictedValue = model.predict_classes(imageArray)
#predictedClass=np_utils.probas_to_classes(predictedValue)
print("Digit is ",predictedValue)