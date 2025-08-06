import time
from reachy_sdk import ReachySDK
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.IP_address import ip_address

reachy = ReachySDK(host=ip_address)
reachy.turn_on('l_arm')
reachy.turn_on('r_arm')

# Define clapping pose
clap_pose = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': -90.0,
    'l_shoulder_roll': -40.0,

    'r_shoulder_pitch': 0.0,
    'r_elbow_pitch': -90.0,
    'r_shoulder_roll': 40.0
}

# Define open arm pose (arms apart)
open_pose = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': -90.0,
    'l_shoulder_roll': 10.0,

    'r_shoulder_pitch': 0.0,
    'r_elbow_pitch': -90.0,
    'r_shoulder_roll': -10.0
}


# Move function for both arms
def move_arms(start, end, steps=40, dt=0.02):
    for i in range(steps + 1):
        alpha = i / steps
        for name in end:
            pos = (1 - alpha) * start[name] + alpha * end[name]
            getattr(reachy.joints, name).goal_position = pos
        time.sleep(dt)


# Capture initial pose
start_pose = {
    name: getattr(reachy.joints, name).present_position for name in clap_pose
}

# Move to open position
move_arms(start_pose, open_pose)

# Perform claps
clap_count = 3
for i in range(clap_count):
    move_arms(open_pose, clap_pose, steps=10, dt=0.02)
    time.sleep(0.25)
    move_arms(clap_pose, open_pose, steps=10, dt=0.02)
    time.sleep(0.25)

# Return arms to rest
rest_pose = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': 0.0,
    'l_shoulder_roll': 0.0,

    'r_shoulder_pitch': 0.0,
    'r_elbow_pitch': 0.0,
    'r_shoulder_roll': 0.0
}

move_arms(open_pose, rest_pose)

reachy.turn_off_smoothly('l_arm')
reachy.turn_off_smoothly('r_arm')
