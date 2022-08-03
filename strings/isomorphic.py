"""
is_isomorphic('foo', 'bar') => False
is_isomorphic('foo', 'bee') => True
complexity: O(n)
"""


def is_isomorphic(base_string: str, string: str) -> bool:
    if len(base_string) != len(string):
        return False
    string_relations = {}
    for base_letter, letter in zip(base_string, string):
        correct_letter = string_relations.get(base_letter)
        if letter in string_relations.values() and correct_letter is None:
            return False
        if correct_letter is None:
            string_relations[base_letter] = letter
            continue
        if correct_letter != letter:
            return False
    return True


if __name__ == "__main__":
    print(is_isomorphic('foo', 'bar') is False)
    print(is_isomorphic('foo', 'bee') is True)
    print(is_isomorphic('fow', 'bee') is False)
    print(is_isomorphic('paper', 'title') is True)
