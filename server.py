import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',5000))

s.listen(5)
print('Waiting for connection...')


def tcplink(sock,addr):
    print(addr)
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Welcome!')
    
    while True:  
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode()=='exit':
            break
        sock.send(('Hello, %s!'%data.decode()).encode())
    sock.close()
    print('Connection from %s:%s closed.'%addr)


while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
