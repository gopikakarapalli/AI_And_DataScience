'''
Morphological Transformations
-->Erosion
--> Dilation
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (1) :
      _,frame = cap.read()
      hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      
      lower_color_range = np.array([1,50,30])
      upper_color_range = np.array([255,190,255])

      mask = cv2.inRange(hsv_frame,lower_color_range,upper_color_range)
      result = cv2.bitwise_and(frame,frame,mask = mask)

      kernel = np.ones((5,5),np.uint8)
      erosion = cv2.erode(mask,kernel,iterations = 1)
      dilation = cv2.dilate(mask,kernel,iterations = 1)

      opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
      closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

      
      #cv2.imshow('frame',frame)
      #cv2.imshow('hsv_frame',hsv_frame)
      #cv2.imshow('mask',mask)
      cv2.imshow('result',result)
      cv2.imshow('erosion',erosion)
      cv2.imshow('dilation',dilation)
      cv2.imshow('opening',opening)
      cv2.imshow('closing',closing)

      k = cv2.waitKey(1) 
      if k == 0xFF & ord("q"):
          break
cap.release()
cv2.destroyAllWindows()

