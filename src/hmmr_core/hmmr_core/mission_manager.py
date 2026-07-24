import rclpy

from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String


class MissionManager(Node):

    def __init__(self):

        super().__init__("mission_manager")

        self.publisher = self.create_publisher(
            String,
            "/hmmr/mission_mode",
            10
        )

        self.battery = 100.0

        self.battery_sub = self.create_subscription(
            Float32,
            "/hmmr/battery",
            self.battery_callback,
            10
        )

        self.mode = "IDLE"

        self.timer = self.create_timer(
            2.0,
            self.publish_mode
        )

        self.get_logger().info(
            "Mission Manager started."
        )


    def publish_mode(self):

        if self.battery < 5:
           self.mode = "FAULT"

        elif self.battery < 20:
           self.mode = "RETURNING_HOME"

        else:
           self.mode = "INSPECTING"

        msg = String()
        msg.data = self.mode

        self.publisher.publish(msg)

    def battery_callback(self, msg):
        self.battery = msg.data


def main(args=None):

    rclpy.init(args=args)

    node = MissionManager()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
