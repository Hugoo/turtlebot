#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Analyse une image Axis cam et publie la liste des pan-tilt sur /pan_tilts

import math
import rospy
import sys
import time
import cv2
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

		#PUB
		self.pub_pantilts = rospy.Publisher('/pan_tilts', PanTilts, queue_size=10)
		self.pub = rospy.Publisher('/imgg/compressed', CompressedImage, queue_size=10)


		#SUB
		self.sub_cam = rospy.Subscriber('/axis/state', Axis, self.update_state)
		self.sub = rospy.Subscriber('axis/image_raw/compressed', CompressedImage, self.callback)
		
		print("Detect node started")

	def nothing(self,x):
		pass

	def update_state(self,axis_data):
		self.current_state = axis_data



	def convertPanTilt(self, pan, tilt, zoom, u, v , u0, v0):
		theta = 4.189301e+001-6.436043e-003*zoom+2.404497e-007*zoom*zoom

  		focale = u0/math.tan((math.pi*theta/180.0)/2)

  		x=u-u0
  		y=v-v0
  		z = focale
  		norme= math.sqrt(x*x+y*y+z*z)

  		x/=norme
  		y/=norme
  		z/=norme

  		beta0=-(math.pi*pan/180.0)
  		alpha0=-(math.pi*tilt/180.0)
  		X=math.cos(beta0)*x+math.sin(alpha0)*math.sin(beta0)*y-math.cos(alpha0)*math.sin(beta0)*z;
  		Y=math.cos(alpha0)*y+math.sin(alpha0)*z;
  		Z=math.sin(beta0)*x-math.sin(alpha0)*math.cos(beta0)*y+math.cos(alpha0)*math.cos(beta0)*z;
  		alpha=math.atan2(Y,math.sqrt(X*X+Z*Z));
  		beta=-math.atan2(X,Z);

  		span = -(180.0*beta/math.pi)
  		tilt = -(180.0*alpha/math.pi)
  		pan_tilt = PanTilt()
  		pan_tilt.pan = span
  		pan_tilt.tilt = tilt
  		return pan_tilt #[span, tilt] #span, tilt



	def publishImage(self,img):
		#img is a numpy image
		msg = CompressedImage()
		msg.header.stamp = rospy.Time.now()
		msg.format = "jpeg"
		msg.data = np.array(cv2.imencode('.jpg', img)[1]).tostring()
		self.pub.publish(msg)


	def computeImage(self, img):
		#img is a numpy array
		#get une image de la camera, retourne l'image avec les cercles autour des bots
		#retourne aussi une liste de coordonées x,y


		"""
		0,0---------> x
		 |
		 |
		 |
		 |
		 v

		 y
		"""

		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		# get current positions of four trackbars
		if slider:
			h_low = cv2.getTrackbarPos('H_low','image')
			s_low = cv2.getTrackbarPos('S_low','image')
			v_low = cv2.getTrackbarPos('V_low','image')

			h_h = cv2.getTrackbarPos('H_high','image')
			s_h = cv2.getTrackbarPos('S_high','image')
			v_h = cv2.getTrackbarPos('V_high','image')
		else:
			h_low = 153
			s_low = 69
			v_low = 59

			h_h = 179
			s_h = 200
			v_h = 255


		# define range of blue color in HSV
		lower = np.array([h_low,s_low,v_low])
		upper = np.array([h_h,s_h,v_h])

		mask = cv2.inRange(hsv, lower, upper)
		res = cv2.bitwise_and(img,img, mask= mask)

		_, cnts, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#print(cnt[0])
		cnts = self.filter_cnts(cnts)
		centers = []
		for cnt in cnts:
			try:
				M = cv2.moments(cnt)
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
				centers.append([cX,cY])
			except:
				pass

			#REVOIR
			if cnt is not None:
				if len(cnt)>=5:
					ellipse = cv2.fitEllipse(cnt)
					cv2.ellipse(img,ellipse,(0,255,0),2)
		if slider:
			img = res	
		return img, centers

	def filter_cnts(self, cnts):
		#Filtre les contours en ne gardant que les "grands contours" (permet de retirer le bruit)
		good_cnts = [cnt for cnt in cnts if cv2.contourArea(cnt)>160]
		return good_cnts

	def callback(self, data_img):
		np_arr = np.fromstring(data_img.data, np.uint8)
		frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
		cv2.namedWindow('image')
		if slider:
			cv2.createTrackbar('H_low','image',153,179,self.nothing)
			cv2.createTrackbar('S_low','image',69,255,self.nothing)
			cv2.createTrackbar('V_low','image',164,255,self.nothing)
			cv2.createTrackbar('H_high','image',172,179,self.nothing)
			cv2.createTrackbar('S_high','image',200,255,self.nothing)
			cv2.createTrackbar('V_high','image',255,255,self.nothing)

		img, centers = self.computeImage(frame) #centers = array de [x,y]
		center_x = img.shape[1]/2
		center_y = img.shape[0]/2

		#Draw a crosshair in the center of the image
		cv2.line(img, (center_x-20, center_y), (center_x+20, center_y), (0, 0, 255), 2)
		cv2.line(img, (center_x, center_y-20), (center_x, center_y+20), (0, 0, 255), 2)

		pan_tilts = PanTilts()
		for center in centers:
			pan_tilt = self.convertPanTilt(self.current_state.pan, self.current_state.tilt,self.current_state.zoom, center[0], center[1], center_x, center_y)
			pan_tilts.array_pantilt.append(pan_tilt)
		
		self.pub_pantilts.publish(pan_tilts)

		cv2.imshow('image',img)
		cv2.waitKey(1) & 0xFF
		

if __name__ == '__main__':
	rospy.init_node('detect', anonymous=True)

	try:
		Tracker()
		rospy.spin()
	except KeyboardInterrupt:
		print "Ok Bye Brow"

