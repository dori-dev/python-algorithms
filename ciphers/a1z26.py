"""
a1z26_encode('dori', 15) => [115, 126, 129, 120]
a1z26_decode([115, 126, 129, 120], 15) => 'dori'
complexity: O(n)
"""

from typing import List


def a1z26_encode(string: str, key: int) -> List[int]:
    result = []
    for letter in string:
        result.append(ord(letter) + abs(key))
    return result


def a1z26_decode(encode_array: List[int], key: int) -> str:
    result = ''
    for element in encode_array:
        try:
            result += chr(element - abs(key))
        except ValueError:
            result += chr(element)
    return result


if __name__ == '__main__':
    string_encode = a1z26_encode('mohammad dori', 8)
    print(string_encode)
    print(a1z26_decode(string_encode, 8))
    print(a1z26_encode('dori', 15) == [115, 126, 129, 120])
    print(a1z26_decode([115, 126, 129, 120], 15) == 'dori')
