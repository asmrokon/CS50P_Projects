from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hEllo") == 0


def test_h():
    assert value("hlw") == 20
    assert value("hola") == 20
    assert value("hey") == 20


def test_other_than_h_or_hello():
    assert value("yo") == 100
    assert value("whats up") == 100
