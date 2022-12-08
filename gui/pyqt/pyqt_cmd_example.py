import sys
import subprocess

from PyQt5 import QtWidgets
from PyQt5 import uic


class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("./gui/pyqt/my_python_ui.ui")
        self.ui.Input_line.editingFinished.connect(self.proceed)
        self.ui.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.key_Enter:
            self.proceed()

    def changeOutput(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.proceed()

    def proceed(self):
        proc = subprocess.Popen("""python -c """ + "%s > c:\\res.txt" % self.ui.Input_line.text(), stdout = subprocess.PIPE)
        output = proc.stdout.read().decode('ascii')
        self.ui.Output_area.setText(">> "+output)

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    app.exec()