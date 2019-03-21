import socket
from args_parser import arg_parser

def set_connection():
    ADDR, PORT = arg_parser()
    sock = socket.socket()
    sock.connect((ADDR, PORT))
    return sock