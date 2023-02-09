from sockets.transfer import ServerSocket

if __name__ == '__main__':
    with ServerSocket() as ss:
        ss.setup_socket()
        client_socket = ss.accept_connection()
        received_file = ss.receive_file(client_socket)
        ss.download_file(client_socket, received_file)
