#!/usr/bin/env python3
import rospy
import std_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import randimage
import cv2
import numpy as np

height = int(rospy.get_param("/player_node/image_height"))
width = int(rospy.get_param("/player_node/image_width"))
img_size = (height,width,3)

pub1 = rospy.Publisher('/result', Image, queue_size=10)
bridge = CvBridge()


def generateRandomImage():
	
	img = randimage.get_random_image((img_size[0],img_size[1]))*255
	img = img.astype(np.uint8)
	return img
	
def compareImage(test_img,src_img):

	B_test = test_img[:,:,0]
	G_test = test_img[:,:,1]
	R_test = test_img[:,:,2]

	B_src = src_img[:,:,0]
	G_src = src_img[:,:,1]
	R_src = src_img[:,:,2]
	
	R_result = ((np.sign(B_test-B_src)+1)*255)//2
	G_result = ((np.sign(R_test-R_src)+1)*255)//2
	B_result = ((np.sign(G_test-G_src)+1)*255)//2

	R_result = R_result.astype("uint8")
	G_result = G_result.astype("uint8")
	B_result = B_result.astype("uint8")

	return cv2.merge([B_result,G_result,R_result])
	
	
def check():
	global imgMsg
	imgMsg = None
	rospy.init_node('checker_node')
	rospy.Subscriber("/guess", Image, guessCallback)
	rospy.sleep(1)
	hidden_image = generateRandomImage()
	hidden_image = hidden_image.astype(int)
	while not rospy.is_shutdown():
		while imgMsg is None:
			pass
		imgMsg = imgMsg.astype(int)
		result = compareImage(imgMsg,hidden_image)
		new_msg = bridge.cv2_to_imgmsg(result,"bgr8")
		imgMsg = None
		pub1.publish(new_msg)
		if(np.count_nonzero(result.astype(int)-127)==0):
			print("Successfully identified the image")
			break
		while imgMsg is None:
			pass
		rospy.sleep(0.2)
def guessCallback(data):
	global imgMsg
	imgMsg = bridge.imgmsg_to_cv2(data,"bgr8")

		
	
if __name__ == '__main__':
	try:
		check()
	except rospy.ROSInterruptException:
		pass












