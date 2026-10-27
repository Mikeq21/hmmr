# `hmmr_navigation`

## Purpose

`hmmr_navigation` is intended to hold HMMR navigation behavior, including localization integration, route planning, waypoint execution, and autonomous return to a known repair-station pose.

## Current state

This package is currently a ROS 2 Python package scaffold. It has no registered console-script nodes and no implemented navigation behavior.

## Intended first milestone

A useful initial navigation milestone is deliberately small:

1. Start from a known pose near a repair station.
2. Navigate to one known waypoint.
3. Trigger a return-to-station request.
4. Confirm navigation reports success and the robot stops at the expected destination.

Mission decisions should remain in `hmmr_core`; navigation should execute goals and report outcomes. The current `mission_manager` only publishes mode strings and does not yet send navigation goals.

## Files

The package currently contains standard ament Python packaging files, a resource marker, an initializer, a README, and generated test scaffolding. No planner, localization node, launch file, map, or navigation configuration is currently present.
