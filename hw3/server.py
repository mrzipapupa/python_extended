import socket
import argparse
import json


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=7777, type=int, help='server port (default 7777)')
    parser.add_argument('-a', '--addr', default='', type=str, help='server ipv4 addr')
    args = parser.parse_args()
    return args.addr, args.port


def start_server(sock):
    while True:
        client, address = sock.accept()
        print(f'Client accepted {address}')

        messageFromClient = receive_message(client)
        messageToClient = set_response(messageFromClient)
        send_response(messageToClient, client)

        client.close()


def set_connection():
    ADDR, PORT = arg_parser()
    sock = socket.socket()
    sock.bind((ADDR, PORT))
    sock.listen(5)
    return sock


def receive_message(client):
    data = client.recv(1024)

    request = json.loads(
        data.decode('utf-8')
    )
    return request


def set_response(request):
    if request.get('action') == 'echo':
        responseString = '1'

    elif request.get('action') == 'whoami':
        responseString = '2'

    elif request.get('action') == 'hello':
        responseString = '3'

    elif request.get('action') == 'bye':
        responseString = '4'

    else:
        responseString = '-1'

    return responseString


def send_response(response, client):
    client.send(response.encode())


if __name__ == '__main__':
    sock = set_connection()
    start_server(sock)

