import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    """
        단순한 문자열 출력
    """
    
    # app = QApplication(sys.argv)
    app = QApplication([])
    label = QLabel("Hello world, I'm python")
    label.show()
    # sys.exit(app.exec_())  
    app.exec()


def window2():
    """
        윈도우 사이즈 및 폰트 설정
    """
    
    app = QApplication(sys.argv)             # QApplication 객체 
    widget = QWidget()                       # 최상위 윈도우 생성
    widget.setGeometry(200, 200, 800, 600)   # widget의 크기
    widget.setWindowTitle('PyQt5 Test')      # 윈도우 타이틀 설정
    
    label = QLabel(widget)              # 레이블을 윈도우에 추가
    label.setText('Hello World!')       # 레이블 문자 설정
    label.move(100, 20)                 # 레이블의 위치 
                                        # (left-top이 원점, 인자는(x, y))
    
    content_label = QLabel(widget)       # 두 번째 레이블
    content_text = 'Hello World!'        # 두 번째 레이블 문자      
    content_label.setText(content_text)  # 두 번째 레이블 문자 설정
    content_label.move(100, 50)                 # 레이블의 위치 
    
    font = QFont()                # 폰트 객체
    font_style = 'Arial'          # 폰트 스타일
    font.setFamily(font_style)    # 폰트 스타일 설정
    font_size = 16                # 폰트 사이즈
    font.setPointSize(font_size)  # 폰트 사이즈 설정
    content_label.setFont(font)   # 폰트 적용
    
    widget.show()
    app.exec()

if __name__ == '__main__':
    # window()    # 단순한 문자열 출력
    window2()   # 윈도우 사이즈 및 폰트 조절



