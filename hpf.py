import cv2
import numpy as np
from scipy import ndimage

kernel_3*3=np.array([[-1,-1,-1],
					[-1,8,-1],
					[-1,-1,-1]])
kernel_5*5=np.array([[-1,-1,-1,-1,-1],
					[-1,1,2,1,-1],
					[-1,2,4,2,-1],
					[-1,1,2,1,-1],
					[-1,-1,-1,-1,-1]])
img=cv2.imread("lena512.jpg",0)

k3=ndimage.convolve(img,kernel_3*3)
k5=ndimage.convolve(img,kernel_5*5)

blurred=cv2.GaussianBlur(img,(11,11),0)
g_hpf=img-blurred

cv2.imshow("3*3",k3)
cv2.imshow("5*5",k5)
cv2.imshow("g_hpf",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()