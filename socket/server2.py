import socket

IP = ''
PORT = ''
SIZE = ''
ADDR = (IP, PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)
    server_socket.listen()


    while True:
        client_socket, client_addr = server_socket.accept()
        msg = client_socket.recv(SIZE)
        