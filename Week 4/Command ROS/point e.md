cd ~/ws_moveit/src
git clone -b <branch> https://github.com/moveit/moveit_task_constructor.git

rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO

cd ~/ws_moveit
colcon build --mixin release

ros2 launch moveit_task_constructor_demo demo.launch.py

ros2 launch moveit_task_constructor_demo run.launch.py exe:=cartesian
ros2 launch moveit_task_constructor_demo run.launch.py exe:=modular
ros2 launch moveit_task_constructor_demo run.launch.py exe:=pick_place_demo

ros2 pkg create \
--build-type ament_cmake \
--dependencies moveit_task_constructor_core rclcpp \
--node-name mtc_node mtc_tutorial

cd ~/ws_moveit
colcon build --mixin release
source ~/ws_moveit/install/setup.bash

ros2 launch moveit2_tutorials mtc_demo.launch.py

ros2 launch mtc_tutorial pick_place_demo.launch.py

ros2 launch moveit2_tutorials mtc_demo_minimal.launch.py

ros2 launch mtc_tutorial pick_place_demo.launch.py

ros2 launch moveit2_tutorials mtc_demo.launch.py

ros2 launch moveit2_tutorials pick_place_demo.launch.py
