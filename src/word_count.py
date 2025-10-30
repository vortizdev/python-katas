import re
from collections import Counter

def word_count(text: str) -> dict:
    """ 
    Count the occurrences of each word in the given string (case-insensitive).
    Ignores punctuation and treats words separated by whitespace.
    """
    #Normalize case
    text = text.lower()
    
    #Remove punctuation using regex, (keep letters and numbers, replace others with space)
    words = re.findall(r'[a-z0-9]+', text)
    
    #Count occurrences using Counter
    counts = Counter(words)
    
    return dict(counts)