'''
Image arithmetics and Logic oprations
'''
import cv2
import numpy as np
import sys

img1 = cv2.imread('./openCV2_data/4_3D_Matplotlib.png')
img2 = cv2.imread('./openCV2_data/4_mainsvmimage.png')


#out_img = img1 + img2 # add to img(we can perform all math oprations like +-,*,**,etc)
out_img = cv2.add(img1,img2)# each numpy array elements willbe add and get the result
#like [155,211,79] + [50,170,200] = [205,381,279] generate this equleven img
out_img = cv2.addWeighted(img1,0.6,img2,0.4,0)#add wrt weighted (img,alf_we,img,we_beta,gamaa)

cv2.imshow("out_img",out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#add logo to img baground
#img1 =out_img
img1 = cv2.imread('./openCV2_data/4_3D_Matplotlib.png')
img2 = cv2.imread("./openCV2_data/4_mainlogo.png")

rows,cols,channels = img1.shape
regon = img1[0:rows,0:cols]
print(rows,cols,channels)
print(img1.shape,"\n",regon)
#cv2.imshow("regon img1",img1)

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)#(image,min_thresh,max_thresh,type_of_thresh)
'''threshoid : it is used to apply the mask in the image
    arg 1= image which image to apply threshold(mask)
    min_threshold &max_threshold : below (220) min_threshold value pixle is convert into balck
    and above min_threshold value(220) is convert into max_threshold(255)'''
#cv2.imshow("img2gray",img2gray) 
#cv2.imshow("mask",mask)
 
#Logic oprations:
mask_inv = cv2.bitwise_not(mask)  # not oprator also apply or,and,xor ,etc
#cv2.imshow("mask_inv",mask_inv)

img1_bg = cv2.bitwise_and(regon,regon,mask=mask_inv)
cv2.imshow("img1_bg",img1_bg)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
cv2.imshow("img2_fg",img2_fg)
dst = cv2.add(img1_bg,img2_fg)
cv2.imshow("dst",dst)


cv2.waitKey(0)
cv2.destroyAllWindows()



'''
mask = cv2.imread('mask.png',0)
im = cv2.imread('guy.png')
mask_inv =  255 - mask;
final_im = mask_inv*im

############mask = np.zeros(regon.shape[:2],np.uint8)

mask_inv = np.where((mask==0),0,1).astype('uint8')
img1_bg = mask_inv*regon[:,:,np.newaxis]
'''




            
