import socket
import os

from tqdm import tqdm

from config import HOST_SERVER, PORT, BUFFER_SIZE, SEPARATOR, PATH_TO_DIR


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

    def receive_metadata(self, client_socket):
        received = client_socket.recv(BUFFER_SIZE).decode()
        client_socket.send(b'Metadata received. Start downloading')
        return received

    def download_file(self, client_socket, filename, progress_bar):
        with open(os.path.join(PATH_TO_DIR, filename), 'wb') as f:
            bytes_received = client_socket.recv(BUFFER_SIZE)
            while bytes_received:
                f.write(bytes_received)
                progress_bar.update(len(bytes_received))
                bytes_received = client_socket.recv(BUFFER_SIZE)

    def get_file(self, received_metadata):
        return os.path.basename(received_metadata)

    def separate_metadata(self, metadata):
        filename, filesize = metadata.split(SEPARATOR)
        return filename, filesize

    def create_progress_bar(self, filename, filesize):
        progress_bar = tqdm(
            range(int(filesize)),
            f'Downloading {filename}',
            unit='B',
            unit_scale=True,
        )
        return progress_bar

    def close_sockets(self, client_socket):
        client_socket.close()
        self.transfer_socket.close()
