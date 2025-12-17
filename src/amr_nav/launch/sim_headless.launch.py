from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="amr_nav",
            executable="dummy_node",
            output="screen",
        )
    ])
