# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Response Validation test.

from response import is_valid

def test_one():
    assert is_valid('malan@harvard.edu') == 'Valid'
    
def test_two():
    assert is_valid('mike@example.com') == 'Valid'
    
def test_three():
    assert is_valid('malan@@@harvard.edu') == 'Valid'
    
def test_four():
    assert is_valid('mike@example..com') == 'Valid'