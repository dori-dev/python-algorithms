"""
binary_search([1, 2, 5, 8, 11, 14, 18, 23, 32, 48], 11) => 4
complexity: O(log n)
"""

from typing import Any


def binary_search(array: list, target: Any) -> int:
    low, high = 0, len(array) - 1
    while low <= high:
        middle = (high + low) // 2
        value = array[middle]
        if value == target:
            return middle
        elif value < target:
            low = middle + 1
        elif target < value:
            high = middle - 1
    return None


if __name__ == "__main__":
    print(binary_search([1, 2, 5, 8, 11, 14, 18, 23, 32, 48], 11) == 4)
