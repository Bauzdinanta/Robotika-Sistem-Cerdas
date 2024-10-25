from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hello_move_it',
            executable='hello_move_it',
            output='screen',
        ),
    ])
