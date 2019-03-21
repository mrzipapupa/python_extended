from .controllers import (
    get_echo, get_hello, get_whoami, get_bye
)


routes = [
    {'action': 'echo', 'controller': get_echo},
    {'action': 'hello', 'controller': get_hello},
    {'action': 'whoami', 'controller': get_whoami},
    {'action': 'bye', 'controller': get_bye},
]