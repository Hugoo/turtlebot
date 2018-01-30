// Generated by gencpp from file cam_tracker/ChangeTrackingModeResponse.msg
// DO NOT EDIT!


#ifndef CAM_TRACKER_MESSAGE_CHANGETRACKINGMODERESPONSE_H
#define CAM_TRACKER_MESSAGE_CHANGETRACKINGMODERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cam_tracker
{
template <class ContainerAllocator>
struct ChangeTrackingModeResponse_
{
  typedef ChangeTrackingModeResponse_<ContainerAllocator> Type;

  ChangeTrackingModeResponse_()
    {
    }
  ChangeTrackingModeResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ChangeTrackingModeResponse_

typedef ::cam_tracker::ChangeTrackingModeResponse_<std::allocator<void> > ChangeTrackingModeResponse;

typedef boost::shared_ptr< ::cam_tracker::ChangeTrackingModeResponse > ChangeTrackingModeResponsePtr;
typedef boost::shared_ptr< ::cam_tracker::ChangeTrackingModeResponse const> ChangeTrackingModeResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cam_tracker

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cam_tracker/ChangeTrackingModeResponse";
  }

  static const char* value(const ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ChangeTrackingModeResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::cam_tracker::ChangeTrackingModeResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // CAM_TRACKER_MESSAGE_CHANGETRACKINGMODERESPONSE_H