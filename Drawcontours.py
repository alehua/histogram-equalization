# -*- coding: utf-8 -*-
import cv2
import numpy as np
#from scipy import ndimage
img=np.zeros((200,200),dtype=np.uint8)
img[50:150,50:150]=255

ret,thresh=cv2.threshold(img,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
color=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img=cv2.drawContours(color,contours,-1,(0,0,255),5)
cv2.imshow("Contours",img)
cv2.waitKey()
cv2.destroyAllWindows()