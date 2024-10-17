sudo apt install python3-rosdep python3-colcon-common-extensions python3-colcon-mixin python3-vcstool
sudo rosdep init
rosdep update
sudo apt update
sudo apt dist-upgrade
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default

mkdir -p ~/ws_moveit/src
cd ~/ws_moveit/src

git clone -b <branch> https://github.com/moveit/moveit2_tutorials
vcs import --recursive < moveit2_tutorials/moveit2_tutorials.repos

sudo apt remove ros-$ROS_DISTRO-moveit*
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y

cd ~/ws_moveit
colcon build --mixin release

colcon build --executor sequential

source ~/ws_moveit/install/setup.bash
echo 'source ~/ws_moveit/install/setup.bash' >> ~/.bashrc
