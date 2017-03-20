import socket
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

a = client_socket.send('From client_1'.encode('utf-8'))
print(a)
time.sleep(10)
data = client_socket.recv(100)
print(data)
while True:
    b=1
client_socket.close()