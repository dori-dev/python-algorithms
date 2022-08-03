"""
rotate("hello", 2) => "llohe"
rotate("hello", 5) => "hello"
rotate("hello", 6) => "elloh"
rotate("hello", 7) => "llohe"
complexity: O(1)
"""


def rotate(string: str, degree: int) -> str:
    degree %= len(string)
    double_string = string + string
    return double_string[degree:degree+len(string)]


if __name__ == "__main__":
    print(rotate("hello", 2) == "llohe")
    print(rotate("hello", 5) == "hello")
    print(rotate("hello", 6) == "elloh")
    print(rotate("hello", 7) == "llohe")
    print(rotate("hello", 102) == "llohe")
