# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:59:57 2021

@author: nguye
"""

import cv2
import numpy as np
import os
import glob as gb

filename = "*.jpg"

img_path = gb.glob(filename)

print(img_path)

tmp_filename = '03_tricam_short.mp4'
save_vid     = ''

# videoWriter = cv2.VideoWriter('tricam_short.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, (1920,1080))
videoWriter = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc(*'mp4v'), 25, (1920,1208))

for path in img_path:
    img     = cv2.imread(path)
    print(path)
    img     = cv2.resize(img,(1920,1208))
    videoWriter.write(img)

videoWriter.release()
os.system('%s -vcodec libx264 -crf 28 %s' % (tmp_filename, save_vid))  
print('video released')
