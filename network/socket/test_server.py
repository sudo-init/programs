
from concurrent.futures import thread
import logging
import socket

from _thread import *


def threaded():
    pass

client_sockets = []

HOST = ''
PORT = ''

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(HOST, PORT)
server_socket.listen()

try:
    while True:
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, ())

except Exception as e:
    logging.exception(e)    


