#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import sys
import time
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
#from geometry_msgs.msg import Pose
from std_msgs.msg      import Float64
from turtlesim.msg       import Pose

#Petit noeud des familles
poseTurtle = Pose()

def nav(x,y,theta):
    pass

def transformPose2D(destination_repere_global, pose_robot):
    #Retourne un X et Y dans le repere du robot

    new_x = math.cos(pose_robot.theta)*(destination_repere_global.x-pose_robot.x)+math.sin(pose_robot.theta)*(destination_repere_global.y-pose_robot.y)
    new_y = -math.sin(pose_robot.theta)*(destination_repere_global.x-pose_robot.x)+math.cos(pose_robot.theta)*(destination_repere_global.y-pose_robot.y)

    print('NEW COORD')
    print('X : {} Y : {}'.format(new_x,new_y))

    return round(new_x),round(new_y)

def position(pose):
    global poseTurtle
    poseTurtle = pose

def callback(publisher, data, pose):
    print("ORDRE RECU")
    print('')
    print("POSITION ACTUELLE :")
    print('')
    print(pose)
    print("ORDRE :")
    print(data)
    twist = Twist()
    
    X,Y = transformPose2D(data, pose)

    #ORIENTATION
    twist_or = Twist()
    twist_or.angular.z = math.atan(Y/X) #VERIFIER X NON NUL
    print("PREMIER ANGLE : "+str(twist_or.angular.z))
    publisher.publish(twist_or)
    time.sleep(4)

    twist.linear.x = X
    #twist.linear.y = Y

    publisher.publish(twist)

if __name__ == '__main__':
    print("started")
    rospy.init_node('nav_to_goal_NODE', anonymous=True)
    turtle_control = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)

    rospy.Subscriber("/turtle1/pose", Pose, position)
    rospy.Subscriber("nav_to_goal", Pose2D, lambda msg:callback(turtle_control, msg, poseTurtle))
    

    rospy.spin()
