from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        DeclareLaunchArgument(
            name='log_level', default_value='debug',
            description='Logging level'
        ),
        # Node(
        #     package='pointcloud_to_laserscan', node_executable='dummy_pointcloud_publisher',
        #     remappings=[('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
        #     parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 2.0, 'cloud_size': 500}],
        #     node_name='cloud_publisher'
        # ),
        # Node(
        #     package='tf2_ros',
        #     node_executable='static_transform_publisher',
        #     node_name='static_transform_publisher',
        #     arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'cloud']
        # ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/camera/depth/points'),
                        ('scan', '/flattened_scan')],
            parameters=[{
                'target_frame': 'camera_0_link',
                'transform_tolerance': 0.01,
                'min_height': -0.1,
                'max_height': 0.75,
                'angle_min': -0.78539816339,  # -M_PI/4
                'angle_max': 0.78539816339,  # M_PI/2
                'angle_increment': 0.00245436926,  # M_PI/360.0
                'scan_time': 0.03333,
                'range_min': 0.45,
                'range_max': 6.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    ])
