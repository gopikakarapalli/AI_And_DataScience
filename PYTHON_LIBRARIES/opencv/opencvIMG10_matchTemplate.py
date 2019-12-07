'''
matchingTemplate alg

'''

import cv2
import numpy as np

img_rgb = cv2.imread('./openCV2_data/10_template_matching.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./openCV2_data/10_template_for_matching.jpg',0)
cv2.imshow('img_gray',img_gray)
#cv2.imshow('template',template)

w, h = template.shape[::-1]
print(w,h,'----------',template.shape)

result =cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#cv2.imshow('result',result)
print(result)
threshold = 0.81
location = np.where(result >threshold)
print(location)

for pt in zip(*location[::-1]):
      cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)
cv2.imshow('img_rgb',img_rgb)


