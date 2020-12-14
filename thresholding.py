import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cap1.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayed",gray)

#simple thresholding[manually specify thrshold value]
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple thresholding",thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple thresholding inverse",thresh_inv)

#Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresholing", adaptive_thresh)
cv.waitKey(0)