"""
    cv2로 이미지를 읽고
    메모리 상에서 imencode를 사용해서 png, jpg 파일 등으로 변환하는 예제.
    저장할 때는 f.write() 사용.
"""

import cv2
import os


def image_load(file):
    cv_img = cv2.imread(file)
    
    status, result = cv2.imencode('.png', cv_img)
    if status:
        return result


def createDirectory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print('Directory created!')
    except OSError as e:
        print('OS Error raised!')
        print(e)


def save_image(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    file_path = './data/'
    file = 'beatles.jpg'
    
    img = image_load(file_path + file)
    save_image(file_path + 'beatles.png', img)