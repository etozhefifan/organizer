from os import getenv

from dotenv import load_dotenv
load_dotenv()

SEPARATOR = '<SEPARATOR>'
BUFFER_SIZE = 4096

HOST_SERVER = getenv('HOST_SERVER')
HOST_CLIENT = getenv('HOST_CLIENT')
PORT = int(getenv('PORT'))
PATH_TO_DIR = getenv('PATH_TO_DIR')
