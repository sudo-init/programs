import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        
        self.initUI()
        
    def initUI(self):
        self.window_width = 600
        self.window_height = 400
        self.tmp_pos = 200
        self.bg_r = 30
        self.bg_g = 30
        self.bg_b = 30
        
        # main window settings
        # self.setWindowTitle('DW Vision System Demo')
        self.setGeometry(self.tmp_pos, self.tmp_pos, self.window_width, self.window_height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # 타이틀바 없애기
        
        main_pal = QPalette()
        main_pal.setColor(QPalette.Background, QColor(self.bg_r, self.bg_g, self.bg_b))
        self.setAutoFillBackground(True)
        self.setPalette(main_pal)
        
        # widget = QWidget(parent=self)
        # widget.setGeometry(self.tmp_pos, self.tmp_pos, self.window_width, self.window_height)
        # widget.set
        
        title_label = QLabel(text='DW Vision System', parent=self)
        title_label.setFont(QFont('궁서', 20))
        title_label.setStyleSheet('Color : white')
        
        ok_button = QPushButton(text='OK', parent=self)
        ok_button.clicked.connect(self.okButtonPressed)
        ok_button.move(200, 200)
        
        close_button = QPushButton(text='Close', parent=self)
        close_button_w = close_button.size().width()
        close_button_h = close_button.size().height()
        close_button_x = self.window_width - close_button_w - 20
        close_button_y = self.window_height - close_button_h - 20
        close_button.move(close_button_x, close_button_y)
        close_button.clicked.connect(QCoreApplication.instance().quit)
        
        # print(close_button.size())
        # print(close_button.size().scale)
        
    def okButtonPressed(self):
        print('OK button Pressed!')
        
        
            
    def closeEvent(self, event):
        quit_msg = '종료하시겠습니까?'
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
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