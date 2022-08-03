"""
linear_search([1, 2, 5, 8, 11, 14, 18, 23, 32, 48], 11) => 4
"""

from typing import Any


def linear_search(array: list, target: Any) -> int:
    for index, element in enumerate(array):
        if element == target:
            return index
    return None


if __name__ == "__main__":
    print(linear_search([1, 2, 5, 8, 11, 14, 18, 23, 32, 48], 11) == 4)
