#!/usr/bin/env python3

import rospy
from random import randint
from my_robot_controller.msg import Num

if __name__ == '__main__':
    rospy.init_node("node1")
    rospy.loginfo("Node started...")
    rate = rospy.Rate(1)

    pub = rospy.Publisher("/my_nodes/num1", Num, queue_size=10)

    msg = Num()
    while not rospy.is_shutdown():
        num = randint(0, 100)
        msg.num = num

        pub.publish(msg)

        rospy.loginfo("x: {x}".format(x=num))
        rate.sleep()

    # rospy.logwarn("Hello world worn")
    # rospy.logerr("Hello world err")
