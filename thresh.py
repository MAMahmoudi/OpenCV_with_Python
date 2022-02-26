import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
#Simple thresholding
threshold, thresh = cv.threshold(gray,150, 255,cv.THRESH_BINARY)
cv.imshow('Simple thresholding',thresh)
#inversing thresholding
threshold, thresh_inv = cv.threshold(gray,150, 255,cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholding',thresh_inv)
#Adapotive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY,11,3)
cv.imshow('Adapotive thresholding',adaptive_thresh)







cv.waitKey(0)