# ROS-Compute-Image
ARK Task Round 2023
## 1. Prerequisites
### 1.1 **Ubuntu** and **ROS**
This package has been tested on Ubuntu 20.04 with ROS Noetic. Installation instructions for ROS Noetic can be found [here](http://wiki.ros.org/noetic/Installation).
<!-- 
### 1.2. **Libraries** 
We used the following libraries: [Numpy](https://numpy.org/)
```
    pip install numpy
``` -->

## 2. Build the Repository
Clone the repository and catkin build:
```
    cd ~/catkin_ws/src
    https://github.com/Lazar-Wolfe/cents_and_dollars
    cd ../
    catkin build cents_and_dollars
    source ~/catkin_ws/devel/setup.bash
```

## 3. Running Part-1: 
```
    cd catkin_ws/src
    roslaunch cents_and_dollars part1.launch
```
You can change the value of digits from /launch/part1.launch

## 4. Running Part-2: 
```
    cd catkin_ws/src
    roslaunch cents_and_dollars part2.launch
```
You can change the value of digits from /launch/part2.launch
