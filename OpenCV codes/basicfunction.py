import cv2 as cv

img = cv.imread(r"photo\scenery.jpg")
cv.imshow("eren", img)

# converting image into grayscale(black & white iamge)
# gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# converting to blur image
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

# edge cascade
# canny = cv.Canny(img, 225, 275)
# cv.imshow("canny", canny)

# dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('dilation', dilated)

# eroding
# eroded = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('Eroded', eroded)
# cv.waitKey(0)

# resize
# resized =cv.resize(img ,(500,500),interpolation=cv.INTER_AREA)
# cv.imshow("resized", resized)
# cv.waitKey(0)

# croping
cropped = img[100:200,200:400]
cv.imshow( "cropped", cropped )
cv.waitKey(0)
