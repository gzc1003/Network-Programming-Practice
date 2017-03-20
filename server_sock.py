import socket
import time

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)
while True:
    sock, addr = server_socket.accept()
    while True:
        data = sock.recv(10)
        print(data)
        if not data:
            break
        # time.sleep(5)
        response = "HELLO, BABY"
        nu = sock.send(response.encode('utf-8'))
        print(nu)
        # time.sleep(5)
        nu = sock.send('hhe'.encode('utf-8'))
        print(nu)
    sock.close()
server_socket.close()