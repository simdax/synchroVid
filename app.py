import cv2
from PyQt4 import QtGui, QtCore

# communication avec supercollider
# oscPort=57121
#import supercollider
from osc import *
import cv2

from dialog import Example

class Capture():

    def __init__(self):
        self.c = cv2.VideoCapture("/home/simdax/Vidéos/Nirvana - In Bloom.mp4")
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
        self.c.release()
        QtCore.QCoreApplication.quit()


class PanelControl(QtGui.QWidget):
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()

        self.start_button = QtGui.QPushButton('Start/Pause',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitCapture)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()

#if __name__ == '__main__' :
import sys
app = QtGui.QApplication(sys.argv)
window = Example()
widget = PanelControl(window)
#window.setCentralWidget(window)
sys.exit(app.exec_())
