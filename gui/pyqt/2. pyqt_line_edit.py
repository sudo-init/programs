
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setWindowTitle('PyQt5 edit form')
    
    form_layout = QFormLayout()  # edit lables을 담을 form layout
    
    edit_label = QLineEdit()              # 문자열 편집이 가능한 edit label
    edit_label.returnPressed.connect(returnTest) # Enter를 눌렀을 때의 동작
    form_layout.addRow('Text', edit_label)       # form layout에 추가
    
    id_label = QLineEdit()
    id_label.setMaxLength(10)           # 문자열의 최대 길이 지정
    form_layout.addRow('Id', id_label)
    
    pw_label = QLineEdit()
    pw_label.setEchoMode(QLineEdit.Password)  # label의 문자 외형을 지정
    form_layout.addRow('Pw', pw_label)
    
    int_valid_label = QLineEdit()
    int_valid_label.setValidator(QIntValidator())
    form_layout.addRow('int', int_valid_label)
    
    double_valid_label = QLineEdit()
    double_valid_label.setValidator(QDoubleValidator(-100, 100, 3))
    form_layout.addRow('double', double_valid_label)
    
    int_mask_label = QLineEdit()
    int_mask_label.setInputMask('999-9999-9999')
    form_layout.addRow('int mask', int_mask_label)
    
    char_mask_label = QLineEdit()
    char_mask_label.setInputMask('aaa.aaa.aaa')
    form_layout.addRow('text mask', char_mask_label)
    
    widget.setLayout(form_layout)       # form layout 을 widget에 추가
    widget.show()
    
    app.exec()

def returnTest(text):
    """
        enter를 눌렀을 때 필요한 동작을 정의한 함수
    """
    print('Enter pressed!')


if __name__ == '__main__':
    window()    
