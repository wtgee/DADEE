#!/usr/bin/env python

import cv2, sys

cam = cv2.VideoCapture(0)   # 0 -> index of camera

# Read initial frame for size
retv, img = cam.read()
frame_size = tuple()

if retv:
    frame_size = cv2.cv.GetSize(cv2.cv.fromarray(img))

fps = 30
writer = cv2.VideoWriter("out.avi", cv2.cv.CV_FOURCC('D', 'I', 'V', 'X'), fps, frame_size, True)

if not cam:
    sys.stdout.write("failed VideoCapture")

if not writer:
    sys.stdout.write("failed writer open")

cv2.namedWindow("cam-test",cv2.CV_WINDOW_AUTOSIZE)
while True:
    retv, img = cam.read()
    if not retv:
        break

    sys.stdout.write( img.tostring() )
    writer.write(img)
    cv2.imshow("cam-test",img)

    press = cv2.waitKey(10)
    if press == 27: # Esc
        break

cam.release()
cv2.destroyAllWindows()
