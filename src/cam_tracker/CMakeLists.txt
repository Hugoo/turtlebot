cmake_minimum_required(VERSION 2.8.3)
project(cam_tracker)
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  message_generation
#  math
#  sys
#  time
#  cv2
#  numpy
)

add_service_files(
  FILES
  ChangeTrackingMode.srv
)

catkin_package()

install(PROGRAMS scripts/detectNEW.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})