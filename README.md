Goldyapper/reachy is a Python-based project—potentially involving CAD models, testing, and robot control—related to Pollen Robotics’ Reachy platform.

Features

Robot connectivity check – confirm Reachy is online and responsive
Arm control tests – move left and right arms individually
Motion validation – demonstrate that the robot responds correctly to commands
Logging support – execution results and errors written to logs.txt
CAD models – includes an AGX holder design for hardware setup

Repository Structure
/

├── AGX-holder-CAD-model/     # 3D CAD files for Jetson AGX holder

├── tests/                    # Scripts to test robot connectivity and arm movement

├── main.py                   # Main entry point for robot control

├── start cmd.txt             # Example startup commands

├── logs.txt                  # Runtime logs

└── .idea/                    # IDE configs (PyCharm)

Getting Started
Prerequisites

- A Reachy 1 robot (real hardware or simulator)
- Python 3.7+
- Reachy SDK

Install the SDK:
```pip install reachy```

Installation
```
# Clone the repo
git clone https://github.com/Goldyapper/reachy.git
cd reachy
```

Usage

1. Power on Reachy and ensure it’s connected to your network.
2. Start the control script:
```python main.py```
3. Run tests to validate arms and motion:
```pytest tests/```

Development

Testing arms:
The tests/ folder includes motion routines to move each arm through a range of motion.
Extending:
You can add new motion scripts inside tests/ to validate specific joints or movements.
Logging:
All runtime details are recorded in logs.txt.
