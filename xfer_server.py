import socket

port = 5001
sock0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock0.connect(("8.8.8.8", 80))
ip = sock0.getsockname()[0]
sock0.close()

sock = socket.socket()
sock.bind((ip,port))
sock.listen(5)

print('Awesome Xfer waiting for your file...')

while True:
    conn, addr = sock.accept()
    print('Got a connection from ', addr)
    print('Awesome Xfer waiting for your file...')

    filename = conn.recv(1024)
    filename = (filename).decode('utf-8')
    file = open('incoming/' + filename, 'wb')

    data = conn.recv(1024)
    while (data):
        print("DATA ", repr(data))
        while (data):
            print('receiving....')
            file.write(data)
            data = conn.recv(1024)
        file.close()
    print('done receiving')
    print('Thanks for connecting')
    conn.close()
sock.close()
