#contours are basically boundary, used in object detection,shape analysis

import numpy as np
import cv2 as cv
img = cv.imread('photos/cap1.jpg')
cv.imshow('cat',img)


#convert to grayyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# #{method-1
# #blur img
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# #Edge cascade
# canny = cv.Canny(img,125,175)
# cv.imshow('edges',canny)
# #---}

#thresholding--tries to binaries the img
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh",thresh)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours drawn", blank)
cv.waitKey(0)
