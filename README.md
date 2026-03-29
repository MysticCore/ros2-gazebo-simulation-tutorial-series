# ROS2 Gazebo Tutorial Series:

This repository contains simulation environments and a simple mobile robot designed to help beginners transition from turtlesim to Gazebo.
Also the steps for creating a simulation.

## Contents:
- Clean World: Basic robot movement
- Obstacle World: Interaction with obstacles
- Sensor World: Maze type world with Lidar and rosbag usage

## Requirements:
- ROS2 Humble/Jazzy
- Ignition or Gazebo SIm

## Robot
![AMR](robot/amr.png)

## Worlds
### Clean World
    • Simple Gazebo environment using SDF and URDF files of the world (walls included) and robot, respectively
    • Robot movement using /cmd_vel
    • Direct mapping from TurtleSim concepts
![Clean World](worlds/clean_world/clean_world.png)
### Obstacle World
    • Add stationary obstacles.
    • Implement simple sensor-based obstacle avoidance
![Obstacle World](worlds/obstacle_world/obstacle_world.png)
### Sensor World
    • Implement simple sensor-based obstacle avoidance using real-time LiDAR data
    • Record and playback data using ‘ros2 bag‘
    • Visualise sensor data using Rviz
![Sensor World](worlds/sensor_world/sensor_world.png)
