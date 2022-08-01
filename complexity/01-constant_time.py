"""
Constant Time -> O(1)
"""

from typing import List


# The length of the numbers is not important for this algorithm
numbers = [3, 4, 5, 98, 123, 42, 6432]


def is_first_number_even(numbers: List[int]) -> int:
    first_number = numbers[0]
    if first_number % 2 == 0:
        return True
    return False


print(is_first_number_even(numbers))
