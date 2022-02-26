import cv2 as cv
import numpy as np

# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
cv.waitKey(0)