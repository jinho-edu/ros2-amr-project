from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package="amr_nav",
        #     executable="dummy_node",
        #     output="screen",
        # )
        Node(package='amr_nav', executable='simple_controller'),
        Node(package='amr_nav', executable='node_health'),
    ])

