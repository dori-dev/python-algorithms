"""
Logarithm Time -> O(log n)
"""

from typing import Any


numbers = [0, 4, 7, 10, 14, 23, 45, 47, 53]


def get_element_index(list_: list, target: Any) -> int:
    index = 0
    for item in list_:
        if item == target:
            return index
        index += 1
    return None


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
    # Bad Way -> Simple Search
    print(get_element_index(numbers, 23))
    # Good Way -> Binary Search
    print(get_element_index(numbers, 23))
