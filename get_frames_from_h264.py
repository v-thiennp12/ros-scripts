# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:43:06 2021

@author: nguye
"""

import numpy as np
import cv2
import os
import argparse

parser = argparse.ArgumentParser(description='Get frames from h264 --input_h264')
parser.add_argument('--input_h264', help='Input h264 file', required=True)
args = parser.parse_args()

tmp_filename = args.input_h264
#tmp_filename = 'tricam_main_FOV60_20210721_oldford_CLOUDY_OS52_demopath_full.h264'

save_path    = os.path.splitext(tmp_filename)[0]
if not os.path.exists(save_path):
    os.makedirs(save_path)
        
cap          = cv2.VideoCapture(tmp_filename)
count        = 0
print('save_path', save_path)

while(cap.isOpened()):
    ret, frame = cap.read()
    count      += 1
    print('count ', count) 
    if not(ret):
        break
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame',frame)
    #cv2.imwrite('{}/{}.jpg'.format(save_path, 'frame_' + str(count)), frame)
    cv2.imwrite('{}/{}.jpg'.format(save_path, 'frame_' + str(count)), frame)
    print('ret ', ret)

cap.release()
