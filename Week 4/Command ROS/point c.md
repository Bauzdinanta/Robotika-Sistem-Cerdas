ros2 pkg create \
--build-type ament_cmake \
--dependencies moveit_ros_planning_interface rclcpp \
--node-name hello_moveit hello_moveit

colcon build --mixin debug

cd ~/ws_moveit
source install/setup.bash

ros2 run hello_moveit hello_moveit

colcon build --mixin debug
ros2 launch moveit2_tutorials demo.launch.py

ros2 run hello_moveit hello_moveit
