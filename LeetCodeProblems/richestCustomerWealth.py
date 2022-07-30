from typing import List
"""
-
"""

def maximumWealth(self, accounts: List[List[int]]) -> int:
    max_num = float("-inf")
    
    for acc in accounts:
        total = sum(acc)
        max_num = max(total, max_num)
    return max_num