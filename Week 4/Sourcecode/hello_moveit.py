import rclpy
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose

def main():
    rclpy.init()
    move_group = MoveGroupCommander("manipulator")

    target_pose = Pose()
    target_pose.orientation.w = 1.0
    target_pose.position.x = 0.28
    target_pose.position.y = -0.2
    target_pose.position.z = 0.5
    move_group.set_pose_target(target_pose)

    if move_group.plan():
        move_group.go(wait=True)
    else:
        print("Planning failed!")

    rclpy.shutdown()

if __name__ == '__main__':
    main()
