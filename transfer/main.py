from sockets.clientele import ClientSocket


if __name__ == '__main__':
    with ClientSocket() as cs:
        cs.connect_socket()
        cs.send_file()
