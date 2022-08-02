from typing import List

"""
-
"""

def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            print("prices left: ", prices[left])
            print("prices left: ", prices[right])
            maxP = max(maxP, profit)
            print("max profit: ", maxP)
            print("profit: ", profit)
        else:
            left = right
        right += 1
    return maxP


# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))

# prices = [7,6,4,3,1]
# print(maxProfit(prices))

prices = [1,2,3,4,5,6,7]
print(maxProfit(prices))

