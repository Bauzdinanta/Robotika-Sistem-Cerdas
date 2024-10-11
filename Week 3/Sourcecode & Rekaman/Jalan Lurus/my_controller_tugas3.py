# controller.py

from controller import Robot

if __name__ == "__main__":
 
    robot = Robot()
    TIME_STEP = 64
    
    left_motor = robot.getDevice('left wheel motor')
    right_motor= robot.getDevice('right wheel motor')
    
    # Set motors to velocity control
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    # Set initial speed (e.g., 1.0 rad/s)
    speed = 5.0
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)
    
    # Main loop
    while robot.step(TIME_STEP) != -1:
        pass  # Robot bergerak maju tanpa henti
