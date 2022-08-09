from typing import List

"""
- Given a list of integers this function returns a boolean value
if the list has a duplicate number
- The list of int's are all added to a hashmap with their value 
intialized to 0
- If the number is in the hashmap more than once that number is 
incrmented by one
- Then we iterate through the hashmap to see if there is a value 
of 1 to any of the numbers. If there is then this func returns 
True if not then this func returns False
- Complexity
    Time - O(n^2) where represents the amount of elements that 
    have to iterated through
    Space - O(n) where n represents the amoount of the elements 
    of the given list
"""

def containsDuplicate(nums: List[int]) -> bool:
    hashmap = {}

    for num in nums:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
        print(hashmap)

    for idx, val in hashmap.items():
        if val > 1:
            return True

    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))