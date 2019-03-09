import json
import socket
import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=7777, type=int, help='server port (default 7777)')
    parser.add_argument('-a', '--addr', default='localhost', type=str, help='server ipv4 addr')
    args = parser.parse_args()
    return args.addr, args.port


def set_connection():
    ADDR, PORT = arg_parser()
    sock = socket.socket()
    sock.connect((ADDR, PORT))
    return sock


def set_presence_message():
    try:
        sock = set_connection()
        print(f'Connection complete')
        print(f'Server: {sock.getpeername()}\n'
              f'Client: {sock.getsockname()}')
        return sock
    except socket.error as msg:
        print(f'Error with socket: {msg}')
        exit(-1)


def send_message(sock):
    action = input('Enter action: ')

    requestString = json.dumps(
        {
            'action': action,
        }
    )

    sock.send(requestString.encode())


def receive_response(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response_parser(data)
    sock.close()


def response_parser(data):
    serverResponse = data.decode('utf-8')
    print(f'Response from server: {serverResponse}')



if __name__ == '__main__':
    sock = set_presence_message()

    send_message(sock)
    receive_response(sock)

