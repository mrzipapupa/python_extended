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
            action = input('Enter action: ')
            data = input('Enter data: ')

            hash_obj = hashlib.sha1()
            hash_obj.update(b'secret_key')

            message = set_message(action, data, hash_obj.hexdigest())
            if message:
                sock.send(message)

    except KeyboardInterrupt:
        sock.close()
        loggerError.error('catch keyboard interrupt from client')


if __name__ == '__main__':
    start_client()

