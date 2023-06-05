# ROS-Compute-Image
ARK Task Round 2023
## 1. Prerequisites
### 1.1 **Ubuntu** and **ROS**
This package has been tested on Ubuntu 20.04 with ROS Noetic. Installation instructions for ROS Noetic can be found [here](http://wiki.ros.org/noetic/Installation).
### 1.2. **Libraries** 
You need to install the following library: [randimage 1.2](https://github.com/nareto/randimage)
```
    pip install randimage
```
### 1.3. **Create a Catkin Workspace** 
Follow this [tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) and create a catkin workspace
## 2. Build the Repository
Before building the repository, make sure that the catkin workspace has been created.
```
    cd ~/catkin_ws/src
    git clone https://github.com/TheCaptain333/ROS-Compute-Image.git
    cd ../
    catkin_make
    source ~/catkin_ws/devel/setup.bash
```

## 3. Running the Challenge: 
```
    cd catkin_ws/src
    roslaunch compute_image compute_image.launch
```
You can change the dimennsions of image from /launch/compute_image.launch.
Changing the dimensions may affect execution speed
