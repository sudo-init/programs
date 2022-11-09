import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('DW Vision System Demo')
        ok_button = QPushButton(text='OK', parent=self)
        ok_button.clicked.connect(self.okButtonPressed)
        
    def okButtonPressed(self):
        print('OK button Pressed!')
    
    
    

if __name__ == '__main__':
    
    # app = QApplication(sys.argv)
    # window = QMainWindow()
    # window.setWindowTitle('DW Vision System Demo')
    # ok_button = QPushButton(text='OK', parent=window)
    # window.show()
    # app.exec()
    
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    app.exec()