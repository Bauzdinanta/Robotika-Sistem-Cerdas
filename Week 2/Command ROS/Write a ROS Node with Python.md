cd catkin_ws/src/my_robot_controller/
ls
mkdir scripts
ls
cd scripts/
touch my_first_node.py
chmod +x my_first_node.py
ls
cd ../../..
cd src/
code .
cd my_robot_controller/scripts/
ls
python3 my_first_node.py
roscore
gedit ~/.bashrc
python3 my_first_node.py
./my_first_node.py
cd
rosrun my_robot_controller my_first_node.py
rosnode list
rosnode kill /test_node
rqt_graph
