'''
Canny Edge Detection and Gradients

doc :https://docs.opencv.org/3.4.1/dd/d1a/group__imgproc__feature.html
'''
#pip install --upgrade opencv-python==3.4.5.20 for laplacian,sobel_x

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (1) :
      _,frame = cap.read()
      #Gradients
      laplacian = cv2.Laplacian(frame,cv2.CV_64F)
      sobel_x = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
      sobel_y = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
      #Edge Detection
      Edge_Detection = cv2.Canny(frame,50,200)

      
      cv2.imshow('frame',frame)
      cv2.imshow('laplacian',laplacian)
      cv2.imshow('sobel_x',sobel_x)
      cv2.imshow('sobel_y',sobel_y)
      cv2.imshow('Edge_Detection',Edge_Detection)

      k = cv2.waitKey(1) 
      if k == 0xFF & ord("q"):
          break
cap.release()
cv2.destroyAllWindows()
