"""
remove_min([4, 5, 2, 8, -2, 5, 1, 9]) => ([4, 5, 2, 8, 5, 1, 9], -2)
complexity: O(n)
"""


def remove_min(numbers: list) -> int:
    if len(numbers) == 0:
        return numbers
    result = []
    min_number = numbers[0]
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    for number in numbers:
        if number != min_number:
            result.append(number)
    return result, min_number


if __name__ == "__main__":
    array = [4, 5, 2, 8, -2, 5, 1, 9]
    print(remove_min(array))
