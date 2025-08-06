from reachy_sdk import ReachySDK
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.IP_address import ip_address

reachy = ReachySDK(host=ip_address,with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'free_wheel'

reachy.mobile_base.goto(x=0.5, y=0, theta=0.0)#go forward 50cm

time.sleep(3)
reachy.mobile_base.goto(x=0, y=0, theta=0.0)#return to start

time.sleep(3)
reachy.mobile_base.set_speed(x_vel=0.0, y_vel=0.0, rot_vel=0.0)
reachy.mobile_base.drive_mode = 'brake'

print("movement test complete")