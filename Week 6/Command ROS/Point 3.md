//terminal 1
git clone https://github.com/Malintha/rrt-ros
cd rrt-ros
catkin_make
source devel/setup.bash

//terminal 2
roscore

//terminal 3
rosrun rrt-planning rrt

//terminal 4
rosrun rviz rviz
