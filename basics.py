import cv2 as cv
img = cv.imread('photos/cap.jpg')
cv.imshow('cap',img)

#convert to grayyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur img
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('edges',canny)

#dilating img
dilated = cv.dilate(canny,(3,3), iterations=3)
cv.imshow('Dilated',dilated)

#eroding
eroded = cv.erode(dilated,(3,3), iterations=3)
cv.imshow('Eroded',eroded)

#resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)