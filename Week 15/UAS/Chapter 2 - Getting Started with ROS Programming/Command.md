git clone https://github.com/PacktPublishing/Mastering-ROS-for-Robotics-Programming-Third-edition

//terminal 1
ros2 run mastering_ros_demo_pkg demo_topic_publisher
//terminal 2
ros2 run mastering_ros_demo_pkg demo_topic_subscriber

//terminal 1
ros2 run mastering_ros_demo_pkg demo_msg_publisher
//terminal 2
ros2 run mastering_ros_demo_pkg demo_msg_subscriber

//terminal 1
ros2 run mastering_ros_demo_pkg demo_service_server
//terminal 2
ros2 run mastering_ros_demo_pkg demo_service_client

//terminal 1
ros2 run mastering_ros_demo_pkg demo_action_client 10 1
//terminal 2
ros2 run mastering_ros_demo_pkg demo_action_server
