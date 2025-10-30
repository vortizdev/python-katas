from src.roman_to_int import roman_to_int
import pytest

def test_single_symbols():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000
    
def test_additive_cases():
    assert roman_to_int("III") == 3
    assert roman_to_int("VIII") == 8
    assert roman_to_int("XXVII") == 27
    assert roman_to_int("LX") == 60
    assert roman_to_int("CL") == 150
    assert roman_to_int("DCC") == 700
    assert roman_to_int("MMXX") == 2020
    
def test_subtractive_cases():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XL") == 40
    assert roman_to_int("XC") == 90
    assert roman_to_int("CD") == 400
    assert roman_to_int("CM") == 900
    
def test_mixed_numbers():
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMXXI") == 2021
    assert roman_to_int("XLII") == 42
    assert roman_to_int("DCCCXC") == 890
    
def test_lowercase_is_allowed():
    assert roman_to_int("mcmxciv") == 1994
    
def test_empty_string_is_zero():
    assert roman_to_int("") == 0
    
def test_invalid_characters():
    with pytest.raises(ValueError):
        roman_to_int("ABCD")
    with pytest.raises(ValueError):
        roman_to_int("123")