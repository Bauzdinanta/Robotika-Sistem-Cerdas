#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit_visual_tools/moveit_visual_tools.h>
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <thread>

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("hello_moveit");
    moveit::planning_interface::MoveGroupInterface move_group_interface(node, "manipulator");

    // Initialize MoveIt Visual Tools
    moveit_visual_tools::MoveItVisualTools visual_tools(node, "base_link");
    visual_tools.deleteAllMarkers();
    visual_tools.loadRemoteControl();

    // Set target pose
    geometry_msgs::msg::Pose target_pose;
    target_pose.orientation.w = 1.0;
    target_pose.position.x = 0.28;
    target_pose.position.y = -0.2;
    target_pose.position.z = 0.5;
    move_group_interface.setPoseTarget(target_pose);

    // Plan and execute
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    if (move_group_interface.plan(plan)) {
        move_group_interface.execute(plan);
    } else {
        RCLCPP_ERROR(node->get_logger(), "Planning failed!");
    }

    rclcpp::shutdown();
    return 0;
}
