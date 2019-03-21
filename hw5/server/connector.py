from args_parser import arg_parser
import socket
import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError

def set_connection():
    ADDR, PORT = arg_parser()
    if not ADDR or not PORT:
        loggerError.warning('cannot get addr or port from cmd')
    sock = socket.socket()
    sock.bind((ADDR, PORT))
    sock.listen(5)
    return sock