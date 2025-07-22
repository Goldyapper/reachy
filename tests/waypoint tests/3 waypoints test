from reachy_sdk import ReachySDK
import time
import math

def safe_goto(x_target, y_target, theta_target):
    """
    Move Reachy safely to (x_target, y_target, theta_target) using incremental steps,
    each limited to 1m in absolute coordinates. Resets odometry after each step.
    """
    step_size = 0.9
    delay = 1.0
    total_distance = math.hypot(x_target, y_target)
    num_steps = max(1, math.ceil(total_distance / step_size))

    dx_step = x_target / num_steps
    dy_step = y_target / num_steps
    dtheta_step = theta_target / num_steps

    for i in range(num_steps):
        print(f"Step {i+1}/{num_steps}: moving by ({dx_step:.2f}, {dy_step:.2f}, {math.degrees(dtheta_step):.1f}°)")
        reachy.mobile_base.goto(x=dx_step, y=dy_step, theta=dtheta_step)
        time.sleep(delay)

        # Reset odometry to zero so the next step is relative to current position
        reachy.mobile_base.reset_odometry()

def turnarround():
    for i in range(6):
        angle_deg = (i + 1) * 60
        print(f"Rotating to {angle_deg}°...")
        # Rotate in place, no translation
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=angle_deg)
        time.sleep(1.5)

# Initialize Reachy
reachy = ReachySDK(host='172.16.42.113', with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'

# 1. Move forward 2 meters
safe_goto(2.0, 0.0, 0.0)

# 2. Turnaround (360 degrees in 60° steps)
turnarround()

# 3. Move 1 meter left (positive Y axis)
safe_goto(0.0, 1.0, 0.0)

# 4. Turnaround again
turnarround()

# 5. Move 1 meter left (positive Y axis)
safe_goto(0.0, 2.0, 90.0)

# 6. Turnaround again
turnarround()

# 7. Return to origin: first go back 1 meter right (Y=0)
safe_goto(0.0, -2.0, 0.0)
safe_goto(0.0, -1.0, 0.0)
# then go back 2 meters backward (X=0)
safe_goto(-2.0, 0.0, 0.0)

# Final stop
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("Movement test complete")