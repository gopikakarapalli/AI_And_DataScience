'''
goodFeaturesToTrack:
---------------------
Corner Detection

doc :https://docs.opencv.org/3.4.1/dd/d1a/group__imgproc__feature.html
'''
import numpy as np
import cv2

img = cv2.imread('./openCV2_data/12_Corner Detection.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#corners	=	cv.goodFeaturesToTrack(	image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)
