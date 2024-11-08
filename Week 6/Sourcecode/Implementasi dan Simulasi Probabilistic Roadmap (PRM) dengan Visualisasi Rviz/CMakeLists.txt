cmake_minimum_required(VERSION 3.5)
project(prm_simulation)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(prm src/prm.cpp)

ament_target_dependencies(prm rclcpp)

install(TARGETS prm
    DESTINATION lib/${PROJECT_NAME})

ament_package()
