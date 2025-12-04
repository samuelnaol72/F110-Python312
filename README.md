# F110-Python312: Setup Manual

This guide outlines the steps to set up the F1/10 simulation environment with ROS 2 Jazzy and Python 3.12.

---

## 1. Prerequisites

* **Operating System:** Ubuntu 24.04 (Noble Numbat)
* **ROS 2 Distribution:** ROS 2 Jazzy 

---

## 2. Clone the Repository

We will create a Colcon workspace and clone the project into it.

### 2.1 Create and enter the Colcon workspace directory

```bash
mkdir -p ~/f110-test-ws
cd ~/f110-test-ws
```

### 2.2 Clone the repository

```bash
git clone https://github.com/samuelnaol72/F110-Python312.git
```

### 2.3 Enter the main project directory

```bash
cd F110-Python312
```

---

## 3. Install f110-gym and Dependencies

This installs the core Python simulation library and its required packages.

### 3.1 Install Python dependencies

```bash
cd f110-gym-py312
pip install -r requirements.txt  # installed in ~/.local/lib/python3.12/site-packages
```

### 3.2 Install the f110-gym Python package

```bash
pip install .       # installed in ~/.local/lib/python3.12/site-packages
```

---

## 4. Test with ROS 2 Integration (gym-ros)

This builds the ROS 2 package responsible for bridging the simulator with ROS.

### 4.1 Navigate to the ROS 2 package source for gym-ros

```bash
cd ..
cd test-package
```

### 4.2 Build and source the workspace
=== IMPORTANT ===
Before building, you must edit the map path in the ROS config file.

Open the simulator configuration file:
```bash
gedit src/f110-gym-ros-py312/config/sim.yaml
```

Edit the following entry:
```bash
map_path: "/ABSOLUTE/PATH/TO/YOUR/MAP.yaml"
```

Replace it with the correct absolute path to the map you want to use, for example:
```bash
map_path: "/home/USERNAME/f110-test-ws/F110-Python312/test-package/src/f110-gym-ros-py312/maps/berlin"
```

Save the file.

Now build and source:
```bash
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```
### 4.3. Test
#### 4.3.1 Launch Simulator + ROS Bridge
In Terminal 1(The same Terminal):
```bash
ros2 launch f1tenth_gym_ros gym_bridge_launch.py
```
This starts the simulator, publishes /scan, and waits for drive commands
#### 4.3.2 Ackermann Drive / Teleoperation

In Terminal 2:
```bash
source /opt/ros/jazzy/setup.bash
source ~/f110-test-ws/F110-Python312/test-package/install/setup.bash
```
Option A — Publish Ackermann commands manually

Install if necessary:
```bash
sudo apt update
sudo apt install ros-jazzy-ackermann-msgs
```
Run(Adjust):
```bash
ros2 topic pub /drive ackermann_msgs/msg/AckermannDriveStamped \
"{drive: {speed: N/A, steering_angle:N/A }}"
```
You should see the car move inside the simulator.

Option B — Keyboard teleop (optional)

Install if necessary:
```bash
sudo apt install ros-jazzy-teleop-twist-keyboard
```
Run:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## 5. Contributions:
1. Python 3.12 / Ubuntu 24.04 Compatibility: Fully verified and working with the latest OS and Python stack.
2. Gymnasium API Compliance: Updated f110-gym to use the new Gymnasium standard (Ex. 5-element return from env.step).
3. Modern Python Imports: Utilizes importlib.resources.files for reliable package asset loading in Python 3.12.
4. Dynamic Map Loading: Removes hardcoded paths, allowing the map to be configured externally via the gym-bridge. 
