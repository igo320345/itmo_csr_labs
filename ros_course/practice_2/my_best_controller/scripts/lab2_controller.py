#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from math import sqrt

class SimpleController():

    points = [(2, 3), (4, 2), (5, 4)]

    def __init__(self):
        rospy.init_node('lab2_controller', anonymous=True)
        rospy.on_shutdown(self.shutdown)
        self.ns = rospy.get_namespace()
        self.cmd_vel_pub = rospy.Publisher(f'{self.ns}turtle1/cmd_vel', Twist, queue_size=1)
        self.rate = rospy.Rate(30)

        self.subscriber = rospy.Subscriber(
            f'/ns1_368912/turtle1/pose', Pose, self.pose_callback)

        self.target_x = 0
        self.target_y = 0

        self.x = 0
        self.y = 0

    def pose_callback(self, msg: Pose):
        self.update_control(msg.x, msg.y)

    def update_control(self, x, y):
        self.x, self.y = x, y
    
    def set_target(self):
        if len(self.points) != 0:
            point = self.points.pop()
            self.target_x = point[0]
            self.target_y = point[1]

    def spin(self):
        while not rospy.is_shutdown():
            twist_msg = Twist()

            diff_x = self.target_x - self.x
            diff_y = self.target_y - self.y

            speed = 2 / sqrt(abs(diff_x) + abs(diff_y) + 0.1)

            twist_msg.linear.x = diff_x * speed
            twist_msg.linear.y = diff_y * speed

            if diff_x == 0 and diff_y == 0:
                self.set_target()

            self.cmd_vel_pub.publish(twist_msg)
            self.rate.sleep()

    def shutdown(self):
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)


simple_mover = SimpleController()
simple_mover.spin()
