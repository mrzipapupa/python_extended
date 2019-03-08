def line_processor(line):
    print('------------------------------------------------')
    print(f'Исходная строка: {line}')
    bytes_line = line.encode('utf-8')
    print(f'Преобразованная строка: {bytes_line}')
    str_line = bytes_line.decode('utf-8')
    print(f'Обратное преобразование: {str_line}')


if __name__ == '__main__':
    line_processor('разработка')
    line_processor('сокет')
    line_processor('декоратор')