def check_bytes_type(line):
    try:
        result = bytes(line, encoding='ascii')
        # result = line.encode(encoding='ascii')
        print(f'Succes. Result byte_str: {result}')
    except:
        print(f'Cannot encode to bytes {line}')


if __name__ == '__main__':
    check_bytes_type('attribute')
    check_bytes_type('класс')
    check_bytes_type('функция')
    check_bytes_type('type')