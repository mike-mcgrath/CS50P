from bank import value

def test_one() :

    assert value('hello') == 0

def test_two() :

    assert value('hey') == 20
	
def test_three() :

    assert value('wassup') == 100