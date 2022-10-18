import socket
import logging

from general import *
from select import select



class Server:

    def __init__(self, ip='127.0.0.1', port=8080, size=1024):
        self.ip = ip
        self.port = port
        self.size = size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def __del__(self):
        self.server_socket.close()
    

    # def run(self):
    #     self.socket.bind(self.ip, self.port)
    #     self.socket.listen()        
    #     LOGGER.info('Server socket generated.')
    #     LOGGER.info('Waiting for connection')

    #     sockets = [self.socket]
        
    #     while True:
    #         readable_sockets, _, _ = select(sockets, [], [])
            
    #         try:

    #             for s in readable_sockets:
    #                 if s == self.socket:  #  신규 클라이언트 접속
    #                     new_client_socket, new_client_addr = self.socket.accept()
    #                     LOGGER.info(f'Connected by {new_client_addr}')
    #                     new_client_socket.send('Successfully connected to the server.'.encode('utf-8'))
    #                     sockets.append(new_client_socket)
                        

    #                 else:   # 기존 클라이언트의 요청
    #                     data = s.recv(self.size)

    #                     if data: # 클라이언트에서 데이터가 들어왔을 때
    #                         data = data.decode('utf-8')
    #                         LOGGER.info(f'received message: {data}')
    #                         s.send('server received the message successfully.'.encode('utf-8'))
    #                     else:
    #                         s.close()
    #                         sockets.remove(s)

    #         except ConnectionResetError as cre:
    #             s.close()
    #             sockets.remove(s)

    #         except Exception as e:
    #             LOGGER.exception(e)
        
    



    

