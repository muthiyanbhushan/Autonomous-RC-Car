#!/usr/bin/env python

import rospy

from race.msg import drive_param
from race.msg import pid_input


pub = rospy.Publisher('drive_parameters', drive_param, queue_size=10)

kp = 1.0
kd = 0.1
ki = 0.0
servo_offset = 0.0
prev_error = 0.0 
error = 0.0
integral = 0.0



def control(data):
	global integral
	global prev_error
	print integral
	velocity = data.pid_vel
	angle = servo_offset
	error = data.pid_error

	if error!=0.0:	
		integral = integral + error	
		control_error = kp*error + kd*(prev_error - error) + ki*integral
		integral = integral/1.3
		print control_error

		angle = angle - control_error

	elif error == 0.0:
		angle = servo_offset

	prev_error = error

	print "Control error",control_error
	print "Velocity",velocity
	print "Angle",angle
	msg = drive_param();
	msg.velocity = velocity
	msg.angle = angle
	pub.publish(msg)


def listener():
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	
	rospy.spin()


if __name__ == '__main__':
	print("Listening to error for PID")
	listener()
