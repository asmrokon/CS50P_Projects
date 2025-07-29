import pytest
from numb3rs import validate

def test_validate_ip4():
    assert validate("127.0.0.1")
    assert not validate("127.00.0.1")
    assert not validate("8.8.8")
    assert not validate("1.1.1.11111")
    
def test_validate_ip6():
    assert not validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

def test_validate_text():
    assert not validate("cat")
    assert not validate("dune")

