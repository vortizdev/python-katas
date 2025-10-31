import pytest
from src.even_or_odd import even_or_odd

def test_even_number():
    assert even_or_odd(4) == "Even"
    
def test_odd_number():
    assert even_or_odd(7) == "Odd"

def test_zero():
    assert even_or_odd(0) == "Even"

def test_negative_even_number():
    assert even_or_odd(-2) == "Even"

def test_negative_odd_number():
    assert even_or_odd(-3) == "Odd"

def test_invalid_input():
    with pytest.raises(TypeError):
        even_or_odd("String")