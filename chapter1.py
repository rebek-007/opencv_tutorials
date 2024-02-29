import cv2
#image
img=cv2.imread("Test_Images/lena.png")
cv2.imshow("Output",img)
cv2.imwrite("Saved Images/Orignal Lena.png")
cv2.waitKey(0)

#video
cap=cv2.VideoCapture("Test_Images/flower.y4m")
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break        

#webcam
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
