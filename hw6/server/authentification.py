import time
from functools import wraps
import inspect
from protocol import make_response
from log.server_log_config import loggerInfo


def login_required(func):
    @wraps(func) # say to func that it is decorator
    def wrap(request, *args, **kwargs):
        if request.get('user'):
            return func(request)
        return make_response(request, 403, 'Access denied')
    return wrap


def log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        methodArgs = ''
        methodName = func.__name__
        methodFromName = inspect.stack()[1].function
        nowTime = time.ctime()
        args = inspect.getfullargspec(func)[0]
        if len(args) == 1:
            methodArgs = args[0]
        elif len(methodArgs) > 1:
            methodArgs = ','.join(args)
        loggerInfo.info(f'<{nowTime}> Function {methodName}({methodArgs}) was ran from function {methodFromName}')
        return
    return wrap


class LoginRequired:
    def __call__(self, func):
        @wraps(func)  # say to func that it is decorator
        def wrap(request, *args, **kwargs):
            print(request)
            print(func)
            if request.get('user'):
                return func(request)
            return make_response(request, 403, 'Access denied')

        return wrap