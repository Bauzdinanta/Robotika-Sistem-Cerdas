//terminal 1
git clone https://github.com/nishadg246/Probabilistic-Roadmap.git
cd ~/ros2_ws/src
cp -r ~/Probabilistic-Roadmap .
cd ~/ros2_ws
colcon build --packages-select probabilistic_roadmap
ls ~/ros2_ws/src/Probabilistic-Roadmap
source ~/ros2_ws/install/setup.bash

//terminal 2
source ~/ros2_ws/install/setup.bash
~/ros2_ws/install/prm_simulation/lib/prm_simulation/prm

//terminal 3
rviz2

//terminal 4
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 1 map base_link
