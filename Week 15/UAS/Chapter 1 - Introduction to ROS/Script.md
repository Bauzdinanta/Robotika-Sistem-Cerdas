Assalamualaikum wr.wb

"Halo semuanya! Dalam video ini, kita akan mengenal apa itu ROS (Robot Operating System) dan bagaimana cara menginstalnya di sistem operasi Ubuntu. Kalau kalian tertarik dengan dunia robotika, ROS adalah salah satu platform yang wajib kalian pelajari!"

Apa itu ROS?
"ROS atau Robot Operating System adalah kerangka kerja perangkat lunak open-source yang digunakan untuk mengembangkan aplikasi robotika. ROS membantu pengembang mengontrol robot dengan lebih mudah, menyediakan tools dan library untuk berbagai keperluan seperti pemetaan, navigasi, dan manipulasi objek."

Kelebihan ROS:
-Mendukung berbagai jenis robot.
-Komunitas global yang besar dan aktif.
-Banyak library siap pakai.
-Mudah diintegrasikan dengan sensor, aktuator, dan algoritma AI.

Distribusi ROS: 
"ROS memiliki beberapa distribusi yang dirilis secara berkala. Misalnya:

-ROS 1: Melodic, Noetic.
-ROS 2: Foxy, Galactic, Humble, dan Iron."

Bagian 2: Cara Install ROS
"Sekarang kita akan masuk ke langkah-langkah instalasi ROS. Di sini, kita akan menginstal ROS 2 Humble di Ubuntu 22.04."

Pertama, pastikan sistem Ubuntu Anda sudah diperbarui:

sudo apt update
sudo apt upgrade

Tambahkan repositori ROS2:

sudo apt install software-properties-common
sudo add-apt-repository universe

Tambahkan GPG key ROS2:

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

Tambahkan repositori ROS2 ke sources list:

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Perbarui package list:

sudo apt update

Install ROS2 Humble (pilih salah satu opsi):
Untuk instalasi Desktop penuh (Recommended):

sudo apt install ros-humble-desktop

Atau untuk instalasi Base saja (minimal):

sudo apt install ros-humble-ros-base

Install development tools:

sudo apt install ros-dev-tools

Tambahkan setup ROS2 ke ~/.bashrc agar otomatis dijalankan setiap kali terminal dibuka:

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

"Sekarang kalian sudah memiliki ROS 2 Humble terinstal di sistem kalian! Dengan ROS, kalian bisa mulai mengembangkan aplikasi robotika yang canggih dan kreatif. Jangan lupa untuk bergabung dengan komunitas ROS untuk belajar lebih lanjut dan berbagi pengalaman!"
