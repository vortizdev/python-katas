from typing import List, Optional

def find_missing_number(nums: List[int]) -> int:
    """ Find the missing number in a list of consecutive integers starting from 1."""
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    
    if not nums:
        return None
    
    # Check if no number is missing
    full_set = set(range(1, len(nums) + 2))
    
    if set(nums) == full_set - {max(full_set)}:
        return None
    
    n = len(nums) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    missing_number = expected_sum - actual_sum
    return missing_number if 1 <= missing_number <= n else None