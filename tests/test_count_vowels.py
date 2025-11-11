from src.count_vowels import count_vowels, count_vowels_dict

def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_empty_string():
    assert count_vowels("") == 0
    
def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0
    
def test_count_vowels_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10 

def test_count_vowels_mixed_case():
    assert count_vowels("HeLLo WoRLd") == 3

def test_invalid_input_type():
    try:
        count_vowels(12345)
        count_vowels_dict(12345)
    except TypeError as e:
        assert str(e) == "Input must be a string."
        
def test_count_vowels_dict():
    assert count_vowels_dict("helloo") == {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}
    
def test_count_vowels_dict_all_vowels():
    assert count_vowels_dict("aeiouAEIOU") == {"a": 2, "e": 2, "i": 2, "o": 2, "u": 2}

def test_count_vowels_dict_no_vowels():
    assert count_vowels_dict("rythm") == {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    