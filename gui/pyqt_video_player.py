
import cv2
import sys
import numpy as np

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, \
                            QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QImage

from general import LOGGER

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)

    def __del__(self):
        self.cap.release()
    
    def run(self):
        while True:
            ret, cv_img = self.cap.read()

            if ret:
                self.change_pixmap_signal.emit(cv_img)


class VideoPlayer(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.captured_img_count = 0
        
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the updateImage slot
        self.thread.change_pixmap_signal.connect(self.updateImage)
        # start the thread
        self.thread.start()
        
        self.capture_button.clicked.connect(self.captureImage)
        self.save_button.clicked.connect(self.saveImage)
        
    def initUI(self):
        # main widgets
        self.video_widget = QWidget()
        self.capture_widget = QWidget()
        
        # component of video widgets
        self.image_label = QLabel()
        self.video_utils_widget = QWidget()
        self.start_button = QPushButton(text='Start')
        self.stop_button = QPushButton(text='Stop')
        self.time_label = QLabel(text='경과시간:')
        
        # component of capture widgets
        self.capture_label = QLabel()
        self.capture_label.setPixmap(returnQPixmap(np.zeros((480, 680, 1))))
        self.capture_utils_widget = QWidget()
        self.capture_button = QPushButton(text='Capture')
        self.save_button = QPushButton(text='Save')
        self.state_label = QLabel('Test')
        
        # video layout
        video_utils_layout = QGridLayout(self.video_utils_widget)
        video_utils_layout.addWidget(self.start_button, 0, 0)
        video_utils_layout.addWidget(self.stop_button, 0, 1)
        video_utils_layout.addWidget(self.time_label, 1, 0)
        video_layout = QVBoxLayout(self.video_widget)
        video_layout.addWidget(self.image_label)
        video_layout.addWidget(self.video_utils_widget)
        
        # capture layout
        capture_utils_layout = QGridLayout(self.capture_utils_widget)
        capture_utils_layout.addWidget(self.capture_button, 0, 3)
        capture_utils_layout.addWidget(self.save_button, 1, 3)
        capture_utils_layout.addWidget(self.state_label, 0, 0)
        capture_layout = QVBoxLayout(self.capture_widget)
        capture_layout.addWidget(self.capture_label)
        capture_layout.addWidget(self.capture_utils_widget)
        
        # main layout
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.video_widget)
        main_layout.addWidget(self.capture_widget)

    @pyqtSlot(np.ndarray)
    def updateImage(self, cv_img):
        """Updates the image_label with a new opencv image"""
        self.cv_img = cv_img
        self.qt_img = convertCvQt(cv_img)
        self.image_label.setPixmap(self.qt_img)
 
    def captureImage(self):
        self.captured_img = self.qt_img
        self.captured_cv_img = self.cv_img
        self.capture_label.setPixmap(self.captured_img)
        
    def saveImage(self):
        file_path = './'
        cv2.imwrite(file_path + 'captured_img' + str(self.captured_img_count) + '.jpg', self.captured_cv_img)
        self.captured_img_count += 1
        LOGGER.info('saved image.')
        
    
    

def convertCvQt(cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    # bytes_per_line = ch * w
    # convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    convert_to_qt_format = QImage(rgb_image.data, w, h, QtGui.QImage.Format_RGB888)
    # p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
    return QPixmap(convert_to_qt_format)
    # return convert_to_qt_format

def returnQPixmap(img):
    h, w, ch = img.shape
    format = QImage(img.data, w, h, QtGui.QImage.Format_RGB888)    
    return QPixmap(format)


if __name__=="__main__":
    app = QApplication(sys.argv)
    video_player = VideoPlayer()
    video_player.show()
    app.exec()