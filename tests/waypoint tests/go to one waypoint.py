from cgitb import reset

from reachy_sdk import ReachySDK
import time

def turnarround():
    for i in range(6):
        angle_deg = (i + 1) * 60
        print(f"Rotating to {angle_deg}°...")
        # Rotate in place, no translation
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=angle_deg)
        time.sleep(1.5)
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=0)
    time.sleep(1.5)

def move_backward_simulated(distance):
    """Simulate backward movement by rotating, moving forward, then rotating back."""
    print(f"Simulating backward movement of {distance} meters...")

    # Turn 180°
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=180)
    time.sleep(2)

    # Move forward (actually moving backward from original heading)
    reachy.mobile_base.goto(x=-distance, y=0.0, theta=180)
    time.sleep(2)

    # Turn back 180°
    reachy.mobile_base.goto(x=-distance, y=0.0, theta=0)
    time.sleep(2)



reachy = ReachySDK(host='172.16.42.113', with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'

# Move forward
reachy.mobile_base.goto(x=1, y=0.0, theta=0.0)
time.sleep(3)
reachy.mobile_base.reset_odometry()

# Rotate 360° in 60° steps
turnarround()
reachy.mobile_base.reset_odometry()

# Return to origin
move_backward_simulated(distance=1.0)
reachy.mobile_base.reset_odometry()


# Final stop
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("Movement test complete")
