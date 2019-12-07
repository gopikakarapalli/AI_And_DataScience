''''
Interactive Foreground Extraction using GrabCut Algorithm:
----------------------------------------------------------
GrabCut Foreground Extraction
(Find the foreground, and remove the background)
How it work: https://docs.opencv.org/3.1.0/d8/d83/tutorial_py_grabcut.html
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./openCV2_data/11_foreground_extraction.jpg',1)
print(img.shape)

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

cv2.imshow('mask',mask)
print('mask', mask.shape)
cv2.imshow('bgdModel',bgdModel)
print('bgdModel', bgdModel.shape)
print('fgdModel', fgdModel.shape)

rect = (100,50,150,250)#(start_x, start_y, width, height)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,30,cv2.GC_INIT_WITH_RECT)

'''
( input image,mask,rectangle for our main object,background model,
foreground model,amount of iterations to run, and what mode you are using)
'''

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
'''
From here, the mask is changed so that all 0 and 2 pixels are converted
to the background, where the 1 and 3 pixels are now the foreground.
From here, we multiply with the input image, and we get our final result
'''
plt.imshow(img)
plt.colorbar()
plt.show()

'''
How it works ?
How it works from user point of view ? Initially user draws a rectangle around the foreground region (foreground region shoule be completely
inside the rectangle). Then algorithm segments it iteratively to get the best result. Done. But in some cases, the segmentation won't be fine,
like, it may have marked some foreground region as background and vice versa. In that case, user need to do fine touch-ups. Just give some strokes
on the images where some faulty results are there. Strokes basically says *"Hey, this region should be foreground, you marked it background,
correct it in next iteration"* or its opposite for background. Then in the next iteration, you get better results.

So what happens in background ?
---------------------------------
User inputs the rectangle. Everything outside this rectangle will be taken as sure background (That is the reason it is mentioned before that your rectangle should include all the objects). Everything inside rectangle is unknown. Similarly any user input specifying foreground and background are considered as hard-labelling which means they won't change in the process.
Computer does an initial labelling depeding on the data we gave. It labels the foreground and background pixels (or it hard-labels)
Now a Gaussian Mixture Model(GMM) is used to model the foreground and background.
Depending on the data we gave, GMM learns and create new pixel distribution. That is, the unknown pixels are labelled either probable foreground or probable background depending on its relation with the other hard-labelled pixels in terms of color statistics (It is just like clustering).
A graph is built from this pixel distribution. Nodes in the graphs are pixels. Additional two nodes are added, Source node and Sink node. Every foreground pixel is connected to Source node and every background pixel is connected to Sink node.
The weights of edges connecting pixels to source node/end node are defined by the probability of a pixel being foreground/background. The weights between the pixels are defined by the edge information or pixel similarity. If there is a large difference in pixel color, the edge between them will get a low weight.
Then a mincut algorithm is used to segment the graph. It cuts the graph into two separating source node and sink node with minimum cost function. The cost function is the sum of all weights of the edges that are cut. After the cut, all the pixels connected to Source node become foreground and those connected to Sink node become background.
The process is continued until the classification converges.
'''
