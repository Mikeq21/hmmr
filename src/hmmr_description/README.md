# `hmmr_description`

## Purpose

`hmmr_description` defines the HMMR robot’s kinematic frame structure and basic geometry used by ROS visualization tools. It is the source of the robot model description consumed by `robot_state_publisher`.

## Files

- `urdf/hmmr.urdf.xacro` — Xacro model defining the `base_link` chassis and fixed sensor links.
- `rviz/hmmr.rviz` — RViz configuration file.
- `meshes/.gitkeep` — keeps the currently empty mesh directory in version control.
- `CMakeLists.txt` and `package.xml` — ament CMake package configuration.

## Model overview

The Xacro defines a rectangular base with nominal dimensions **0.55 m × 0.45 m × 0.25 m**, plus fixed links for:

| Link | Nominal placement relative to `base_link` |
|---|---|
| `camera_link` | `(0.25, 0, 0.30)` m |
| `lidar_link` | `(0, 0, 0.32)` m |
| `imu_link` | `(0, 0, 0.15)` m |
| `thermal_camera_link` | `(-0.20, 0, 0.25)` m |
| `environment_sensor_link` | `(0, 0.20, 0.20)` m |

The base includes visual geometry, collision geometry, and an inertial element. Sensor links currently have simple visual shapes to make their locations visible. The model does not yet define wheels, movable joints, sensor data plugins, transmissions, or a complete physics simulation.

## View the model

From the ROS 2 Humble container, build and source the workspace, then run:

```bash
ros2 launch hmmr_bringup hmmr_description.launch.py
```

That starts `robot_state_publisher` and makes the robot description and fixed transforms available. The launch file does not start RViz automatically. To use the saved RViz layout, launch RViz separately and load `rviz/hmmr.rviz` from this package’s source path, or provide the file path in your RViz workflow.

## Coordinate note

Sensor placements are expressed as joint origins relative to `base_link`. Treat these as the current prototype layout; validate them against the intended physical geometry before using them for navigation, perception, or simulation.
