import cv2 as cv
img = cv.imread(r"photo\eren.webp")
# print(img)
cv.imshow('eren', img)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture(r"video\cat2.mp4")
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
# just trying for  web cam
capture = cv.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

while True:
    success, frame = capture.read()

    if not success:
         #Handle the case when the frame is not captured successfully
        print("Failed to capture frame.")
        break

    cv.imshow('Face Attendance', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        # Break the loop if 'q' key is pressed
        break

# Release the video capture object and close the window
capture.release()
cv.destroyAllWindows()


