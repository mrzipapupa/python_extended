from data_processor import (
    set_presence_message, set_message, receive_response
)

def start_client():
    sock = set_presence_message()

    action = input('Enter action: ')
    data = input('Enter data: ')
    message = set_message(action, data)

    if message:
        sock.send(message)
        serverResponse = receive_response(sock)
        print(f'Response from server: {serverResponse}')
    else:
        sock.close()


if __name__ == '__main__':
    start_client()

