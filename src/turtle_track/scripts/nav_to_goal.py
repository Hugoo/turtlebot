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

    #print('NEW COORD')
    #print('X : {} Y : {}'.format(new_x,new_y))

    return new_x,new_y

def position(pose):
    global poseTurtle
    poseTurtle = pose

def callback(publisher, publisher_turtlebot, data):
    global poseTurtle
    print(' ')
    print("ORDRE RECU")
    print('')
    print("POSITION ACTUELLE :")
    print('')
    print(poseTurtle)
    print("ORDRE :")
    print(data)
    
    
    X,Y = transformPose2D(data, poseTurtle)


    #Boucle fermee

    
    angle_target = math.atan(float(Y)/float(X))/0.5
    if X<0:
        angle_target+=3.14


    twist = Twist()
    twist.angular.z = angle_target #VERIFIER X NON NUL
    while poseTurtle.theta - angle_target < 0.05:

        
        publisher.publish(twist)
        publisher_turtlebot.publish(twist)
        time.sleep(0.1)

    dist = math.sqrt(X**2+Y**2)

    while dist > 0.05:

        X,Y = transformPose2D(data, poseTurtle)

        #ORIENTATION
        if X!=0:
            angle = math.atan(float(Y)/float(X))/0.1
            #if X<0:
            #    angle+=3.14
            twist.angular.z = angle #VERIFIER X NON NUL
        #print("PREMIER ANGLE : "+str(twist.angular.z))
        dist = math.sqrt(X**2+Y**2)
        twist.linear.x = X
        publisher.publish(twist)
        publisher_turtlebot.publish(twist)
        print(dist)
        time.sleep(0.1)
        
    twist = Twist()
    twist.angular.z= data.theta%6.28-poseTurtle.theta
    publisher.publish(twist)
    publisher_turtlebot.publish(twist)

if __name__ == '__main__':
    print("started")
    rospy.init_node('nav_to_goal_NODE', anonymous=True)
    turtle_control = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)

    turtlebot_control = rospy.Publisher('/teleop_velocity_smoother/raw_cmd_vel', Twist, queue_size=1)

    rospy.Subscriber("/turtle1/pose", Pose, position)
    rospy.Subscriber("nav_to_goal", Pose2D, lambda msg:callback(turtle_control, turtlebot_control, msg))
    

    rospy.spin()
