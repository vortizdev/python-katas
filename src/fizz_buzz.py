from typing import List

def fizz_buzz(num: int) -> List[str]:
    """ 
    Return FizzBuzz list from 1..n (inclusive).
    - "fizz" for multiples of 3
    - "buzz" for multiples of 5
    - "fizzbuzz" for multiples of 15
    - otherwise the number itself as a string
    Returns [] if n <= 0.
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    
    if num <= 0:
        return []
    
    out: List[str] = []
    for i in range(1, num + 1):
        s = ""
        if i % 3 == 0:
            s += "fizz"
        if i % 5 == 0:
            s += "buzz"
        out.append(s or str(i))
            
    return out