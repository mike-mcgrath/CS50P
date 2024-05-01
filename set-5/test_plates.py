from plates import is_valid

def test_one() :
    assert is_valid('AAA222') == True
	
def test_two() :
    assert is_valid('ABC123') == True
	
def test_three() :
    assert not is_valid('AA022A') == True
	