

import sys

from PyQt5.QtWidgets import *


class Application(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.button_1.clicked.connect(self.button1Function)
        
    
    
    def button1Function(self):
        print('Button 1 clicked!')
    
    
    
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
    app = QApplication([])
    label = QLabel("Hello world, I'm python")
    label.show()
    # sys.exit(app.exec_())  # python
    app.exec()
    
    