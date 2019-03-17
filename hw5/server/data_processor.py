import json
from routes import get_server_routes
import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError

def receive_message(data):
    request = json.loads(
        data.decode('utf-8')
    )
    loggerInfo.debug('receive message from client')
    return request


def set_response(request, path='.'):
    loggerInfo.debug('set response to client')
    client_action = request.get('action')
    if client_action:
        client_action = client_action.lower()
    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action,
            get_server_routes(path)
        )
    )
    route = resolved_routes[0] if resolved_routes else None
    if route:
        controller = route.get('controller')
        response_string = controller(request.get('data'))
    else:
        response_string = 'Action not supported'

    return response_string


def send_response(response, client):
    loggerInfo.debug('message to client was sent')
    client.send(response.encode())