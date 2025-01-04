//terminal 1
ros2 launch seven_dof_arm_gazebo seven_dof_arm_gazebo_control.launch
//terminal 2
rostopic pub /seven_dof_arm/joint4_position_controller/command std_msgs/float64 "data: 1.0"

//terminal 1
ros2 launch diff_wheeled_robot_gazebo diff_wheeled_gazebo_full.launch
//terminal 2
ros2 launch diff_wheeled_robot_control_keyboard_teleop.launch
//terminal 3
rviz
