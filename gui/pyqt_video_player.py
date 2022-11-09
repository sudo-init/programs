
import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PyQtVideoPlayer(QObject):
    
    # def __init__(self, parent=None):
    #     super(PyQtVideoPlayer, self).__init__()
    
    def __init__(self)                                          :
        super(PyQtVideoPlayer, self).__init__()
        
        self.camera = cv2.VideoCapture(0)
    
        VideoSignal1 = pyqtSignal(QImage)
        VideoSignal2 = pyqtSignal(QImage)
        
    @pyqtSlot()
    def videoPlayer(self):
        # global image 
        
        while True:
            
            status, frame = self.camera.read()
            
            if status:
                pass
    