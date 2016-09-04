# -*- coding: utf-8 -*-

import cv2

class Capture():

    def __init__(self, filename="/home/simdax/Videos/Nirvana - In Bloom.mp4"):
        print filename
        self.c = cv2.VideoCapture(str(filename))
        self.go = False

        #helper
    def tbCallback(self, n):
        self.c.set(1,n)
        
    def togglePause(self):
        if self.go == False:
            self.go = True
        else:
            self.go=False

            
    def startCapture(self):
        self.togglePause()
        cv2.namedWindow("Capture")
        nbFrames= self.c.get(7)
        cv2.createTrackbar("test", "Capture", cv2.getTrackbarPos("test", "Capture"), int(nbFrames), self.tbCallback)
        while(self.go):
            ret, frame = self.c.read()
            cv2.imshow("Capture", frame)

            cv2.waitKey(25)

    def quitCapture(self):
        self.go=False
        cv2.destroyAllWindows()
        #self.c.release()
       # QtCore.QCoreApplication.quit()

