from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("ar3", package_name="ar3_moveit_config")
        .robot_description(
            file_path="config/ar3.urdf.xacro", 
            mappings={
                "serial_port": "/dev/ttyCobot1"
            }
        )
    ).to_moveit_configs()
    return generate_demo_launch(moveit_config)
