#!/usr/bin/env python3

import rospy
from lidar import LidarHandler
from std_msgs.msg import Float64

class DiffDriveController():
    def __init__(self):
        rospy.init_node("diff_drive_robot")
        rospy.on_shutdown(self.shutdown)

        LidarHandler(self.lidar_callback)

        self.left_wheel_controller = rospy.Publisher('/diff_drive_robot/left_wheel_controller/command', Float64, queue_size=10)
        self.right_wheel_controller = rospy.Publisher('/diff_drive_robot/right_wheel_controller/command', Float64, queue_size=10)

    def lidar_callback(self, data):
        if data.ranges[len(data.ranges) // 2] < 1:
            self.velocity = 0.0
        else:
            self.velocity = 2.0

        self.left_wheel_controller.publish(-self.velocity)
        self.right_wheel_controller.publish(-self.velocity)


    def shutdown(self):
        self.left_wheel_controller.publish(0)
        self.right_wheel_controller.publish(0)
        rospy.sleep(1)


if __name__ == '__main__':
    diff_drive_controller = DiffDriveController()
    rospy.spin()