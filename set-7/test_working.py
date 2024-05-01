# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Working 9 to 5 test.

from working import convert

def test_one() :

    assert convert('09:00 AM to 05:30 PM') == '09:00 to 17:30'

def test_two():
 
    assert convert('9 AM to 11 PM') == '09:00 to 23:00'
    
def test_three():

    assert convert('12 PM to 6 AM') == '00:00 to 06:00'
    
def test_four() :

    assert convert('10 pm to 3 am') == '22:00 to 03:00'