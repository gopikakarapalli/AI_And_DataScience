'''
pixle selection
copy_past with pixle

'''

import numpy as np
import cv2
#pixle selection

img=cv2.imread('./openCV2_data/car.png',cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
print('org pix',img[55,55])
#cv2.imshow('org',img)
#cv2.imshow('org',img[55,55])

#copy_past with pixle

img[55,60] = [0,0,255]
print('change R,c',img[55,55])


img[100:200,100:200] = [0,0,255]
print('change R:C,R:C',img[200:150,200:150])

copy_past = img[37:111,107:194]
img[0:74,0:87] = copy_past

cv2.imshow('change org',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



