import rosbag
bag = rosbag.Bag('test.bag')
for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
    pub.publish(msg)
bag.close()

if __name__ == '__main__':
    print("Laser node started")
    rospy.init_node('ros_bag',anonymous = True)
    rospy.Subscriber("scan",LaserScan,callback)

    rospy.spin()
    
