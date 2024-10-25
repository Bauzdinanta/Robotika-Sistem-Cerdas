cmake_minimum_required(VERSION 3.5)
project(pick_and_place)

# Default to C11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_task_constructor REQUIRED)
find_package(moveit_visual_tools REQUIRED)

include_directories(include)

# Create the executable
add_executable(pick_and_place_with_moveit_task_constructor src/pick_and_place_with_moveit_task_constructor.cpp)

# Link the libraries
ament_target_dependencies(pick_and_place_with_moveit_task_constructor
  rclcpp
  moveit_ros_planning_interface
  moveit_task_constructor
  moveit_visual_tools
)

install(TARGETS
  pick_and_place_with_moveit_task_constructor
  DESTINATION lib/${PROJECT_NAME})

ament_package()
