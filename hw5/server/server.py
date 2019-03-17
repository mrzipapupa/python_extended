from data_processor import (
    receive_message, set_response, send_response
)
from connector import set_connection
import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError


def start_server():
    sock = set_connection()
    loggerInfo.debug('server was started')
    try:
        while True:
            client, address = sock.accept()
            loggerInfo.info(f'Client accepted {address}')

            while True:
                data = client.recv(1024)
                if not data:
                    break
                messageFromClient = receive_message(data)
                messageToClient = set_response(messageFromClient)
                send_response(messageToClient, client)

            client.close()
    except KeyboardInterrupt:
        loggerError.error('Catch keyboard interrupt from server')
        sock.close()


if __name__ == '__main__':
    start_server()

