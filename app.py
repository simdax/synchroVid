# -*- coding: utf-8 -*-

import cv2
from PyQt4 import QtGui, QtCore

# communication avec supercollider
# oscPort=57121
import supercollider
from osc import *
from capture import Capture
from dialog import Example

class PanelControl(QtGui.QWidget):
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()

        self.start_button = QtGui.QPushButton('Start/Pause',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.stop_button = QtGui.QPushButton('Stop',self)
        self.stop_button.clicked.connect(self.capture.stopCapture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.quit)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()

    def quit(self):
        self.capture.c.release()
        QtCore.QCoreApplication.quit()

    
#if __name__ == '__main__' :
import sys
app = QtGui.QApplication(sys.argv)
window = Example()
widget = PanelControl(window)
#window.setCentralWidget(window)
sys.exit(app.exec_())
