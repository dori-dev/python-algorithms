"""
move_zeros([True, 3, 5, 0, 3, False, None, 0, 'dori', 0]) =>
    [True, 3, 5, 3, False, None, 'dori', 0, 0, 0]
complexity: O(n)
"""


def move_zeros(sequence: list) -> list:
    result = []
    zeros_count = 0
    for item in sequence:
        if item == 0 and not isinstance(item, bool):
            zeros_count += 1
        else:
            result.append(item)
    result.extend([0] * zeros_count)
    return result


if __name__ == "__main__":
    print(move_zeros([True, 3, 5, 0, 3, False, None, 0, 'dori', 0]))
