import pytest
from src.fizz_buzz import fizz_buzz

def test_fizz():
    assert fizz_buzz(3)[2] == "fizz"

def test_buzz():
    assert fizz_buzz(5)[4] == "buzz"

def test_fizzbuzz():
    assert fizz_buzz(15)[14] == "fizzbuzz"
    
def test_numbers_are_strings():
    res = fizz_buzz(2)
    assert res == ["1", "2"]
    
def test_len_matches_input():
    n = 20
    assert len(fizz_buzz(n)) == n
    
def test_zero_returns_empty():
    assert fizz_buzz(0) == []

def test_negative_returns_empty():
    assert fizz_buzz(-5) == []
    
def test_invalid_type_raises():
    with pytest.raises(TypeError):
        fizz_buzz("15")

            
                
            
