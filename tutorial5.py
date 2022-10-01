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
   
    #adding a line arguments -source starting,ending,color,thickness(-1 for fill)
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10) 
    img = cv2.line(frame,(0,height),(width,0),(255,0,0),10) 
    img = cv2.rectangle(img,(100,100),(200,200),(23,145,56),-1)
    img = cv2.circle(img,(300,300),60,(90,234,12),-1)
    font = cv2.FONT_HERSHEY_COMPLEX
    #to put text you need to pass source,text,starting and ending pos,font,scale,color,thickness,opt arg
    img = cv2.putText(img,'Onepiece is real!!!',(10,height-10),font,2,(0,0,0),5,cv2.LINE_AA)



    cv2.imshow('frame',img)
    #if q is pressed exits
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()