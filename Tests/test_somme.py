from SOMME.add import addition

def test_somme():
    # arrange
    a = 5
    b = 2
    # act
    res = addition(a, b)
    # assert
    assert res == 7
    
def test_somme_5_2_is_less_than_8():
    assert addition(5, 2) < 8

def test_somme_5_2_is_more_than_6():
    assert addition(5, 2) > 6
