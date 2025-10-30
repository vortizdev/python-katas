def reverse_string(text: str) -> str:
    """
    Reverses the given string, correctly handling Unicode characters and empty strings.
    example: reverse_string("hello") returns "olleh"
    """
    return "".join(reversed(text))