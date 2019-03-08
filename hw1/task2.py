def byte_line_info(byte_line):
    print('------------------------------------------------')
    print(f'type of line: {type(byte_line)}')
    print(f'line: {byte_line}')
    print(f'len of line: {len(byte_line)}')


if __name__ == '__main__':
    byte_line_info(bytes('class', encoding='ascii'))
    byte_line_info(bytes('function', encoding='ascii'))
    byte_line_info(bytes('method', encoding='ascii'))