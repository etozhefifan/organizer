from transfer.sockets.clientele import ClientSocket


def main_client(path):
    if path:
        with ClientSocket() as cs:
            cs.connect_socket()
            filename, filesize = cs.set_file(path)
            cs.send_file_metadata(filename, filesize)
            cs.data_received()
            cs.send_file(filename, filesize)
    print('Please, choose file to upload to server')
