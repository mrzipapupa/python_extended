import pytest
import sys
sys.path.insert(0, '..\\')
from args_parser import arg_parser


def test_arg_parse():
    assert arg_parser() == ('', 7777)
