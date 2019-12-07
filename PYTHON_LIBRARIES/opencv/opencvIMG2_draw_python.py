'''
opencv :
-------
Art drwing in the img
text
'''

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./openCV2_data/gray apple.png',1)

cv2.line(img,(0,0),(150,150),(250,35,255),10)#img,startco-ord(x1,y1),end co-ord(x2,y2),(BGR),width)
cv2.rectangle(img,(0,0),(150,150),(250,0,0),5)#img,top Left coner co-ord(x1,y1),Botam right coner co-ord(x2,y2),(BGR),width)
cv2.circle(img,(100,63),10,(150,200,0),-1)#img,(center of circle),r,(BGR),fillS= -1)

pts=np.array([[10,5],[20,30],[70,20],[50,10],[60,80]],np.int32)
cv2.polylines(img,[pts],True,(0,0,255),5)#img,[list of points],connectionT\F,(BGR),pix)

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img,'apple_draw',(0,130),font,1,(0,0,150),3,cv2.LINE_AA)
#img,'text',(co-ord),fount,size,(BGR),width,)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
