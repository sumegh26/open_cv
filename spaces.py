import cv2 as cv
import matplotlib.pyplot as plt
#keep in mind inversion of colors btween diff lib.
img = cv.imread('photos/cap1.jpg')
cv.imshow('cat',img)

# plt.imshow(img)
# plt.show()
#BGR to grayyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#grayscale to bgr
bg = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray---->bgr',bg)
#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)