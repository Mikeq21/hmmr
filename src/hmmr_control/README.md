# `hmmr_control`

## Purpose

`hmmr_control` is the intended home for HMMR motion and actuator-control logic—for example, translating navigation commands into wheel or drive commands once the robot model and simulation interfaces support them.

## Current state

This package is currently a ROS 2 Python package scaffold. Its `setup.py` does not register any console-script nodes, and the package contains no implemented control node yet.

## Intended responsibility

Keep low-level movement execution here rather than placing it in the mission manager. The mission manager should decide **what the robot should do**; control components should handle **how movement commands are executed**.

## Files

- `hmmr_control/` — Python package initializer.
- `package.xml` — ROS package metadata.
- `setup.py` and `setup.cfg` — Python/ament packaging configuration.
- `resource/hmmr_control` — ament package-index marker.
- `test/` — generated lint/test scaffolding.
