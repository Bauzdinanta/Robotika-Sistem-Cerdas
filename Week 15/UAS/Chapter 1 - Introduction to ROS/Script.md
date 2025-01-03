Pengenalan ROS dan Cara Installnya di Ubuntu
Pendahuluan
"Halo semuanya! Dalam video ini, kita akan mengenal apa itu ROS (Robot Operating System) dan bagaimana cara menginstalnya di sistem operasi Ubuntu. Kalau kalian tertarik dengan dunia robotika, ROS adalah salah satu platform yang wajib kalian pelajari!"

Bagian 1: 
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

Langkah 1: Update Sistem

sudo apt update && sudo apt upgrade -y

Langkah 2: Tambahkan Repository ROS

sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update

Langkah 3: Tambahkan GPG Key dan Repository ROS 2

sudo apt install curl -y
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update

Langkah 4: Instalasi ROS

sudo apt install ros-humble-desktop
"Paket ini akan menginstal ROS 2 Humble dengan semua fitur utama seperti navigasi, pemetaan, dan kontrol robot."

Langkah 5: Set Variabel Lingkungan
Tambahkan konfigurasi ke file ~/.bashrc:

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

Langkah 6: Verifikasi Instalasi
Untuk memeriksa instalasi, jalankan:

ros2 --version

Penutup
"Sekarang kalian sudah memiliki ROS 2 Humble terinstal di sistem kalian! Dengan ROS, kalian bisa mulai mengembangkan aplikasi robotika yang canggih dan kreatif. Jangan lupa untuk bergabung dengan komunitas ROS untuk belajar lebih lanjut dan berbagi pengalaman!"
