import cv2 as cv
import numpy as np
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
#Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('combined_sobel', combined_sobel)




















cv.waitKey(0)