"""
array = [4, 7, 9, 2, 3, 6, 7]
bead_sort(array) => [2, 3, 4, 6, 7, 7, 9]
"""

from typing import List


def bead_sort(sequence: List[int]) -> List[int]:
    for number in sequence:
        if not isinstance(number, int) or number < 0:
            raise TypeError('Sequence must be list or non-negative integers.')
    for _ in range(len(sequence)):
        for i, (first, second) in enumerate(zip(sequence, sequence[1:])):
            if second < first:
                distance = first - second
                sequence[i] -= distance
                sequence[i+1] += distance
    return sequence


if __name__ == "__main__":
    array = [4, 7, 9, 2, 3, 6, 7]
    bead_sort(array)
    print(array == [2, 3, 4, 6, 7, 7, 9])
