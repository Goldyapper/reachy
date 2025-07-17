import time
import numpy as np
from reachy_sdk import ReachySDK

reachy = ReachySDK(host='192.168.100.100')
reachy.turn_on('l_arm')
print(reachy.joints.l_shoulder_pitch.compliant)  # should be False

# Set target positions (in degrees)
target_positions = {
    'l_shoulder_pitch': -90.0,
    'l_elbow_pitch': 40.0,
    'l_shoulder_roll': 0.0
}

# Duration of movement in seconds
duration = 2.0
steps = 50
dt = duration / steps

start_positions = {
    name: getattr(reachy.joints, name).present_position for name in target_positions
}

# Interpolate and apply
for i in range(steps + 1):
    alpha = i / steps
    for name in target_positions:
        pos = (1 - alpha) * start_positions[name] + alpha * target_positions[name]
        getattr(reachy.joints, name).goal_position = pos
    time.sleep(dt)

reachy.turn_off_smoothly('l_arm')
