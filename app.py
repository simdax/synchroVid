#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2

def tbCallback(n):
    cap.set(1,n)
    bob()

cap = cv2.VideoCapture("/home/simdax/Vidéos/Nirvana - In Bloom.mp4")
# 7 prop = nbFrames
nbFrames= cap.get(7)

#open win
cv2.namedWindow('frame')
cv2.createTrackbar("test", 'frame', 0, int(nbFrames), tbCallback)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        kill()
        break
    
cap.release()
cv2.destroyWindow('frame')
