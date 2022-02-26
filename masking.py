import cv2 as cv
import numpy as np
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank', blank)
circle = cv.circle(blank.copy(),(img.shape[1]//2-50,img.shape[0]//2-100),100,255,-1)
# cv.imshow('Mask', mask)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# cv.imshow('Mask2', mask2)
weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('weird shape', weird_shape)
# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Masked', masked)
weird_shape_masked_img = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('weird_shape_masked_img', weird_shape_masked_img)

cv.waitKey(0)