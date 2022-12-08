import socket
import logging

from select import select


IP = '127.0.0.1'
PORT = 8080
SIZE = 1024
ADDR = (IP, PORT)

logging.basicConfig(
    level=logging.INFO,

    # 로그 출력 형태
    # format="%(asctime)s [%(levelname)s] %(message)s",
    format = '[%(asctime)s] %(message)s',

    # 로그 파일 저장
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)
    server_socket.listen()
    # client_socket, client_addr = server_socket.accept()
    logging.info('Server socket generated.')
    logging.info('Waiting for connection.')


    # with client_socket:
    #     logging.info(f'Connected by {client_addr}')
    #     client_socket.send('Connection success!'.encode())

    sockets = [server_socket]
    
    while True:
        readable_sockets, _, _ = select(sockets, [], [])
        
        try:

            for s in readable_sockets:
                if s == server_socket:  #  신규 클라이언트 접속
                    new_client_socket, new_client_addr = server_socket.accept()
                    logging.info(f'Connected by {new_client_addr}')
                    new_client_socket.send('Successfully connected to the server.'.encode('utf-8'))
                    sockets.append(new_client_socket)
                    

                else:   # 기존 클라이언트의 요청
                    data = s.recv(SIZE)
                    
                    if not data: # 클라이언트에서 데이터가 들어왔을 때
                        logging.info(data)
                        logging.info('데이터 전송이 없음.')
                        sockets.remove(s)
                        s.close()
                        

                    else:
                        logging.info(data)
                        data = data.decode('utf-8')
                        logging.info(f'received message: {data}')
                        s.send('server received the message successfully.'.encode('utf-8'))


        except ConnectionResetError or ConnectionAbortedError as connection_error:
            logging.info(connection_error)
            logging.info('클라이언트와의 연결이 끊겼습니다.')
            sockets.remove(s)
            s.close()

        except Exception as e:
            logging.exception(e)

        

            # 트리거 전송
            
            
            # 모델 좌표계산
            
            
            # 좌표 전송
    
    



    

