#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Petit node de detection du NinjaBot

import math
import rospy
import sys
import time
import cv2
import numpy as np
#from geometry_msgs.msg import Twist
#from geometry_msgs.msg import Pose2D
#from geometry_msgs.msg import Pose
#from std_msgs.msg      import Float64
#from turtlesim.msg       import Pose
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

		self.pub = rospy.Publisher('/imgg/compressed', CompressedImage, queue_size=10)
		self.sub = rospy.Subscriber('axis/image_raw/compressed', CompressedImage, self.callback)
		self.sub_cam = rospy.Subscriber('/axis/state', Axis, self.update_state)
		self.pub_cam = rospy.Publisher('axis/cmd', Axis)
		#http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29#rospy_tutorials.2BAC8-Tutorials.2BAC8-WritingServiceClient.CA-27047f5058d93f3c972525600be4e0b4132b06a5_13
		self.ser_mode = rospy.Service('/camera_mod', ChangeTrackingMode, self.change_mode)
		

	def nothing(self,x):
		pass

	def update_state(self,axis_data):
		self.current_state = axis_data

	def change_mode(self,mode_data):
		print(mode_data.command)
		if mode_data.command in ['TRACK', 'SEARCH', 'SCAN']:
			self.mode = mode_data.command
		else:
			self.mode = 'TRACK'
		return None

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
  		return [span, tilt] #span, tilt



	def publishImage(self,img):
		#img is a numpy image
		msg = CompressedImage()
		msg.header.stamp = rospy.Time.now()
		msg.format = "jpeg"
		msg.data = np.array(cv2.imencode('.jpg', img)[1]).tostring()
		self.pub.publish(msg)

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



	def computeImage(self, img):
		#img is a numpy array
		#get une image de la camera, retourne l'image avec un point + coordonées x,y


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
			v_low = 164

			h_h = 172
			s_h = 200
			v_h = 255


		# define range of blue color in HSV
		lower = np.array([h_low,s_low,v_low])
		upper = np.array([h_h,s_h,v_h])

		mask = cv2.inRange(hsv, lower, upper)
		res = cv2.bitwise_and(img,img, mask= mask)

		_, cnts, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#print(cnt[0])
		cnt = self.get_biggest_contour(cnts)

		cX = -1
		cY = -1
		try:
			M = cv2.moments(cnt)
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
			cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
		except:
			pass
		#cv2.drawContours(img, cnt, -1, (255,255,0),2)

		#print("contours",what)
		if cnt != None:
			if len(cnt)>=5:
				ellipse = cv2.fitEllipse(cnt)
				cv2.ellipse(img,ellipse,(0,255,0),2)

		return img, cX, cY

	def get_biggest_contour(self, cnts):
		#cnts is a list of contours
		#returns a contour
		best_cnt = None
		max_area = -1
		for cnt in cnts:
			area = cv2.contourArea(cnt)
			if area > max_area:
				best_cnt = cnt

		return best_cnt

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


		if self.mode=='SCAN': #MODE SCAN
			cv2.imshow('image',frame)
			self.scanMode()
		else:
			img, u, v = self.computeImage(frame) #u = x et v = y
			if u != -1 and v != -1 and time.time()-self.lastcall > 1.5:
				u0 = img.shape[1]/2
				v0 = img.shape[0]/2
				cv2.circle(img, (u0, v0), 7, (255, 255, 255), -1)
				# pan_tilt est un tableau [span, tilt]

				pan_tilt = self.convertPanTilt(self.current_state.pan, self.current_state.tilt,self.current_state.zoom, u, v , u0, v0)

				delta_pan = pan_tilt[0] - self.current_state.pan
				delta_tilt = pan_tilt[1] - self.current_state.tilt
			
				next_state = copy.copy(self.current_state)
				
				seuil = 5

				if delta_pan > seuil:
					next_state.pan = self.current_state.pan+seuil
				elif delta_pan < -seuil:
					next_state.pan = self.current_state.pan-seuil
				else:
					next_state.pan = pan_tilt[0]

				if delta_tilt > seuil:
					next_state.tilt = self.current_state.tilt+seuil
				elif delta_tilt < -seuil:
					next_state.tilt = self.current_state.tilt-seuil
				else:
					next_state.tilt = pan_tilt[1]

				delta_pan = pan_tilt[0] - self.current_state.pan
				delta_tilt = pan_tilt[1] - self.current_state.tilt

				if abs(pan_tilt[0]) > 3 and abs(pan_tilt[1]) >3:
					#print("post it : \n X: "+str(u)+"\n Y: "+str(v))
					print("ordre : \n span: "+str(delta_pan)+"\n Tilt: "+str(delta_tilt))
					self.pub_cam.publish(next_state)
					self.lastcall = time.time()

		
			cv2.imshow('image',img)
		cv2.waitKey(1) & 0xFF
		
		#self.publishImage(img)

if __name__ == '__main__':
	rospy.init_node('tracker_NODE', anonymous=True)

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

