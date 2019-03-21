import unittest
import sys
sys.path.insert(0, '..\\')
from args_parser import arg_parser


class TestServerMethods(unittest.TestCase):
    def test_arg_parse(self):
        self.assertEqual(arg_parser(), ('localhost', 7777))


if __name__ == '__main__':
    unittest.main()