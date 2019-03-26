import socket
from select import select
import sys
from data_processor import (
    receive_message, set_response, send_response
)
from connector import set_connection
sys.path.insert(0, '..\\')
from log.server_log_config import (
    loggerInfo, loggerError
)

connections = []
responses = []

def start_server():
    server_socket = set_connection()
    loggerInfo.debug('server was started')
    connections.append(server_socket)
    try:
        while True:
            readList, writeList, _ = select(connections, connections, [])

            for conn in connections:
                try:
                    if conn in readList and conn is server_socket:
                        client, address = server_socket.accept()
                        connections.append(client)
                        loggerInfo.info(f'Client accepted {address}')

                    elif conn in readList:
                        data = client.recv(1024)

                        messageFromClient = receive_message(data)
                        messageToClient = set_response(messageFromClient)

                        if messageToClient.get('code') == 200:
                            responses.append(messageToClient)
    

                    elif conn in writeList:
                        if responses:
                            for conn in writeList:
                                for response in responses:
                                    send_response(response, conn)
                            responses.clear()
                except socket.error as ex:
                    loggerError.error(str(ex))
                    connections.remove(conn)
                    continue


    except KeyboardInterrupt:
        loggerError.error('Catch keyboard interrupt from server')
        server_socket.close()


if __name__ == '__main__':
    start_server()

