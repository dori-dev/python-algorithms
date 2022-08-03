"""
search_range([5, 7, 7, 8, 8, 8, 10], 8) => [3, 5]
search_range([5, 7, 7, 8, 8, 8, 10], 11) => [None, None]
complexity: O(n)
"""

from typing import List


def search_range(array: List[int], target: int) -> tuple:
    sorted_array = sorted(array)
    start_index = None
    end_index = None
    found = False
    for index, item in enumerate(sorted_array):
        if item == target and found is False:
            found = True
            start_index = index
        if item != target and found is True and end_index is None:
            end_index = index - 1
    return sorted_array, target, [start_index, end_index]


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 8, 10], 8))
    print(search_range([5, 7, 7, 8, 8, 8, 10], 11))
