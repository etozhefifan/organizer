import socket
import os

from tqdm import trange, tqdm


from transfer.config import BUFFER_SIZE, SEPARATOR, PORT, HOST_CLIENT


class ClientSocket:
    host = HOST_CLIENT
    port = PORT
    separator = SEPARATOR

    def __enter__(self):
        print(f"[+] Connecting to {self.host}:{self.port}")
        return self

    def __exit__(self, *args):
        self.close_socket()

    def __init__(self):
        self.transfer_socket = socket.socket()

    def connect_socket(self):
        print("[+] Connected to ", self.host)
        try:
            self.transfer_socket.connect((self.host, self.port))
        except ConnectionRefusedError as err:
            raise err

    def send_file(self, filename, filesize):
        self.open_file(
            filename,
            self.create_progress_bar(filename, filesize),
        )

    def open_file(self, filename, progress_bar):
        with open(filename, mode='rb') as f:
            print('Sending ', os.path.basename(filename))
            bytes_to_transfer = f.read(BUFFER_SIZE)
            while bytes_to_transfer:
                progress_bar.update(len(bytes_to_transfer))
                self.transfer_socket.send(bytes_to_transfer)
                bytes_to_transfer = f.read(BUFFER_SIZE)

    def create_progress_bar(self, filename, filesize):
        progress_bar = tqdm(
            trange(filesize),
            f'Sending {filename}',
            unit='B',
            unit_scale=True,
        )
        return progress_bar

    def send_file_metadata(self, filename, filesize):
        return self.transfer_socket.sendall(
            f'{filename}{SEPARATOR}{filesize}'.encode()
        )

    def data_received(self):
        confirmation = self.transfer_socket.recv(BUFFER_SIZE)
        print(confirmation)

    def set_file(self, path):
        filesize = os.path.getsize(path)
        return path, filesize

    def close_socket(self):
        print('[-] Connection closed')
        self.transfer_socket.shutdown(socket.SHUT_WR)
        self.transfer_socket.close()
