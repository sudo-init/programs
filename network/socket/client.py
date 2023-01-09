#-*- coding:utf-8 -*-

import socket
import time
import keyboard
import logging

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

logging.basicConfig(
    level=logging.INFO,
    # format="%(asctime)s [%(levelname)s] %(message)s",
    format = '[%(asctime)s] %(message)s',
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)
    # client_socket.send('connection test'.encode())

    # test_list = [i for i in range(10)]
    idx = 0
    trig = 'TRIG'.encode('utf-8')
    while True:
        data = client_socket.recv(SIZE)

        if data:
            msg = data.decode()
            logging.info(msg)           # 서버로부터 응답받은 메시지 출력
            time.sleep(3)
            client_socket.send(trig)
        
            if msg == 'OFF':
                logging.info('Server off!')
                break
        
        # time.sleep(1)
        
        # logging.info('loop running')

        # if keyboard.is_pressed('Esc'):
        #         logging.info('클라이언트를 종료합니다.')
        #         break