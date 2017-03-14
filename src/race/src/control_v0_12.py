#!/usr/bin/env python



import rospy
from race.msg import angle_param
from race.msg import velocity_param
from race.msg import pid_input
from std_msgs.msg import String
import math



kp = 14.0 * 2
kd = 0.09 * 4 	## handling how fast
servo_offset = 18.5
prev_error = 0.0 
vel_input = 0.0
mode = 'wall'


velocityPub = rospy.Publisher('velocity_parameters', velocity_param, queue_size=1)
anglePub = rospy.Publisher('angle_parameters', angle_param, queue_size=1)


def control(data):

    global kp
    global kd
    global servo_offset
    global prev_error
    global vel_input
    global mode

    angleMsg = angle_param()
    velocityMsg = velocity_param()
    velocityMsg.velocity = data.pid_vel

    if mode == 'wall':
        pid_error = data.pid_error
        error = pid_error * kp
        errordot = kd * (pid_error - prev_error)

        angle = error + errordot

        if angle > 100:
            angle = 100
        elif angle < -100:
            angle = -100

        prev_error = pid_error
        print 'pid_error {}\nangle {}'.format(pid_error, angle)

        angleMsg.angle = angle

    elif mode == 'corner':
        print 'corner mode, angle 100'
        angleMsg.angle = 100



	##	(BK v0.11)

##  rospy.sleep(0.1) ## <<<<<<<< optimization needed to solve SYNC LOST problem with Teensy

    anglePub.publish(angleMsg)
    velocityPub.publish(velocityMsg)





def update_mode(_mode):
	global mode
	mode = _mode.data





if __name__ == '__main__':
	print("Listening to error for PID")
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)

	rospy.Subscriber("mode", String, update_mode)

	rospy.spin()




