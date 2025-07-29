from twttr import shorten
import pytest


def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("hello") == "hll"
    assert shorten("ROKON") == "RKN"


def test_numbers():
    assert shorten("123") == "123"
    assert shorten("1212414") == "1212414"


def test_punctuation():
    assert shorten(",") == ","
    assert shorten("!") == "!"
    assert shorten("'") == "'"
    assert shorten(".") == "."
