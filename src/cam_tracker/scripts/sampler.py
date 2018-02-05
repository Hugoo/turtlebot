#! /usr/bin/env python
# -*- coding: utf-8 -*-


import math
import rospy
import sys
import time
import os
import numpy as np
import copy
from axis_camera.msg import Axis
from cam_tracker.srv import *
from cam_tracker.msg import *
from std_srvs.srv  import Empty


class Sampler:
	def __init__(self, pos_filename):

		self.current_state = Axis()

		#SUB
		self.sub_cam = rospy.Subscriber('/axis/state', Axis, self.update_state)

		#http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29#rospy_tutorials.2BAC8-Tutorials.2BAC8-WritingServiceClient.CA-27047f5058d93f3c972525600be4e0b4132b06a5_13
		self.ser = rospy.Service('/record', Empty, self.save_position)
		self.positions = []

		with open(pos_filename, 'r') as f:
			self.positions = [x.split(',') for x in f.read().split('\n')[1:-1]]
			
		self.pos_index = 0

		self.data = open('positions_pan_tilt.txt', 'a')

		self.next_pos()

	def next_pos(self):
		print('Place turtle bot in')
		print('x: '+str(self.positions[self.pos_index][0]))
		print('y: '+str(self.positions[self.pos_index][1]))
		print('and send service command')
		print('')

	def save_position(self, data):
		print("ordre recu")
		line = str(self.current_state.pan)+','+str(self.current_state.tilt)+','+str(self.positions[self.pos_index][0])+','+str(self.positions[self.pos_index][1])+'\n'
		print(line)
		self.data.write(line)

		self.pos_index += 1

		if self.pos_index == len(self.positions):
			print('OVER')
			exit()
		
		self.next_pos()


	def update_state(self,axis_data):
		self.current_state = axis_data
		


if __name__ == '__main__':
	rospy.init_node('sampler', anonymous=True)

	try:

		if len(sys.argv) < 1:
			print("usage: sampler.py filename")
		else:
			Sampler(sys.argv[1])
			rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

