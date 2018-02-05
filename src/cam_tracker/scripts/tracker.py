#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Petit node de detection du NinjaBot

import math
import rospy
import sys
import time
import numpy as np
from sensor_msgs.msg import CompressedImage
from axis_camera.msg import Axis
import copy
from cam_tracker.srv import *
from cam_tracker.msg import *

slider = False #Mettre à false pour désactiver les curseurs

class Tracker:
	def __init__(self):

		self.current_state = Axis()
		self.lastcall = time.time()
		self.mode = 'TRACK'
		self.sens_pan = 1

		
		#PUB
		self.pub_cam = rospy.Publisher('axis/cmd', Axis)
		

		#SUB
		self.sub_cam = rospy.Subscriber('/axis/state', Axis, self.update_state)
		self.sub_pantilts = rospy.Subscriber('/pan_tilts', PanTilts, self.callback)

		#http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29#rospy_tutorials.2BAC8-Tutorials.2BAC8-WritingServiceClient.CA-27047f5058d93f3c972525600be4e0b4132b06a5_13
		self.ser_mode = rospy.Service('/camera_mod', ChangeTrackingMode, self.change_mode)
		
		print("Tracker started in mode : "+self.mode)

	def update_state(self,axis_data):
		self.current_state = axis_data

	def change_mode(self,mode_data):
		print(mode_data.command)
		if mode_data.command in ['TRACK', 'SEARCH', 'SCAN', 'STOP']:
			self.mode = mode_data.command
		else:
			self.mode = 'TRACK'
		
		return None



	def scanMode(self):
		if self.current_state==None:
			return

		limites_pan = [-31, 31]
		limites_tilt = [-87, 96]
		

		next_state = copy.copy(self.current_state)
		next_state.tilt = -42
		next_state.pan = self.current_state.pan + 10*self.sens_pan


		if next_state.pan>limites_pan[1]:
			self.sens_pan = -self.sens_pan
			next_state.pan = self.current_state.pan + 10*self.sens_pan
		elif next_state.pan<limites_pan[0]:
			self.sens_pan = -self.sens_pan
			next_state.pan = self.current_state.pan + 10*self.sens_pan

		if time.time()-self.lastcall > 1.5:
			self.lastcall = time.time()
			self.pub_cam.publish(next_state)


	def callback(self, pan_tilts):
		#Appelé constamment, pan_tilts non vide si il y a des turtle bots
		if self.mode=='SCAN': #MODE SCAN
			self.scanMode()

		elif self.mode=='SEARCH':
			pass
		elif self.mode=='STOP':
			if len(pan_tilts.array_pantilt)>0:
				pan_tilt = pan_tilts.array_pantilt[0]
				#print(pan_tilt)
		elif self.mode=='TRACK' and len(pan_tilts.array_pantilt)>0 and time.time()-self.lastcall > 1.5:
			print('track')
			#Revoir, pour le moment on prend le premier ordre
			pan_tilt = pan_tilts.array_pantilt[0]
			#print(pan_tilt)

			delta_pan = pan_tilt.pan - self.current_state.pan
			delta_tilt = pan_tilt.tilt - self.current_state.tilt
			
			next_state = copy.copy(self.current_state)
			
			seuil = 5

			if delta_pan > seuil:
				next_state.pan = self.current_state.pan+seuil
			elif delta_pan < -seuil:
				next_state.pan = self.current_state.pan-seuil
			else:
				next_state.pan = pan_tilt.pan

			if delta_tilt > seuil:
				next_state.tilt = self.current_state.tilt+seuil
			elif delta_tilt < -seuil:
				next_state.tilt = self.current_state.tilt-seuil
			else:
				next_state.tilt = pan_tilt.tilt

			delta_pan = pan_tilt.pan - self.current_state.pan
			delta_tilt = pan_tilt.tilt - self.current_state.tilt

			if abs(pan_tilt.pan) > 0.5 or abs(pan_tilt.tilt) >0.5:
				print("ordre : \n span: "+str(delta_pan)+"\n Tilt: "+str(delta_tilt))
				self.pub_cam.publish(next_state)
				self.lastcall = time.time()
			
		


if __name__ == '__main__':
	rospy.init_node('tracker', anonymous=True)

	"""
	
    - Mode track : Le tracker positionne la camera sur le Turtlebot visible.
    Quand il y en a plus d'un, le positionnement se fait sur la cible qui engendre
    le déplacement minimal. Si aucun Turtlebot n'est visible, pas de mouvement.
    
    - Mode search : Le tracker cherche un Turtlebot jusqu'à ce qu'il soit détecté.
    
    - Mode scan : Le tracker pouge périodiquement de sorte à couvrir la zone 
    			d'observation, indépendemment de la détection de robots

	"""

	try:
		Tracker()
		rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

