'''
open cv :
----------
image loadind save
  -> resize
  -> shape
  -> colour conversion BGR2GRAY
'''
import cv2 
import numpy as np
import matplotlib.pyplot as plt

#image loading:
#---------------
img = cv2.imread('../opencv/openCV2_data/apple.jpeg',cv2.IMREAD_COLOR)
#cv2.IMREAD_GRAYSCALE --> 0
#cv2.IMREAD_COLOR --> 1
#cv2.IMREAD_UNCHANGED -->-1

#img = cv2.imread('../opencv/openCV2_data/apple.jpeg'',
#                 -1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


resizeImage = cv2.resize(img,(300,300))
resizeImage = cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
cv2.imshow('image',img)
h,w,c =img.shape
print('array elements of img \n',img,'\n shape of colour img',img.shape)
print('array elements of gray_img \n',gray_img,'\n shape of gray_img',gray_img.shape)
print('array elements of resizeimage \n',resizeImage,'\n shape of colour resizeimg',resizeImage.shape)


cv2.imshow('image',img)
cv2.imshow('gray_image',gray_img)
cv2.imshow('resizeImage',resizeImage)

cv2.waitKey()
#cv2.waitKey(10)

cv2.destroyAllWindows()


#plt.imshow(img,cmap='gray')
#plt.show()

cv2.imwrite('./openCV2_data/gray apple.png',gray_img)# to save the img

