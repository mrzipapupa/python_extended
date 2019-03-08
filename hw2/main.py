from csv_parser import write_to_csv
from json_parser import write_order_to_json
from yaml_parser import write_order_to_yaml


if __name__ == '__main__':
    write_to_csv('report.csv')
    write_order_to_json('report.json')
    write_order_to_yaml('report.yaml')