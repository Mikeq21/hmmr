# `hmmr_interfaces`

## Purpose

`hmmr_interfaces` is reserved for HMMR-specific ROS interfaces, such as custom message (`.msg`), service (`.srv`), and action (`.action`) definitions.

## Current state

The package currently contains its ROS package metadata and CMake configuration, but no custom interface definition files are present. The existing prototype nodes therefore use standard message types from `std_msgs`.

## Future interface design

Add a custom interface here when the data contract needs more structure than a standard message can provide. Before introducing an interface, document:

- the meaning and units of each field;
- valid ranges and enumerated states;
- which node publishes or serves it;
- which nodes subscribe to or call it;
- behavior for missing, stale, or invalid data.

Custom interfaces must be added to the package build configuration and declared as dependencies by any package that uses them. No custom interface is currently required to run the existing prototype nodes.
