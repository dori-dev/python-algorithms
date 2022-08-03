"""
Complexity
    Time | Space
Big O(operation) notation
"""

from typing import Any

# The length of the numbers is important
# for running time and space
numbers = [2, 4, 5, 7, 11, 40, 119]


def get_index(list_: list, element: Any) -> Any:
    index = 0
    for item in list_:
        if item == element:
            return index
        index += 1
    return None


if __name__ == "__main__":
    print(get_index(numbers, 40))
