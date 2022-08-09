from typing import List

"""
- You are given an array prices where prices[i] is the price 
of a given stock on that day.
- You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.
- Three variables are made left and right being pointers and maxp being the 
maximum profit on thats specifc day
- Looped through the list then compared elements at the first and second indexes
to then perform the subtraction to retrieve the 


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

