import socket
import os
import sys

port = 5001
sock0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock0.connect(("8.8.8.8", 80))
ip = sock0.getsockname()[0]
sock0.close()

sock = socket.socket()
sock.connect((ip, port))

filename = sys.argv[1]
if not os.path.isfile(filename):
    print(filename + " does not exist")
    sys.exit(1)

file = open(filename, 'rb')
sock.sendall(filename.encode('utf-8'))

print('Sending....')
data = file.read(1024)
while(data):
    print('sending...')
    sock.send(data)
    data = file.read(1024)
file.close()
print('Done Sending')
sock.shutdown(socket.SHUT_WR)
sock.close()
