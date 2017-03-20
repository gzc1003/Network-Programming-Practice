import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5000))
print(s.recv(1024).decode('utf-8'))
for data in [b'Guo',b'Liu',b'Zhang']:
    s.send(data)
    print(s.recv(1024).decode())

s.send(b'exit')

s.close
