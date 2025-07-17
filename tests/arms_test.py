from reachy_sdk import ReachySDK
import time

reachy = ReachySDK(host='192.168.100.100')
time.sleep(3)  # wait for motion to complete

reachy.turn_on('l_arm')
print(reachy.joints.l_shoulder_pitch.present_position)

# Set the target position in radians:
reachy.joints.l_shoulder_pitch.goal_position = 20.0
reachy.joints.l_elbow_pitch.goal_position = 20.0
reachy.joints.l_shoulder_roll.goal_position = 20.0

time.sleep(3)  # wait for motion to complete
reachy.turn_off_smoothly('l_arm')
