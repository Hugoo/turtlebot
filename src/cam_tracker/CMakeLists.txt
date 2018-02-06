cmake_minimum_required(VERSION 2.8.3)
project(cam_tracker)
find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  sensor_msgs
  message_generation
#  math
#  sys
#  time
#  cv2
#  numpy
)


#include_directories(
#  ${catkin_INCLUDE_DIRS}
#)

#add_executable(cam_tracker src/share.cpp)

## Specify libraries to link a library or executable target against
#target_link_libraries(cam_tracker
#  ${catkin_LIBRARIES}
#)

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