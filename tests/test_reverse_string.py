from src.reverse_string import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_unicode_string():
    assert reverse_string("こんにちは") == "はちにんこ"