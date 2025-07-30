import time
import math

def turnarround(reachy):
    for i in range(6):
        angle_deg = (i + 1) * 60
        print(f"Rotating to {angle_deg}°...")
        # Rotate in place, no translation
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=angle_deg)
        time.sleep(1.5)
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=0)
    time.sleep(1.5)

def move_backward_simulated(reachy,x_target, y_target):
    """Simulate backward movement by rotating, moving forward, then rotating back."""
    print(f"Simulating backward movement to x={x_target}, y={y_target}")

    # Turn 180°
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=180)
    time.sleep(2)

    # Move forward (actually moving backward from original heading)
    safe_goto(reachy,x_target, -y_target, 0.0)
    reachy.mobile_base.reset_odometry()

    # Turn back 180°
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=0)
    time.sleep(2)
    reachy.mobile_base.reset_odometry()


def safe_goto(reachy,x_target, y_target, theta_target):
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
