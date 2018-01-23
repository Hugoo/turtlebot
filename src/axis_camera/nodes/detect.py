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


def nothing(x):
	pass

print("ici")
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
print("la")
# create trackbars for color change
cv2.createTrackbar('H_low','image',0,179,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)

cv2.createTrackbar('H_high','image',0,179,nothing)
cv2.createTrackbar('S_high','image',0,255,nothing)
cv2.createTrackbar('V_high','image',0,255,nothing)
print("apres slider")
#cv2.imshow('image',img)

def computeImage(img):
	#img is a numpy array
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	print("hello")

	# get current positions of four trackbars
	h_low = cv2.getTrackbarPos('H_low','image')
	s_low = cv2.getTrackbarPos('S_low','image')
	v_low = cv2.getTrackbarPos('V_low','image')

	h_h = cv2.getTrackbarPos('H_high','image')
	s_h = cv2.getTrackbarPos('S_high','image')
	v_h = cv2.getTrackbarPos('V_high','image')

	# define range of blue color in HSV
	lower = np.array([h_low,s_low,v_low])
	upper = np.array([h_h,s_h,v_h])

	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(img,img, mask= mask)

	cv2.imshow('image',res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

	return res

def callback(data_img):
	print("callback")

	np_arr = np.fromstring(data_img.data, np.uint8)
	frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


	img = computeImage(frame)#np.zeros([50,50,3])



	pub = rospy.Publisher('/imgg/compressed', CompressedImage, queue_size=10)
	# pub.publish(left_img_msg)

	msg = CompressedImage()
	msg.header.stamp = rospy.Time.now()
	msg.format = "jpeg"
	msg.data = np.array(cv2.imencode('.jpg', img)[1]).tostring()
	pub.publish(msg)

	


if __name__ == '__main__':
    rospy.init_node('detect_NODE', anonymous=True)
    #pub_ = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1) #
    
    #rospy.Subscriber("nav_to_goal", Pose2D, lambda msg:callback(turtle_control, turtlebot_control, msg))
    rospy.Subscriber("axis/image_raw/compressed", CompressedImage, callback)
    
    rospy.spin()
