from typing import Dict

#Mapping of single roman symbols to their integer values
_VALUES: Dict[str, int] = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000 ,
}

def roman_to_int(s: str) -> int:
    """
    Convert Roman numeral string to an integer.
    
    Rules:
    - Add values when a symbol >= next symbol (e.g. VI 5 + 1 = 6)
    - Subtract values when a symbol < next symbol (e.g. IV = 1 - 5 = 4)
    - Empty string returns 0.
    - Lowercase input is accepted.
    - Invalid characters raise ValueError.
    """
    
    if not s:
        return 0;
    
    s = s.upper()
    
    # Validate characters
    for ch in s:
        if ch not in _VALUES:
            raise ValueError(f"Invalid Roman symbol: {ch}")
    
    total = 0
    i = 0
    n = len(s)
    
    while i < n:
        # Current symbol value
        curr = _VALUES[s[i]]
        
        # Look ahead to decide add vs subtract (subtraction notation)
        if i + 1 < n:
            nxt = _VALUES[s[i + 1]]
            if curr < nxt:
                # Subtractive pair (e.g. I before V or X)
                total += (nxt - curr)
                i += 2
                continue
        
        # Additive case or last symbol
        total += curr
        i += 1
        
    return total
