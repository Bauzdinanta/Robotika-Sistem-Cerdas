#include <moveit_visual_tools/moveit_visual_tools.h>
#include <rclcpp/rclcpp.hpp>
#include <thread>

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("hello_moveit");

    moveit_visual_tools::MoveItVisualTools visual_tools(node, "base_link");
    visual_tools.deleteAllMarkers();
    visual_tools.loadRemoteControl();

    auto const draw_title = [&visual_tools](auto text) {
        auto const text_pose = [] {
            auto msg = Eigen::Isometry3d::Identity();
            msg.translation().z() = 1.0;  // Place text 1m above the base link
            return msg;
        }();
        visual_tools.publishText(text_pose, text, rviz_visual_tools::WHITE, rviz_visual_tools::XLARGE);
    };

    draw_title("Hello MoveIt!");
    visual_tools.trigger();

    rclcpp::shutdown();
    return 0;
}
