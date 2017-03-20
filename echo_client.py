from echo_server import create_server_socket, send_msg, recv_msg
import socket

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    msg = input('Type the message:')
    try:
        send_msg(client_socket, msg)
        print('Send %s' % msg)
        msg = recv_msg(client_socket)
        print(msg)
    except ConnectionError:
        print('Socket is closed prematurely')
    finally:
        client_socket.close()
        print('Connection is closed')

