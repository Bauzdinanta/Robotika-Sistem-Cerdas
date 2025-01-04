Assalamualaikum wr.wb

Pada video kedua kali ini, saya akan menunjukkan bagaimana cara ROS berkomunikasi

pertama, pastikan untuk clone repository dengan perintah : 
git clone https://github.com/PacktPublishing/Mastering-ROS-for-Robotics-Programming-Third-edition

Simulasi pertama
Publisher dan Subscriber dengan Topic
Terminal 1:
ros2 run mastering_ros_demo_pkg demo_topic_publisher
Tujuan: Menjalankan node yang mempublikasikan pesan ke sebuah topic tertentu.

Terminal 2:
ros2 run mastering_ros_demo_pkg demo_topic_subscriber
Tujuan: Menjalankan node yang berlangganan ke topic yang sama untuk menerima dan memproses pesan.

Hasil: Jika berhasil, subscriber akan mencetak atau memproses pesan yang diterima dari publisher.

Simulasi kedua 

Publisher dan Subscriber dengan Custom Message
Terminal 1:
ros2 run mastering_ros_demo_pkg demo_msg_publisher
Tujuan: Memublikasikan pesan khusus (custom message) yang didefinisikan dalam package ini ke sebuah topic.

Terminal 2:
ros2 run mastering_ros_demo_pkg demo_msg_subscriber
Tujuan: Berlangganan ke topic yang sama untuk menerima dan memproses pesan khusus tersebut.
Hasil: Anda dapat melihat demonstrasi penggunaan custom message di ROS 2.

Simulasi ketiga
Service Server dan Client
Terminal 1:
ros2 run mastering_ros_demo_pkg demo_service_server
Tujuan: Menjalankan node service server yang menyediakan sebuah layanan (service).

Terminal 2:
ros2 run mastering_ros_demo_pkg demo_service_client
Tujuan: Menjalankan node service client untuk memanggil layanan dari server.
Hasil: Client akan mengirim permintaan ke server, dan server akan merespons sesuai dengan logika yang telah didefinisikan.

Simulasi keempat
Action Client dan Server
Terminal 1:
ros2 run mastering_ros_demo_pkg demo_action_client 10 1
Tujuan: Menjalankan action client yang meminta sebuah aksi dengan parameter (misalnya 10 dan 1 sebagai input).

Terminal 2:
ros2 run mastering_ros_demo_pkg demo_action_server
Tujuan: Menjalankan action server yang menerima permintaan dari client dan mengeksekusi aksi sesuai logika yang telah didefinisikan.

Parameter 10 dan 1 mungkin mengacu pada jumlah tugas dan interval waktu eksekusi.
Client mengirimkan permintaan ke server, yang kemudian memproses aksi dan memberikan hasil atau pembaruan status.
Hasil: Action server akan melaporkan status eksekusi atau hasil akhir kepada client.

demikian simulasi yang dapat saya sampaikan pada video kedua saya, terimakasih
