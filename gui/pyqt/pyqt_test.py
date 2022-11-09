import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    
    widget = QWidget()
    widget.setWindowTitle('PyQt5 Test')
    
    ok_button = QPushButton('OK', widget)
    ok_button.clicked.connect(okButtonClicked)
    
    ok_button.move(100, 50)
    ok_button.resize(70, 20)
    
    widget.show()
    app.exec()
    
def okButtonClicked():
    print('Button pressed!')



class App(QWidget):
   
   def __init__(self):
      super().__init__()
		
      
      
      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked():
         print("button pressed")
      else:
         print("button released")
			
   def whichbtn(self,b):
      print("clicked button is "+b.text())


if __name__ == '__main__':
   window()