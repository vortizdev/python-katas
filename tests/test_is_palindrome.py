from src.is_palindrome import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") is True

def test_non_palindrome():
    assert is_palindrome("hello") is False

def test_ignore_case_palindrome():
    assert is_palindrome("Madam") is True

def test_ignore_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_empty_string():
    assert is_palindrome("") is True