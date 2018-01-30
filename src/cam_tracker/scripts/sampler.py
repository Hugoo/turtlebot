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

from std_msgs.msg import Empty


class Sampler:
	def __init__(self):

		#PUB
		#self.pub_cam = rospy.Publisher('axis/cmd', Axis)
		

		#SUB
		#self.sub_cam = rospy.Subscriber('/axis/state', Axis, self.update_state)
		self.sub_pantilts = rospy.Subscriber('/pan_tilts', PanTilts, self.callback)

		#http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29#rospy_tutorials.2BAC8-Tutorials.2BAC8-WritingServiceClient.CA-27047f5058d93f3c972525600be4e0b4132b06a5_13
		#self.ser_mode = rospy.Service('/camera_mod', ChangeTrackingMode, self.change_mode)
		
		#self.positionFilePath = 

	
	def callback(self, pan_tilts):
		print("Message pan tilts recu")
		print(pan_tilts)
		
		
if __name__ == '__main__':
	rospy.init_node('sampler', anonymous=True)

	try:
		Sampler()
		rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

