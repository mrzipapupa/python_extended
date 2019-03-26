import json
from routes import get_server_routes
import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError
from protocol import make_response, make_400, make_404

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
            response = controller(request)
        else:
            response = make_400(request)

    else:
        loggerError.error(f'Action not found: {client_action}')
        response = make_404(request)

    if request.get('code') == 400:
        loggerError.error(f'Bad request: {client_action} request: {request}')

    return response


def send_response(response, client):
    response_string = json.dumps(response)
    loggerInfo.debug('message to client was sent')
    client.send(response_string.encode())