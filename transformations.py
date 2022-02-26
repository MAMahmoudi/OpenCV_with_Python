import cv2 as cv
import numpy as np

#Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# Read image
img = cv.imread('Photos/test.jpg')
translated = translate(img,-100,100)
cv.imshow('translated', translated)
cv.waitKey(0)

#Rotation
def rotate(img, angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)

#Resizing

resized = cv.resize(img,(800,800),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
cv.waitKey(0)

#flipping
flip = cv.flip(img,-1)
cv.imshow('flip', flip)
cv.waitKey(0)

#Cropping
cropped = img[200:400:,300:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)