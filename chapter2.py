
# GrayScale Lena
import cv2
import numpy as np
img=cv2.imread("Test_Images/lena.png")
#Gray Lena
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Orignal Lena",img)

cv2.imshow("Gray Lena",imgGray)
cv2.imwrite("Saved Images/GrayLena.png",imgGray)
cv2.waitKey(0)

#Blurred Lena
imgBlur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Blurred Image",imgBlur)
cv2.imwrite("Saved Images/BlurredLena.png",imgBlur)
cv2.waitKey(0)

#Canny Lena
imgCanny=cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)
cv2.imwrite("Saved Images/CannyLena.png",imgCanny)
cv2.waitKey(0)

#Diluted Lena
kernel=np.ones((5,5),np.uint8)
imgDilation=cv2.dilate(img,kernel,iterations=1)
cv2.imshow("Dilated Image",imgDilation)
cv2.imwrite("Saved Images/DilutedLena.png",imgDilation)
cv2.waitKey(0)