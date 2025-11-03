from typing import List

def sum_of_multiples(limit: int, multiples: List[int] | None = None) -> int:
    if multiples is None:
        multiples = [3, 5]
    
    if not isinstance(limit, int):
        raise TypeError("Input must be an integer")
    
    for num in multiples:
        if not isinstance(num, int):
            raise TypeError("Multiples must be integers")
    
    if limit <= 0:
        return 0
    
    total = 0
    for num in range(limit):
        for multiple in multiples:
            if multiple <= 0:
                continue
            if num % multiple == 0:
                total += num
                break
    
    return total