import cv2
import random
#for reading image -1 for og 0 for gs 1 for alpha
image = cv2.imread('assets/coca-cola-logo.png',-1)
#prints numpy array of pixels
print(image)
#prints height,width,channels(RGB)
print(image.shape)
#for first 100 rows
for i in range(100):
    #for all columns,shape[1] returns column no
    for j in range(image.shape[1]):
        image[i][j]=[ random.randint(0,255),random.randint(0,255),random.randint(0,255) ]

cv2.imshow("Image",image)
#for waiting till key pressed o=infinte
cv2.waitKey(0)
cv2.destroyAllWindows()