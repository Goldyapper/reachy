import time
from reachy_sdk import ReachySDK

time.sleep(4)
reachy = ReachySDK(host='192.168.100.100')
reachy.turn_on('l_arm')

def move_arm(start, end, steps, dt):
    for i in range(steps + 1):
        alpha = i / steps
        for name in end:
            pos = (1 - alpha) * start[name] + alpha * end[name]
            getattr(reachy.joints, name).goal_position = pos
        time.sleep(dt)

# Set target positions (in degrees)
wave_positions = {
    'l_shoulder_pitch': -90.0,
    'l_elbow_pitch': -90.0,
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
    name: getattr(reachy.joints, name).present_position for name in wave_positions
}

move_arm(start_positions, wave_positions, steps, dt)

time.sleep(1)

# Do the wave (oscillate wrist roll)
wave_amplitude = 30.0  # degrees
wave_count = 4
wave_delay = 0.3

for i in range(wave_count):
    reachy.joints.l_wrist_roll.goal_position = wave_amplitude
    time.sleep(wave_delay)
    reachy.joints.l_wrist_roll.goal_position = -wave_amplitude
    time.sleep(wave_delay)

# Return wrist to center
reachy.joints.l_wrist_roll.goal_position = 0.0
time.sleep(0.5)

current_postion = {
    name: getattr(reachy.joints, name).present_position for name in rest_positions
}
move_arm(current_postion, rest_positions, steps, dt)


reachy.turn_off_smoothly('l_arm')