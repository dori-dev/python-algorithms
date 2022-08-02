"""
top_one([1, 1, 2, 2, 3, 4]) => [1, 2]
complexity: O(n)
"""


def top_one(array: list) -> list:
    values = {}
    for item in array:
        values[item] = values.get(item, 0) + 1
    max_repetition = max(values.values())
    result = []
    for key in values.keys():
        if values[key] == max_repetition:
            result.append(key)
    return result


print(top_one([1, 1, 2, 2, 3, 4]))
