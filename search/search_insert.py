"""
search_insert([1, 3, 5, 6], 3) => 1
search_insert([1, 3, 5, 6], 4) => 2
search_insert([1, 3, 5, 6], 7) => 4
search_insert([1, 3, 5, 6], 0) => 0
"""

from typing import Any


def bubble_sort(array: list) -> list:
    array = array.copy()
    length = len(array)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            break
    return array


def get_index(array: list, element: Any) -> int:
    index = 0
    for item in array:
        if item == element:
            return index
        index += 1
    return None


def get_insert_place(array: list, target: int) -> int:
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if array[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return low


def search_insert(array: list, number: int) -> int:
    # complexity: O(n^2)
    bubble_sort(array)
    # complexity: O(n)
    index = get_index(array, number)
    if index is None:
        # complexity: O(log n)
        return get_insert_place(array, number)
    return index


if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 3) == 1)
    print(search_insert([1, 3, 5, 6], 4) == 2)
    print(search_insert([1, 3, 5, 6], 7) == 4)
    print(search_insert([1, 3, 5, 6], 0) == 0)
