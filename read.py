import cv2 as cv
# Read image
#img = cv.imread('Photos/test.jpg')
#cv.imshow('test', img)
#cv.waitKey(0)

# Read video
capture = cv.VideoCapture('Videos/test.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyWindow()

