import sys, os
import cv2
import rosbag
import getopt
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import uuid

# example command
# python get_rosbag_arg.py 2019-09-21-09-35-11.bag

#*need sudo apt-get install libx264-dev

def main(argv):
    inputfile = str(sys.argv[1])
    print('inputfile ', inputfile)
    
    save_path = os.path.splitext(str(sys.argv[1]))[0]
    print('save_path ', save_path)
    if not os.path.exists(save_path):
        os.makedirs(save_path)   
           
    tmp_filename = save_path + '/' + uuid.uuid1().hex + '.h264'
    save_vid     = ''
    videoWriter_h264 = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc('h','2','6','4'), 20, (1920,1208))
    #videoWriter_h264 = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc(*'avc1'), 20, (1920,1208))
    print('count +0')
    
    bag     = rosbag.Bag(inputfile)
    count   = 0
    bridge  = CvBridge()
    for topic, msg, t in bag.read_messages(topics=['/camera/tricam/mid/image_raw/compressed']):
        #try:
        #print('count +1')
        count += 1
        cv_img = bridge.compressed_imgmsg_to_cv2(msg, "bgr8")

            #cv2.imwrite('{}/{}.jpg'.format(save_path, str(msg.header.seq)), cv_img)

        videoWriter_h264.write(cv_img)
        #except:
            #print("error: ", topic, msg, t)
            
    print("total frame: ", count)

    videoWriter_h264.release()    
    os.system('%s -vcodec libx264 -crf 28 %s' % (tmp_filename, save_vid))
    print('video released')    
    bag.close()

if __name__ == "__main__":
   main(sys.argv)
