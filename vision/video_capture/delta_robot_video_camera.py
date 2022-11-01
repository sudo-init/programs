
import cv2
import threading

from math import ceil

from utils.general import LOGGER


class VideoModule:
    def __init__(self, video_source = 0 + cv2.CAP_DSHOW):
        self.cam = cv2.VideoCapture(video_source)
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.window_name = 'Video 01'
        self.frame = []
        # self.img = None

    def __del__(self):
        self.cam.release()
    
    def setWindowName(self, window_name):
        self.window_name = window_name

    def setCam(self, video_source, width, height):
        """
            video camera setting
        """
        try:
            self.cam = cv2.VideoCapture(video_source)
            self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        except Exception as e:
            LOGGER.info('Camera setting error!')

    def cropImg(self, cam, img, width, height):
        cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        x = ceil(cam_w / 2) - ceil(width / 2)
        y = ceil(cam_h / 2) - ceil(height / 2)
        cropped_img = img[:, y: y + height, x: x + width]

        return cropped_img

    def runVideo(self, image_q, settings):
        LOGGER.info('Video test2')
        if self.cam.isOpened():
            LOGGER.info('Video test2')
            while True:
                if not settings['camera_on']:    # 카메라 꺼지면 종료
                    LOGGER.info('Video camera off!')
                    LOGGER.info('Video thread exited!')
                    break

                # status, frame = self.cam.read()
                # if status and settings['trigger']:
                if settings['trigger']:
                        status, frame = self.cam.read()
                        if status:
                            settings['trigger'] = False
                            evt = threading.Event()
                            image_q.put((frame, evt))
                            evt.wait()
        else:
            LOGGER.info('Could not open camera.')
            exit()


    def runVideo2(self, image_q, settings):
        LOGGER.info('Video thread running..')
        if self.cam.isOpened():
            LOGGER.info('Camera opened')
            while True:
                status, frame = self.cam.read()
                if status:
                    self.frame = frame
                else:
                    settings['camera_on'] = False
                    LOGGER.info('Video camera off!')
                    LOGGER.info('Video camera thread exited!')
                    break
        else:
            LOGGER.info('Could not open camera.')
            exit()
                
                
