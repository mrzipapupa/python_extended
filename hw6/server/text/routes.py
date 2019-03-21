from .controllers import (
    get_lower, get_upper
)


routes = [
    {'action': 'upper', 'controller': get_upper},
    {'action': 'lower', 'controller': get_lower},
]