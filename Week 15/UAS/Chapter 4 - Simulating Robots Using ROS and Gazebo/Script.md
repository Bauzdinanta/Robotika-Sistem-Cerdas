Assalamualaikum wr.wb 

pada video keempat ini saya akan menunjukan simulasi robot menggunakan ROS dan Gazebo

pastikan kalian sudah clone git

buka terminal, kemudian masuk ke folder Chapter 4

simulasi pertama adalah menggerakkan lengan robot

pada terminal 1 jalankan perintah :
roslaunch seven_dof_arm_gazebo seven_dof_arm_gazebo_control.launch
pada terminal 2 jalankan perintah :
rostopic pub /seven_dof_arm/joint4_position_controller/command std_msgs/float64 "data: 1.0"

simulasi kedua adalah menggerakkan posisi robot 

pada terminal 1 jalankan perintah :
roslaunch diff_wheeled_robot_gazebo diff_wheeled_gazebo_full.launch
pada terminal 2 jalankan perintah :
roslaunch diff_wheeled_robot_control_keyboard_teleop.launch
pada terminal 3 jalankan perintah :
rviz

kemudian ubah fixed frame menjadi "odom"

demikian simulasi yang dapat saya sampaikan, terimakasih
