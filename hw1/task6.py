""" .txt файлы по умолчанию имеют кодировку ANSI """


if __name__ == '__main__':
    with open('test_file.txt', 'r', encoding='unicode-escape', errors='ignore') as f: # либо utf-8
        print(f.read())
