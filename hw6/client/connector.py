import socket
from args_parser import arg_parser
import sys
sys.path.insert(0, '..\\')
from log.client_log_config import loggerInfo, loggerError

def set_connection():
    ADDR, PORT = arg_parser()
    if not ADDR or not PORT:
        loggerError.warning('cannot get ip-addr or port from cmd')
    sock = socket.socket()
    sock.connect((ADDR, PORT))
    return sock