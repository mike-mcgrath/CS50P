# CS50’s Introduction to Programming with Python.
# Problem Set 7 - NUMB3RS test.

from numb3rs import validate

def test_one():
    assert validate( '127.0.0.1' )  == True
    
def test_two():
    assert validate( '255.255.255.255' ) == True

# Too short.
def test_three():  
    assert not validate( '192.168.0' ) == True

# Out of range.    
def test_four():
    assert not validate( '192.256.0.0' )  == True
    
# Too long.
def test_five() :
    assert not validate( '255.255.255.255.0' ) == True 
 
# Not numeric. 
def test_six():
    assert not validate( 'CS50' )  == True              
