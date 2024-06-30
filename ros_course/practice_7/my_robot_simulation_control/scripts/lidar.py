#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

class LidarHandler:
    def __init__(self, lidar_callback):
        sub_topic_name = '/diff_drive_robot/lidar'
        self.lidar_subscriber = rospy.Subscriber(sub_topic_name, LaserScan, lidar_callback)
