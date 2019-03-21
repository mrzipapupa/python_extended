import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=7777, type=int, help='server port (default 7777)')
    parser.add_argument('-a', '--addr', default='', type=str, help='server ipv4 addr')
    args = parser.parse_args()
    return args.addr, args.port