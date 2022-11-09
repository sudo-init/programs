

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Application(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.button_1.clicked.connect(self.button1Function)
        
    
    
    def button1Function(self):
        print('Button 1 clicked!')
    
    

def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    label = QLabel(widget)
    label.setText('Hello World!')
    widget.setGeometry(200, 200, 800, 600)   # widget의 크기
    
    label.move(50, 20)
    widget.setWindowTitle('PyQt5 Test')
    widget.show()
    app.exec()

class TestWindow(QWidget):
    
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(200, 50)
        self.setWindowTitle("PyQt5 Test")
        
        self.content_text = 'Hello World!'
        self.content_label = QLabel(self.content_text)
        
        # self.font = QFont()
        # self.font.setfamily()
        # self.font.setPointSize()
        # self.content_label.setFont(self.font)
    
    def set_label_text(self, label, text):
        label.setText(text)
        
    
if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # testApp = Application()
    # testApp.show()
    # app.exec_()
    
    # app = QApplication([])
    # label = QLabel('Hello World!')
    # label.show()
    # app.exec()
    
    # app = QApplication(sys.argv)
    # app = QApplication([])
    # label = QLabel("Hello world, I'm python")
    # label.show()
    # sys.exit(app.exec_())  # python
    # app.exec()
    
    window()
    
    