from reachy_sdk import ReachySDK
import time
from waypoint_functions import *

reachy = ReachySDK(host='172.16.42.113', with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'

# Move forward
reachy.mobile_base.goto(x=1, y=0.0, theta=0.0)
time.sleep(3)
reachy.mobile_base.reset_odometry()

# Rotate 360° in 60° steps
turnarround(reachy)
reachy.mobile_base.reset_odometry()

# Return to origin
move_backward_simulated(reachy,-1,0)
reachy.mobile_base.reset_odometry()

# Final stop
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("Movement test complete")
