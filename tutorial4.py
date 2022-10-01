from email.mime import image
from tkinter import Frame
import numpy as np
import cv2
#pass camera no as argument
cap = cv2.VideoCapture(0)

while True:
    #read returns the image and a ret which shows if successful
    ret, frame = cap.read()
    #get returns the value of property passed 3 for width 4 for height
    width = int(cap.get(3))
    height = int(cap.get(4))
    #resizing to mirror
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    #creating a numpy array of zeros of size of our video
    image = np.zeros(frame.shape,np.uint8)
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[:height//2,width//2:]=smaller_frame
    image[height//2:,width//2:]=smaller_frame
    

    cv2.imshow('frame',image)
    #if q is pressed exits
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()