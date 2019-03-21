import pytest
import json
import sys
sys.path.insert(0, '..\\')
from data_processor import receive_message, set_response

def test_receive_message():
    clientMessage = json.dumps({'action': 'upper', 'data': 'test'}).encode()
    resultMessage = {'action': 'upper', 'data': 'test'}
    assert receive_message(clientMessage) == resultMessage

def test_set_response_upper():
    request = {'action': 'upper', 'data': 'test'}
    response_string = 'TEST'
    assert set_response(request, '..') == response_string

def test_set_response_lower():
    request = {'action': 'lower', 'data': 'TEST'}
    response_string = 'test'
    assert set_response(request, '..') == response_string

def test_set_response_echo():
    request = {'action': 'echo', 'data': 'test'}
    response_string = '1'
    assert set_response(request, '..') == response_string

def test_set_response_empty():
    request = {}
    response_string = 'Action not supported'
    assert set_response(request, '..') == response_string