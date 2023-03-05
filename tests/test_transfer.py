import pytest
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir_content = os.listdir(BASE_DIR)


def test_check_folder():
    assert "transfer" in root_dir_content


class TestServerSocket:
    from transfer.sockets.server_socket import ServerSocket

    server = ServerSocket()
    port = int(os.getenv("PORT"))
    host = os.getenv("HOST_SERVER")

    def test_server_socket_existence(self):
        assert self.server

    def test_server_port(self):
        assert self.server.port == self.port

    def test_server_host(self):
        assert self.server.host == self.host

    def test_server_separator(self):
        from transfer.config import SEPARATOR

        assert self.server.separator == SEPARATOR

    def test_setup_server_socket(self):
        self.server.setup_socket()
        assert self.server.transfer_socket.getsockname() == (self.host, self.port)

    # def test_server_accepts_connections(self):
    #     assert self.server.transfer_socket.accept()
