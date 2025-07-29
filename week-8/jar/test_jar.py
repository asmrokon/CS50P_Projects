from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0 
    


def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4