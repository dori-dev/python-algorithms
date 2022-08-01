"""
Exponential Time > O(2^n)
"""

from itertools import chain, combinations
from typing import Iterable


def subsets(iterable: Iterable) -> list:
    subsets_ = []
    for r in range(len(iterable) + 1):
        subsets_.append(combinations(iterable, r))
    return chain.from_iterable(subsets_)


# O(2^n)
print(list(subsets([1, 2, 3])))
print(list(subsets(['a', 'b', 'c'])))
