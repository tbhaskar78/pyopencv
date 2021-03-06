#!/usr/bin/env python3
'''
 Author: Bhaskar Tallamraju
 Date: 03 Sep 2020

 REQUIREMENTS:
       1. cv2 : pip3 install opencv-python
       2. os

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at https://mozilla.org/MPL/2.0/.
'''
import cv2
import os
import time

# directory of images
directory = '../images/'

# absolute path of haarcascades
haarcascade = "../../../opencv/data/haarcascades/haarcascade_frontalface_alt.xml"

def draw_str(dst, target, s):
    x, y = target
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.LINE_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)

# iterate over all files in images and then read the images in
for filename in os.listdir(directory):
    # only pick up images
    if filename.endswith(("jpeg", "jpg", "png", "bmp", "webp")):
        faces = cv2.CascadeClassifier(haarcascade)                  # open the haarcascade classifier
        img = cv2.imread(directory+filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # convert it to gray scale
        #img_gray = cv2.equalizeHist(img_gray)

        t = time.process_time()
        # detections give the x, y coordinates and the width and height in the form (x, y, w, h)
        detections = faces.detectMultiScale(img_gray, scaleFactor=1.01, minNeighbors=20)

        # go over the array of detections and create a rectangle of red color (b, g, r), not (r, g, b)
        for (x, y, w, h) in detections :
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        winname = "faces"                # name the window
        cv2.namedWindow(winname)         # Create a named window
        cv2.moveWindow(winname, 40, 30)  # Move it to (40,30)

        dt = time.process_time() - t

        draw_str(img, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow(winname, img)

        # in linux, the waitkey does not seem to destroy the window, created a hacky way of doing it
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    else:                               # ignore non images
        continue
