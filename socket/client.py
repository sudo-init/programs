#-*- coding:utf-8 -*-

import socket

SERVER_IP = ''
SERVER_PORT = ''
SIZE = 0
SERVER_ADDR = (SERVER_IP, SERVER_PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)
    client_socket.send('hi'.encode())

    msg = client_socket.recv(SIZE)
    print(msg) # 서버로부터 응답받은 메시지 출력