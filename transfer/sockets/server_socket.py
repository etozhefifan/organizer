import socket
import os

from tqdm import tqdm

from .utils.decorator import logger_decorator
from .utils.config import HOST_SERVER, PORT, BUFFER_SIZE, SEPARATOR, NAME_OF_PROGRAM


class ServerSocket:
    host = HOST_SERVER
    port = PORT
    separator = SEPARATOR
    server_online = True

    def __enter__(self):
        print(
            f"Listening at {self.host}:{self.port} "
            "Waiting for the client to connect !*!"
        )
        return self

    def __exit__(self, *args, **kwargs):
        print("Server closed")
        self.close_sockets()

    def __init__(self):
        self.transfer_socket = socket.socket()

    @logger_decorator
    def setup_socket(self):
        self.transfer_socket.bind((self.host, self.port))
        self.transfer_socket.listen(10)

    @logger_decorator
    def accept_connection(self):
        try:
            print("Server is ready to accept connections")
            client_socket, address = self.transfer_socket.accept()
            print(f"{address} is connected and ready to upload")
        except ValueError:
            print("client and address were not connected")
        return client_socket

    @logger_decorator
    def receive_metadata(self, client_socket):
        received = client_socket.recv(BUFFER_SIZE).decode()
        client_socket.send(b"Metadata received. Start uploading")
        return received

    @logger_decorator
    def download_file(
        self, client_socket, filename: str, progress_bar, path_to_storage: str
    ) -> None:
        with open(os.path.join(path_to_storage, filename), "wb") as f:
            bytes_received = client_socket.recv(BUFFER_SIZE)
            while bytes_received:
                f.write(bytes_received)
                progress_bar.update(len(bytes_received))
                bytes_received = client_socket.recv(BUFFER_SIZE)
        print(f"{filename} downloaded")

    def get_file(self, received_metadata):
        return os.path.basename(received_metadata)

    @logger_decorator
    def separate_metadata(self, metadata):
        filename, filesize = metadata.split(SEPARATOR)
        return filename, filesize

    def create_progress_bar(self, filename, filesize):
        progress_bar = tqdm(
            range(int(filesize)),
            f"Downloading {filename}",
            unit="B",
            unit_scale=True,
        )
        return progress_bar

    @logger_decorator
    def close_sockets(self) -> None:
        print("Server closed")
        self.transfer_socket.close()

    @logger_decorator
    def get_path_to_downloads(self) -> str:
        if os.name == "nt":
            path_to_downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
        path_to_downloads = f"{os.getenv('HOME')}/Downloads"
        return path_to_downloads

    @logger_decorator
    def check_if_storage_exists(self, path_to_downloads: str) -> str:
        downloads_content = os.listdir(path_to_downloads)
        if NAME_OF_PROGRAM in downloads_content:
            print("Directory is already created")
        else:
            os.mkdir(os.path.join(path_to_downloads, NAME_OF_PROGRAM))
            print("Directory created")
        return os.path.join(path_to_downloads, NAME_OF_PROGRAM)

    @logger_decorator
    def stop_server(self):
        self.server_online = False
