import socket
import sys


client_socket = socket.socket()
client_socket.connect(('localhost', 8000))
print('connect to %s' % str(client_socket.getpeername()))

ifile = client_socket.makefile('r')
ofile = client_socket.makefile('w')

original_stdout = sys.stdout
sys.stdin = ifile
sys.stdout = ofile

print('hola server')
# sys.stdout.write('hola tech crunch\n')
data = input()
original_stdout.write(data)

