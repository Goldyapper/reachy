import time
from reachy_sdk import ReachySDK
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.IP_address import ip_address

reachy = ReachySDK(host=ip_address)
reachy.turn_on('l_arm')

print(reachy.joints.l_shoulder_pitch.compliant)  # should be False

def move_arm(start, end, steps, dt):
    for i in range(steps + 1):
        alpha = i / steps
        for name in end:
            pos = (1 - alpha) * start[name] + alpha * end[name]
            getattr(reachy.joints, name).goal_position = pos
        time.sleep(dt)

# Hand control functions
def open_hand():
    reachy.joints.l_gripper.goal_position = 50.0  # Adjust as needed
    time.sleep(0.3)

def close_hand():
    reachy.joints.l_gripper.goal_position = -20.0
    time.sleep(0.3)

# Target pose (arm up)
target_positions = {
    'l_shoulder_pitch': -90.0,
    'l_elbow_pitch': -90.0,
    'l_shoulder_roll': 0.0
}

# Rest pose (arm down)
rest_positions = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': 0.0,
    'l_shoulder_roll': 0.0
}

# Motion settings
duration = 2.0
steps = 50
dt = duration / steps

# Move arm to raised position
start_positions = {
    name: getattr(reachy.joints, name).present_position for name in target_positions
}
move_arm(start_positions, target_positions, steps, dt)

# Open and close hand 3 times
for _ in range(3):
    open_hand()
    close_hand()

# Move arm back to rest
current_position = {
    name: getattr(reachy.joints, name).present_position for name in rest_positions
}
move_arm(current_position, rest_positions, steps, dt)

reachy.turn_off_smoothly('l_arm')

print("Right gripper position:", reachy.joints.r_gripper.present_position)

