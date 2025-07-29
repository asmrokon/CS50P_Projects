from plates import is_valid


def test_first_two_letter_alpha():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False


def test_numbers_in_middle():
    assert is_valid("CS50") == True
    assert is_valid("CS50AD") == False


def test_punctuations():
    assert is_valid("CS50") == True
    assert is_valid("CS,50") == False


def test_maximum_letters():
    assert is_valid("CS50") == True
    assert is_valid("CS5046456546") == False


def test_minimum_letters():
    assert is_valid("CS50") == True
    assert is_valid("C") == False

from plates import is_valid


def test_first_two_letter_alpha():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False


def test_numbers_in_middle():
    assert is_valid("CS50") == True
    assert is_valid("CS50AD") == False


def test_punctuations():
    assert is_valid("CS50") == True
    assert is_valid("CS,50") == False


def test_maximum_letters():
    assert is_valid("CS50") == True
    assert is_valid("CS5046456546") == False


def test_zero_as_first_number():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
