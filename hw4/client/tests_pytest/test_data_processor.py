import pytest
import json
import sys
sys.path.insert(0, '..\\')
from data_processor import set_message, response_parser


def test_set_message():
    assert set_message('upper', 'test') == json.dumps({'action': 'upper', 'data': 'test'}).encode()

def test_repsonse_parser():
    assert response_parser(b'TEST') == 'TEST'
