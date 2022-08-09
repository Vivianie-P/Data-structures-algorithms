from typing import List

"""
- Given a 2D list this function returns an int that represents the
weatlth of the richest customer in the list
- This func iterates through the 2D list and finds the total of 
each customer's wealth then uses the max method to return which 
customer's wealth is the largest
- Complexity
    Time - O(n) where n represents the amount of nested lists
    Space - O(n) where n represents the two methods being called 
    sum() & max()
"""

def maximumWealth(accounts: List[List[int]]) -> int:
    max_num = float("-inf")
    
    for acc in accounts:
        total = sum(acc)
        max_num = max(total, max_num)
    return max_num