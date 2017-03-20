import socket


def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8000))
    server_socket.listen(5)
    return server_socket


def recv_msg(sock):
    msg = ''
    data = bytearray()
    while not msg:
        chunk = sock.recv(4096)
        print(chunk)
        if not chunk:
            raise ConnectionError
        data += chunk
        if b'\0' in data:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg


def send_msg(sock, msg):
    msg = msg+'\0'
    sock.sendall(msg.encode('utf-8'))


if __name__ == '__main__':
    server_socket = create_server_socket()
    while True:
        sock, addr = server_socket.accept()
        print('Connection from %s' % str(addr))
        try:
            msg = recv_msg(sock)
            print('Receive %s' % msg)
            send_msg(sock, msg)
        except ConnectionError:
            print('Socket is closed prematurely')
        finally:
            sock.close()
            print('Connection is closed')