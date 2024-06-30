#!/usr/bin/env python3

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class CameraHandler:
    def __init__(self):
        sub_topic_name ="/diff_drive_robot/camera1/image_raw"
        self.camera_subscriber = rospy.Subscriber(sub_topic_name, Image, self.camera_callback)
        self.bridge = CvBridge()
        self.curent_image = None

    def camera_callback(self, data):
        frame = self.bridge.imgmsg_to_cv2(data)
        print(frame.shape)
