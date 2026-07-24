import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import String


class RobotState(Node):

    def __init__(self):

        super().__init__("robot_state")

        self.battery = 100.0
        self.status = "Unknown"
        self.mission = "UNKNOWN"

        self.create_subscription(
            Float32,
            "/hmmr/battery",
            self.battery_callback,
            10
        )

        self.create_subscription(
            String,
            "/hmmr/status",
            self.status_callback,
            10
        )

        self.create_subscription(
            String,
            "/hmmr/mission_mode",
            self.mission_callback,
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.print_state
        )

        self.get_logger().info(
            "Robot State Manager started."
        )


    def battery_callback(self, msg):
        self.battery = msg.data


    def status_callback(self, msg):
        self.status = msg.data

    def mission_callback(self, msg):
        self.mission = msg.data

    def print_state(self):
        self.get_logger().info(
            f"Battery: {self.battery:.1f}% | "
            f"Mission: {self.mission} | "
            f" Status: {self.status}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotState()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
