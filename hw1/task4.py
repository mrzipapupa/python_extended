def encode_decode_line(line):
    print('---------------------------------------------')
    result_bytes = line.encode()
    print(f'After encode: {result_bytes}')
    result_str = result_bytes.decode()
    print(f'After decode: {result_str}')


if __name__ == '__main__':
    encode_decode_line('разработка')
    encode_decode_line('protocol')
    encode_decode_line('standard')