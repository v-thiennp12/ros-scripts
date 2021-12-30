#!/usr/bin/env python
"""OpenCV feature detectors with ros CompressedImage Topics in python.

This example subscribes to a ros topic containing sensor_msgs 
CompressedImage. It converts the CompressedImage into a numpy.ndarray, 
then detects and marks features in that image. It finally displays 
and publishes the new image - again as CompressedImage topic.
"""
__author__ =  'Simon Haller <simon.haller at uibk.ac.at>'
__version__=  '0.1'
__license__ = 'BSD'
# Python libs
import sys, time
import os

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage
# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError

VERBOSE=False

class image_feature:

    def __init__(self, topic_name, save_path):
        '''Initialize ros publisher, ros subscriber'''
        '''
        # topic where we publish
        self.image_pub = rospy.Publisher("/output/image_raw/compressed",
            CompressedImage)
        # self.bridge = CvBridge()
        '''
        self.save_path = save_path 
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # subscribed Topic
        self.subscriber = rospy.Subscriber(topic_name,
            CompressedImage, self.callback,  queue_size = 1)
        if VERBOSE :
            print(topic_name)


    def callback(self, ros_data):
        '''Callback function of subscribed topic. 
        Here images get converted and features detected'''
        if VERBOSE :
            print('received image of type: "%s"' % ros_data.format)

        #### direct conversion to CV2 ####
        np_arr = np.fromstring(ros_data.data, np.uint8)
        #image_np = cv2.imdecode(np_arr, cv2.IMRREAD_UNCHANGED)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) # OpenCV >= 3.0:
        
        '''
        #### Feature detectors using CV2 #### 
        # "","Grid","Pyramid" + 
        # "FAST","GFTT","HARRIS","MSER","ORB","SIFT","STAR","SURF"
        method = "GridFAST"
        feat_det = cv2.FeatureDetector_create(method)
        time1 = time.time()

        # convert np image to grayscale
        featPoints = feat_det.detect(
            cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY))
        time2 = time.time()
        if VERBOSE :
            print '%s detector found: %s points in: %s sec.'%(method,
                len(featPoints),time2-time1)

        for featpoint in featPoints:
            x,y = featpoint.pt
            cv2.circle(image_np,(int(x),int(y)), 3, (0,0,255), -1)
        '''
        #print(ros_data.header.seq)
        cv2.imwrite('{}/{}.jpg'.format(self.save_path, ros_data.header.seq), image_np)
        #cv2.imshow('cv_img', image_np)
        #cv2.waitKey(2)
        
        '''
        #### Create CompressedIamge ####
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
        # Publish new image
        self.image_pub.publish(msg)
        
        #self.subscriber.unregister()
        '''

def main(args):
    '''Initializes and cleanup ros node'''
    sidecam_rl = image_feature("/camera/side/cam_rl/image_raw/compressed", "images/sidecam_rl")
    sidecam_rr = image_feature("/camera/side/cam_rr/image_raw/compressed", "images/sidecam_rr")
    tricam_long = image_feature("/camera/tricam/long/image_raw/compressed", "images/tricam_long")
    tricam_mid = image_feature("/camera/tricam/mid/image_raw/compressed", "images/tricam_mid")
    tricam_short = image_feature("/camera/tricam/short/image_raw/compressed", "images/tricam_short")

    rospy.init_node('image_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS Image feature detector module")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
