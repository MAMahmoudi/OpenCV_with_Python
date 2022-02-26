import cv2 as cv
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
#Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average blur',average)
#Gaussian blur
gauss = cv.GaussianBlur(img,(3,3),sigmaX=0)
cv.imshow('Gaussian Blur',gauss)
#Median blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)
#Bilateral blur
bilateral = cv.bilateralFilter(img,5,sigmaColor=15,sigmaSpace=15)
cv.imshow('Bilateral Blur',bilateral)

cv.waitKey(0)