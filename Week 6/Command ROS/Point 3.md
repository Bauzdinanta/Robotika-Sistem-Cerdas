//terminal 1
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python rrt_planner
cd ~/ros2_ws
colcon build --packages-select rrt_planner
source install/setup.bash

//terminal 2
cd ~/ros2_ws/src
cd rrt_planner
mkdir -p resource
cd ~/ros2_ws/src/rrt_planner
touch rrt_planner/__init__.py
chmod +x ~/ros2_ws/src/rrt_planner/rrt_planner/rrt_node.py
cd ~/ros2_ws/src
rm -rf rrt_planner
ros2 pkg create --build-type ament_python rrt_planner
cd rrt_planner
mkdir -p resource
touch rrt_planner/__init__.py
nano rrt_planner/rrt_node.py
nano setup.py
nano package.xml
touch resource/rrt_planner
chmod +x rrt_planner/rrt_node.py
cd ~/ros2_ws
colcon build --packages-select rrt_planner --symlink-install
source install/setup.bash
ros2 run rrt_planner rrt_planner

//terminal 3
rviz2
