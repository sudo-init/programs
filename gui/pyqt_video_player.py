
import cv2
import sys
import numpy as np

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage

from general import LOGGER

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()
        # self.change_pixmap_signal = pyqtSignal(np.ndarray)
        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
        # self.cap = cv2.VideoCapture(0)
        # print('video thread init')

    def __del__(self):
        self.cap.release()
    
    def run(self):
        # capture from web cam
        while True:
            ret, cv_img = self.cap.read()
            print('Video running..')

            if ret:
                self.change_pixmap_signal.emit(cv_img)


class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.display_width = 640
        self.display_height = 480
        
        # create the label that holds the image
        self.image_label = QLabel()
        # self.image_label.resize(self.disply_width, self.display_height)
        self.image_label.resize(self.display_width, self.display_height)
 
        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        self.setGeometry(200, 200, self.display_width, self.display_height)
        
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the updateImage slot
        self.thread.change_pixmap_signal.connect(self.updateImage)
        # start the thread
        self.thread.start()

    @pyqtSlot(np.ndarray)
    def updateImage(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convertCvQt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convertCvQt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        # bytes_per_line = ch * w
        # convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        convert_to_qt_format = QImage(rgb_image.data, w, h, QtGui.QImage.Format_RGB888)
        # p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap(convert_to_qt_format)
        # return convert_to_qt_format
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    video_player = VideoPlayer()
    video_player.show()
    app.exec()