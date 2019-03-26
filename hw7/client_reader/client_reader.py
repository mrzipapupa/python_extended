import hashlib
import sys
from data_processor import (
    set_presence_message, set_message, receive_response
)
sys.path.insert(0, '..\\')
from log.client_log_config import loggerInfo, loggerError

def start_client():
    try:
        loggerInfo.debug('client was started')
        sock = set_presence_message()

        while True:
            serverResponse = receive_response(sock)
            if serverResponse:
                loggerInfo.info(
                    f'Response from server: ({serverResponse.get("data")}) code: ({serverResponse.get("code")})')
                # break


    except KeyboardInterrupt:
        sock.close()
        loggerError.error('catch keyboard interrupt from client')


if __name__ == '__main__':
    start_client()

