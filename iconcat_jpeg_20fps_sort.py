# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:59:57 2021

@author: nguye
"""

import uuid
import cv2
import numpy as np
import os
import glob as gb
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image
from PIL import Image
import imageio
import re


filename = "*.jpg"

img_path        = gb.glob(filename)

#print(os.path.splitext(img_path[0]))
#print(re.split('_',img_path[0]))
print(int(os.path.splitext(re.split('_',img_path[0])[-1])[0]))

img_path        = sorted(img_path,key=lambda x: int(os.path.splitext(re.split('_', x)[-1])[0]))
#img_path.sort()
#img_path = sorted(img_path, key=os.path.getmtime)
#img_path = sorted(img_path, key=os.path.getctime)
print(img_path)

tmp_filename = uuid.uuid1().hex + '.mp4'
save_vid     = ''

img             = cv2.imread(img_path[0])
img_h,img_w,_   = img.shape

shape = (img_w, img_h)
# videoWriter = cv2.VideoWriter('tricam_short.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, (1920,1208))
videoWriter = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc(*'mp4v'), 20, shape)

for path in img_path:
    img             = cv2.imread(path)    
    print(path)
    #img     = cv2.resize(img,(1386,453))
    videoWriter.write(img)

videoWriter.release()
os.system('%s -vcodec libx264 -crf 28 %s' % (tmp_filename, save_vid))  
print('video released')
