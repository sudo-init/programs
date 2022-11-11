import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *

from pyqt_video_player import VideoPlayer


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.window_width = 900
        self.window_height = 600
        self.tmp_pos = 200
        self.bg_r = 30
        self.bg_g = 30
        self.bg_b = 30
        
        # main window settings
        # self.setWindowTitle('DW Vision System Demo')
        self.setGeometry(self.tmp_pos, self.tmp_pos, self.window_width, self.window_height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # 타이틀바 없애기
        # self.setWindowFlags(Qt.FramelessWindowHint)
        
        # main_pal = QPalette()
        # main_pal.setColor(QPalette.Background, QColor(self.bg_r, self.bg_g, self.bg_b))
        # self.setAutoFillBackground(True)
        # self.setPalette(main_pal)
        
        # widget = QWidget(parent=self)
        # widget.setGeometry(self.tmp_pos, self.tmp_pos, self.window_width, self.window_height)
        # widget.set
        
        # widget
        widget = QWidget(parent=self)
        
        # widget_pal = QPalette()
        # widget_pal.setColor(QPalette.Background, QColor(255, 255, 255))
        # widget.setAutoFillBackground(True)
        # widget.setPalette(widget_pal)
        
        title_label = QLabel(text='DW Vision System', parent=widget)
        title_label.setFont(QFont('궁서', 20))
        title_label.setStyleSheet('Color : white')
        
        
        
        video_player = VideoPlayer()
        video_player.setParent(widget)
        
        # test 
        # test_label = QLabel(text='TEST', parent=widget)
        
        # ok_button = QPushButton(text='OK', parent=self)
        # ok_button.clicked.connect(self.okButtonPressed)
        # ok_button.move(200, 200)
        
        close_button = QPushButton(text='Close', parent=widget)
        close_button_w = close_button.size().width()
        close_button_h = close_button.size().height()
        close_button_x = self.window_width - close_button_w - 20
        close_button_y = self.window_height - close_button_h - 20
        close_button.move(close_button_x, close_button_y)
        # close_button.clicked.connect(QCoreApplication.instance().quit)
        close_button.clicked.connect(self.closeEvent)
        
        
        
        # widget layout
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(title_label, 0, 0)
        layout.addWidget(video_player, 1, 0)
        layout.addWidget(close_button, 2, 0)
        # layout.addWidget(test_label, 1, 0)
        # layout.addWidget(title_label, 9)
        # layout.addWidget(ok_button, 2, 0)
        
        
        
        # widget.show()
        
        # print(close_button.size())
        # print(close_button.size().scale)
        
    def okButtonPressed(self):
        print('OK button Pressed!')
        
        
            
    def closeEvent(self):
        quit_msg = '종료하시겠습니까?'
        reply = QMessageBox.question(self, '알림', quit_msg, QMessageBox.Yes, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        # else:
        #     event.ignore()
    
    # def cvtQtImg(self, image):
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     h, w, ch = image.shape
    #     bytes_per_line = ch * w
    #     qt_image =  QImage(image.data, w, h, bytes_per_line, 
    #                        QImage.Format_RGB888)
    #     pixmap = QPixmap(qt_image)
        
    # def update_image(self, image):
    #     cvtQtImg()
        
    

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