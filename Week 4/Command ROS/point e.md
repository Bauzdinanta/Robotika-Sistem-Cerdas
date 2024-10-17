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
