from connector import set_connection
import socket
import json
import sys
sys.path.insert(0, '..\\')
from log.client_log_config import loggerInfo, loggerError


def set_presence_message():
    try:
        sock = set_connection()
        loggerInfo.info('connection complete')
        loggerInfo.info(f'Server: {sock.getpeername()}\n'
                        f'Client: {sock.getsockname()}')
        return sock
    except socket.error as msg:
        loggerError.error(f'Error with socket: {msg}')
        exit(-1)


def set_message(action, data):
    loggerInfo.debug('forming message for server...')
    requestString = json.dumps(
        {
            'action': action,
            'data': data
        }
    )
    return requestString.encode()



def receive_response(sock):
    data = sock.recv(1024)
    loggerInfo.debug('get message from server')
    if data:
        response_parser(data)
    sock.close()


def response_parser(data):
    loggerInfo.debug('send message to server')
    serverResponse = data.decode('utf-8')
    return serverResponse
