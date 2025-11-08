
def count_vowels(string: str) -> int:
    """ Count the total number of vowels in a list of strings. """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    total_vowels = 0
    vowels = set("aeiouAEIOU")
    
    total_vowels += sum(1 for char in string if char in vowels)
    
    return total_vowels