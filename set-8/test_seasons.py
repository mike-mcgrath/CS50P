# CS50’s Introduction to Programming with Python.
# Problem Set 8 - Seasons of Love test.

from seasons import parse

def test_one() :
    assert parse( '2023-04-28' )
    
def test_two() :
    assert parse( '2024-04-28' )