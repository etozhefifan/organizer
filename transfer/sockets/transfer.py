import socket
import os

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8081
BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'

sock = socket.socket()

sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(10)
print(
    f'Listening at {SERVER_HOST}:{SERVER_PORT}\n'
    'Waiting for the client to connect !*!'
)
client_socket, address = sock.accept()
print(f'{address} is connected')
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
client_socket.close()
socket.close() 
