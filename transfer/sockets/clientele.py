import socket
import os

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
        self.transfer_socket.send(
            f"{filename}{self.separator}{filesize}".encode()
        )
        with open(filename, mode='rb') as f:
            while (filesize - BUFFER_SIZE) > 0 or filesize > 0:
                try:
                    bytes_read = f.read(BUFFER_SIZE)
                    filesize -= BUFFER_SIZE
                except Exception as err:
                    raise err
                self.transfer_socket.sendall(bytes_read)

    def close_socket(self):
        print('[-] Connection closed')
        self.transfer_socket.close()
