import cv2 as cv

# img = cv.imread('photos/cat.jpg')

# cv.imshow('cat',img)
capture = cv.VideoCapture('videos/getoi.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
#cv.waitKey(0)
capture.release()
cv.destroyAllWindows()