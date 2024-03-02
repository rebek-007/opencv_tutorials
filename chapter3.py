import cv2
img = cv2.imread("Test_Images/Lena.png")
print(img.shape)# for determing the resoulation
imgResize=cv2.resize(img,(200,200)) #resizing the  image
cv2.imshow("Output",img)
cv2.imshow("NewOutput",imgResize)
cv2.waitKey(0)

imgCropped = img[0:200,100:200]#cropping the images by matrix method
cv2.imshow("Output",img)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)