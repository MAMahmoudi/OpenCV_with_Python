import cv2 as cv
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)

#Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('Canny', canny)
cv.waitKey(0)
#2
canny2 = cv.Canny(blur,125,175)
cv.imshow('Canny2', canny2)
cv.waitKey(0)

#Dilating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated', dilated)
cv.waitKey(0)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded', eroded)
cv.waitKey(0)

#Resize
resized = cv.resize(img,(200,200),interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)
cv.waitKey(0)

#Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
