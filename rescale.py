import cv2 as cv

#writing functions

def rescaleFrame(frame, scale=0.20):
    #for images,videos,live feed
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #for live feed only
    capture.set(3,width)
    capture.set(4,height)

#reading pics
img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

resized_image = rescaleFrame(img)
cv.imshow('catt',resized_image)

#reading videos
capture = cv.VideoCapture('videos/getoi.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()