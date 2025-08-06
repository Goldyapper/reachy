from reachy_sdk import ReachySDK
from IP_address import *
import cv2 as cv
from rplidar import RPLidar

reachy_mobile = ReachySDK(host=ip_address)
print(reachy_mobile)
#reachy_mobile.turn_off("reachy")
#reachy_mobile.mobile_base.reset_odometry()
#reachy_mobile.mobile_base.goto(x=0.0, y=-1.0, theta=0.0)



# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
