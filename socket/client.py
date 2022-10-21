#-*- coding:utf-8 -*-

import socket
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
    client_socket.send('connection test'.encode())

    test_list = [i for i in range(10)]
    idx = 0

    while True:
        msg = client_socket.recv(SIZE)

        logging.info(msg)
        if msg:
            logging.info(msg.decode()) # 서버로부터 응답받은 메시지 출력
        
        if idx < 10:
            send_msg = f'connection test {test_list[idx]}'.encode('utf-8')
            client_socket.send(send_msg)
            idx += 1
        
        else:
            break

        # if keyboard.is_pressed('Esc'):
        #         logging.info('클라이언트를 종료합니다.')
        #         break