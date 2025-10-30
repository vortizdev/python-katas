import re

def is_palindrome(text: str) -> bool:
    """
    Return True if the given string is a palindrome, ignoring case, spaces, and punctuation.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]