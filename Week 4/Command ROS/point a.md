Install ROS 2 and colcon :
source /opt/ros/iron/setup.bash

Install rosdep to install system dependencies :
sudo apt install python3-rosdep

Once you have ROS 2 installed, make sure you have the most up to date packages:
sudo rosdep init
rosdep update
sudo apt update
sudo apt dist-upgrade

Install Colcon the ROS 2 build system with mixin:
sudo apt install python3-colcon-common-extensions
sudo apt install python3-colcon-mixin
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default

Install vcstool :
sudo apt install python3-vcstool

Create A Colcon Workspace :
mkdir -p ~/ws_moveit/src

Download Source Code of MoveIt and the Tutorials :
cd ~/ws_moveit/src
git clone -b <branch> https://github.com/moveit/moveit2_tutorials

Download the source code for the rest of MoveIt :
vcs import --recursive < moveit2_tutorials/moveit2_tutorials.repos

Remove all previously installed moveit binaries :
sudo apt remove ros-$ROS_DISTRO-moveit*

Install MoveIt and all of its dependencies :
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y

Configure your Colcon workspace :
cd ~/ws_moveit
colcon build --mixin release

Source the Colcon workspace:
source ~/ws_moveit/install/setup.bash

Optional: add the previous command to your .bashrc:
echo 'source ~/ws_moveit/install/setup.bash' >> ~/.bashrc
