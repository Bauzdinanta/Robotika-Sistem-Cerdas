sudo apt install git

pip install conan==1.59.0
conan remote add conancenter https://center.conan.io

sudo apt install python-is-python3 \
ros-noetic-amcl \
ros-noetic-base-local-planner \
ros-noetic-map-server \
ros-noetic-move-base \
ros-noetic-navfn \
libgoogle-glog-dev

git clone https://github.com/ai-winter/ros_motion_planning.git

cd scripts/
./build.sh  # you may need to install catkin-tools using: sudo apt install python-catkin-tools

cd scripts/
./main.sh

cd scripts/
./killpro.sh

# 1. Replace with user_config_multi.yaml in main.sh
# 2. Wait for initialization
# 3. Publish goals
rosrun sim_env goal_publisher.py