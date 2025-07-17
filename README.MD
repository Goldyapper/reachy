Safety Distance Params

/reachy_ws/install/zuuu_hal/share/zuuu_hal/config/params.yaml 
set safety to 0.7
critical to 0.55


run to startsdk server:
ros2 launch reachy_sdk_server reachy_sdk_server.launch.py

run to turn on hit detection
ros2 launch zuuu_hal hal.launch.py