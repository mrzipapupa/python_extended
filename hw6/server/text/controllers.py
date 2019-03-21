import sys
sys.path.insert(0, '..\\')
from log.server_log_config import loggerInfo, loggerError
from protocol import make_response, make_400
from authentification import login_required, log

@log
@login_required
def get_upper(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        data.upper()
    )

@log
@login_required
def get_lower(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    loggerInfo.info(f'get {data}')
    return make_response(
        request,
        200,
        data.lower()
    )