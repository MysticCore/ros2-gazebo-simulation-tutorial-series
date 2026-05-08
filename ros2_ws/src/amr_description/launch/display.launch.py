from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

from launch.substitutions import Command
from launch.substitutions import PathJoinSubstitution

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Package Name
    package_name = "amr_description"

    # Robot Description Path
    robot_description_path = PathJoinSubstitution([
        FindPackageShare(package_name),
        "urdf",
        "amr.urdf.xacro"
    ])

    # Robot Description Parameter
    robot_description = Command([
        "xacro ",
        robot_description_path
    ])

    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{
            "robot_description": robot_description,
            "use_sim_time": True
        }]
    )

    # Joint State Publisher
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        output="screen"
    )

    # Start Gazebo
    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            "-s",
            "libgazebo_ros_factory.so"
        ],
        output="screen"
    )

    # Spawn Robot in Gazebo
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "amr"
        ],
        output="screen"
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        gazebo,
        spawn_robot
    ])