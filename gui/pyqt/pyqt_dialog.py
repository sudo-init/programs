#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialog example')
        self.setGeometry(100, 100, 300, 150)

        # widget
        self.explain_label = QLabel('This is Pyqt5 dialog example')
        self.open_button = QPushButton('Open Dialog')
        self.open_button.clicked.connect(self.openDialog)
        
        # layout
        self.layout = QVBoxLayout(self)
        self.layout.addStretch(1)
        self.layout.addWidget(self.explain_label, alignment=Qt.AlignCenter)
        self.layout.addStretch(2)
        self.layout.addWidget(self.open_button)
        
        # QDialog 
        self.dialog = QDialog()

    def openDialog(self):
        dialog_hello_label = QLabel("Hello, it's me..")
        dialog_ok_button = QPushButton("OK")
        
        dialog_layout = QVBoxLayout(self.dialog)
        dialog_layout.addWidget(dialog_hello_label, alignment=Qt.AlignCenter)
        dialog_layout.addWidget(dialog_ok_button)
        
        dialog_ok_button.clicked.connect(self.closeDialog)

        # QDialog
        self.dialog.setWindowTitle('Dialog')
        """
        setWindowModality()
            Qt.NonModal: 값은 0, 다른 윈도우 화면 입력을 차단하지 않음
            Qt.WindowModal: 값은 1, 모든 윈도우 창의 입력을 차단
            Qt.ApplicationModal: 값은 2, dialog를 실행시킨 부모 프로그램만 차단
        """
        self.dialog.setWindowModality(Qt.ApplicationModal) 
        self.dialog.setFixedSize(200, 80)
        self.dialog.show()

    def closeDialog(self):
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()