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
![AMR](images/amr.png)

## Worlds
### Clean World
<ul>
  <li>Simple Gazebo environment using SDF and URDF files of the world (walls included) and robot, respectively</li>
  <li>Robot movement using /cmd_vel</li>
  <li>Direct mapping from TurtleSim concepts</li>
</ul>

![Clean World](images/clean_world.png)

### Obstacle World
<ul>
    <li>Add stationary obstacles.</li>
    <li>Implement simple sensor-based obstacle avoidance</li>
</ul>

![Obstacle World](images/obstacle_world.png)

### Sensor World
<ul>
    <li>Implement simple sensor-based obstacle avoidance using real-time LiDAR data</li>
    <li>Record and playback data using ‘ros2 bag‘</li>
    <li>Visualise sensor data using Rviz</li>
</ul>

![Sensor World](images/sensor_world.png)
