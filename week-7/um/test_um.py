import pytest
from um import count

def test_count_normal_text():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("Hello") == 0
def test_count_capital():
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now") == 2
def test_count():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
