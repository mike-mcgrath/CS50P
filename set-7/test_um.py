# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Um test.

from um import count

def test_one() :
    assert count('Um...') == 1
	
def test_two() :
    assert count( 'Um, thanks for the album') == 1
	
def test_three() :
    assert count('um, er, um...') == 2
	
def test_four() :
    assert count('um#') == 0