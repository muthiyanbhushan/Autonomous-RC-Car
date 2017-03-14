#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <sensor_msgs/LaserScan.h>
#include <math.h>

class scan_modifier
{

  public:
	scan_modifier(){
	  sub_ = nh_.subscribe("/scan",10,&scan_modifier::scanCb, this);
	  pub_ = nh_.advertise<sensor_msgs::LaserScan>("/processed_scan", 10);
		
	}

  private:
	ros::Publisher pub_;
	ros::Subscriber sub_;
	sensor_msgs::LaserScan out_scan_;
	ros::NodeHandle nh_;

  void scanCb(const sensor_msgs::LaserScan& scan_in){
	
	//ROS_INFO("Cb");
	
	int iter_;
	out_scan_ = scan_in;

	for (iter_ = 0; iter_ < out_scan_.ranges.size(); iter_++){
	
	  if (std::isnan(out_scan_.ranges[iter_])){
		out_scan_.ranges[iter_] = out_scan_.range_max;
		ROS_INFO("IN");
	  }
	}
	
	pub_.publish(out_scan_);
  }
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "process_scan");
    scan_modifier modifier_object;
    ros::spin();
    return 0;
}

