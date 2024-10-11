# stop_on_obstacle_controller.py

from controller import Robot

# Constants
TIME_STEP = 64  # ms
THRESHOLD = 80  # Sesuaikan dengan sensitivitas sensor

# Create the Robot instance
robot = Robot()

# Initialize motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set initial kecepatan
speed = 5.0
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)

# Initialize proximity sensors
proximity_sensors = []
for i in range(8):  # e-puck memiliki 8 sensor proximity
    sensor = robot.getDevice(f'ps{i}')
    sensor.enable(TIME_STEP)
    proximity_sensors.append(sensor)

# Fungsi untuk mengecek apakah ada objek di depan
def is_obstacle_ahead():
    # Biasanya sensor ps2, ps3 adalah sensor depan
    front_sensors = [proximity_sensors[2].getValue(), proximity_sensors[3].getValue()]
    for value in front_sensors:
        if value > THRESHOLD:
            return True
    return False

# Main loop
while robot.step(TIME_STEP) != -1:
    if is_obstacle_ahead():
        # Hentikan robot
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("Objek terdeteksi! Robot dihentikan.")
        break  # Keluar dari loop jika robot dihentikan
