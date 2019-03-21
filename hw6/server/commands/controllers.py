import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError
from protocol import make_response, make_400
from authentification import login_required, log


@log
@login_required
def get_echo(request):
    data = request.get('data')
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        '1'
    )


@log
@login_required
def get_whoami(request):
    data = request.get('data')
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        '2'
    )


@log
@login_required
def get_hello(request):
    data = request.get('data')
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        '3'
    )


@log
@login_required
def get_bye(request):
    data = request.get('data')
    if not data:
        data = 'empty'
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        '4'
    )