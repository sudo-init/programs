
from math import ceil
from tkinter import W
import cv2
import logging
from time import time

def setLogger(level=logging.INFO, formatter=None, save_path=''):
    logger = logging.getLogger()
    logger.setLevel(level)    # 로그 level 설정 (INFO, ERROR 등등)
    
    if formatter == None:
        formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)s} %(levelname)s - %(message)s')
    else:
        formatter = formatter
        
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)     # 로그 출력 형태 설정
    logger.addHandler(stream_handler)

    return logger


def get_cam(video_source, cam_width, cam_height):
    cam = cv2.VideoCapture(video_source)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)
    
    return cam 

def crop_img(cam, img, width, height):
    cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    x = ceil(cam_w / 2) - ceil(width / 2)
    y = ceil(cam_h / 2) - ceil(height / 2)
    cropped_img = img[:, y: y + height, x: x + width]
    
    return cropped_img

# ------------------------------------------------------

# log 설정
logger = setLogger()

video_source = 0 + cv2.CAP_DSHOW
video_source2 = cv2.CAP_V4L2
video_sourec3 = 0
window_name = 'test'
w = 640 # // 2
h = 480 # // 2

# Video Capture 인스턴스 생성
# cam = cv2.VideoCapture(video_source)
cam = get_cam(video_source, w, h)

cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(cam_w, cam_h)

# ----------------------------------------------------------

if cam.isOpened():
    count = 1
    while True:
        status, frame = cam.read()
        
        # if (not status) or (cv2.waitKey() == 27):
        #     break
        
        if status:
            
            # resized_frame = cv2.resize(frame, (w, h))
            # cv2.imshow(window_name, resized_frame)
            # print(f'frame_img: {frame.shape}')

            try:
                if count == 1:
                    print(frame)
                    print(type(frame))
                    print(len(frame))
                    print(frame.shape)
                    count += 1
            except Exception as e:
                logging.exception(e)    
            
            # cropped_img = crop_img(cam, frame, w, h)
            # print(f'cropped_img: {cropped_img.shape}')
            # cv2.imshow(window_name, cropped_img)

            cv2.imshow(window_name, frame)

        if cv2.waitKey(1) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) <1:
            break
        
else:
    logger.info('Colud not open e-con camera.')
    exit()

cam.release()
cv2.destroyAllWindows()




import cv2

from math import ceil

class VideoModule:

    def __init___(self, video_source = 0 + cv2.CAP_DSHOW):
        self.video_source = video_source
        self.cam = cv2.VideoCapture(self.video_source)
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def set_cam(self, video_source, width, height):
        self.cam = cv2.VideoCapture(video_source)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def get_cam(self):
        return self.cam

    def crop_img(self, cam, img, width, height):
        cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        x = ceil(cam_w / 2) - ceil(width / 2)
        y = ceil(cam_h / 2) - ceil(height / 2)
        cropped_img = img[:, y: y + height, x: x + width]

        return cropped_img