"""
two_sum([2, 7, 11, 15], 18) => [7, 11]
two_sum([2, 7, 11, 15], 9) => [2, 7]
complexity: O(n)
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for first, second in zip(numbers, numbers[1:]):
        if first + second == target:
            return [first, second]
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 18) == [7, 11])
    print(two_sum([2, 7, 11, 15], 9) == [2, 7])
