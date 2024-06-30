#!/usr/bin/env python3

import rospy
import message_filters
from my_robot_controller.msg import Num

def sum_callback(x, y):
    sum = x.num + y.num
    rospy.loginfo("sum: {sum}".format(sum = sum))
    pub = rospy.Publisher("result_368912", Num, queue_size=10)
    msg = Num()
    msg.num = sum
    pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node("node2")
    rospy.loginfo("Node started...")

    subscriber1 = message_filters.Subscriber("/my_nodes/num1", Num,)
    subscriber2 = message_filters.Subscriber("/my_nodes/num2", Num)

    ts = message_filters.ApproximateTimeSynchronizer([subscriber1, subscriber2], queue_size=10, slop=0.5, allow_headerless=True)
    ts.registerCallback(sum_callback)

    
    rospy.spin()
