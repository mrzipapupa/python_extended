from args_parser import arg_parser
import socket

def set_connection():
    ADDR, PORT = arg_parser()
    sock = socket.socket()
    sock.bind((ADDR, PORT))
    sock.listen(5)
    return sock