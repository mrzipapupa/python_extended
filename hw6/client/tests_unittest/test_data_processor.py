import unittest
import json
import sys
sys.path.insert(0, '..\\')
from data_processor import set_message, response_parser


class TestProcessorMethods(unittest.TestCase):
    def test_set_message(self):
        self.assertEqual(set_message('upper', 'test'), json.dumps({'action': 'upper', 'data': 'test'}).encode())

    def test_repsonse_parser(self):
        self.assertEqual(response_parser(b'TEST'), 'TEST')


if __name__ == '__main__':
    unittest.main()
