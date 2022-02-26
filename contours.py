import cv2 as cv
import  numpy as np
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
# canny = cv.Canny(blur,125,175)
# cv.imshow('Canny', canny)
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(countours)} countours found!')
cv.drawContours(blank,countours,-1,(0,0,255),1)
cv.imshow('Countours drawn',blank)
cv.waitKey(0)