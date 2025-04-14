import os
from ament_index_python import get_package_share_directory as get_pkg_dir
from launch import LaunchDescription as LD
from launch.actions import DeclareLaunchArgument as DeclareArg
from launch.substitutions import LaunchConfiguration as LaunchConf
from launch_ros.actions import Node

def generate_launch_description():
    params_dir = LaunchConf(
        'params_dir',
        default=os.path.join(get_pkg_dir('opencv_pkg'), 'params', 'size.yaml')
    )
    
    return LD([
        DeclareArg(
            'params_dir',
            default_value=params_dir
        ),
        Node(
            package='opencv_pkg',
            executable='img_publish',
            name='img_publish',
            parameters=[params_dir],
            output='screen'
        ),
    ])
