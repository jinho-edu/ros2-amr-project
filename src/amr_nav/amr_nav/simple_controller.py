import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SimpleController(Node):
    def __init__(self):
        super().__init__('simple_controller')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_cmd)

    def publish_cmd(self):
        msg = Twist()
        msg.linear.x = 0.1
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = SimpleController()
    rclpy.spin(node)
    rclpy.shutdown()
