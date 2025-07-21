from reachy_sdk import ReachySDK
import time
import math

def turnarround():
    for i in range(6):
        angle_deg = (i + 1) * 60
        print(f"Rotating to {angle_deg}°...")
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=angle_deg)
        time.sleep(1.5)

reachy = ReachySDK(host='172.16.42.113', with_mobile_base=True)

reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'

# Move forward diagonally
reachy.mobile_base.goto(x=0.5, y=1.0, theta=0.0)
time.sleep(3)

# Rotate 360° in 60° steps
turnarround()

# Return to origin
reachy.mobile_base.goto(x=0.0, y=0.0, theta=0.0)
time.sleep(3)

# Final stop
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("Movement test complete")
