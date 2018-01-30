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

add_message_files(
  FILES
  PanTilt.msg
  PanTilts.msg
  ArenaPosition.msg
  ArenaPositions.msg
)

install(PROGRAMS scripts/detectNEW.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)