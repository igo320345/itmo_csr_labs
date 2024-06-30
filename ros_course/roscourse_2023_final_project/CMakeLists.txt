cmake_minimum_required(VERSION 2.8.3)
project(roscourse_2023_project_scene)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  controller_manager
  joint_state_controller
)
catkin_package()
