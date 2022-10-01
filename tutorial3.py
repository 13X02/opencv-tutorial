import cv2
import random
#for reading image -1 for og 0 for gs 1 for alpha
image = cv2.imread('assets/New_Zealand_Lake_SAVED.png',-1)
#slices image and stores in tag
tag= image[500:600,600:800]
#stores the pixels in tag to image thus cutting and pasting
image[100:200,640:840]=tag
cv2.imshow("Image",image)
#for waiting till key pressed o=infinte
cv2.waitKey(0)
cv2.destroyAllWindows() 
