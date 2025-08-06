from reachy_sdk import ReachySDK
from waypoint_functions import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.IP_address import ip_address

reachy = ReachySDK(host=ip_address,with_mobile_base=True)
reachy.mobile_base.reset_odometry()
reachy.mobile_base.drive_mode = 'brake'


move_backward_simulated(reachy,-4.0, 0.0)