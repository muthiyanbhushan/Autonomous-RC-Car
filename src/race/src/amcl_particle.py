#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
import numpy as np
import tf

pub = rospy.Publisher('amcl_particle', PoseStamped, queue_size=10)

def callback(data):
	posses = data.poses
	points = []
	framid = data.header.frame_id
	seqa = data.header.seq
	for i in posses:
		#print(i.position.x)
		#print(i.position.y)
		points.append([i.position.x,i.position.y,i.orientation.x, i.orientation.y, i.orientation.z, i.orientation.w])
		b = np.array(points);
	a = np.median(b,axis = 0)
	print(a)
	msg = PoseStamped()
	msg.header.seq = seqa
	msg.header.stamp = rospy.Time.now()
	msg.header.frame_id = framid
	msg.pose.position.x = np.float(a[0])
	msg.pose.position.y = np.float(a[1])
	msg.pose.orientation.x = np.float(a[2])
	msg.pose.orientation.y = np.float(a[3])
	msg.pose.orientation.z = np.float(a[4])
	msg.pose.orientation.w = np.float(a[5])
	pub.publish(msg)

if __name__ == '__main__':
	rospy.init_node('amcl_particle', anonymous=True)
	rospy.Subscriber("particlecloud", PoseArray, callback)
	rospy.spin()
