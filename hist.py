# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

def calcAndDrawHist(image, color):  
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])  
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)  
    histImg = np.zeros([256,256,3], np.uint8)  
    hpt = int(0.9* 256);  
      
    for h in range(256):  
        intensity = int(hist[h]*hpt/maxVal)  
        cv2.line(histImg,(h,256), (h,256-intensity), color,5)  
         
    return histImg; 

def imHist(image,channal):
	hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])
	S_cum=[]#np.zeros([1,5],np.uint8)
	for value in range(256):
		if value==0:
			tmp=(hist[value]*channal/image.size)
			S_cum.append(tmp)
		else:
			tmp=S_cum[-1]+(hist[value]*channal/image.size)
			S_cum.append(tmp)
	#S_cum_nor=S_cum/maxVal  unsuppoted		
	Img_histed = np.zeros(image.shape, np.uint8)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			Img_histed[i,j]=int(S_cum[image[i,j,1]]*256)
	return Img_histed 

pic = cv2.imread("D:\opencv\gray_elephant.jpg")
hist_i = calcAndDrawHist(pic,[255,0,0])
pic_o = imHist(pic,pic.shape[2])
hist_o = calcAndDrawHist(pic_o,[255,0,0])

plt.figure(1)
plt.subplot(2,2,1)
#cv2.imshow('pic',pic)
plt.imshow(pic)
plt.title('input image')
plt.subplot(2,2,2)
plt.imshow(hist_i)
plt.title('hist_i')
plt.subplot(2,2,3)
plt.imshow(pic_o)
plt.title('output image')
plt.subplot(2,2,4)
plt.imshow(hist_o)
plt.title('hist_o')
plt.show()
# cv2.imshow('pic',hist1)
# cv2.waitKey()
# cv2.destroyAllWindows()
# 直方图均衡化 即把图像像素点映射到累计分布直方图上