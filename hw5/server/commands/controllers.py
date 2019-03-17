import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError

def get_echo(data):
    if not data:
        data = 'empty'
    result = 1
    loggerInfo.info(f'get {data}. send {result}')
    return str(result)


def get_whoami(data):
    result = 2
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}. send {result}')
    return str(result)


def get_hello(data):
    result = 3
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}. send {result}')
    return str(result)


def get_bye(data):
    result = 4
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}. send {result}')
    return str(result)