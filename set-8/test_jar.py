# CS50’s Introduction to Programming with Python.
# Problem Set 8 - Cookie Jar test.

from jar import Jar

def test_init():
    jar = Jar()
    assert jar.space == 12
    assert jar.cookies == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""


def test_deposit():
    jar = Jar()    
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    
def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(6)
    assert jar.cookies == 4
