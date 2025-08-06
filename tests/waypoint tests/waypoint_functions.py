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


def move_backward_simulated(reachy, x_target, y_target, max_step=0.9):
    """
    Simulate backward movement using small steps without exceeding SDK limits.
    - Rotate once to 180°
    - Move in cumulative steps up to ±1.0m total
    - Avoid repeated rotation by not resetting odometry mid-way
    """
    print(f"Simulating backward movement to x={x_target}, y={y_target}")

    # Step 1: Rotate to face backward
    reachy.mobile_base.goto(x=0.0, y=0.0, theta=180)
    time.sleep(2)

    total_distance = math.hypot(x_target, y_target)
    if total_distance == 0:
        print("No movement needed.")
        return

    num_steps = math.ceil(total_distance / max_step)
    dx = x_target / total_distance
    dy = y_target / total_distance

    current_x, current_y = 0.0, 0.0
    current_theta = 180

    for i in range(num_steps):
        step_distance = min(max_step, total_distance - i * max_step)
        step_x = dx * step_distance
        step_y = dy * step_distance

        current_x += step_x
        current_y += step_y

        # Prevent exceeding SDK max range
        if abs(current_x) > 1.0 or abs(current_y) > 1.0:
            print(f"Step {i+1}: Position out of bounds, resetting odometry.")
            reachy.mobile_base.reset_odometry()
            time.sleep(0.5)
            current_x = -step_x
            current_y = -step_y
            current_theta = 0

        print(f"Step {i+1}/{num_steps}: Moving to x={current_x:.2f}, y={current_y:.2f}, heading=180°")
        reachy.mobile_base.goto(x=current_x, y=current_y, theta=current_theta)
        time.sleep(1)

    # Step 3: Rotate back to original heading
    print("Rotating back to original heading")
    reachy.mobile_base.goto(x=current_x, y=current_y, theta=180)
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
