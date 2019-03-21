from connector import set_connection
import socket
import json


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


def set_message(action, data):
    requestString = json.dumps(
        {
            'action': action,
            'data': data
        }
    )
    return requestString.encode()



def receive_response(sock):
    data = sock.recv(1024)
    if data:
        response_parser(data)
    sock.close()


def response_parser(data):
    serverResponse = data.decode('utf-8')
    return serverResponse
