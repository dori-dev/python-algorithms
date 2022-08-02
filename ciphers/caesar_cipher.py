"""
caesar cipher algorithm, implement in python
complexity: O(n)
"""

from string import ascii_letters


def encrypt(input_string: str, key: int) -> str:
    alpha = ascii_letters
    result = ""
    for letter in input_string:
        if letter not in alpha:
            result += letter
            continue
        new_key = (alpha.index(letter) + key) % len(alpha)
        result += alpha[new_key]
    return result


def decrypt(input_string: str, key: int) -> str:
    key *= -1
    return encrypt(input_string, key)


def brute_force(input_string: str) -> dict:
    alpha = ascii_letters
    key = 1
    brute_force_data = {}
    while key <= len(alpha):
        result = decrypt(input_string, key)
        brute_force_data[key] = result
        key += 1
    return brute_force_data


if __name__ == '__main__':
    # encrypt & decrypt mohammad dori
    print(encrypt('mohammad dori', 8))
    print(decrypt('uwpiuuil lwzq', 8))
    # encrypt & decrypt dori-dev
    print(encrypt('dori-dev', 8))
    print(decrypt('lwzq-lmD', 8))
    # return brute force data for lwzq-lmD encrypted text
    # and find the key `8` and true text `dori-dev`
    print(brute_force('lwzq-lmD'))
