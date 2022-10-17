import socket
import logging

IP = '127.0.0.1'
PORT = 8080
SIZE = 1024
ADDR = (IP, PORT)

logging.basicConfig(
    level=logging.INFO,
    # format="%(asctime)s [%(levelname)s] %(message)s",
    format = '[%(asctime)s] %(message)s',
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)
    server_socket.listen()

    try:
        client_socket, client_addr = server_socket.accept()

        with client_socket:
            logging.info(f'Connected by {client_addr}')

            while True:
                
                msg = client_socket.recv(SIZE)
    
    except Exception as e:
        logging.exception(e)

    # finally:
    #     client_socket.close()

    

