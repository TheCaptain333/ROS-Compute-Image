#!/usr/bin/env python3
import rospy
import std_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

pub1 = rospy.Publisher('/guess', Image, queue_size=10)

def strategy():
	rospy.init_node('player_node')
	rospy.Subscriber("/result", Image, guessCallback)
			
def guessCallback(data):
	pass
	
if __name__ == '__main__':
	try:
		strategy()
	except rospy.ROSInterruptException:
		pass












