# circular_motion_controller.py

from controller import Robot

# Constants
TIME_STEP = 64  # ms

# Create the Robot instance
robot = Robot()

# Initialize motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motors to velocity control
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan roda dengan roda kiri lebih lambat
left_speed = 5.0  # rad/s
right_speed = 6.28  # rad/s

left_motor.setVelocity(left_speed)
right_motor.setVelocity(right_speed)

# Main loop
while robot.step(TIME_STEP) != -1:
    pass  # Robot bergerak melingkar
