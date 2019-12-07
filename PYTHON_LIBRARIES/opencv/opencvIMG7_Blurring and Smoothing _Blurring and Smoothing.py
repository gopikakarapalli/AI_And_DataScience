'''
Blurring and Smoothing
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (1) :
      _,frame = cap.read()
      hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      
      lower_color_range = np.array([1,50,30])
      upper_color_range = np.array([30,190,255])

      mask = cv2.inRange(hsv_frame,lower_color_range,upper_color_range)
      result = cv2.bitwise_and(frame,frame,mask = mask)

      #Blurring and Smoothing
      #Smoothing

      kernel = np.ones((15,15),np.float32)/225
      result_smoothed = cv2.filter2D(result,-1,kernel)
      
      #Blurring

      result_blur = cv2.GaussianBlur(result,(15,15),0)
      result_median = cv2.medianBlur(result,15)
      bilateral = cv2.bilateralFilter(result,15,75,75)

      
      #cv2.imshow('frame',frame)
      #cv2.imshow('hsv_frame',hsv_frame)
      #cv2.imshow('mask',mask)
      cv2.imshow('result',result)
      #cv2.imshow('result_smoothed',result_smoothed)
      cv2.imshow('result_blur',result_blur)
      cv2.imshow('result_median',result_median)
      cv2.imshow('bilateral',bilateral)

      k = cv2.waitKey(1) & 0xFF
      if k == 27 &ord("q"):
          break
cv2.destroyAllWindows()
cap.release()
