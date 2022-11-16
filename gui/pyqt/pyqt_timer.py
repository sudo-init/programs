import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.timer.timeout.connect(self.timeout) 
        self.start_button.clicked.connect(self.startButtonClicked)
        self.stop_button.clicked.connect(self.stopButtonClicked)
 
        self.stop_button.setEnabled(False)
        
    def initUI(self):
        self.setWindowTitle('Timer')
        self.setGeometry(200, 200, 400, 200)
        
        # timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.time = QTime.fromString('00:00:00', 'hh:mm:ss')
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)
        self.lcd.display('00:00:00')
        self.lcd.setStyleSheet('border-style: None;')
        self.lcd.setSegmentStyle(2)
        
        # buttons
        self.start_button = QPushButton('start')
        self.stop_button = QPushButton('stop')

        # layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.lcd)
        sub_layout = QHBoxLayout()
        sub_layout.addWidget(self.start_button)
        sub_layout.addWidget(self.stop_button)
        main_layout.addLayout(sub_layout)
        
    def startButtonClicked(self):
        self.timer.start()
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)
    
    def stopButtonClicked(self):
        self.timer.stop()
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
    
    def timeout(self):
        self.time = self.time.addSecs(1)
        if id(self.sender()) == id(self.timer):
            self.lcd.display(self.time.toString("hh:mm:ss"))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    app.exec()