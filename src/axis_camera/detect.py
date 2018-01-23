#Petit node de detection du NinjaBot

#! /usr/bin/env python
# -*- coding: utf-8 -*-
print("Starting node")
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

def callback(data_img):
   np_arr = np.fromstring(data_img, np.uint8)
   image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
   print(np.mean(image_np))

if __name__ == '__main__':
    print("Starting node")
    rospy.init_node('detect_NODE', anonymous=True)
    #pub_ = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1) #
    
    #rospy.Subscriber("nav_to_goal", Pose2D, lambda msg:callback(turtle_control, turtlebot_control, msg))
    rospy.Subscriber("/image_raw/compressed", CompressedImage, callback)
    
    rospy.spin()
