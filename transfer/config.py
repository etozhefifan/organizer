import os


from dotenv import load_dotenv

load_dotenv()

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

NAME_OF_PROGRAM = "dlibrary"

HOST_SERVER = os.getenv("HOST_SERVER")
HOST_CLIENT = os.getenv("HOST_CLIENT")
PORT = int(os.getenv("PORT"))
