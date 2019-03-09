import json
import datetime
import random

def write_order_to_json(fileName):
    fileCollection = {}
    orders = []
    for i in range(5):
        order = {
            'item': generator_items(),
            'quantity': generator_quantity(),
            'price': generator_price(),
            'buyer': generator_buyer(),
            'date': generator_date()
        }
        orders.append(order)
    fileCollection['orders'] = orders
    with open(fileName, 'w') as fileJson:
        json.dump(fileCollection, fileJson, indent=4)


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    result = start + datetime.timedelta(seconds=random_second)
    return result.strftime("%d-%b-%Y (%H:%M)")


def generator_items():
    items = ['apple', 'pineapple', 'cherry', 'watermelon', 'carrot', 'cucumber', 'tomato', 'peach']
    return random.choice(items)


def generator_quantity():
    return random.randint(1,20)


def generator_price():
    return random.uniform(1,4)


def generator_buyer():
    buyers = ['Nick', 'Mary', 'Moe', 'Mia', 'Mark', 'Billy', 'Sam', 'John']
    return random.choice(buyers)


def generator_date():
    d1 = datetime.datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.datetime.strptime('3/8/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    return random_date(d1, d2)

if __name__ == '__main__':
    write_order_to_json('report.json')