from sockets.clientele import ClientSocket


if __name__ == '__main__':
    with ClientSocket() as cs:
        cs.connect_socket()
        filename, filesize = cs.set_file()
        cs.send_file_metadata(filename, filesize)
        cs.connect_socket()
        cs.send_file(filename, filesize)
