import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# Read image
img = cv.imread('Photos/test.jpg')
cv.imshow('test', img)
#converting img to grayscale
# gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# cv.imshow('Gray', gray)
blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2-50,img.shape[0]//2-100),100,255,-1)
# mask = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('',mask)
# #Grayscal histogram
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
#Color histogram
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('',mask)
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)