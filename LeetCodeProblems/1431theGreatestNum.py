from typing import List
"""
- Given a list of integers and a secondary integer this function returns a 
list of booleans when the element at the current index plus the secondary integer 
is the greatest number of candies amoung the kids
- A empty list was made to hold the boolean values
- A variable was made that is initialized to the maximum number in the given list
- Looped through the given list to compare the if current element plus the secondary
integer is greater than the maximum number in the given list
- If it is "True" is added to the empty list if not "False" is added to the empty
list
- The new list of boolean values is returned 
- Complexity
    Time - O(n) where n represents the amount of elements in the given list that
    has to be visted in the loop
    Space - O(n) where n represents the amount of elements in the list of booleans

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

candies = [4,2,1,1,2] 
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))

candies = [12,1,12] 
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))