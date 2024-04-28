import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 1337))
sock.listen(10)

conn = False

while True:
    if conn is False:
        print('Waiting for connection')
        conn, client = sock.accept()
        print('Connection from', client)
    else:
        received = conn.recv(1024)
        print(received)

sock.close()
