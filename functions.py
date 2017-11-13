__author__ = 'Artgor'
from codecs import open
import os
import uuid
import boto3
from boto.s3.key import Key
from boto.s3.connection import S3Connection


class Model(object):
	def __init__(self):
		#self.model = joblib.load()
		self.nothing = 0

	def save_image(self, drawn_digit, image):
		filename = 'digit' + str(drawn_digit) + '__' + str(uuid.uuid1()) + '.BMP'
		with open('tmp/' + filename, 'wb') as f:
			f.write(image)
			
		print('Image written')
		


		return ('Image saved successfully with the name {0}'.format(filename))
