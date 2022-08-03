"""
zigzag iterator
array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10]
zigzag_iterator = ZigZag(array1, array2)
while zigzag_iterator.has_next():
    print(zigzag_iterator.next(), end=" ")
1 2 3 4 5 6 7 8 9 10
"""

from copy import deepcopy
from typing import List


class ZigZag:
    def __init__(self, array1: list, array2: list):
        self.queue: List[list] = [
            deepcopy(array1), deepcopy(array2)
        ]

    def next(self):
        array = self.queue.pop(0)
        item = array.pop(0)
        if array:
            self.queue.append(array)
        return item

    def has_next(self):
        return bool(self.queue)


if __name__ == "__main__":
    array1 = [1, 3, 5, 7, 9]
    array2 = [2, 4, 6, 8, 10]
    zigzag_iterator = ZigZag(array1, array2)
    while zigzag_iterator.has_next():
        print(zigzag_iterator.next())
