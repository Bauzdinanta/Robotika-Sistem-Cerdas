from controller import Robot

def run_robot(robot):
    # Inisialisasi waktu dan kecepatan
    time_step = 32
    max_speed = 6.28 * 0.3
    
    # Inisialisasi motor
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    # Set posisi dan kecepatan awal
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # Inisialisasi sensor IR
    left_ir = robot.getDevice('ir0')
    right_ir = robot.getDevice('ir1')
    left_ir.enable(time_step)
    right_ir.enable(time_step)
    
    # Konstanta threshold untuk deteksi garis
    BLACK_THRESHOLD = 5  # Sesuaikan dengan nilai pembacaan garis hitam
    
    while robot.step(time_step) != -1:
        # Baca nilai sensor
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print(f"left: {left_ir_value:.2f} right: {right_ir_value:.2f}")
        
        # Logika line following
        left_speed = max_speed
        right_speed = max_speed
        
        # Jika kedua sensor mendeteksi garis (hitam)
        if left_ir_value < BLACK_THRESHOLD and right_ir_value < BLACK_THRESHOLD:
            # Jalan lurus
            left_speed = max_speed
            right_speed = max_speed
            
        # Jika sensor kiri mendeteksi garis
        elif left_ir_value < BLACK_THRESHOLD:
            # Belok kiri
            left_speed = -max_speed * 0.5
            right_speed = max_speed
            print("Turn Left")
            
        # Jika sensor kanan mendeteksi garis
        elif right_ir_value < BLACK_THRESHOLD:
            # Belok kanan
            left_speed = max_speed
            right_speed = -max_speed * 0.5
            print("Turn Right")
            
        # Set kecepatan motor
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
