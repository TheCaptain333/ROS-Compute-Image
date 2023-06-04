#!/usr/bin/env python3
import rospy
import std_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import randimage
import cv2
import numpy as np

pub1 = rospy.Publisher('/guess', Image, queue_size=10)


	
	
def strategy():
	global imgMsg
	imgMsg = None
	rospy.init_node('player_node')
	rospy.Subscriber("/result", Image, guessCallback)
	

	
		
def guessCallback(data):
	global imgMsg
	

		
	
if __name__ == '__main__':
	try:
		strategy()
	except rospy.ROSInterruptException:
		pass












