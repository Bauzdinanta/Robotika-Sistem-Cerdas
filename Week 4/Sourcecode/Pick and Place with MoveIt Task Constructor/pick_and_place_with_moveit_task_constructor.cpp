#include <moveit/task_constructor/task_constructor.h>
#include <moveit/planning_interface/planning_interface.h>
#include <moveit_visual_tools/moveit_visual_tools.h>
#include <rclcpp/rclcpp.hpp>

using namespace moveit::task_constructor;

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("pick_and_place");
    MoveItVisualTools visual_tools(node, "base_link");
    
    // Create a Task
    Task task("pick_and_place_task");

    // Define your robot's planning scene
    task.loadRobotModel("panda");
    
    // Define pick and place steps
    auto pick = task.add(std::make_shared<Pick>("object"));
    auto place = task.add(std::make_shared<Place>("object"));
    
    // Add steps to the task
    pick->setGroup("manipulator");
    place->setGroup("manipulator");
    
    // Set up constraints and parameters for picking and placing
    pick->setMaxAttempts(5);
    place->setMaxAttempts(5);

    // Execute the task
    if (task.plan())
    {
        task.execute();
    }
    else
    {
        RCLCPP_ERROR(node->get_logger(), "Task planning failed");
    }

    rclcpp::shutdown();
    return 0;
}
