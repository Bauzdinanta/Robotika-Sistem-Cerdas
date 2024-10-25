from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pick_and_place',
            executable='pick_and_place_with_moveit_task_constructor',
            output='screen',
        ),
    ])
