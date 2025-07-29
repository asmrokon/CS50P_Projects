from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("5/6") == 83
    assert convert("1/10") == 10

def test_gauge():
    assert gauge(83) == "83%"
    assert gauge(10) == "10%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_convert_str_valueerror():
    with pytest.raises(ValueError):
        convert("cat")

def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_convert_negative_int_valueerror():
    with pytest.raises(ValueError):
        convert("-5/6")
