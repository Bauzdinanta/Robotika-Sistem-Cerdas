pip3 install numpy matplotlib networkx scipy pyyaml
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_pyhton prm_simulation

nano prm.py
nano params.yaml
nano params.launch
nano ~/ros2_ws/src/prm_simulation/setup.py

cd ~/ros2_ws
colcon build

source install/setup.bash

ros2 launch prm_simulation prm_launch.py
