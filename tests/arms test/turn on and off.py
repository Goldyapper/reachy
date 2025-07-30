import time
from reachy_sdk import ReachySDK

reachy = ReachySDK(host='172.16.42.113')
reachy.turn_on('l_arm')
reachy.turn_on('r_arm')
print(reachy.joints.l_shoulder_pitch.compliant)  # should be False


def move_arm(start, end, steps, dt):
    for i in range(steps + 1):
        alpha = i / steps
        for name in end:
            pos = (1 - alpha) * start[name] + alpha * end[name]
            getattr(reachy.joints, name).goal_position = pos
        time.sleep(dt)

# Set target positions (in degrees)
target_positions = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': 0.0,
    'l_shoulder_roll': 0.0
}

rest_positions = {
    'l_shoulder_pitch': 0.0,
    'l_elbow_pitch': 0.0,
    'l_shoulder_roll': 0.0
}


# Duration of movement in seconds
duration = 2.0
steps = 50
dt = duration / steps

start_positions = {
    name: getattr(reachy.joints, name).present_position for name in target_positions
}

move_arm(start_positions, target_positions, steps, dt)

time.sleep(1)

current_postion = {
    name: getattr(reachy.joints, name).present_position for name in rest_positions
}
move_arm(current_postion, rest_positions, steps, dt)


reachy.turn_off_smoothly('l_arm')
reachy.turn_off_smoothly('r_arm')

print(reachy.joints.keys())
