import rclpy

from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String


MISSION_UPDATE_RATE = 2.0  # Hz


class MissionManager(Node):

    def __init__(self):
        super().__init__("mission_manager")

        # Publishers
        self.publisher = self.create_publisher(
            String,
            "/hmmr/mission_mode",
            10,
        )

        # Subscribers
        self.battery_sub = self.create_subscription(
            Float32,
            "/hmmr/battery",
            self.battery_callback,
            10,
        )

        # Robot State
        self.battery = 100.0
        self.mode = None

        # Main mission evaluation loop
        self.timer = self.create_timer(
            1.0 / MISSION_UPDATE_RATE,
            self.evaluate_mission,
        )

        self.get_logger().info("Mission Manager started.")

    def evaluate_mission(self):
        """Determine the robot's current mission based on battery level."""

        if self.battery < 5.0:
            new_mode = "FAULT"

        elif self.battery < 20.0:
            new_mode = "RETURNING_HOME"

        else:
            new_mode = "INSPECTING"

        # Only publish when the mission changes.
        if new_mode != self.mode:
            self.mode = new_mode

            msg = String()
            msg.data = self.mode

            self.publisher.publish(msg)

            self.get_logger().info(
                f"Mission changed to: {self.mode}"
            )

    def battery_callback(self, msg):
        """Store the latest battery percentage."""
        self.battery = msg.data


def main(args=None):
    rclpy.init(args=args)

    node = MissionManager()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
