#!/usr/bin/env python

import rospy
import math
from race.msg import pid_input
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion
import tf
import numpy

pub = rospy.Publisher('error', pid_input, queue_size=10)


x1 = 0.0
y1 = 0.0
x2 = 9.26874517233
y2 = -0.165325415217

vel = 14.4


def path_error(data):
	global x1
	global y1
	global x2
	global y2
	global vel

	y = data.pose.position.y
	x = data.pose.position.x
	l = 0.5;
	quaternion = (data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w)
	euler = tf.transformations.euler_from_quaternion(quaternion)
	
	roll = euler[0]
	pitch = euler[1]
	theta = (-1)*euler[2]

	y = y + l*math.sin(theta)
	x = x + l*math.cos(theta)
	m = (y2-y1) / (x2-x1)
	c = y1 - m*x1
	error = (-1)*(y - m*x - c)

	print "Error:", error
	print "theta:", theta
	
	msg = pid_input();
	msg.pid_error = error
	msg.pid_vel = vel
	pub.publish(msg)


def listener():
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("amcl_particle", PoseStamped, path_error)
	
	rospy.spin()


if __name__ == '__main__':
	print("Listening to error for PID")
	listener()