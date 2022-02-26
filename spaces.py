import cv2 as cv
import matplotlib.pyplot as plt
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
plt.imshow(img)
plt.show()
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#BGR to l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
plt.show()
#hsv to bgr
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)
cv.waitKey(0)