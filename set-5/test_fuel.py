from fuel import convert, gauge

def test_one() :
    assert convert('3/4') == 75
    assert convert('1/2') == 50
    
def test_two() :
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    
def test_three() :
    assert gauge(50) == '50%'


    