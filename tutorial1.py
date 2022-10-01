import cv2
#for reading image
image = cv2.imread('assets/coca-cola-logo.png',-1)
#for resizing image fx multiplies x axis and fy multiplies y
image = cv2.resize(image,(0,0),fx=.5,fy=0.5);
#for roating add ROTATE_DEGREE_FORMAT
image = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()