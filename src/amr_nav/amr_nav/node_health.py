import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class NodeHealth(Node):
    def __init__(self):
        super().__init__('node_health')
        self.pub = self.create_publisher(Bool, '/node_alive', 10)
        self.timer = self.create_timer(1.0, self.publish_health)

    def publish_health(self):
        msg = Bool()
        msg.data = True
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = NodeHealth()
    rclpy.spin(node)
    rclpy.shutdown()
