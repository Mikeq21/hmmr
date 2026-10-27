# `hmmr_diagnostics`

## Purpose

`hmmr_diagnostics` contains prototype health/status monitoring for HMMR. The current node simulates a changing battery value and publishes a basic operational status string.

## Node: `health_monitor`

Entry point:

```bash
ros2 run hmmr_diagnostics health_monitor
```

Implementation: `hmmr_diagnostics/health_monitor.py`

Every second, the node:

1. Decreases its internal battery value by 5.0 percentage points.
2. Publishes that value to `/hmmr/battery` as `std_msgs/msg/Float32`.
3. Publishes `HMMR operational` to `/hmmr/status` as `std_msgs/msg/String`.

## Topics

| Topic | Type | Direction |
|---|---|---|
| `/hmmr/battery` | `std_msgs/msg/Float32` | Publish |
| `/hmmr/status` | `std_msgs/msg/String` | Publish |

## Important prototype behavior

This is a test signal generator, not a hardware or simulator battery integration. The battery value starts at 100.0 and continues decreasing without a lower bound, while the status remains `HMMR operational` regardless of battery level. A future diagnostic implementation should define valid ranges, fault states, stale-data behavior, and the source of each health measurement.

The node can be run alongside `mission_manager` and `robot_state` to exercise the current topic flow.
