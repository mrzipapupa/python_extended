import random
import yaml
from pprint import pprint


def generate_list():
    lists = [
        ['apple', 'pineapple', 'cherry', 'watermelon', 'carrot', 'cucumber', 'tomato', 'peach'],
        ['T-shirt', 'snickers', 'shorts', 'pants', 'sweater', 'jacket', 'vest', 'cap'],
    ]
    return random.choice(lists)


def generate_int():
    return random.randint(1,50)


def generate_dict():
    random_dict = {
        generate_key(): ['one', 'two', 'three'],
        generate_key(): 'test_string',
        generate_key(): 123,
    }
    return random_dict


#где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €)
def generate_key():
    listKeys = [198,  664, 1902, 2472, 3197, 3735]
    return random.choice(listKeys)


def generate_data():
    dictForFile = {
        generate_int(): generate_list(),
        generate_int(): generate_int(),
        generate_int(): generate_dict(),
    }
    return dictForFile


def write_order_to_yaml(fileName, dataForFile):
    with open(fileName, 'w', encoding='utf-8') as fileYaml:
        yaml.dump(dataForFile, fileYaml, default_flow_style=False, allow_unicode=True)


def read_data_from_yaml(fileName):
    with open(fileName, 'r', encoding='utf-8') as fileYaml:
        return yaml.load(fileYaml)


def check_data(dictTo, dictFrom):
    if dictTo == dictFrom:
        print('dicts are same')
    else:
        print('dicts are different')


if __name__ == '__main__':
    dictForFile = generate_data()
    pprint(dictForFile)
    write_order_to_yaml('report.yaml', dictForFile)
    dictFromFile = read_data_from_yaml('report.yaml')
    check_data(dictForFile, dictFromFile)