// Generated by gencpp from file race/velocity_param.msg
// DO NOT EDIT!


#ifndef RACE_MESSAGE_VELOCITY_PARAM_H
#define RACE_MESSAGE_VELOCITY_PARAM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace race
{
template <class ContainerAllocator>
struct velocity_param_
{
  typedef velocity_param_<ContainerAllocator> Type;

  velocity_param_()
    : velocity(0.0)  {
    }
  velocity_param_(const ContainerAllocator& _alloc)
    : velocity(0.0)  {
  (void)_alloc;
    }



   typedef float _velocity_type;
  _velocity_type velocity;




  typedef boost::shared_ptr< ::race::velocity_param_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::race::velocity_param_<ContainerAllocator> const> ConstPtr;

}; // struct velocity_param_

typedef ::race::velocity_param_<std::allocator<void> > velocity_param;

typedef boost::shared_ptr< ::race::velocity_param > velocity_paramPtr;
typedef boost::shared_ptr< ::race::velocity_param const> velocity_paramConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::race::velocity_param_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::race::velocity_param_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace race

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'race': ['/home/ubuntu/catkin_ws/src/race/msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::race::velocity_param_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::race::velocity_param_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::race::velocity_param_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::race::velocity_param_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::race::velocity_param_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::race::velocity_param_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::race::velocity_param_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e4ff88b32504f688719a85e0753f63ce";
  }

  static const char* value(const ::race::velocity_param_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe4ff88b32504f688ULL;
  static const uint64_t static_value2 = 0x719a85e0753f63ceULL;
};

template<class ContainerAllocator>
struct DataType< ::race::velocity_param_<ContainerAllocator> >
{
  static const char* value()
  {
    return "race/velocity_param";
  }

  static const char* value(const ::race::velocity_param_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::race::velocity_param_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 velocity\n\
";
  }

  static const char* value(const ::race::velocity_param_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::race::velocity_param_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct velocity_param_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::race::velocity_param_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::race::velocity_param_<ContainerAllocator>& v)
  {
    s << indent << "velocity: ";
    Printer<float>::stream(s, indent + "  ", v.velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RACE_MESSAGE_VELOCITY_PARAM_H
