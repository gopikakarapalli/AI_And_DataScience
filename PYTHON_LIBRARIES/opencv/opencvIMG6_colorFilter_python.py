'''colorFilter
'''
'''
# to convert single color:q
dark_red = np.uint8([[[12,22,121]]])
dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
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

      
      cv2.imshow('frame',frame)
      cv2.imshow('hsv_frame',hsv_frame)
      cv2.imshow('mask',mask)
      cv2.imshow('result',result)

      k = cv2.waitKey(5) & 0xFF
      if k == 27:
          break

cv2.destroyAllWindows()
cap.release()



      
