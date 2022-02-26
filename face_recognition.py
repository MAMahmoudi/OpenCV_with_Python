import cv2 as cv
import numpy as np
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# features = np.load('features.npy')
# labels = np.load('labels.npy')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(r'F:\OpenCV_Python\Faces\val\ben_afflek\3.jpg')
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Person',gray)
faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y + h, x:x + w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Dtected face',img)
cv.waitKey(0)






