import cv2
import numpy as np


img = cv2.imread('./openCV2_data/5_page.jpg')
grayimg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval,threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
retval2,threshold_grayimg = cv2.threshold(grayimg,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY,115,0)
retval3,otcu = cv2.threshold(grayimg,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(retval,retval2,retval3)
cv2.imshow("org",img)
cv2.imshow("threshold",threshold)
cv2.imshow("threshold_grayimg",threshold_grayimg)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C(gaus)",gaus)
cv2.imshow("OTSU",otcu)


cv2.waitKey(0)
cv2.destroyAllWindows()



