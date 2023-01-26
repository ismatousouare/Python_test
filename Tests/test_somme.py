from SOMME.add import addition
import pytest

def test_somme():
    # arrange
    a = 5
    b = 2
    # act
    res = addition(a, b)
    # assert
    assert res == 7
    
def test_somme_5_2_is_less_than_8():
    assert addition(4, 3) < 8

def test_somme_5_2_is_more_than_6():
    assert addition(6, 1) > 6
    
@pytest.mark.xfail  
def test_somme_expect_to_fail():
    assert addition(2,2) == 5
    