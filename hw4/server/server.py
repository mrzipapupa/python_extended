from data_processor import (
    receive_message, set_response, send_response
)
from connector import set_connection


def start_server():
    sock = set_connection()
    while True:
        client, address = sock.accept()
        print(f'Client accepted {address}')

        while True:
            data = client.recv(1024)
            if not data:
                break
            messageFromClient = receive_message(data)
            messageToClient = set_response(messageFromClient)
            send_response(messageToClient, client)

        client.close()


if __name__ == '__main__':
    start_server()

