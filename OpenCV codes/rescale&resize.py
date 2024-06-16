import cv2 as cv

img = cv.imread(r"photo\eren.webp")

capture = cv.VideoCapture(r"video\cat2.mp4")
# Resizing(changing the resolution of image or video) and Rescaling Images(changing its height & width to a particular height & width)
def rescaleFrame(frame, scale=0.75):
# this works for images ,videos and live video
# 1 is here -width of the image
# 0 is here - height of the image
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

# it only works for live video(web cam)
# def changeRes(width, height):
#     capture.set(3, width)
#     capture.set(3, height)


resized_image = rescaleFrame(img)
cv.imshow('resized Image',resized_image)
cv.waitKey(0)

#video  frame by frame                                                                                                          

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('video',frame)
    cv.imshow('video resized',frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindow()           
