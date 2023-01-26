from MULT.fois import mult

def test_mult():
    # arrange
    a = 5
    b = 2
    # act
    res = mult(a, b)
    # assert
    assert res == 10
    
def test_mult_5_2_is_less_than_11():
    assert mult(5, 2) < 11

def test_mult_5_2_is_more_than_6():
    assert mult(5, 2) > 6

