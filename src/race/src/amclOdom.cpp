#include <ros/ros.h>
#include <geometry_msgs/Pose2D.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/PoseWithCovariance.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <tf/transform_broadcaster.h>

class genOdom
{
  ros::NodeHandle nh_;
  ros::NodeHandle private_nh_;

  ros::Publisher pub_;
  ros::Subscriber sub_;
  nav_msgs::Odometry odom_;  
  

  void callback(const geometry_msgs::PoseWithCovarianceStamped& msg)
  {
	odom_.header.stamp = ros::Time::now();
	odom_.header.frame_id = "odom";

	//quaternion from yaw
	geometry_msgs::Quaternion odom_quat = msg.pose.pose.orientation;


	//set the odometry message 
	odom_.pose.pose.position.x = msg.pose.pose.position.x;
	odom_.pose.pose.position.y = msg.pose.pose.position.y;
	odom_.pose.pose.position.z = 0;
	odom_.pose.pose.orientation = odom_quat;

	//publish the message
	pub_.publish(odom_);	
	
  }

  public:
  genOdom():nh_(), private_nh_("~")
  {
	pub_ = nh_.advertise<nav_msgs::Odometry>("amclOdom",10);
	sub_ = nh_.subscribe("/amcl_pose",10,&genOdom::callback,this);

  }
  
};

int main(int argc, char** argv)
{
	ros::init(argc,argv,"amclOdom");
	genOdom odomObject;
	ros::spin();
	return 0;
}


