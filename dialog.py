# -*- coding: utf-8 -*-

from capture import Capture
import cv2

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

#        self.textEdit = QtGui.QTextEdit()
#        self.setCentralWidget(self.textEdit)
#        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/simdax/Videos/')
        #TODO encode pb
        #fname=str(fname).encode('utf-8').decode('utf-8', 'replace')
        a=self.children()[-1]
        #a.capture.quitCapture()
        print fname
        a.capture.c=cv2.VideoCapture(str(fname))
                                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
