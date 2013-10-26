#!/usr/bin/env python

import cv2
import sys

# Some setup values
cam_device = 0

output_filename = 'foo.avi'
fourcc = cv2.cv.CV_FOURCC('F', 'M', 'P', '4')
is_color = False

# Setup capture and write device
vc = cv2.VideoCapture()
vw = cv2.VideoWriter()

vc.open(cam_device)


def get_fps():
    # return vc.get(cv2.cv.CV_CAP_PROP_FPS)
    return 30


def get_size():
    width = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    return (width, height)

fps = get_fps()
video_size = get_size()

print("{} at {}".format(fps, video_size))

vw.open(output_filename, fourcc, fps, video_size, is_color)

# Show the grab
cv2.namedWindow("cam-test", cv2.CV_WINDOW_AUTOSIZE)

# Test if device was opened and start capturing
if vc.isOpened() and vw.isOpened():

    # Loop until we loose image
    i = 0
    while i < 10:
        got_img, img = vc.read()

        if got_img:
            img_name = "imgs/image_{}.jpg".format(i)
            vw.write(img)
            cv2.imwrite(img_name, img)
            cv2.imshow("cam-test",img)
            i += 1

        press = cv2.waitKey(300)
        if press == 27:  # Esc
            cv2.destroyAllWindows()
            vc.release()
            del(vc)
            del(vw)
            break

else:
    print("Problem opening device {}".format(cam_device))
