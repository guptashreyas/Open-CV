# contours - a technique used to extract curves that represent object shapes from images.

import cv2 as cv

img = cv.imread(r"photo\cat3.jpg")
cv.imshow("cat", img)
# showing img  to gray
Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", Gray)
#  we can  decrease the value of contors  bu using blur 
# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blured", blur)

# #  to grab the edges of the img
# canny = cv.Canny(blur , 125, 175)
# cv.imshow("Edges", canny)
 
ret,thresh = cv.threshold(Gray,155,255,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)

# here RETR_TREE means you want all hierarchial contours
# here RETR_EXTERNAL means you want only external contours
# here RETR_LIST means you want all the contours in the img
contours, hierarchives = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#  here  CHAIN_APPROX_SIMPLE mean it compress all the contours that are return
#  here  CHAIN_APPROX_NONE mean it return all the contours 
print(f'{len(contours)} Contour(s) found')
cv.waitKey(0)
