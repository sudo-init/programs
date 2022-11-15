import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *

from pyqt_video_player import VideoPlayer


class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.window_width = 1200
        self.window_height = 800
        self.tmp_pos = 200
        self.bg_r = 38
        self.bg_g = 50
        self.bg_b = 56
        
        # main window settings
        # self.setGeometry(self.tmp_pos, self.tmp_pos, self.window_width, self.window_height)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # 타이틀바 없애기
        
        # main window palette
        main_pal = QPalette()
        main_pal.setColor(QPalette.Background, QColor(self.bg_r, self.bg_g, self.bg_b))
        self.setAutoFillBackground(True)
        self.setPalette(main_pal)
        
        """-------------------- widget -------------------- """
        # title label
        title_label = QLabel(text='DW Vision System')
        title_label.setFont(QFont('궁서', 20))
        title_label.setStyleSheet("Color : white; \
                                  border-style: solid; \
                                  border-width: 2px; \
                                  border-color: white")
        
        # widget
        middle_widget = QWidget()
        middle_widget.setStyleSheet("Color : white; \
                                  border-style: solid; \
                                  border-width: 2px; \
                                  border-color: white")
        # widget_pal = QPalette()
        # widget_pal.setColor(QPalette.Background, QColor(255, 255, 255))
        # widget.setAutoFillBackground(True)
        # widget.setPalette(widget_pal)
        
        video_player = VideoPlayer()
        video_player.setParent(middle_widget)
        
        test_label = QLabel(text='TEST', parent = middle_widget)
        
        # ok_button = QPushButton(text='OK', parent=self)
        # ok_button.clicked.connect(self.okButtonPressed)
        # ok_button.move(200, 200)
        
        bottom_widget = QWidget()
        bottom_widget.setStyleSheet("Color : white; \
                                  border-style: solid; \
                                  border-width: 2px; \
                                  border-color: white")
        
        close_button = QPushButton(text='Close')
        close_button.setStyleSheet("color: black;\
                                min-width: 120px;\
                                min-height: 30px;\
                                font-size: 16px;\
                                font-style: consolas;\
                                background-color: rgb(242, 243, 237);")
                                # font-weight: bold;\
        # close_button_w = close_button.size().width()
        # close_button_h = close_button.size().height()
        # close_button_x = self.window_width - close_button_w - 20
        # close_button_y = self.window_height - close_button_h - 20
        # close_button.move(close_button_x, close_button_y)
        close_button.clicked.connect(self.closeEvent)
        
        # ------------------ Layout ------------------
        # main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(title_label)
        main_layout.addStretch(1)
        main_layout.addWidget(middle_widget)
        main_layout.addStretch(1)
        main_layout.addWidget(bottom_widget)

        # middle widget layout
        # grid
        # middle_layout = QGridLayout()
        # middle_widget.setLayout(middle_layout)
        # middle_layout.addWidget(video_player, 0, 0)
        # middle_layout.addWidget(test_label, 0, 1)
        middle_layout = QHBoxLayout()
        middle_widget.setLayout(middle_layout)
        middle_layout.addWidget(video_player)
        middle_layout.addStretch(1)
        middle_layout.addWidget(test_label)
        
        
        # bottom widget layout
        bottom_layout = QHBoxLayout()
        bottom_widget.setLayout(bottom_layout)
        bottom_layout.addStretch(3)
        bottom_layout.addWidget(close_button)
        
        
        
        
    def okButtonPressed(self):
        print('OK button Pressed!')
        
        
            
    def closeEvent(self):
        quit_msg = '종료하시겠습니까?'
        reply = QMessageBox.question(self, '알림', quit_msg, QMessageBox.Yes, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    # main_window.showMaximized()
    app.exec()
