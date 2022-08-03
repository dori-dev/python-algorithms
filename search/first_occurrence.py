"""
first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 3) => 3
first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 2) => 0
complexity: O(log n)
"""

from typing import Any


def first_occurrence(array: list, target: Any) -> int:
    low, high = 0, len(array) - 1
    while low < high:
        middle = (low + high) // 2
        if array[middle] < target:
            low = middle + 1
        else:  # when target <= array[middle]
            high = middle - 1
    if array[low] == target:
        return low
    return None


if __name__ == "__main__":
    print(first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 3) == 3)
    print(first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 2) == 0)
