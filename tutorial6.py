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
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #returns only matching ones
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    # takes two sources and blends them using mask 
    result = cv2.bitwise_and(frame,frame,mask=mask)



    cv2.imshow('frame',result)
    #if q is pressed exits
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()