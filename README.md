# ROS2 Gazebo Simulation Tutorial Series

A beginner-friendly ROS2 project designed to bridge the gap between turtlesim and real-world robot simulation using Gazebo.

This project introduces a structured learning pipeline using progressively complex environments.

## Overview
This project provides a structured ROS2 learning pathway from turtlesim to Gazebo simulation.

It introduces three environments:
- Clean World → Basic motion
- Obstacle World → Interaction
- Sensor World → Lidar and data handling

## Learning Flow

turtlesim → Basic Control → Gazebo Simulation → Obstacles → Sensors → RViz Visualization

## Repository Structure

- worlds/ → Simulation environments (SDF)
- models/ → Robot model (SDF)
- urdf/ → Robot description (URDF)
- launch/ → Launch files
- images/ → Screenshots and diagrams

## Motivation

This project aims to improve beginner onboarding in ROS2 by providing a smooth transition from abstract learning tools to realistic simulation environments.

## Future Work

- Integration with Navigation2 (Nav2)
- Advanced sensor simulation
- Autonomous navigation examples

## Robot
<ul>
<li>A simple Mobile Robot.</li>
<li>Easier for understanding.</li>
</ul>

![AMR](images/amr.png)

## Simulation Worlds

### Clean World
Basic environment for learning robot motion using `/cmd_vel`.

![Clean World](images/clean_world.png)

---

### Obstacle World
Introduces obstacles for interaction and navigation.

![Obstacle World](images/obstacle_world.png)

---

### Sensor World
Structured environment for Lidar perception and rosbag recording.

![Sensor World](images/sensor_world.png)
