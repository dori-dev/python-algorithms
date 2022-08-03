"""
text = 'dori'
ciphers, keys = encrypt(text)
decrypt(ciphers, keys)
complexity: O(n)
"""
from random import randint
from typing import List, Tuple


def encrypt(text: str) -> Tuple[List[int]]:
    plain = [ord(letter) for letter in text]
    keys = []
    ciphers = []
    for letter_code in plain:
        random_key = randint(1, 300)
        cipher = (letter_code + random_key) * random_key
        keys.append(random_key)
        ciphers.append(cipher)
    return ciphers, keys


def decrypt(ciphers: List[int], keys: List[int]) -> str:
    if len(ciphers) != len(keys):
        return None
    text = ""
    for cipher, key in zip(ciphers, keys):
        letter_code = int(cipher / key) - key
        text += chr(letter_code)
    return text


if __name__ == "__main__":
    text = 'dori'
    ciphers, keys = encrypt(text)
    print(ciphers)
    print(keys)
    print(decrypt(ciphers, keys))
