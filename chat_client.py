import socket
from threading import Thread
from chat_server import send_msg, recv_msgs


def client_send_msg(sock: socket.socket):
    print("Type massage or 'q' to quit")
    while True:
        msg = input()
        if msg == 'q':
            break
        try:
            send_msg(sock, msg)
        except ConnectionError:
            break
    print('Close client connection')
    sock.close()


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    send_thread = Thread(target=client_send_msg, args=(client_socket,))
    send_thread.start()
    rest = bytes()
    while True:
        try:
            msgs, rest = recv_msgs(client_socket, rest)
        except ConnectionError:
            client_socket.close()
            break
        for msg in msgs:
            msg = msg.decode('utf-8')
            print(msg)

