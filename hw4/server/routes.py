import os
import sys
from importlib import __import__
from functools import reduce

'''
def get_server_routes(path):
    modules = []
    routes = []

    # os.chdir(path)
    for itm in os.listdir(path):
        if os.path.isdir(itm) and itm != '__pycache__' and itm != '.pytest_cache':
            try:
                module = __import__(f'{itm}.routes')
                modules.append(module)
            except:
                continue

    for module in modules:
        routes += getattr(module, 'routes', [])

    return routes
'''

def get_server_routes(path):
    localRoutes = ['commands', 'text']
    modules = []
    routes = []

    for itm in localRoutes:
        sys.path.insert(0, f'{path}\\{itm}\\routes')
        module = __import__(f'{itm}.routes')
        modules.append(module)

    for module in modules:
        routes += getattr(module, 'routes', [])

    return routes




'''
def get_server_routes():
    return reduce(
        lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(
            lambda modules, dir: modules + [__import__(f'{dir}.routes')],
            filter(
                lambda itm: os.path.isdir(itm) and itm != '__pycache__',
                os.listdir('.')
            ),
            []
        ),
        []
    )
'''