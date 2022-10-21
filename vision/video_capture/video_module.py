
import cv2
import threading

from math import ceil

# from utils.general import LOGGER
# from general import LOGGER

class VideoModule:

    def __init__(self, video_source = 0 + cv2.CAP_DSHOW):
        self.cam = cv2.VideoCapture(video_source)
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.window_name = 'Video 01'
        # self.img = None

    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()
    
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

    def runVideo(self, image_q):
        if self.cam.isOpened():
            while True:
                status, frame = self.cam.read()
                if status:
                    image_q.put(frame)
                    cv2.imshow(self.window_name, frame)
                    
                if cv2.waitKey(10) == 27 or cv2.getWindowProperty(self.window_name, cv2.WND_PROP_VISIBLE) < 1:
                    break
        else:
            LOGGER.info('Could not open camera.')
            exit()

        
# if __name__ == '__main__':
#     VideoModule().runVideo()
                
                
