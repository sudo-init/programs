
import cv2
import sys
import numpy as np

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, \
                            QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QImage, QFont

from general import LOGGER

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    capture_img_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
        self.frame_count = 0
        self.save_per_frame = 50

    def __del__(self):
        self.cap.release()
    
    def run(self):
        while True:
            ret, img = self.cap.read()

            if ret:
                self.change_pixmap_signal.emit(img)
                
                self.frame_count += 1
                
                if self.frame_count == self.save_per_frame:
                    self.capture_img_signal.emit(img)


class VideoPlayer(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.captured_img_count = 0
        self.auto_captured_img_count = 0
        self.initUI()
        
        # video thread
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.updateImage) # connect its signal to the updateImage slot
        self.thread.start()
        
        # timer
        self.timer.timeout.connect(self.timeout)
        
        # button action
        # self.start_button.clicked.connect()
        self.capture_button.clicked.connect(self.captureImage)
        self.save_button.clicked.connect(self.saveImage)
        self.start_button.clicked.connect(self.startButtonClicked)
        self.stop_button.clicked.connect(self.stopButtonClicked)
        self.stop_button.setEnabled(False)
        
        
    def initUI(self):
        # main widgets
        self.video_widget = QWidget()
        self.capture_widget = QWidget()
        self.default_font = 'arial'
        self.default_font_size = 10
        
        # component of video widgets
        self.image_label = QLabel()
        self.video_utils_widget = QWidget()
        self.start_button = QPushButton(text='Start')
        self.stop_button = QPushButton(text='Stop')
        self.reset_button = QPushButton(text='reset')
        self.time_label = QLabel(text='경과시간: ')
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.time = QTime().fromString('00:00:00', 'hh:mm:ss')
        self.time_display_label = QLabel(self.time.toString('hh:mm:ss'))
        self.time_display_label.setFont(QFont(self.default_font, self.default_font_size))
        self.save_img_count_label = QLabel('수집된 이미지 수: ')
        self.save_img_count_display = QLabel(str(self.auto_captured_img_count))
        self.save_img_count_display.setFont(QFont(self.default_font, self.default_font_size))
        
        # component of capture widgets
        self.capture_label = QLabel()
        self.capture_label.setPixmap(returnQPixmap(np.zeros((480, 640, 1))))
        self.capture_utils_widget = QWidget()
        self.capture_button = QPushButton(text='Capture')
        self.save_button = QPushButton(text='Save')
        self.state_label = QLabel('Test')
        
        # video layout
        video_utils_layout = QGridLayout(self.video_utils_widget)
        video_utils_layout.addWidget(self.start_button, 0, 0, 1, 3)
        video_utils_layout.addWidget(self.stop_button, 0, 3, 1, 3)
        video_utils_layout.addWidget(self.reset_button, 0, 6, alignment=Qt.AlignmentFlag.AlignRight)
        video_utils_layout.addWidget(self.time_label, 1, 0,)           # '경과 시간' label
        video_utils_layout.addWidget(self.time_display_label, 1, 1,)   # 시간 표시 label
        video_utils_layout.addWidget(self.save_img_count_label, 4, 0, 1, 1)
        video_utils_layout.addWidget(self.save_img_count_display, 4, 1)
        
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
        
    def timeout(self):
        self.time = self.time.addSecs(1)
        if id(self.sender()) == id(self.timer):
            self.time_display_label.setText(self.time.toString('hh:mm:ss'))
    
    def startButtonClicked(self):
        self.timer.start()
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)
    
    def stopButtonClicked(self):
        self.timer.stop()
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
        
    def resetButtonClicked(self):
        # 알람버튼 뜨도록
        pass
        
    

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