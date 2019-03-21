import unittest
import json
import sys
sys.path.insert(0, '..\\')
from data_processor import receive_message, set_response

class TestProcessorMethods(unittest.TestCase):
    def test_receive_message(self):
        clientMessage = json.dumps({'action': 'upper', 'data': 'test'}).encode()
        resultMessage = {'action': 'upper', 'data': 'test'}
        self.assertEqual(receive_message(clientMessage), resultMessage)

    def test_set_response_upper(self):
        request = {'action': 'upper', 'data': 'test'}
        response_string = 'TEST'
        self.assertEqual(set_response(request, '..'), response_string)

    def test_set_response_lower(self):
        request = {'action': 'lower', 'data': 'TEST'}
        response_string = 'test'
        self.assertEqual(set_response(request, '..'), response_string)

    def test_set_response_echo(self):
        request = {'action': 'echo', 'data': 'test'}
        response_string = '1'
        self.assertEqual(set_response(request, '..'), response_string)

    def test_set_response_empty(self):
        request = {}
        response_string = 'Action not supported'
        self.assertEqual(set_response(request, '..'), response_string)


if __name__ == '__main__':
    unittest.main()
