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
pip install -r requirements.txt
```

### 3.2 Install the f110-gym Python package

```bash
pip install .
```

---

## 4. Test with ROS 2 Integration (gym-ros)

This builds the ROS 2 package responsible for bridging the simulator with ROS.

### 4.1 Navigate to the ROS 2 package source for gym-ros

```bash
cd ..
cd test-package
```

### 4.2 Install necessary system dependencies

```bash
sudo apt update
sudo apt install ros-jazzy-ackermann-msgs
```

### 4.3 Build and source the workspace

```bash
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```
