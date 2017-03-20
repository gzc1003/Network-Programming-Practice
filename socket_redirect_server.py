import socket
import sys
import time
import os


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(5)
conn, addr = server_socket.accept()
print('connection from %s' % str(addr))
ifile = conn.makefile('r')
ofile = conn.makefile('w')

sys.stdin = ifile
original_stdout = sys.stdout
sys.stdout = ofile

data = input()
# original_stdout.write(str(os.isatty(original_stdout.fileno())))
original_stdout.write(data)
# original_stdout.flush()
print('hello %s\n' % str(conn.getpeername()))
time.sleep(5)
sys.stdout.flush()
