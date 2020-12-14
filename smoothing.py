import cv2 as cv

img = cv.imread('photos/cap1.jpg')
cv.imshow('cat',img)

#averaging
average = cv.blur(img, (3,3))
cv.imshow("avg blur",average)

#gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gauss blur",gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow("median blur",median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25 )
cv.imshow("bilateral blur",bilateral)

cv.waitKey(0)