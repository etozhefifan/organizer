import socket
import os
import time

from io import BytesIO
from tqdm import tqdm


from config import BUFFER_SIZE, SEPARATOR, PORT, HOST_CLIENT

# s = socket.socket()
# print(f"[+] Connecting to {HOST_CLIENT}:{PORT}")
# s.connect((HOST_CLIENT, PORT))
# print("[+] Connected to ", HOST_CLIENT)
# filename = input("File to Transfer : ")
# filesize = os.path.getsize(filename)
# s.send(f"{filename}{SEPARATOR}{filesize}".encode(encoding='utf-8'))
# progress = tqdm(
#     range(filesize),
#     f'Sending {filename}',
#     unit='B',
#     unit_scale=True
# )
# with open(filename, mode="rb") as f:
#     while True:
#         bytes_read = f.read(BUFFER_SIZE)
#         if not bytes_read:
#             break
#         s.sendall(bytes_read)
#         progress.update(len(bytes_read))
# s.close()


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

    def send_file(self):
        filename = input("File to Transfer : ")
        filesize = os.path.getsize(filename)
        # self.transfer_socket.send(
        #     f"{filename}".encode()
        # )
        self.open_file(
            filename,
            self.create_progress_bar(filename, filesize),
        )

    def open_file(self, filename, progress):
        with open(filename, mode='rb') as f:
            bytes_to_transfer = f.read(BUFFER_SIZE)
            while bytes_to_transfer:
                progress.update(len(bytes_to_transfer))
                self.transfer_socket.send(bytes_to_transfer)
                bytes_to_transfer = f.read(BUFFER_SIZE)

    def create_progress_bar(self, filename, filesize):
        progress = tqdm(
            range(filesize),
            f'Sending {filename}',
            unit='B',
            unit_scale=True,
        )
        return progress

    def close_socket(self):
        print('[-] Connection closed')
        self.transfer_socket.shutdown(socket.SHUT_WR)
        self.transfer_socket.close()
