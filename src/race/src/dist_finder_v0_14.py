#!/usr/bin/env python


import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input


desired_trajectory = 1
DT_Left = 1
vel = 7.3
rate = 0
MINIMUM_DISTANCE = 0.7

pub = rospy.Publisher('error', pid_input, queue_size=10)


def getRange(data, theta):

    """ Find the index of the arary that corresponds to angle theta.
    Return the lidar scan value at that index
    Do some error checking for NaN and absurd values
	data: the LidarScan data
	theta: the angle to return the distance for
	"""

    car_theta = math.radians(theta) - math.pi / 2

    if car_theta > 3 * math.pi / 4:
        car_theta = 3 * math.pi / 4
    elif car_theta < -3 * math.pi / 4:
        car_theta = -3 * math.pi / 4


    float_index = (car_theta + 3 * math.pi / 4) / data.angle_increment
    index = int(float_index)

	## check the index and data (BK v0.11)
#    print "idx= {} : data= {}\n".format(index, data.ranges[index])
    return data.ranges[index]

    



def callback(data):
	
    theta_right = 40;
    theta_left = 180 - theta_right
    theta_front = 90
    theta180 = 180


    a = getRange(data, theta_right)
    a90 = getRange(data, theta_left)

    b = getRange(data, 0)
    b180 = getRange(data, theta180)

    front = getRange(data, theta_front)

    swing = math.radians(theta_right)
    swing90 = math.radians(theta_left)

    alpha = math.atan2( a * math.cos(swing) - b , a * math.sin(swing) )	# car angle of deviation from desired trajectory
    alpha90 = math.atan2( a90 * math.cos(swing90) - b180 , a90 * math.sin(swing90) )	

    AB = b * math.cos(alpha)
    AB90 = b180 * math.cos(alpha90)

    AC = 1.0	# next point of Lidar measure

    CD = AB + AC * math.sin(alpha)
    CD90 = AB90 + AC * math.sin(alpha90)

    #error = AB - desired_trajectory
    error = CD - desired_trajectory
    error90 = CD90 - DT_Left
    error90 *= -1.0


    #ABprime = a * math.cos(math.asin(a * math.sin(swing) / math.sqrt(a*a + b*b - 2*a*b*math.cos(swing))) - math.pi / 2 + swing)



    print "a {}\na90 {}\nb {}\nb180 {} front {}".format(a, a90, b, b180, front)
    print "AB {}\nAB90 {}".format(AB, AB90)
    print "DT_L {}\nDT_R {}".format(DT_Left, desired_trajectory)

    #print "ABprime {}".format(ABprime)
    print "error {}\nerror90 {}".format(error, error90)


    msg = pid_input()
    if a > a90: # when distance from right-wall is bigger, should turn left
       msg.pid_error = error
    else:
       msg.pid_error = error90

#    msg.pid_error = error		## taking only right-turn
    msg.pid_error = error90		## taking only left-turn
    errDist = abs(a-a90)
    print "erD {}".format(errDist) 
    if (front < MINIMUM_DISTANCE) and (abs(a-a90) < MINIMUM_DISTANCE):
       msg.pid_vel = 0
    else:
       msg.pid_vel = vel



    # Publish not too many -> It will make SYNC LOSS in Teensy (BK v0.11)
    global rate
    rate += 1
    if (rate % 10 == 0):
        pub.publish(msg)
        rate = 0
  



if __name__ == '__main__':
    print("Laser node started")
    rospy.init_node('dist_finder',anonymous = True)
    rospy.Subscriber("scan",LaserScan,callback)

    rospy.spin()


