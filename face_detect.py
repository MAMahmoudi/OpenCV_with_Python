import cv2 as cv
# Read image
img = cv.imread('Photos/test2.jpg')
cv.imshow('test', img)
#converting img to grayscale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
print(f'# of faces found= {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected faces', img)






cv.waitKey(0)