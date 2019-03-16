def get_echo(data):
    if not data:
        data = 'empty'
    result = 1
    print(f'get {data} \n'
          f'send {result}')
    return str(result)


def get_whoami(data):
    result = 2
    if not data:
        data = 'empty'
    print(f'get {data} \n'
          f'send {result}')
    return str(result)


def get_hello(data):
    result = 3
    if not data:
        data = 'empty'
    print(f'get {data} \n'
          f'send {result}')
    return str(result)


def get_bye(data):
    result = 4
    if not data:
        data = 'empty'
    print(f'get {data} \n'
          f'send {result}')
    return str(result)