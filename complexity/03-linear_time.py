"""
Linear Time -> O(n)
"""

numbers = [2, 16, 7, 9, 8, 23, 12]


def get_max_number(numbers: int) -> int:
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


if __name__ == "__main__":
    print(get_max_number(numbers))
