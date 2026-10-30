# `hmmr_bringup`

## Purpose

`hmmr_bringup` contains launch files used to start and configure HMMR ROS 2 components. Its current launch file publishes the robot model description and its link transforms.

## Files

- `launch/hmmr_description.launch.py` — locates `hmmr_description/urdf/hmmr.urdf.xacro`, expands it with Xacro, and starts `robot_state_publisher` with the resulting `robot_description` parameter.
- `package.xml` — ROS package metadata and build type.
- `setup.py` — installs this package and its `launch/*.launch.py` files into the ROS package share directory.

## Launch

From the ROS 2 Humble container, after building the workspace and sourcing its overlay:

```bash
ros2 launch hmmr_bringup hmmr_description.launch.py
```

The launch file currently starts only `robot_state_publisher`. It does **not** start RViz, Foxglove Bridge, the health monitor, mission manager, navigation, or a simulator.

## Current limitations

The launch file declares a `DeclareLaunchArgument` import but does not currently declare or use any launch arguments. The description is provided through a Xacro command substitution. Ensure the `xacro` and `robot_state_publisher` packages are installed in the ROS environment.
