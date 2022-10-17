import cv2
import os
import logging


class VideoCapture():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)    # 로그 level 설정 (INFO, ERROR 등등)
        formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)s} %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)     # 로그 출력 형태 설정
        self.logger.addHandler(stream_handler)

    def dataLoad(self, data_path):
        return cv2.VideoCapture(data_path)
        
    def imageCapture(eslf, videoCapture : cv2.VideoCapture):
        images = []
        
        while True:
            retval, image = videoCapture.read()
            
            if not(retval):
                break
            
            images.append(image)
            
        if videoCapture.isOpened():
            videoCapture.release()
        
        return images

    def createDirectory(self, file_path):
        file_path = file_path + '/captured_images'
        
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
        
        except OSError as e:
            logging.exception(e)

        return file_path


    def saveImage(self, images, file_path=None):
        """이미지 저장 함수

        Args:
            images (list): 저장할 이미지
            file_path (string, optional): 이미지가 저장될 위치. Defaults to None.
        """
        
        # 디렉토리 생성 및 경로 반환
        file_path = self.createDirectory(file_path)
        
        # 이미지 저장
        for i, image in enumerate(images):
            # bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            path = file_path + '/' + 'image_' + str(i) + '.jpg'
            cv2.imwrite(path, image)

    def run(self, path, file):
        total_path = os.path.join(path, file)
        
        try:
            vc = self.dataLoad(total_path)   # get cv2.VideoCapture
            self.logger.info('Data load completed!')
            
            images = self.imageCapture(vc)   # capture of images
            self.logger.info('image capture completed!')
            # self.logger.info()
            
            self.saveImage(images, path)           # saving images
            self.logger.info('saving images completed!')
            
        except Exception as e:
            logging.exception(e)
        
def main():
    path = 'C:/Users/user/projects/delta_robot/yolov5/runs/detect/exp'
    file_name = 'test.mp4'
    # file_path = os.path.join(path, file_name)
    
    VideoCapture().run(path, file_name)
    

if __name__ == '__main__':
    main()