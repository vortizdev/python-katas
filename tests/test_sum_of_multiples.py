from src.sum_of_multiples import sum_of_multiples
import pytest

def test_sum_of_multiples_basic():
    assert sum_of_multiples(10, [3, 5]) == 23  # 3, 5, 6, 9

def test_sum_of_multiples_no_multiples():
    assert sum_of_multiples(2, []) == 0  # No multiples of 3 or 5 below 2

def test_sum_of_multiples_large():
    assert sum_of_multiples(1000) == 233168

def test_sum_of_multiples_zero():
    assert sum_of_multiples(0) == 0

def test_sum_of_multiples_negative():
    assert sum_of_multiples(-10) == 0

def test_sum_of_multiples_invalid_type():
    with pytest.raises(TypeError):
        sum_of_multiples("100")

def test_sum_of_multiples_custom_multiples():
    assert sum_of_multiples(20, [4, 6]) == 64  # 4, 6, 8, 12, 16, 18

def test_sum_of_multiples_single_multiple():
    assert sum_of_multiples(15, [7]) == 21  # 7, 14

def test_sum_of_multiples_no_custom_multiples():
    assert sum_of_multiples(10) == 23  # Default multiples 3 and 5

def test_sum_of_multiples_non_integer_multiple():
    with pytest.raises(TypeError):
        sum_of_multiples(10, ["3", 5])

def test_sum_of_multiples_zero_multiple():
    assert sum_of_multiples(10, [0, 5]) == 5  # Only 5 is valid multiple
