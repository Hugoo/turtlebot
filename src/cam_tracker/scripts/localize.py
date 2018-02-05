#! /usr/bin/env python
# -*- coding: utf-8 -*-


import math
import rospy
import sys
import time
import numpy as np
import copy
from cam_tracker.srv import *
from cam_tracker.msg import *


class Localize:
	def __init__(self):
		

		#SUB
		self.sub_pantilts = rospy.Subscriber('/pan_tilts', PanTilts, self.pantilts_to_positions)

		#PUB
		self.pub_arenas = rospy.Publisher('/arena_positions', ArenaPositions, queue_size=10)
		
	def pantilts_to_positions(self, pan_tilts):
		positions = ArenaPositions()
		for pan_tilt in pan_tilts.array_pantilt:
			position = ArenaPosition()
			## ADD LOGIC HERE
			# func is SVM
			# x,y = func(pan_tilt.pan, pan_tilt.tilt)
			position.x = 0
			position.y = 0
			positions.array_arena.append(position)

		self.pub_arenas.publish(positions)


if __name__ == '__main__':
	rospy.init_node('localize', anonymous=True)

	try:
		Localize()
		rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

