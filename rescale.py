import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    # Images, Videos and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, heigth):
    #Live videos only
    capture.set(3,width)
    capture.set(4, heigth)

# Read image
'''
img = cv.imread('Photos/test.jpg')



resize_img = rescaleFrame(img,scale=0.2)
cv.imshow('test', resize_img)
cv.waitKey(0)

# Read video
'''
capture = cv.VideoCapture('Videos/test.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resizd = rescaleFrame(frame,scale=.5)
    cv.imshow('Video',frame_resizd)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyWindow()
