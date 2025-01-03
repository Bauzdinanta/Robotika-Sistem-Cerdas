//Update Sistem

sudo apt update && sudo apt upgrade -y

//Tambahkan Repository ROS

sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update

//Tambahkan GPG Key dan Repository ROS 2

sudo apt install curl -y
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update

//Instalasi ROS

sudo apt install ros-humble-desktop

//Set Variabel Lingkungan
//Tambahkan konfigurasi ke file ~/.bashrc:

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
