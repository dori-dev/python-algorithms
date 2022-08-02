"""
limit([1, 2, 3, 4, 5], None, 3) = [1, 2, 3]
complexity = O(n)
"""


def min_check(value: int, min_limit: int) -> bool:
    if min_limit is None:
        return True
    return min_limit <= value


def max_check(value: int, max_limit: int) -> bool:
    if max_limit is None:
        return True
    return value <= max_limit


def limit(array: list, min_limit: int = None, max_limit: int = None) -> list:
    result = []
    for value in array:
        if min_check(value, min_limit) and max_check(value, max_limit):
            result.append(value)
    return result


print(limit([1, 2, 3, 4, 5], None, 3))
