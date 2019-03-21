import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError


def get_upper(data):
    result = data.upper()
    loggerInfo.info(f'get {data}. send {result}')
    return result


def get_lower(data):
    result = data.lower()
    loggerInfo.info(f'get {data}. send {result}')
    return result