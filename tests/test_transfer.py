import pytest
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir_content = os.listdir(BASE_DIR)


def test_check_folder():
    assert 'transfer' in root_dir_content


class TestServerSocket():
    from transfer.sockets.server_socket import ServerSocket
    server = ServerSocket()

    def test_server_socket_existence(self):
        assert self.server

    def test_server_port(self):
        assert self.server.port == int(os.getenv('PORT'))

    def test_server_host(self):
        assert self.server.host == os.getenv('HOST_SERVER')

    def test_server_separator(self):
        from transfer.config import SEPARATOR
        assert self.server.separator == SEPARATOR

    def test_setup_server_socket(self):
        assert self.server.setup_socket()