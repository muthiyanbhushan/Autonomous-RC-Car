#include <ros/ros.h>
#include <geometry_msgs/Pose2D.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/PoseWithCovariance.h>
#include <tf/transform_broadcaster.h>

class genOdom
{
  ros::NodeHandle nh_;
  ros::NodeHandle private_nh_;

  ros::Publisher pub_;
  ros::Subscriber sub_;
  nav_msgs::Odometry odom_;  
  tf::TransformBroadcaster odom_broadcaster;
  geometry_msgs::TransformStamped odom_trans;


  void callback(const geometry_msgs::Pose2D& msg)
  {
	odom_.header.stamp = ros::Time::now();
	odom_.header.frame_id = "odom";
//	odom_.child_frame_id = "base_link";
	odom_.child_frame_id = "base_frame";

	//quaternion from yaw
	geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(msg.theta);

	geometry_msgs::TransformStamped odom_trans;
	odom_trans.header.stamp = ros::Time::now();
	odom_trans.header.frame_id = "odom";
//	odom_trans.child_frame_id = "base_link";
	odom_trans.child_frame_id = "base_frame";
	odom_trans.transform.translation.x = msg.x;
	odom_trans.transform.translation.y = msg.y;
	odom_trans.transform.translation.z = 0.0;
	odom_trans.transform.rotation = odom_quat;

	//send the transmform
	odom_broadcaster.sendTransform(odom_trans);

	//set the odometry message 
	odom_.pose.pose.position.x = msg.x;
	odom_.pose.pose.position.y = msg.y;
	odom_.pose.pose.position.z = 0;
	odom_.pose.pose.orientation = odom_quat;

	//publish the message
	pub_.publish(odom_);	
	
  }

  public:
  genOdom():nh_(), private_nh_("~")
  {
	pub_ = nh_.advertise<nav_msgs::Odometry>("matcherOdom",10);
	sub_ = nh_.subscribe("/pose2D",10,&genOdom::callback,this);

  }
  
};

int main(int argc, char** argv)
{
	ros::init(argc,argv,"getOdomFromMatcher");
	genOdom odomObject;
	ros::spin();
	return 0;
}


