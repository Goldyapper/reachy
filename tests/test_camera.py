import time

import cv2 as cv
from reachy_sdk import ReachySDK

reachy_mobile = ReachySDK(host='172.16.42.113', with_mobile_base=True)
print('connected')
print(reachy_mobile.right_camera)
print("grabbing frame")
img = reachy_mobile.left_camera.last_frame
print("retrieved frame")

if img is not None:
    cv.imwrite('right_frame.jpg', img)
    print('saved image')
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('no image')
