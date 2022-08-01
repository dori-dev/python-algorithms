"""
Logarithm Time -> O(log n)
"""

from typing import Any


numbers = [0, 4, 7, 10, 14, 23, 45, 47, 53]


# Bad Way -> Simple Search
# TODO Good Way -> Binary Search


def get_element_index(list_: list, element: Any) -> Any:
    index = 0
    for item in list_:
        if item == element:
            return index
        index += 1
    return None


print(get_element_index(numbers, 23))
