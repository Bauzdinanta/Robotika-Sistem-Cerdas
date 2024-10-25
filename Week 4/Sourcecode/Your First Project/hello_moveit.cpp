#include <rclcpp/rclcpp.hpp>
#include <moveit/planning_interface/planning_interface.h>
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("hello_move_it");

    moveit::planning_interface::MoveGroupInterface move_group(node, "manipulator");

    // Set a target pose
    geometry_msgs::msg::Pose target_pose;
    target_pose.orientation.w = 1.0;
    target_pose.position.x = 0.28;
    target_pose.position.y = -0.2;
    target_pose.position.z = 0.5;

    move_group.setPoseTarget(target_pose);

    // Plan and execute
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    bool success = (move_group.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);

    if (success) {
        move_group.execute(my_plan);
    } else {
        RCLCPP_ERROR(node->get_logger(), "Planning failed!");
    }

    rclcpp::shutdown();
    return 0;
}
