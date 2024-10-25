cd ~/ws_moveit
colcon build --mixin debug

cd ~/ws_moveit
source /opt/ros/rolling/setup.bash
colcon build --mixin debug

cd ~/ws_moveit
source install/setup.bash
ros2 launch moveit2_tutorials demo.launch.py

cd ~/ws_moveit
source install/setup.bash
ros2 run hello_moveit hello_moveit
