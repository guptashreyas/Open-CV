import cv2 as cv
import numpy as np


img = cv.imread(r"photo\eren.webp")


# Translation
# def translation(img, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)


# # this means where the image is shifting
# # -x = left
# # -y = up
# # x = right
# # y = down

# translate = translation(img, 100, 100)
# cv.imshow("Translated Image", translate)
# cv.imshow("eren", img)


# Rotation
# def rotate(img, angle, rotpoint=None):
#     (height, width) = img.shape[:2]

#     if rotpoint is None:
#         rotpoint = (width // 2, height // 2)

#     rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
#     dimensions = (height, width)

#     return cv.warpAffine(img, rotMat, dimensions)


# rotate = rotate(img, 45)
# cv.imshow("rotated img", rotate)

# Resizing
# agar enlargeing the image  karni hai toh interpolation mai inter_linear or inter_cubic use kar sak te ho
# agar shrinking  the image  karni hai toh interpolation mai inter_area or use default one use kar sak te ho

# resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) 
# # here we use cubic bcz is slower but image is good

# cv.imshow("resized image ",resized)

# flipping
# flip= cv.flip(img,1) 
# # here 0 for vertical
# # here  1 for  horizontal
# # here -1 for both
# cv.imshow("flipped",flip)

# Cropping 
cropped = img[200:400 , 150:400]
cv.imshow("cropped  image", cropped)

cv.waitKey(0)
