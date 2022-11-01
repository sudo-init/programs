"""
    Delta Robot Vision System
"""

import cv2
import keyboard
import os
import time
import threading

from pathlib import Path
from queue import Queue
from select import select

from utils.general import LOGGER
from utils.server import Server
from utils.video_module import VideoModule
from utils.dw_detect import DwDetect
from utils.vision_tools import camera_realtimeXYZ

ROOT = str(Path(__file__).resolve().parent)

class DeltaRobotVisionSystem:

    def __init__(self, ip='127.0.0.1', port=8080, size=1024):
        # Test version
        self.video_data = ROOT + '/data/raw_data/test.mp4'
        self.test_win_name = 'Test'
        
        # variables
        self.size = size
        self.image_q = Queue()          # 카메라에서 읽어들이는 영상을 저장하는 queue
        self.response_q = Queue()     # detected product x, y values
        self.trigger_q = Queue()        # 트리거 신호가 올 때 마다 해당 이벤트를 저장하는 Queue
        self.settings = {'camera_on': True, 'trigger': False}
        self.camera_path = ROOT + '/utils/camera_data/'
        self.weight_path = ROOT + '/models/weights/' + 'delta_robot_ep300.pt'
        
        # module
        self.server = Server(ip, port)                           # 서버 
        # self.video_module = VideoModule()                      # 비디오 카메라 (device 0)
        self.video_module = VideoModule(self.video_data)         # 비디오 카메라 (test 용)
        self.model = DwDetect(self.weight_path)                  # 탐지 모델
        self.calibration = camera_realtimeXYZ(self.camera_path)  # 보정 모듈
        
        # 쓰레드
        self.commu_thread = threading.Thread(tartget=self.server.run(self.settings, self.response_q, self.trigger_q,))  # 통신 쓰레드
        self.video_thread = threading.Thread(target=self.video_module.runVideo, args=(self.image_q, self.settings,))    # 카메라 쓰레드
        self.detect_thread = threading.Thread(target=self.detectSystem, args=(self.image_q,))                           # 객체 탐지 쓰레드
        
        # ----- Latch signal 주의사항 -----
        # latch를 받은 시점(Rising Edge) 오브젝트의 엔코더 데이터를 저장
        # 획득된 이미지 안의 상황에 래치신호가 On이 최대한 동기화 되어야 함
        # 반드시 래치신호가 TCP/IP로 도착하는 좌표값보다 먼저 도착해야 함(순서가 어긋나면 에러 발생)
        # 한 번의 래치에 한 번의 데이터가 와야 함(한 번의 래치에 두 개 이상의 데이터가 오면 에러)
        

    def detectSystem(self, image_q):
        while True:
            LOGGER.info('detect System Running')
            if not image_q.empty():
                # start = time.time()
                # LOGGER.info('Enter image_q loop')
                data, evt = image_q.get()   # 이미지 get
                image_q.task_done()
                evt.set()
                # data = image_q.get()
                
                # 여기서 Latch 신호 ON
                # Latch on 신호를 보냄

                if len(data) != 0:
                    LOGGER.info('Enter if len(data) != 0')
                    img = self.calibration.imgUndistort(data)  # camera calibration
                    pred_coordinates = self.model.robot_detect(img)  # 객체 탐지   (centerX, Y 반환)
                    response = self.setData(pred_coordinates)        # 반환값 구성 (client 요청에 대한 response)
                    self.response_q.put(response)
            
                # 여기서 Latch 신호 Off
                # Latch off 신호를 보냄
                
                trigger_evt = self.trigger_q.get()   # 트리거 이벤트 get
                self.trigger_q.task_done()           # 트리거 큐 동기화
                trigger_evt.set()                    # 트리거 이벤트 대기 해제
                
                LOGGER.info(pred_coordinates)    
            
                
            # LOGGER.info(f'get 경과 시간: {time.time() - start}')
# -------------------------------- test start --------------------------------
                # start2 = time.time()
                # if self.settings['trigger']:        # if trigger == True
                #     img, pred_coordinates = self.model.ai_detect(data)
                # if pred_coordinates:
                #     self.coordinate_q.put(pred_coordinates)
            
                # 화면 출력 (test용)
                # img, pred_coordinates = self.model.ai_detect(data)
                # cv2.imshow(self.test_win_name, img)
                # # LOGGER.info(f'detect 경과 시간: {time.time() - start2}')
                # if cv2.waitKey(10) != -1 or cv2.getWindowProperty(self.test_win_name, cv2.WND_PROP_VISIBLE) < 1 \
                #     or not self.settings['camera_on']:
                #     cv2.destroyAllWindows()            
                #     self.settings['camera_on'] = False
                #     LOGGER.info('Detect thread loop break!')
                #     break
# ---------------------------------- test end ----------------------------------
            
            if not self.settings['camera_on']:
                break
            
        while not image_q.empty():
            _, evt = image_q.get()
            evt.set() 
            image_q.task_done()
            # LOGGER.info('Running queue loop')
        
        LOGGER.info('Detect thread exited!')


    def setData(self, pred_coordinates):
        if pred_coordinates:
            x, y = pred_coordinates[0]
            a = 0
            attr = 0
            id = 0
        else:
            x = y = 0
                
        a = 0
        attr = 0
        id = 0
            
        return f'[X:{x};Y:{y};A:{a};ATTR:{attr};ID:{id}]'
    
    
    def sendLatchSignal(self, signal):
        pass
    

    def run(self):
        # start = time.time()
        
        self.commu_thread.start()       # 소켓 통신 thread
        time.sleep(1)
        self.video_thread.start()       # 비디오 카메라 thread
        time.sleep(1)
        self.detect_thread.start()      # 객체 탐지 thread
        
        

        # self.image_q.join()
        # self.coordinate_q.join()
        # self.trigger_q.join()
        # LOGGER.info(f'경과 시간: {time.time() - start}')
       

if __name__ == '__main__':
    try:
        DeltaRobotVisionSystem().run()
    except Exception as e:
        LOGGER.info(e)
        exit()
    



    


