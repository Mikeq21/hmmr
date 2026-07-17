import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, String


class HealthMonitor(Node):

    def __init__(self):
        super().__init__('hmmr_health_monitor')

        self.battery_pub = self.create_publisher(
            Float32,
            '/hmmr/battery',
            10
        )

        self.status_pub = self.create_publisher(
            String,
            '/hmmr/status',
            10
        )

        self.battery = 100.0

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

        self.get_logger().info(
            'HMMR Health Monitor started'
        )


    def publish_status(self):

        self.battery -= 0.1

        battery_msg = Float32()
        battery_msg.data = self.battery

        self.battery_pub.publish(
            battery_msg
        )


        status_msg = String()
        status_msg.data = (
            "HMMR operational"
        )

        self.status_pub.publish(
            status_msg
        )


def main(args=None):

    rclpy.init(args=args)

    node = HealthMonitor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
