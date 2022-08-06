from typing import List
"""
-
"""

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    output = []
    maxNum = max(candies)
    
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxNum:
            output.append(True)
        else:
            output.append(False)
    return output

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
