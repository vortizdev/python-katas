def even_or_odd(number):
    """Check if a number is even, handles zero and invalid input."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return "Even" if number % 2 == 0 else "Odd"