#! /usr/bin/env python
# -*- coding: utf-8 -*-


import math
import rospy
import sys
import time
import numpy as np
import copy
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from cam_tracker.srv import *
from cam_tracker.msg import *


class Localize:
	def __init__(self):
		

		#SUB
		self.sub_pantilts = rospy.Subscriber('/pan_tilts', PanTilts, self.pantilts_to_positions)

		#PUB
		self.pub_arenas = rospy.Publisher('/arena_positions', ArenaPositions, queue_size=10)
		
		#Models
		self.scaler = joblib.load('src/cam_tracker/models/scaler.pkl') 
		self.clf_X = joblib.load('src/cam_tracker/models/model-X.pkl')
		self.clf_Y = joblib.load('src/cam_tracker/models/model-Y.pkl') 



	def pantilts_to_positions(self, pan_tilts):
		if len(pan_tilts.array_pantilt) > 0:

			pan_tilt_array = np.array([[x.pan, x.tilt] for x in pan_tilts.array_pantilt]).astype(float)

			pan_tilt_array_norm = self.scaler.transform(pan_tilt_array)

			Xs = np.rint(self.clf_X.predict(pan_tilt_array_norm))
			Ys = np.rint(self.clf_Y.predict(pan_tilt_array_norm))
			
			positions = ArenaPositions()
			for x,y in zip(Xs, Ys):
				position = ArenaPosition()
				position.x = x
				position.y = y
				positions.array_arena.append(position)

			self.pub_arenas.publish(positions)


if __name__ == '__main__':
	rospy.init_node('localize', anonymous=True)

	try:
		Localize()
		rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

