# -*- coding: utf-8 -*-

import cv2
import os

class Capture():

    def __init__(self, filename=os.path.abspath("video.mkv") ):
        print filename
        self.c = cv2.VideoCapture(str(filename))
        self.go = False

        #helper
    def tbCallback(self, n):
        self.c.set(1,n)
        ret, frame = self.c.read()
        cv2.imshow("Capture", frame)
        
    def togglePause(self):
        if self.go == False:
            self.go = True
        else:
            self.go=False

            
    def startCapture(self):
        self.togglePause()
        cv2.namedWindow("Capture",0)
        nbFrames= self.c.get(7)
        cv2.createTrackbar("test", "Capture", cv2.getTrackbarPos("test", "Capture"), int(nbFrames), self.tbCallback)
        while(self.go):
            ret, frame = self.c.read()
            cv2.imshow("Capture", frame)
            cv2.waitKey(25)

    def stopCapture(self):
        self.go=False
        cv2.destroyAllWindows()

