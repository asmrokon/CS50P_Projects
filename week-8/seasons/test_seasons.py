import pytest
from seasons import process
import datetime


def test_process():
    assert process("2007-7-20") == datetime.datetime(2007, 7, 20, 0, 0)
    assert process("2009-8-25") == datetime.datetime(2009, 8, 25, 0, 0)
