import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cap1.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayed",gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap =  np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#sabel
sabelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
sabely = cv.Sobel(gray,cv.CV_64F, 0, 1)
combined_sabel = cv.bitwise_or(sabelx,sabely)
cv.imshow("sabel_com",combined_sabel)
cv.imshow("sabelx",sabelx)
cv.imshow("sabely",sabely)

#canny
canny = cv.Canny(img,150,175)
cv.imshow('edges',canny)
cv.waitKey(0)