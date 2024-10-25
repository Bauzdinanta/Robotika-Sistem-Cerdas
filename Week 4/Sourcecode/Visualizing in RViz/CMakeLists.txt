cmake_minimum_required(VERSION 3.5)
project(hello_moveit)

# Default to C11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_visual_tools REQUIRED)

include_directories(include)

# Create the executable
add_executable(hello_moveit src/hello_moveit.cpp)

# Link the libraries
ament_target_dependencies(hello_moveit
  rclcpp
  moveit_ros_planning_interface
  moveit_visual_tools
)

install(TARGETS
  hello_moveit
  DESTINATION lib/${PROJECT_NAME})

ament_package()
