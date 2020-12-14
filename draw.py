import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)
# img = cv.imread('photos/cat.jpg')
# cv.imshow('cat', img)

# blank[200:300, 300:400] = 0,255,255
# cv.imshow('Green' , blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0),  thickness=-1)
cv.imshow('Rectangle',blank)

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)
cv.imshow('Circle',blank)

#draw line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('line',blank)

#write text on img
cv.putText(blank, 'Hello there!', (255,255), cv.FONT_HERSHEY_TRIPLEX , 1.0, (0,255,0), 2)
cv.imshow('Text',blank)
cv.waitKey(0)