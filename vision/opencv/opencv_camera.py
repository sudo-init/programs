
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
    x = (cam_w / 2) - (width / 2)
    y = (cam_h / 2) - (height / 2)
    cropped_img = img[y: y + height, x: x + width]
    
    return cropped_img

# ------------------------------------------------------

# log 설정
logger = setLogger()

video_source = 0 + cv2.CAP_DSHOW
video_source2 = cv2.CAP_V4L2
video_sourec3 = 0
window_name = 'test'
w = 640
h = 480

# Video Capture 인스턴스 생성
cam = cv2.VideoCapture(video_source)
# cam = get_cam(video_source, cam_width, cam_height)

cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(cam_w, cam_h)

# ----------------------------------------------------------

if cam.isOpened():
    pass
    # cv2.namedWindow('demo', cv2.WINDOW_AUTOSIZE)
    
    # while True:
    #     status, frame = cam.read()
        
    #     # if (not status) or (cv2.waitKey() == 27):
    #     #     break
        
    #     if status:
    #         # start = time()
            
    #         resized_frame = cv2.resize(frame, (w, h))
    #         cv2.imshow(window_name, resized_frame)
            
    #         # logging.info(time()- start)
    #         # cropped_img = crop_img(cam, frame, w, h)
    #         # try:
    #         #     print(frame)
    #         #     print(type(frame))
    #         #     print(len(frame))
    #         # except Exception as e:
    #         #     logging.exception(e)    
            
    #         # cv2.imshow(window_name, frame)
        
    #     if cv2.waitKey(1) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) <1:
    #         break
        
else:
    logger.info('Colud not open e-con camera.')
    exit()

cam.release()
cv2.destroyAllWindows()
