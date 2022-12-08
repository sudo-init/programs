

import socket
import threading

from select import select

from utils.general import LOGGER



class Server:

    def __init__(self, ip='127.0.0.1', port=8080, size=1024):
        self.ip = ip
        self.port = port
        self.size = size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = [self.socket]
        self.client_socket, self.client_addr = self.open()

    def __del__(self):
        self.client_socket.close()
        self.socket.close()
    
    def open(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(1)        
        LOGGER.info('Server socket generated.')
        LOGGER.info('Waiting for connection')

        client_socket, client_addr = self.socket.accept()
        LOGGER.info(f'Connected by {client_addr}')
        client_socket.send('Connection success!'.encode())

        return (client_socket, client_addr)

    def run(self, settings, response_q, trigger_q):
        # self.socket.bind((self.ip, self.port))
        # self.socket.listen(1)        
        # LOGGER.info('Server socket generated.')
        # LOGGER.info('Waiting for connection')

        # client_socket, client_addr = self.socket.accept()
        
        try:
            while True:
                data = self.client_socket.recv(self.size)
                
                if data:
                    msg = data.decode()
                    if str(msg) == 'TRIG':   # Robot에서 trigger 줄 때
                        settings['trigger'] = True
                        trig_evt = threading.Event()     # TRIG 신호가 오면
                        trigger_q.put(trig_evt)          # 이벤트 발생시켜서 중단 시켰다가
                        trig_evt.wait()                  # 현재 온 신호에 대한 처리가 완료되면 작업 재개
       
                        if not response_q.empty(): # 응답이 있으면
                            response = response_q.get()
                            response_q.task_done()
                            self.client_socket.sendall(response.encode())    # client에게 응답 (객체 탐지 좌표 보내기)
                        else:
                            response = str(0)
                            self.client_socket.send(response.encode())
                            
                if settings['camera_on'] == False:
                    break

        except Exception as e:
            LOGGER.exception(e)
        
        # while True:
        #     readable_sockets, _, _ = select(self.sockets, [], [])
        #     LOGGER.info('socket loop running..')
            
            
            # try:
            #     for s in readable_sockets:
            #         if s == self.socket:  #  신규 클라이언트 접속
            #             new_client_socket, new_client_addr = self.socket.accept()
            #             LOGGER.info(f'Connected by {new_client_addr}')
            #             new_client_socket.send('Successfully connected to the server.'.encode('utf-8'))
            #             self.sockets.append(new_client_socket)


            #         else:   # 기존 클라이언트의 요청
            #             data = s.recv(self.size)
            #             msg = data.decode('utf-8')
                        
            #             LOGGER.info(msg)
            #             if msg == 'TRIG':   # Robot에서 trigger 줄 때
            #                 settings['trigger'] = True
            #                 # trig_evt = threading.Event()     # TRIG 신호가 오면
            #                 # trigger_q.put(trig_evt)          # 이벤트 발생시켜서 중단 시켰다가
            #                 # LOGGER.info('test3')

            #                 # trig_evt.wait()                  # 현재 온 신호에 대한 처리가 완료되면 작업 재개

            #                 if not response_q.empty(): # 응답이 있으면
            #                     response = response_q.get()
            #                     response_q.task_done()
            #                     s.sendall(response.encode())    # client에게 응답 (객체 탐지 좌표 보내기)
            #             # LOGGER.info(f'received message: {data}')
            #             # s.send('server received the message successfully.'.encode('utf-8'))

            # except ConnectionResetError as cre:
            #     s.close()
            #     self.sockets.remove(s)

            # except Exception as e:
            #     LOGGER.exception(e)

            # if settings['camera_on'] == False:
            #     s.close()
            #     self.sockets.remove(s)
            #     break

    

    # def response(self, socket, data):
    #     socket.sendall(data.encode())
        
        
        
    

