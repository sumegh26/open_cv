import cv2 as cv
import numpy as np

img = cv.imread('photos/cap.jpg')
cv.imshow('cap',img)

#translation
# -x  ----->left
# -y  ----->up
# x  ----->right
# y  ----->Down
def traslate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
traslated = traslate(img,100,100)
cv.imshow("translated",traslated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated  = rotate(img,-45)
rotated_rot = rotate(rotated,-45)
cv.imshow("rotated img",rotated)
cv.imshow("twice rot",rotated_rot)

#resizing
#enlarge[INTER_CUBIC/INTER_LINEAR]
#SMALL[INTER_AREA/IT IS DEFAULT]
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow("resized",resized)

#flip
# 0 vertically
# 1 horizontally
# -1 both

flip = cv.flip(img,-1)
cv.imshow("flip",flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)