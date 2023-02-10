import socket
import os

from config import HOST_SERVER, PORT, BUFFER_SIZE, SEPARATOR

# sock = socket.socket()

# sock.bind((SERVER_HOST, SERVER_PORT))
# sock.listen(10)
# print(
#     f'Listening at {SERVER_HOST}:{SERVER_PORT}\n'
#     'Waiting for the client to connect !*!'
# )
# client_socket, address = sock.accept()
# print(f'{address} is connected')
# received = client_socket.recv(BUFFER_SIZE).decode()
# filename, filesize = received.split(SEPARATOR)
# filename = os.path.basename(filename)
# filesize = int(filesize)
# with open(filename, "wb") as f:
#     while True:
#         bytes_read = client_socket.recv(BUFFER_SIZE)
#         if not bytes_read:
#             break
#         f.write(bytes_read)
# client_socket.close()
# socket.close()


class ServerSocket:
    host = HOST_SERVER
    port = PORT
    separator = SEPARATOR

    def __enter__(self):
        print(
            f'Listening at {self.host}:{self.port}\n'
            'Waiting for the client to connect !*!'
        )
        return self
    
    def __exit__(self, *args):
        pass

    def __init__(self):
        self.transfer_socket = socket.socket()

    def setup_socket(self):
        self.transfer_socket.bind((self.host, self.port))
        self.transfer_socket.listen(10)

    def accept_connection(self):
        try:
            client_socket, address = self.transfer_socket.accept()
            print(f'{address} is connected and ready to upload')
        except ValueError:
            print('client and address were not connected')
        return client_socket

    def receive_file(self, client_socket):
        received = client_socket.recv(BUFFER_SIZE).decode()
        return received

    def download_file(self, client_socket, received_file):
        filename, filesize = received_file.split(self.separator)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        with open(filename, 'wb') as f:
            while (filesize - BUFFER_SIZE) > 0 or filesize > 0:
                try:
                    bytes_read = client_socket.recv(BUFFER_SIZE)
                    filesize -= BUFFER_SIZE
                except Exception as err:
                    raise err
                f.write(bytes_read)
        # КАК ЕГО ЗАКРЫТЬ?!?!?!?!?!?!?!
        client_socket.close()

    def close_sockets(self, client_socket):
        client_socket.close()
        self.transfer_socket.close()
