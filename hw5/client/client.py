from data_processor import (
    set_presence_message, set_message, receive_response
)
import sys
sys.path.insert(0, '..\\')
from log.client_log_config import loggerInfo, loggerError

def start_client():
    loggerInfo.debug('client was started')
    sock = set_presence_message()

    try:
        action = input('Enter action: ')
        data = input('Enter data: ')
        message = set_message(action, data)

        if message:
            try:
                sock.send(message)
                serverResponse = receive_response(sock)
                loggerInfo.info(f'Response from server: {serverResponse}')
            except Exception as ex:
                loggerError.error(f'cannot send message. More: {str(ex)}')
        else:
            loggerInfo.debug('client was stopped')
            sock.close()
    except KeyboardInterrupt:
        sock.close()
        loggerError.error('catch keyboard interrupt from client')


if __name__ == '__main__':
    start_client()

