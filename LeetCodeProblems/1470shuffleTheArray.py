from typing import List

"""
- Given a list that is consisting of 2n elements in the form 
[x1, x2, x3, .... y1, y2, y3] this func. chnages the order of the list to 
[x1, y1, x2, y2, x3, y3,...]
- A new variable is made to hold the values of the re-ordered list
- Looped through the list then added the element at the current index
to the new list and then adding the element at the current index plus the 
integer that we are being given 
- The new list is returned in the correct format
- Complexity
    Time - O(n) where n represents the amount of elements that have to be 
    visted in the loop
    Space - O(n) where n represents the amount of elemets in the new returned 
    list
"""


def shuffle(nums: List[int], n: int) -> List[int]:
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

nums = [2,5,1,3,4,7] 
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))