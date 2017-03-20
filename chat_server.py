import socket
from threading import Thread, Lock
from queue import Queue


def recv_msgs(sock, data=bytes()):
    msgs = []
    while not msgs:
        received = sock.recv(1024)
        if not received:
            raise ConnectionError()
        data = data + received
        data = data.split(b'\0')
        msgs = data[:-1]
        rest = data[-1]
    return msgs, rest


def broadcast(msg):
    with lock:
        for q in send_queue.values():
            q.put(msg)


def handle_disconnect(sock, addr):
    with lock:
        q = send_queue.get(sock.fileno(), None)
    if q:
        with lock:
            q.put(None)
            del send_queue[sock.fileno()]
        sock.close()
        print('Client %s is disconnected.' % str(addr))


def handle_recv(sock:socket.socket, addr):
    rest = bytes()
    while True:
        try:
            msgs, rest = recv_msgs(sock, rest)
        except ConnectionError:
            handle_disconnect(sock, addr)
            break
        msgs = [msg.decode('utf-8') for msg in msgs]
        for msg in msgs:
            msg = '{}:{}'.format(addr, msg)
            print(msg)
            broadcast(msg)


def send_msg(sock, msg):
    msg = msg+'\0'
    sock.sendall(msg.encode('utf-8'))


def handle_send(sock, q:Queue, addr):
    while True:
        msg = q.get()
        if not msg:
            break
        try:
            send_msg(sock, msg)
        except ConnectionError:
            handle_disconnect(sock, addr)


if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8000))
    server_socket.listen(10)
    send_queue = {}
    lock = Lock()

    while True:
        sock, addr = server_socket.accept()
        print('Connection from %s' % str(addr))
        q = Queue()
        with lock:
            send_queue[sock.fileno()] = q
        recv_thread = Thread(target=handle_recv, args=(sock, addr), daemon=True)
        send_thread = Thread(target=handle_send, args=(sock, q, addr), daemon=True)
        recv_thread.start()
        send_thread.start()
