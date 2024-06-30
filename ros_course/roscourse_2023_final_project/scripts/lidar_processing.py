#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

ACCELERATION = 6 # no more daddy please
BASIC_SPEED = 25.0 
THRESHOLD_DISTANCE  = 0.8
BOOST = 35

ns = 'project_robot_888888'

def round_int(x):
    if x in [float('-inf'),float('inf')]: return 3
    else: return int(round(x))


class ObstacleAvoidance:
    def __init__(self):
        rospy.init_node('lidar_processing_node', anonymous=True)
        rospy.Subscriber(f'/{ns}/lidar_main',
                         LaserScan, self.lidar_callback)

        # Publish joint velocity commands for the wheels
        self.right_wheel_controller = rospy.Publisher(
            f'/{ns}/right_wheel_controller/command', Float64, queue_size=1)
        self.left_wheel_controller = rospy.Publisher(
            f'/{ns}/left_wheel_controller/command', Float64, queue_size=1)



    def move_forward(self, speed):
        self.right_wheel_controller.publish(-speed)
        self.left_wheel_controller.publish(-speed)

    def move_back(self):
        joint_speed = 4.0
        self.right_wheel_controller.publish(joint_speed)
        self.left_wheel_controller.publish(joint_speed)

    def turn_left(self, dist):
        self.right_wheel_controller.publish(-BASIC_SPEED-ACCELERATION)
        self.left_wheel_controller.publish(BASIC_SPEED)

    def turn_right(self, dist):
        self.right_wheel_controller.publish(BASIC_SPEED)
        self.left_wheel_controller.publish(-BASIC_SPEED-ACCELERATION)

    def lidar_callback(self, data):
        rospy.logwarn(
            f'dist: left:{data.ranges[-1]} mid:{data.ranges[4]} right:{data.ranges[0]}')

        if abs(data.ranges[4]) > 3 and round_int(data.ranges[0]) >= 1 and round_int(data.ranges[-1]) >= 1:
            self.move_forward(BOOST)
        elif data.ranges[0] < THRESHOLD_DISTANCE :
            self.turn_right(data.ranges[0])
        elif data.ranges[-1] < THRESHOLD_DISTANCE :
            self.turn_left(data.ranges[-1])
        elif sum(data.ranges) < THRESHOLD_DISTANCE *9:
            self.move_back()
        else:
            self.move_forward(BASIC_SPEED)


def main():
    try:
        ObstacleAvoidance()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()
