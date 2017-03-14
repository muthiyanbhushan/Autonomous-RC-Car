#!/usr/bin/env python

import rospy
from race.msg import drive_values
from race.msg import velocity_param
from race.msg import angle_param
from std_msgs.msg import Bool
from sensor_msgs.msg import Imu

global car_velocity
global car_angle

pub = rospy.Publisher('drive_pwm', drive_values, queue_size=10)
em_pub = rospy.Publisher('eStop', Bool, queue_size=10)
imu_pub = rospy.Publisher('Imu', Imu, queue_size=40)

# function to map from one range to another, similar to arduino
def arduino_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# callback function on occurance of drive parameters(angle & velocity)
def velocity_callback(data):
	velocity = data.velocity
	car_velocity = velocity
	print("Velocity: ",velocity,"Angle: ",angle)
	# Do the computation
	pwm1 = arduino_map(velocity,-100,100,6554,13108);
	msg = drive_values()
	msg.pwm_drive = pwm1
	msg.pwm_angle = car_angle
	pub.publish(msg)

def angle_callback(data):
	angle = data.angle
	car_angle = angle
	msg = drive_values()
	pwm2 = arduino_map(angle,-100,100,6554,13108);
	msg.pwm_drive = car_velocity
	msg.pwm_angle = pwm2

def Imu_callback(data):
	imu_msg = Imu()
	LAC_x = data.linear_acceleration_covariance[0]
	print("LAC_x: ", LAC_x)
	imu_msg.lac_x = LAC_x

def talker():
	rospy.init_node('serial_talker', anonymous=True)
	em_pub.publish(False)
	rospy.Subscriber("velocity_parameters", velocity_param, velocity_callback)
	rospy.Subscriber("angle_parameters", angle_param, angle_callback)
	rospy.Subscriber("Imu", Imu, Imu_callback)
	
	rospy.spin()

if __name__ == '__main__':
	print("Serial talker initialized")
	talker()
