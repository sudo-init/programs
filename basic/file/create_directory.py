"""
파일 및 디렉토리 생성 example
"""

import os


# 디렉토리 생성하는 함수 정의
def createDirectory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print('Directory created!')
    except OSError as e:
        print('OS Error raised!')
        print(e)


if __name__ == '__main__':
    parent_abs_path = str(os.getcwd())
    file_path = parent_abs_path + '/tmp_direcotry/'

    try:
        # 파일 생성
        f = open(file_path + 'test.txt', 'w')
        
    # try except로 디렉토리 없으면 생성하도록
    except FileNotFoundError as e:
        print('-----------------')
        print('Error: No such file or directory ' + file_path)
        print('-----------------')
        createDirectory(file_path)
        f = open(file_path + 'test.txt', 'w')
    
    f.close()
    print('program run well.')



        
    

