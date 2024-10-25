import rclpy
from moveit_commander import MoveGroupCommander

def main():
    rclpy.init()
    task_group = MoveGroupCommander("manipulator")
    
    # Define your pick and place logic
    # task_group.pick(object_name)
    # task_group.place(object_name)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
