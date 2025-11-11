
def count_vowels(string: str) -> int:
    """ Count the total number of vowels in a string. """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    total_vowels = 0
    vowels = set("aeiouAEIOU")
    
    total_vowels += sum(1 for char in string if char in vowels)
    
    return total_vowels
    

def count_vowels_dict(_string: str) -> dict:
    """ 
    Count the total number of vowels in a string and return a dict showing how many 
    times each vowel appears.
    """
    if not isinstance(_string, str):
        raise TypeError("Input must be a string.")
    
    string = _string.lower()
    vowels = set("aeiou")
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0,}
    
    for char in string:
        if char in vowels:
            vowel_count[f"{char}"] += 1
                
    return vowel_count