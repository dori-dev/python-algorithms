"""
buy-sell stock:
    max_profit([7, 1, 5, 3, 6, 4]) => 5
    max_profit([9, 7, 6, 4, 3, 1]) => 0
complexity: O(n)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    profitable_stocks = {}
    for first, second in zip(prices, prices[1:]):
        distance = second - first
        if distance > 0:
            profitable_stocks[(first, second)] = distance
    if not profitable_stocks:
        return 0
    best_match = max(
        profitable_stocks,
        key=lambda key: profitable_stocks[key]
    )
    return best_match[1]


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]) == 5)
    print(max_profit([9, 7, 6, 4, 3, 1]) == 0)
