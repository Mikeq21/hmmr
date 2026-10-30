# `hmmr_perception`

## Purpose

`hmmr_perception` is intended for interpreting HMMR sensor data to understand the robot’s surroundings and identify conditions relevant to inspection and maintenance.

Potential future responsibilities include processing camera/LiDAR data, identifying environmental or structural anomalies, and producing observations that can be evaluated by the diagnostics and mission layers.

## Current state

This package is currently a ROS 2 Python package scaffold. It has no registered console-script nodes, sensor-processing implementation, or defined perception topics.

## Design boundary

Perception should publish observations with clear confidence and frame/timestamp semantics. It should not independently take over mission decisions or directly implement low-level motion control. The exact sensors and algorithms remain to be selected as the robot model and simulation capabilities mature.

## Files

The package currently contains standard ament Python packaging files, a resource marker, an initializer, a README, and generated test scaffolding.
