from transfer.sockets.server_socket import ServerSocket

# def close_sockets():
#     ss.close_sockets()


def main_server():
    with ServerSocket() as ss:
        ss.setup_socket()
        while True:
            client_socket = ss.accept_connection()
            received_metadata = ss.receive_metadata(client_socket)
            filename, filesize = ss.separate_metadata(received_metadata)
            filename = ss.get_file(filename)
            ss.download_file(
                client_socket,
                filename,
                ss.create_progress_bar(filename, filesize))
