import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)


#img[:]=0,0,255#red
#img[:]=0,255,0#green
#img[:]=255,0,0#blue

#drawing lines using the line function
#cv2.line(img,(1,1),(256,256),(0,0,255),3)                    ###line from top left to middle of the image
#cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(255,0,0),4)  ###line from top left to bottom right
#cv2.line(img,(0,0),(img.shape[1],0),(0,255,0),4)             ### line the length of the width of the image
#cv2.line(img,(0,0),(0,img.shape[1]),(0,0,255),4)             ### line the length of the height of the image


### drawing rectangle using the rectangle function
#cv2.rectangle(img,(200,300),(50,325),(0,255,255),4)

#cv2.rectangle(img, (100,150),(200,260),(0,255,0),cv2.FILLED)

###drawing circle using the circle function
#cv2.circle(img,(100,100),25,(255,255,0),3)

### putting text on images
#cv2.putText(img," Learning OpenCV by rebek-007",(50,100),cv2.FONT_ITALIC,1.15,(150,0,200),5)


cv2.imshow("Image",img)

cv2.waitKey(0)