import rosbag
import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
bag = rosbag.Bag('raw_data_2021-06-03-23-34-37_72.bag')
count = 0
bridge = CvBridge()
for topic, msg, t in bag.read_messages(topics=['/camera/tricam/mid/image_raw/compressed']):
    count += 1
    cv_img = bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
    cv2.imwrite("frame_id_{}.png".format(count), cv_img)
print("total frame: ", count)
bag.close()
