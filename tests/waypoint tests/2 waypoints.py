from reachy_sdk import ReachySDK
from waypoint_functions import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.IP_address import ip_address

reachy = ReachySDK(host=ip_address,with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'

# 1. Move forward 2 meters
safe_goto(reachy,2.0, 0.0, 0.0)

# 2. Turnaround (360 degrees in 60° steps)
turnarround(reachy)

# 3. Move 1 meter left (positive Y axis)
safe_goto(reachy,0.0, 1.0, 0.0)

# 4. Turnaround again
turnarround(reachy)

# 5. Return to origin: first go back 1 meter right (Y=0)
safe_goto(reachy,0.0, -1.0, 0.0)
# then go back 2 meters backward (X=0)
move_backward_simulated(reachy,2.0, 0.0)
# Final stop
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("Movement test complete")