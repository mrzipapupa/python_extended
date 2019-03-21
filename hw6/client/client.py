import hashlib
import sys
from data_processor import (
    set_presence_message, set_message, receive_response
)
sys.path.insert(0, '..\\')
from log.client_log_config import loggerInfo, loggerError

def start_client():
    loggerInfo.debug('client was started')
    sock = set_presence_message()

    try:
        action = input('Enter action: ')
        data = input('Enter data: ')

        hash_obj = hashlib.sha1()
        hash_obj.update(b'secret_key')

        message = set_message(action, data, hash_obj.hexdigest())

        if message:
            try:
                sock.send(message)
                serverResponse = receive_response(sock)
                loggerInfo.info(f'Response from server: {serverResponse.get("data")} code: {serverResponse.get("code")}')
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

