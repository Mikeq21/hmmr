# `hmmr_core`

## Purpose

`hmmr_core` contains high-level robot logic that coordinates mission mode and reports a consolidated view of robot state. It currently contains two ROS 2 Python nodes.

## Nodes

### `mission_manager`

Entry point:

```bash
ros2 run hmmr_core mission_manager
```

Implementation: `hmmr_core/mission_manager.py`

- Publishes `/hmmr/mission_mode` as `std_msgs/msg/String`.
- Subscribes to `/hmmr/battery` as `std_msgs/msg/Float32`.
- Evaluates battery level on a 2-second timer.
- Selects `FAULT` below 5%, `RETURNING_HOME` below 20%, or `INSPECTING` otherwise.

**Important:** these are currently mode labels only. The node does not yet command a navigation stack, initiate an actual return-home action, or verify arrival. Its initial battery value is 100.0 until a battery message is received.

### `robot_state`

Entry point:

```bash
ros2 run hmmr_core robot_state
```

Implementation: `hmmr_core/robot_state.py`

- Subscribes to `/hmmr/battery` (`Float32`), `/hmmr/status` (`String`), and `/hmmr/mission_mode` (`String`).
- Logs battery, mission mode, and status together every 2 seconds.
- Holds initial placeholder values until messages arrive.

This node currently reports state through ROS logs; it does not publish a combined state topic.

## Topic interfaces

| Topic | Type | Direction | Used by |
|---|---|---|---|
| `/hmmr/battery` | `std_msgs/msg/Float32` | Subscribe | `mission_manager`, `robot_state` |
| `/hmmr/mission_mode` | `std_msgs/msg/String` | `mission_manager`: publish; `robot_state`: subscribe | Mission mode reporting |
| `/hmmr/status` | `std_msgs/msg/String` | Subscribe | `robot_state` |

## Dependencies and run order

The nodes use `rclpy` and standard messages from `std_msgs`. For the prototype behavior to be observable, run `health_monitor` from `hmmr_diagnostics` alongside these nodes. The nodes are not automatically launched by the current `hmmr_bringup` launch file.
