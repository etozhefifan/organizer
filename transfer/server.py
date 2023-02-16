from sockets.transfer import ServerSocket

if __name__ == '__main__':
    with ServerSocket() as ss:
        ss.setup_socket()
        while True:
            client_socket = ss.accept_connection()
            received_metadata = ss.receive_metadata(client_socket)
            filename, filesize = ss.separate_metadata(received_metadata)
            ss.download_file(
                client_socket,
                ss.get_file(filename),
                ss.create_progress_bar(filename, filesize))
        ss.close_sockets(client_socket)
