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



filename = "*.data"

img_path = gb.glob(filename)
img_path.sort()
#sorted(img_path, key=os.path.basename)

print(img_path)

tmp_filename = uuid.uuid1().hex + '.mp4'
#tmp_filename = 'ISP_tricam_.mp4'
save_vid     = ''

# videoWriter = cv2.VideoWriter('tricam_short.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, (1920,1080))
# videoWriter = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc(*'mp4v'), 25, (1920,1080))

videoWriter = cv2.VideoWriter(tmp_filename, cv2.VideoWriter_fourcc(*'mp4v'), 20, (1920, 1208))

for path in img_path:
    try:
        # img     = cv2.imread(path)
        # img     = Image.open(path)
        # img.show()
        # cv2.imshow(img)
        print(path)
        
        # f = open(path, "rb").read() 
        # plt.imshow(f)
        # plt.show()
            
        # img = image.imread(path)
        
        # img     = cv2.resize(img,(1920,1080))
        

        # In[ ]:
        
        
        # RGBFileName = 'GMSL_AC03-FOV120-CSI-AB_IDX0_framegrab_2595564103.data'
        RGBDataArray = np.fromfile(path, dtype=np.uint8)
        
        
        # In[ ]:
        
        
        RGBreshape = RGBDataArray.reshape(1208,1920,3)
        
        RGBreshape = cv2.cvtColor(RGBreshape, cv2.COLOR_BGR2RGB)
        # In[ ]:
        
        
        # img = Image.fromarray(RGBreshape)
        
        
        # In[ ]:
        
        # img.show()
        
        # img.show()
        videoWriter.write(RGBreshape)
        
        # videoWriter.write(img)
    except Exception:
        pass    
        
videoWriter.release()
# os.system('%s -vcodec libx264 -crf 28 %s' % (tmp_filename, save_vid))
os.system('%s -vcodec libx264 -crf 28 %s' % (tmp_filename, save_vid))
print('video released')
