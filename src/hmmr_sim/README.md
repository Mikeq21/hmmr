# `hmmr_sim`

## Purpose

`hmmr_sim` is intended to contain simulation-specific assets and configuration for developing and validating HMMR before relying on physical hardware.

## Current state

This package is currently a ROS 2 Python package scaffold. It does not yet contain simulator worlds, simulator-specific robot plugins, simulation launch files, or registered console-script nodes.

The robot’s current Xacro description lives in `hmmr_description`; keeping reusable robot geometry separate from simulator worlds and simulation-only configuration avoids tying the core model to one simulator.

## Intended use

As simulation is added, document the simulator/version, world files, physics assumptions, sensor and drive plugins, launch commands, and known simplifications here. Simulation should support repeatable tests of health monitoring, fault handling, and eventually the leave-waypoint-return-to-repair-station mission.

## Files

The package currently contains standard ament Python packaging files, a resource marker, an initializer, a README, and generated test scaffolding.
