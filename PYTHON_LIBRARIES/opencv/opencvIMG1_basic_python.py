'''
open cv :
----------
#video loading and save
videocapture and save
'''
import cv2 ,time
import numpy as np
import matplotlib.pyplot as plt

#videocapture :(capture first img of video)
#-------------

video = cv2.VideoCapture(0)# this will read the first frame/img of the video  
check,frame = video.read()
'''  "chek" it is  bool data type ,returns if python is able to read the the videocapture object
      "feame" it read first image in videocapture in the form of numpy array'''
print(check)
print(frame)

cv2.imshow('capturing',frame)
cv2.waitKey()

video.release()
cv2.destroyAllWindows()

#======================================================================

##videocapture :(capture video)
#---------------

video = cv2.VideoCapture(0)
a=1
while True:
      a = a+1
      ret,frame= video.read()
      #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      cv2.imshow("org frame",frame)
      #cv2.imshow("grayframe",gray)
      key = cv2.waitKey(1)

      if key ==0xFF & ord('q'):
            break
print(a)
video.release()
cv2.destroyAllWindows()




#==================================================================
#videocapture saveing:
#--------------------

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('opcv2_output.avi',fourcc,20.0,(640,480))

while True:
      ret,frame= cap.read()
      out.write(frame)
      cv2.imshow("frame",frame)
      key = cv2.waitKey(1)

      if key ==0xFF & ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()
      

