#!/usr/bin/env python



import rospy

import math

from sensor_msgs.msg import LaserScan

from race.msg import pid_input



desired_trajectory = .5

vel = 5

rate = 0

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

    print "idx= {} : data= {}\n".format(index, data.ranges[index])

    return data.ranges[index]

    



def callback(data):

    theta = 40;
    theta_plus90 = theta + 90

    a = getRange(data, theta)
    b = getRange(data, 0)
    bb = getRange(data, theta_plus90)

    swing = math.radians(theta)



    alpha = math.atan2( a * math.cos(swing) - b , a * math.sin(swing) )

    AB = b * math.cos(alpha)



    AC = 1

    CD = AB + AC * math.sin(alpha)



    #error = AB - desired_trajectory

    error = CD - desired_trajectory



    #ABprime = a * math.cos(math.asin(a * math.sin(swing) / math.sqrt(a*a + b*b - 2*a*b*math.cos(swing))) - math.pi / 2 + swing)



    print "a {}\nb {} bb {}".format(a, b, bb)

    print "AB {}".format(AB)

    #print "ABprime {}".format(ABprime)

    print "error {}".format(error)



    msg = pid_input()

    msg.pid_error = error

    msg.pid_vel = vel



### Publish not too many -> It will make SYNC LOSS in Teensy (BK v0.11)

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


