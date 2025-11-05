from src.find_missing_number import find_missing_number

def test_missing_number_in_middle():
    assert find_missing_number([1, 2, 4, 5]) == 3

def test_missing_number_at_start():
    assert find_missing_number([2, 3, 4, 5]) == 1
    
def test_no_missing_number():
    assert find_missing_number([1, 2, 3, 4, 5]) is None

def test_empty_list():
    assert find_missing_number([]) is None

def test_single_element_list():
    assert find_missing_number([2]) == 1
    
def test_invalid_input_type():
    try:
        find_missing_number("not a list")
    except TypeError as e:
        assert str(e) == "Input must be a list of integers."