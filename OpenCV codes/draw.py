import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

# # paint the image a certain colour
# blank[:] = 0,0,255
# cv.imshow('Green',blank)
# cv.waitKey(0)


# blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)

# # to color a certain portion in a image
# blank[200:300,300:450] = 0,0,255
# cv.imshow('Green',blank)
# cv.waitKey(0)

# Draw a Rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
# cv.imshow('green',blank)
# cv.waitKey(0)

# Draw a Circle
# cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
# cv.imshow('green',blank)
# cv.waitKey(0)

# Draw a line 
# cv.line(blank,(0,0),(500,500),(0,0,255),thickness=3)
# cv.imshow('green',blank)
# cv.waitKey(0)

#Write text 
cv.putText(blank,"HELLO WORLD ",(200,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0), thickness = 2 )
cv.imshow( "Hello World", blank )
cv.waitKey(0)