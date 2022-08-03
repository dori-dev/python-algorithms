"""
last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 3) => 4
last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 2) => 2
complexity: O(log n)
"""

from typing import Any


def last_occurrence(array: list, target: Any) -> int:
    low, high = 0, len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if target < array[middle]:
            high = middle - 1
        else:  # when array[middle] <= target
            low = middle + 1
    if array[high] == target:
        return high
    return None


if __name__ == "__main__":
    print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 3) == 4)
    print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 2) == 2)
    print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4) == 6)
    print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 5) == 9)
