import pytest
from working import convert # type: ignore


def test_convert_am():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"


def test_convert_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"


def test_convert_12():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_convert_60():
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 4:60 PM")


def test_convert_misplacement():
    with pytest.raises(ValueError):
        assert convert("9AM to 5PM")
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        assert convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        assert convert("10:7 AM - 5:1 PM")


def test_convert_morenumer():
    with pytest.raises(ValueError):
        assert convert("09 AM to 5:001 PM")
