from src.word_count import word_count

def test_basic_count():
    text = "hello world hello"
    expected = {"hello": 2, "world": 1}
    assert word_count(text) == expected

def test_ignore_case():
    text = "Hello hello HELLO"
    expected = {"hello": 3}
    assert word_count(text) == expected
    
def test_punctuation():
    text = "hello, world! hello."
    expected = {"hello": 2, "world": 1}
    assert word_count(text) == expected

def test_empty_string():
    text = ""
    expected = {}
    assert word_count(text) == expected

def test_mixed_spaces():
    text = "hello   world \n hello\tworld"
    expected = {"hello": 2, "world": 2}
    assert word_count(text) == expected