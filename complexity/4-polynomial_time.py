"""
Polynomial Time -> O(n^x)
"""

numbers = [64, 34, 25, 12, 22, 11, 90]


def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-i-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    # O(n^2)
    print(bubble_sort(numbers))
